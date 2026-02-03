"""
Crew Manager - Orchestrates the multi-agent system
"""
import os
from typing import Optional, Dict, Any
from crewai import Crew, Task, Process
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

from agents.researcher import ResearchAgent
from agents.writer import WriterAgent
from agents.reviewer import ReviewerAgent
from agents.presentation_maker import create_presentation_maker_agent


class CrewManager:
    """
    Manages the multi-agent crew and coordinates tasks
    """

    def __init__(
        self,
        model_name: str = "claude-sonnet-4-20250514",
        temperature: float = 0.7,
        api_key: Optional[str] = None,
        use_anthropic: bool = None,
    ):
        """
        Initialize the Crew Manager

        Args:
            model_name: Name of the LLM model to use
            temperature: Temperature setting for the LLM
            api_key: API key (OpenAI or Anthropic, optional, can be set via environment)
            use_anthropic: Whether to use Anthropic Claude (auto-detected if None)
        """
        load_dotenv()

        # Determine which provider to use
        if use_anthropic is None:
            use_anthropic = os.getenv("USE_ANTHROPIC", "").lower() == "true"

        # Set up LLM based on provider
        if use_anthropic:
            self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
            if not self.api_key:
                raise ValueError("ANTHROPIC_API_KEY must be provided or set in environment")

            self.llm = ChatAnthropic(
                model=model_name,
                temperature=temperature,
                api_key=self.api_key,
                max_tokens=4096
            )
        else:
            self.api_key = api_key or os.getenv("OPENAI_API_KEY")
            if not self.api_key:
                raise ValueError("OPENAI_API_KEY must be provided or set in environment")

            self.llm = ChatOpenAI(
                model=model_name, temperature=temperature, api_key=self.api_key
            )

        # Initialize agents
        self.researcher = ResearchAgent(self.llm)
        self.writer = WriterAgent(self.llm)
        self.reviewer = ReviewerAgent(self.llm)
        self.presentation_maker = create_presentation_maker_agent(self.llm)

    def create_research_crew(
        self, topic: str, content_type: str = "article"
    ) -> Crew:
        """
        Create a crew for research and content creation

        Args:
            topic: The topic to research and write about
            content_type: Type of content to create

        Returns:
            Crew: Configured crew ready to execute
        """
        # Create agent instances
        research_agent = self.researcher.create_agent()
        writer_agent = self.writer.create_agent()
        reviewer_agent = self.reviewer.create_agent()

        # Define tasks
        research_task = Task(
            description=ResearchAgent.get_research_task_description(topic),
            agent=research_agent,
            expected_output="A comprehensive research summary with key findings, statistics, and credible sources",
        )

        writing_task = Task(
            description=WriterAgent.get_writing_task_description(content_type),
            agent=writer_agent,
            expected_output=f"A well-structured {content_type} in Markdown format based on the research",
            context=[research_task],
        )

        review_task = Task(
            description=ReviewerAgent.get_review_task_description(),
            agent=reviewer_agent,
            expected_output="A detailed review with quality score, strengths, improvements, and final verdict",
            context=[writing_task],
        )

        # Create and return crew
        crew = Crew(
            agents=[research_agent, writer_agent, reviewer_agent],
            tasks=[research_task, writing_task, review_task],
            process=Process.sequential,
            verbose=True,
        )

        return crew

    def execute_research_workflow(
        self, topic: str, content_type: str = "article"
    ) -> Dict[str, Any]:
        """
        Execute the complete research and content creation workflow

        Args:
            topic: The topic to research and write about
            content_type: Type of content to create

        Returns:
            Dict containing the results from each stage
        """
        try:
            crew = self.create_research_crew(topic, content_type)
            result = crew.kickoff()

            # IMPORTANT: Extract the Writer's original content from task outputs
            # The Writer task is at index 1 (research=0, writer=1, reviewer=2)
            writer_output = None
            if hasattr(crew, 'tasks') and len(crew.tasks) >= 2:
                writer_task = crew.tasks[1]
                if hasattr(writer_task, 'output'):
                    # Get the Writer's raw output (original, unmodified content)
                    writer_output = writer_task.output.raw if hasattr(writer_task.output, 'raw') else writer_task.output

            # Use the Writer's output if available, otherwise fall back to final result
            final_content = writer_output if writer_output else result

            return {
                "success": True,
                "topic": topic,
                "content_type": content_type,
                "result": final_content,
                "message": "Workflow completed successfully",
            }
        except Exception as e:
            return {
                "success": False,
                "topic": topic,
                "content_type": content_type,
                "result": None,
                "message": f"Error during workflow execution: {str(e)}",
            }

    def execute_presentation_workflow(
        self, topic: str, text_content: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Execute text-to-presentation workflow

        Args:
            topic: The presentation topic
            text_content: Optional existing content to convert (if None, will research first)

        Returns:
            Dict containing the presentation results
        """
        try:
            # If no content provided, research first
            if not text_content:
                # Research → Write → Convert to Presentation
                research_agent = self.researcher.create_agent()
                writer_agent = self.writer.create_agent()

                research_task = Task(
                    description=ResearchAgent.get_research_task_description(topic),
                    agent=research_agent,
                    expected_output="A comprehensive research summary with key findings",
                )

                writing_task = Task(
                    description=WriterAgent.get_writing_task_description("article"),
                    agent=writer_agent,
                    expected_output="A well-structured article in Markdown format",
                    context=[research_task],
                )

                presentation_task = Task(
                    description=self._get_presentation_task_description(),
                    agent=self.presentation_maker,
                    expected_output="""A complete presentation with 10-15 slides in this EXACT Markdown format:

# Slide 1: [Title]
**[Subtitle]**
📅 [Date]

---

# Slide 2: What We'll Cover
- [Topic 1]
- [Topic 2]
- [Topic 3]

---

# Slide 3: [Descriptive Title]
**[Optional context]**
- [Bullet point 1]
- [Bullet point 2]
- [Bullet point 3]

💡 **Key Insight:** [Takeaway]

[Visual suggestion: Chart/Image]

---

[Continue with 7-12 more content slides using the same format]

CRITICAL: Each slide MUST start with "# Slide N:" and be separated by exactly "---" on its own line.""",
                    context=[writing_task],
                )

                crew = Crew(
                    agents=[research_agent, writer_agent, self.presentation_maker],
                    tasks=[research_task, writing_task, presentation_task],
                    process=Process.sequential,
                    verbose=True,
                )
            else:
                # Just convert existing content to presentation
                presentation_task = Task(
                    description=f"""Convert the following content into a professional presentation:

{text_content}

{self._get_presentation_task_description()}""",
                    agent=self.presentation_maker,
                    expected_output="""A complete presentation with 10-15 slides in this EXACT Markdown format:

# Slide 1: [Title]
**[Subtitle]**
📅 [Date]

---

# Slide 2: What We'll Cover
- [Topic 1]
- [Topic 2]
- [Topic 3]

---

# Slide 3: [Descriptive Title]
**[Optional context]**
- [Bullet point 1]
- [Bullet point 2]
- [Bullet point 3]

💡 **Key Insight:** [Takeaway]

[Visual suggestion: Chart/Image]

---

[Continue with 7-12 more content slides using the same format]

CRITICAL: Each slide MUST start with "# Slide N:" and be separated by exactly "---" on its own line.""",
                )

                crew = Crew(
                    agents=[self.presentation_maker],
                    tasks=[presentation_task],
                    process=Process.sequential,
                    verbose=True,
                )

            result = crew.kickoff()

            return {
                "success": True,
                "topic": topic,
                "content_type": "presentation",
                "result": result,
                "message": "Presentation created successfully",
            }
        except Exception as e:
            return {
                "success": False,
                "topic": topic,
                "content_type": "presentation",
                "result": None,
                "message": f"Error during presentation creation: {str(e)}",
            }

    def _get_presentation_task_description(self) -> str:
        """Get the task description for presentation creation"""
        return """Create a professional, visually-structured presentation from the content provided.

⚠️ **MANDATORY OUTPUT FORMAT - YOU MUST FOLLOW THIS EXACTLY:**

Your output MUST look like this (this is not optional):

```
# Slide 1: Compelling Title Here

**Brief subtitle or description**

📅 January 2026

---

# Slide 2: What We'll Cover

- First main topic
- Second main topic
- Third main topic
- Fourth main topic

---

# Slide 3: Descriptive Action-Oriented Title

**Optional one-sentence context**

- Short bullet point (5-10 words)
- Another concise point with data
- Third impactful point
- Optional fourth point

💡 **Key Insight:** One memorable takeaway sentence

[Visual suggestion: Chart showing growth trends]

---

# Slide 4: Another Great Title

[Continue this pattern for 10-15 slides total]
```

**CRITICAL FORMATTING RULES - DO NOT DEVIATE:**
- Each slide MUST start with "# Slide [number]: [Title]" - NO EXCEPTIONS
- Slides MUST be separated by exactly "---" on its own line
- Use bullet points (- or *) for lists, NEVER write paragraphs
- Keep bullet points short: 5-10 words maximum
- ALWAYS include blank line after slide title before content
- ALWAYS include blank line before "---" separator
- NO prose, NO paragraphs, NO essay-style writing

**PRESENTATION STRUCTURE (10-15 slides total):**

**1. Title Slide:**
Format:
```
# Slide 1: [Compelling Main Title]

**[Subtitle or brief description]**

📅 [Date/Context if relevant]
```

**2. Agenda/Overview Slide:**
Format:
```
# Slide 2: What We'll Cover

- [Key topic 1]
- [Key topic 2]
- [Key topic 3]
- [Key topic 4]
- [Key topic 5]
```

**3. Content Slides (8-12 slides):**
Each content slide should follow this template:

```
# Slide [N]: [Action-Oriented Title]

**[Optional: One sentence context or question]**

- [Key point 1 - concise and impactful]
- [Key point 2 - use numbers/data when possible]
- [Key point 3 - focus on benefits/outcomes]
- [Key point 4 - optional fourth point]

💡 **Key Insight:** [One memorable takeaway sentence]

[Visual suggestion: Chart/Graph/Image/Diagram]
```

**Guidelines for Content Slides:**
- ONE main idea per slide
- Title must be descriptive and engaging (not generic)
- 3-5 bullet points maximum per slide
- Each bullet: 5-10 words (never full sentences)
- Use strong action verbs (Transform, Accelerate, Enhance, etc.)
- Include data/statistics when available (e.g., "85% improvement")
- Suggest relevant visuals: [Chart: Revenue Growth], [Image: Team collaboration], [Diagram: Process flow]

**4. Key Insights/Summary Slide:**
Format:
```
# Slide [N]: Key Takeaways

🎯 **Main Insights:**

- [Critical insight 1]
- [Critical insight 2]
- [Critical insight 3]
- [Critical insight 4]

**Remember:** [One powerful closing statement]
```

**5. Call to Action / Next Steps Slide:**
Format:
```
# Slide [N]: Next Steps

**What You Can Do:**

1. [Specific action step 1]
2. [Specific action step 2]
3. [Specific action step 3]

📧 **Contact:** [Email/Website if relevant]
🔗 **Resources:** [Links/References if relevant]
```

**SLIDE DESIGN BEST PRACTICES:**

✅ **DO:**
- Use numbers and statistics for credibility
- Keep slides visual and scannable
- Use consistent formatting across slides
- Write titles that tell the story (even without reading content)
- Suggest visual elements [Chart: X], [Image: Y], [Icon: Z]
- Use emojis sparingly for visual markers (📊, 🎯, ⚡, 💡, 🚀)

❌ **DON'T:**
- Write paragraphs or long sentences
- Use more than 6 bullet points per slide
- Make titles generic ("Introduction", "Overview", "Conclusion")
- Overcrowd slides with text
- Use complex jargon without explanation

**COMPLETE OUTPUT EXAMPLE:**

```
# Slide 1: AI Transforms Healthcare in 2026

**How artificial intelligence is revolutionizing patient care and medical diagnostics**

📅 January 2026

---

# Slide 2: What We'll Cover

- AI diagnostic tools and accuracy
- Patient care automation benefits
- Cost reduction and efficiency gains
- Real-world implementation examples
- Future trends and opportunities

---

# Slide 3: AI Diagnostic Accuracy Reaches 95%

**Modern AI systems now outperform traditional methods**

- 95% diagnostic accuracy vs 87% traditional
- 40% faster diagnosis time
- Early disease detection improved by 60%
- Reduced false positives by 50%

💡 **Key Insight:** AI catches diseases earlier, saving lives and reducing costs

[Visual suggestion: Chart showing accuracy comparison between AI vs traditional diagnostics]

---

# Slide 4: Automated Patient Care Systems

**Reducing workload while improving patient outcomes**

- 24/7 patient monitoring capabilities
- Instant alert system for emergencies
- 70% reduction in manual paperwork
- Personalized treatment recommendations

💡 **Key Insight:** Automation frees healthcare workers to focus on critical care

[Visual suggestion: Diagram of automated patient monitoring workflow]

---

# Slide 5: Cost Savings and ROI

**Healthcare facilities see significant financial benefits**

- Average 35% operational cost reduction
- $2.4M annual savings per facility
- ROI achieved within 18 months
- 50% fewer administrative staff needed

💡 **Key Insight:** AI investments pay for themselves quickly while improving care

[Visual suggestion: Bar chart showing cost savings over 3 years]

---

# Slide 6: Key Takeaways

🎯 **Main Insights:**

- AI diagnostics are now more accurate than traditional methods
- Automation dramatically reduces costs and workload
- Early disease detection saves lives and money
- ROI is achieved within 18 months

**Remember:** AI in healthcare is not the future—it's happening now

---

# Slide 7: Next Steps

**How to Get Started:**

1. Assess your current diagnostic processes
2. Pilot AI tools in one department
3. Measure outcomes and expand gradually

📧 **Learn More:** healthcare-ai@example.com
🔗 **Resources:** www.healthcare-ai-guide.com
```

**FINAL CHECKLIST:**
✓ 10-15 slides total
✓ Each slide starts with # Slide N: Title
✓ Slides separated by ---
✓ Bullet points are short (5-10 words)
✓ Visual suggestions included
✓ Titles are descriptive and engaging
✓ Content is scannable, not essay-style
✓ One main idea per slide
✓ Consistent formatting throughout
"""


if __name__ == "__main__":
    # Example usage
    manager = CrewManager()
    result = manager.execute_research_workflow(
        topic="Artificial Intelligence in Healthcare 2026", content_type="article"
    )

    print("\n" + "=" * 80)
    print("WORKFLOW RESULT")
    print("=" * 80)
    print(f"Success: {result['success']}")
    print(f"Message: {result['message']}")
    if result["success"]:
        print(f"\nFinal Output:\n{result['result']}")
