"""
Configuration management for the AI Multi-Agent System
"""
import os
from typing import Optional
from dataclasses import dataclass, field
from dotenv import load_dotenv

load_dotenv()


@dataclass
class LLMConfig:
    """Configuration for Language Model"""

    model_name: str = os.getenv("MODEL_NAME", "gpt-4-turbo-preview")
    temperature: float = float(os.getenv("TEMPERATURE", "0.7"))
    max_tokens: int = int(os.getenv("MAX_TOKENS", "2000"))
    api_key: Optional[str] = os.getenv("OPENAI_API_KEY")


@dataclass
class VectorDBConfig:
    """Configuration for Vector Database"""

    persist_directory: str = os.getenv(
        "CHROMA_PERSIST_DIRECTORY", "./data/chroma_db"
    )


@dataclass
class LoggingConfig:
    """Configuration for Logging"""

    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    log_file: str = os.getenv("LOG_FILE", "./logs/app.log")


@dataclass
class AppConfig:
    """Main application configuration"""

    llm: LLMConfig = field(default_factory=LLMConfig)
    vector_db: VectorDBConfig = field(default_factory=VectorDBConfig)
    logging: LoggingConfig = field(default_factory=LoggingConfig)

    def validate(self) -> bool:
        """
        Validate configuration

        Returns:
            bool: True if configuration is valid
        """
        if not self.llm.api_key:
            raise ValueError("OPENAI_API_KEY is required")

        if self.llm.temperature < 0 or self.llm.temperature > 1:
            raise ValueError("Temperature must be between 0 and 1")

        return True


# Global config instance
config = AppConfig()
