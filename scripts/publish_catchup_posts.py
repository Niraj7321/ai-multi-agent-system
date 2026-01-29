"""
Catch-up Blog Publishing
Publish posts to make up for missed days
"""
import sys
import io
import os
from pathlib import Path
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Fix Windows console encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from trending_blogger import TrendingBlogger

def main():
    print("="*80)
    print("📰 CATCH-UP BLOG PUBLISHING")
    print("="*80)
    print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("📊 Publishing 10 posts to catch up on missed days...")
    print("="*80)

    # Get blog ID from environment
    blog_id = os.getenv('BLOGGER_BLOG_ID')
    if not blog_id:
        print("❌ Error: BLOGGER_BLOG_ID not found in .env file")
        return

    print(f"\n✅ Blog ID: {blog_id}")

    # Initialize trending blogger with images enabled
    print("🔧 Initializing AI blog publisher...")
    trending_blogger = TrendingBlogger(blog_id=blog_id)

    # Run batch of 10 posts
    print("\n🚀 Starting publication process...\n")
    trending_blogger.run_daily_batch(num_posts=10)

    print("\n" + "="*80)
    print("✅ CATCH-UP PUBLISHING COMPLETE!")
    print(f"⏰ Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80)

if __name__ == "__main__":
    main()
