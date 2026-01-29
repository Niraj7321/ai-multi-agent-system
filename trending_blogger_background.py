"""
Trending Blogger - Background Service Version
Runs in background without user interaction
"""
import sys
import io
import os
import time
import schedule
from datetime import datetime
import logging

# Fix Windows console encoding issues
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from src.blogger_publisher import BloggerPublisher
from trending_blogger import TrendingBlogger

# Set up logging
logging.basicConfig(
    filename='logs/background_service.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_blog_id():
    """
    Get blog ID from environment or config file
    """
    # Try environment variable first
    blog_id = os.getenv('BLOGGER_BLOG_ID')

    if blog_id:
        return blog_id

    # Try config file
    config_file = 'blog_config.txt'
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            blog_id = f.read().strip()
            return blog_id

    # Otherwise, get from API
    try:
        publisher = BloggerPublisher()
        publisher.authenticate()
        blogs = publisher.get_blogs()

        if blogs:
            blog_id = blogs[0]['id']

            # Save for next time
            with open(config_file, 'w') as f:
                f.write(blog_id)

            logging.info(f"Using blog: {blogs[0]['name']} (ID: {blog_id})")
            return blog_id
    except Exception as e:
        logging.error(f"Failed to get blog ID: {str(e)}")
        return None

def run_scheduled_batch():
    """
    Run the scheduled batch
    """
    try:
        logging.info("="*80)
        logging.info("Starting scheduled trending topics batch")

        blog_id = get_blog_id()
        if not blog_id:
            logging.error("No blog ID configured. Exiting.")
            return

        # Initialize trending blogger
        trending_blogger = TrendingBlogger(blog_id=blog_id)

        # Run batch (5 posts)
        trending_blogger.run_daily_batch(num_posts=5)

        logging.info("Scheduled batch completed successfully")
        logging.info("="*80)

    except Exception as e:
        logging.error(f"Error in scheduled batch: {str(e)}")
        logging.exception("Full traceback:")

def main():
    """
    Main background service
    """
    logging.info("="*80)
    logging.info("TRENDING TOPICS BLOGGER - BACKGROUND SERVICE STARTED")
    logging.info(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logging.info("="*80)

    # Get configuration
    schedule_time = os.getenv('BLOGGER_SCHEDULE_TIME', '09:00')
    num_posts = int(os.getenv('BLOGGER_NUM_POSTS', '5'))

    logging.info(f"Configuration:")
    logging.info(f"  Schedule Time: {schedule_time}")
    logging.info(f"  Posts per day: {num_posts}")

    # Verify blog ID
    blog_id = get_blog_id()
    if not blog_id:
        logging.error("Failed to get blog ID. Service cannot start.")
        sys.exit(1)

    logging.info(f"  Blog ID: {blog_id}")
    logging.info("="*80)

    # Schedule the job
    schedule.every().day.at(schedule_time).do(run_scheduled_batch)

    logging.info(f"Service scheduled to run daily at {schedule_time}")
    logging.info("Service is now running in background...")
    logging.info("Press Ctrl+C to stop (if running in foreground)")

    # Run immediately on start (optional, comment out if you don't want this)
    # run_scheduled_batch()

    # Main loop
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        logging.info("Service stopped by user (Ctrl+C)")
    except Exception as e:
        logging.error(f"Service crashed: {str(e)}")
        logging.exception("Full traceback:")
    finally:
        logging.info("="*80)
        logging.info("BACKGROUND SERVICE STOPPED")
        logging.info(f"Stopped at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logging.info("="*80)

if __name__ == "__main__":
    main()
