"""
Writer Agent - Responsible for creating high-quality content
"""
from crewai import Agent
from langchain_openai import ChatOpenAI


class WriterAgent:
    """
    Writer Agent that creates engaging and informative content
    """

    def __init__(self, llm: ChatOpenAI):
        self.llm = llm

    def create_agent(self) -> Agent:
        """
        Creates and configures the writer agent

        Returns:
            Agent: Configured CrewAI agent
        """
        return Agent(
            role="Senior Content Writer",
            goal="Transform research findings into clear, engaging, and well-structured content",
            backstory="""You are an accomplished content writer with years of experience
            in creating compelling narratives. You excel at taking complex research and
            transforming it into accessible, engaging content that resonates with the
            target audience. Your writing is clear, concise, and captivating.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            max_iter=10,
        )

    @staticmethod
    def get_writing_task_description(content_type: str = "article") -> str:
        """
        Generate task description for writing

        Args:
            content_type: Type of content to create (article, report, blog post, etc.)

        Returns:
            str: Task description
        """
        if content_type.lower() in ["blog post", "blog"]:
            return """
            Based on the research provided, create a comprehensive, SEO-friendly blog post that is COMPLETELY ORIGINAL and copyright-free.

            IMPORTANT: You must create entirely original content based on your knowledge and the research. Do NOT copy or reproduce any copyrighted material.

            Your blog post MUST include the following structure:

            1. **Title (H1):**
               - Catchy, SEO-friendly, and relevant to the topic
               - Should grab attention and clearly indicate what the post is about

            2. **Introduction (2-3 paragraphs):**
               - Hook the reader with an engaging opening
               - Explain what the topic is and why it matters
               - Preview what readers will learn

            3. **Problem / Use Case / Background (Section with H2):**
               - Describe the problem or scenario this topic addresses
               - Explain the context and why this is important
               - Use real-world examples or scenarios

            4. **Solution / Methodology / How-To Guide (Multiple H2 sections):**
               - Step-by-step explanation or tutorial
               - Break down complex concepts into digestible parts
               - Include code snippets (Python preferred if applicable) with explanations
               - Add practical examples and workflows
               - Use bullet points and numbered lists for clarity
               - Include best practices and tips

            5. **Results / Examples / Demo (Section with H2):**
               - Show practical outcomes or examples
               - Describe what results to expect
               - Include performance metrics or benchmarks if relevant
               - Explain the impact and benefits

            6. **Conclusion / Key Takeaways (Section with H2):**
               - Summarize the main points clearly
               - Provide actionable takeaways
               - End with a call-to-action or next steps

            7. **References / Further Reading (Optional Section with H2):**
               - List relevant resources, documentation, or tutorials
               - Format as bullet points with brief descriptions

            **Writing Guidelines:**
            - Use clear, easy-to-understand language
            - Avoid unnecessary jargon; explain technical terms when needed
            - Make content engaging and practical
            - Use headings (##), subheadings (###), bullet points, and numbered lists
            - Include code blocks with proper syntax highlighting (```python)
            - Add emphasis with **bold** for important points
            - Write in an informative yet conversational tone
            - Ensure all content is 100% original and copyright-free

            **Format:** Output in clean Markdown format with proper heading hierarchy.

            **Length:** Aim for 1500-2500 words for a comprehensive, valuable blog post.
            """
        else:
            return f"""
            Based on the research provided, create a comprehensive {content_type} that:

            1. Has a compelling introduction that hooks the reader
            2. Presents information in a logical, well-structured manner
            3. Uses clear and engaging language
            4. Includes relevant examples and data points
            5. Provides actionable insights or takeaways
            6. Has a strong conclusion that summarizes key points

            Ensure the content is:
            - Well-organized with clear headings and sections
            - Free of jargon or overly technical language
            - Engaging and interesting to read
            - Informative and valuable to the audience
            - 100% original and copyright-free

            Output should be in Markdown format.
            """
