"""
Reviewer Agent - Responsible for quality assurance and content review
"""
from crewai import Agent
from langchain_openai import ChatOpenAI


class ReviewerAgent:
    """
    Reviewer Agent that ensures content quality and accuracy
    """

    def __init__(self, llm: ChatOpenAI):
        self.llm = llm

    def create_agent(self) -> Agent:
        """
        Creates and configures the reviewer agent

        Returns:
            Agent: Configured CrewAI agent
        """
        return Agent(
            role="Senior Content Reviewer & Quality Assurance Specialist",
            goal="Review content for accuracy, clarity, and quality, providing constructive feedback",
            backstory="""You are a meticulous editor and quality assurance specialist
            with a sharp eye for detail. You excel at identifying inconsistencies,
            factual errors, and areas for improvement. Your feedback is constructive,
            specific, and helps elevate content to the highest standards.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            max_iter=10,
        )

    @staticmethod
    def get_review_task_description() -> str:
        """
        Generate task description for content review

        Returns:
            str: Task description
        """
        return """
        Review the provided content and assess it based on the following criteria:

        1. **Originality & Copyright**: Verify content is 100% original and copyright-free
        2. **Accuracy**: Verify facts, technical details, and claims are correct
        3. **Structure & Format**:
           - For blog posts: Check for proper structure (Title, Intro, Problem, Solution, Results, Conclusion, References)
           - Verify proper Markdown formatting with headings, code blocks, and lists
        4. **Clarity**: Ensure ideas are expressed clearly and concisely
        5. **Engagement**: Assess readability, tone, and audience appeal
        6. **Completeness**: Ensure all key sections and points are covered
        7. **Technical Quality**: Check code examples are correct and well-explained
        8. **SEO & Readability**: Assess if title is catchy and content is scannable
        9. **Grammar & Style**: Check for language errors and consistency

        Provide a detailed review with:
        - **Overall quality score (1-10)** with justification
        - **Specific strengths** of the content (bullet points)
        - **Areas needing improvement** with actionable suggestions (bullet points)
        - **Copyright assessment**: Confirm content is original and copyright-free
        - **Final verdict**: Approve / Needs Minor Revision / Needs Major Revision

        IMPORTANT: Return the ORIGINAL content without modifications. Your role is to review and provide feedback, not to edit the content.

        Be thorough, constructive, and specific in your feedback.
        """
