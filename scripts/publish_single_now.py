"""
Publish Single Post Now - Fast single post publishing
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from trending_blogger import TrendingBlogger
from src.logger import logger
import os

def main():
    logger.info("="*80)
    logger.info("📰 PUBLISHING SINGLE POST NOW")
    logger.info("="*80)

    # Get blog ID from environment
    blog_id = os.getenv('BLOGGER_BLOG_ID')
    if not blog_id:
        logger.error("BLOGGER_BLOG_ID not found in .env file")
        return

    logger.info(f"Blog ID: {blog_id}")

    # Initialize trending blogger
    trending_blogger = TrendingBlogger(blog_id=blog_id)

    # Single topic
    topic = "Latest AI and Machine Learning Development Trends in 2026"

    logger.info(f"Topic: {topic}")
    logger.info("Starting post generation...")

    # Publish one post
    success = trending_blogger.generate_and_publish_post(topic, 1)

    if success:
        logger.info("="*80)
        logger.info("✅ POST PUBLISHED SUCCESSFULLY!")
        logger.info("="*80)
    else:
        logger.error("❌ PUBLISHING FAILED")

if __name__ == "__main__":
    main()
