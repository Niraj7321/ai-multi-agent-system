"""
Test Blogger - Run One Post Immediately
For testing the blog publishing system
"""
import sys
from trending_blogger import TrendingBlogger
from src.blogger_publisher import BloggerPublisher
from src.logger import logger

def main():
    print("="*80)
    print("🧪 TESTING BLOGGER - PUBLISH ONE POST NOW")
    print("="*80)

    # Get blog ID
    print("\n📚 Getting blog information...")
    publisher = BloggerPublisher()
    publisher.authenticate()
    blogs = publisher.get_blogs()

    if not blogs:
        print("❌ No blogs found. Please create a blog at blogger.com first.")
        return

    blog = blogs[0]
    print(f"✅ Using blog: {blog['name']}")
    print(f"   URL: {blog['url']}")

    # Initialize trending blogger
    print("\n🔥 Initializing trending blogger...")
    trending_blogger = TrendingBlogger(blog_id=blog['id'])

    # Test topic
    test_topic = "Latest AI Development Tools and Frameworks in 2026"
    print(f"\n📰 Test Topic: {test_topic}")

    # Generate and publish
    print("\n🚀 Generating and publishing post...")
    print("   This may take 2-3 minutes...")

    success = trending_blogger.generate_and_publish_post(test_topic, 1)

    if success:
        print("\n" + "="*80)
        print("✅ SUCCESS! Blog post published!")
        print("="*80)
        print(f"\n🔗 Check your blog: {blog['url']}")
    else:
        print("\n" + "="*80)
        print("❌ FAILED - Check logs for details")
        print("="*80)
        print(f"   Log file: logs/app.log")

if __name__ == "__main__":
    main()
