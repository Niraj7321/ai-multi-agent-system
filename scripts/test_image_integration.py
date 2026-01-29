"""
Test Image Integration for Blog Posts
Quick test to verify Unsplash image fetching works
"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from trending_blogger import TrendingBlogger
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    print("="*80)
    print("🖼️  TESTING IMAGE INTEGRATION")
    print("="*80)

    # Check if Unsplash API key is configured
    api_key = os.getenv('UNSPLASH_ACCESS_KEY')
    if not api_key or api_key == 'your_unsplash_access_key_here':
        print("\n⚠️  WARNING: Unsplash API key not configured!")
        print("\n📝 To add images to your blog posts:")
        print("   1. Go to: https://unsplash.com/developers")
        print("   2. Sign up/login and create a new app")
        print("   3. Copy your Access Key")
        print("   4. Add to .env file:")
        print("      UNSPLASH_ACCESS_KEY=your_actual_key_here")
        print("\n💡 Posts will still publish WITHOUT images if key is missing.")
        print("="*80)
        return

    print(f"\n✅ Unsplash API key found: {api_key[:20]}...")

    # Get blog ID
    blog_id = os.getenv('BLOGGER_BLOG_ID')
    if not blog_id:
        print("❌ BLOGGER_BLOG_ID not found in .env")
        return

    # Initialize blogger
    print(f"\n📚 Initializing TrendingBlogger...")
    blogger = TrendingBlogger(blog_id=blog_id)

    # Test topics
    test_topics = [
        "AI Development Tools",
        "Python Programming",
        "Web Development React",
        "Cloud Computing AWS",
        "Machine Learning"
    ]

    print(f"\n🖼️  Testing image search for {len(test_topics)} topics:")
    print("-"*80)

    success_count = 0
    for i, topic in enumerate(test_topics, 1):
        print(f"\n[{i}/{len(test_topics)}] Topic: {topic}")
        image_url = blogger.get_topic_image(topic)

        if image_url:
            print(f"   ✅ Found: {image_url[:60]}...")
            success_count += 1
        else:
            print(f"   ❌ No image found")

    print("\n" + "="*80)
    print(f"📊 RESULTS: {success_count}/{len(test_topics)} images found")
    print("="*80)

    if success_count > 0:
        print("\n✅ Image integration is working!")
        print("📝 Future blog posts will automatically include relevant images.")
    else:
        print("\n⚠️  No images found. Check your API key and internet connection.")

if __name__ == "__main__":
    main()
