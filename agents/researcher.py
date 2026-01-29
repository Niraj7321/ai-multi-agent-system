"""
Research Agent - Responsible for gathering and analyzing information
"""
import os
from crewai import Agent
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool, ScrapeWebsiteTool


class ResearchAgent:
    """
    Research Agent that performs web searches and gathers information
    """

    def __init__(self, llm: ChatOpenAI):
        self.llm = llm
        # Only initialize tools if API keys are available
        self.tools = []

        # Check for SERPER_API_KEY before initializing search tools
        if os.getenv("SERPER_API_KEY"):
            try:
                self.search_tool = SerperDevTool()
                self.scrape_tool = ScrapeWebsiteTool()
                self.tools = [self.search_tool, self.scrape_tool]
            except Exception:
                # If tools fail to initialize, use no tools
                self.tools = []

    def create_agent(self) -> Agent:
        """
        Creates and configures the research agent

        Returns:
            Agent: Configured CrewAI agent
        """
        return Agent(
            role="Senior Research Analyst",
            goal="Conduct comprehensive research on given topics using your knowledge and analytical skills",
            backstory="""You are an experienced research analyst with deep knowledge across
            multiple domains. You excel at synthesizing information, analyzing trends,
            and providing well-reasoned insights. You can draw upon your extensive knowledge
            to provide comprehensive analysis on any topic, identifying key themes, important
            considerations, and relevant context.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=self.tools,
            max_iter=15,
        )

    @staticmethod
    def get_research_task_description(topic: str) -> str:
        """
        Generate task description for research

        Args:
            topic: The topic to research

        Returns:
            str: Task description
        """
        return f"""
        Conduct comprehensive, original research on the following topic: {topic}

        IMPORTANT: Use your extensive knowledge to provide original analysis and insights. All information should be synthesized from your understanding and presented in your own words.

        Your research should include:
        1. **Current trends and developments** - What's happening in this space now
        2. **Key concepts and fundamentals** - Core principles and important background
        3. **Technical details and methodologies** - How things work, step-by-step explanations
        4. **Real-world applications and use cases** - Practical examples and scenarios
        5. **Best practices and recommendations** - What works well and why
        6. **Challenges and limitations** - Common issues and how to address them
        7. **Future outlook** - Where things are heading

        Provide a well-structured, comprehensive research summary that can be used to create original, copyright-free content.

        Focus on providing deep insights and practical information that will be valuable for creating educational blog content.
        """
