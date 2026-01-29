"""
Quick test to verify blog labels/tags are being added
"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from src.blogger_publisher import BloggerPublisher

def test_labels():
    print("="*80)
    print("TESTING BLOG LABELS/TAGS")
    print("="*80)

    # Initialize publisher
    publisher = BloggerPublisher()
    publisher.authenticate()

    # Get blog
    blogs = publisher.get_blogs()
    if not blogs:
        print("ERROR: No blogs found")
        return

    blog_id = blogs[0]['id']
    print(f"\nUsing blog: {blogs[0]['name']}")

    # Test post with explicit labels
    test_labels = ["TestTag1", "TestTag2", "Python", "AI", "Tutorial"]
    print(f"\nTesting with labels: {test_labels}")

    result = publisher.publish_post(
        blog_id=blog_id,
        title="Label Test Post - Please Delete",
        content="<h1>Testing Labels</h1><p>This is a test post to verify labels/tags are working. Please delete this post.</p>",
        labels=test_labels,
        is_draft=True  # Save as draft so it doesn't clutter your blog
    )

    print("\n" + "="*80)
    if result['success']:
        print("SUCCESS!")
        print(f"   Post ID: {result['post_id']}")
        print(f"   URL: {result['url']}")
        print(f"   Status: {result['status']}")
        print(f"   Labels sent: {test_labels}")
        print(f"   Labels returned: {result.get('labels', 'Not in response')}")
        print("\nCheck your blog drafts to verify labels appear!")
        print(f"   Visit: {blogs[0]['url']}")
    else:
        print("FAILED!")
        print(f"   Error: {result['message']}")

    print("="*80)

if __name__ == "__main__":
    test_labels()
