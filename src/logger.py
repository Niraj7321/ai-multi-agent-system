"""
Logging configuration for the application
"""
import logging
import os
from pathlib import Path
from pythonjsonlogger import jsonlogger

from src.config import config


def setup_logger(name: str = "ai_multi_agent") -> logging.Logger:
    """
    Set up application logger with JSON formatting

    Args:
        name: Logger name

    Returns:
        logging.Logger: Configured logger instance
    """
    # Create logs directory if it doesn't exist
    log_dir = Path(config.logging.log_file).parent
    log_dir.mkdir(parents=True, exist_ok=True)

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, config.logging.log_level))

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(console_format)

    # File handler with JSON formatting
    file_handler = logging.FileHandler(config.logging.log_file)
    file_handler.setLevel(logging.DEBUG)
    json_format = jsonlogger.JsonFormatter(
        "%(asctime)s %(name)s %(levelname)s %(message)s"
    )
    file_handler.setFormatter(json_format)

    # Add handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


# Global logger instance
logger = setup_logger()
