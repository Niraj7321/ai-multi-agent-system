"""
Unit tests for CrewManager
"""
import pytest
from unittest.mock import Mock, patch
from src.crew_manager import CrewManager


class TestCrewManager:
    """Test cases for CrewManager class"""

    @patch("src.crew_manager.ChatOpenAI")
    def test_initialization(self, mock_llm):
        """Test CrewManager initialization"""
        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}):
            manager = CrewManager(api_key="test-key")
            assert manager.api_key == "test-key"
            assert manager.llm is not None

    @patch("src.crew_manager.ChatOpenAI")
    def test_initialization_without_api_key(self, mock_llm):
        """Test CrewManager initialization without API key"""
        with patch.dict("os.environ", {}, clear=True):
            with pytest.raises(ValueError, match="OPENAI_API_KEY"):
                CrewManager()

    @patch("src.crew_manager.ChatOpenAI")
    def test_create_research_crew(self, mock_llm):
        """Test research crew creation"""
        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}):
            manager = CrewManager(api_key="test-key")
            crew = manager.create_research_crew(
                topic="Test Topic", content_type="article"
            )
            assert crew is not None
            assert len(crew.agents) == 3
            assert len(crew.tasks) == 3

    @patch("src.crew_manager.Crew")
    @patch("src.crew_manager.ChatOpenAI")
    def test_execute_research_workflow_success(self, mock_llm, mock_crew):
        """Test successful workflow execution"""
        mock_crew_instance = Mock()
        mock_crew_instance.kickoff.return_value = "Test Result"
        mock_crew.return_value = mock_crew_instance

        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}):
            manager = CrewManager(api_key="test-key")
            result = manager.execute_research_workflow(
                topic="Test Topic", content_type="article"
            )

            assert result["success"] is True
            assert result["topic"] == "Test Topic"
            assert result["content_type"] == "article"
            assert result["result"] == "Test Result"

    @patch("src.crew_manager.Crew")
    @patch("src.crew_manager.ChatOpenAI")
    def test_execute_research_workflow_failure(self, mock_llm, mock_crew):
        """Test workflow execution with error"""
        mock_crew_instance = Mock()
        mock_crew_instance.kickoff.side_effect = Exception("Test Error")
        mock_crew.return_value = mock_crew_instance

        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}):
            manager = CrewManager(api_key="test-key")
            result = manager.execute_research_workflow(
                topic="Test Topic", content_type="article"
            )

            assert result["success"] is False
            assert "Test Error" in result["message"]
