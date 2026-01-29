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
