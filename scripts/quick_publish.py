"""
Quick Publish - Publish posts immediately
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
    logger.info("📰 QUICK PUBLISH - 10 POSTS")
    logger.info("="*80)

    # Get blog ID from environment
    blog_id = os.getenv('BLOGGER_BLOG_ID')
    if not blog_id:
        logger.error("BLOGGER_BLOG_ID not found in .env file")
        return

    logger.info(f"Blog ID: {blog_id}")
    logger.info("Initializing trending blogger...")

    # Initialize trending blogger
    trending_blogger = TrendingBlogger(blog_id=blog_id)

    # Run batch of 10 posts
    logger.info("Starting publication of 10 posts...")
    trending_blogger.run_daily_batch(num_posts=10)

    logger.info("="*80)
    logger.info("QUICK PUBLISH COMPLETE")
    logger.info("="*80)

if __name__ == "__main__":
    main()
