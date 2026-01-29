"""Quick script to get blog ID"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from src.blogger_publisher import BloggerPublisher

try:
    print("Connecting to Blogger...")
    publisher = BloggerPublisher()
    publisher.authenticate()

    blogs = publisher.get_blogs()

    if blogs:
        for blog in blogs:
            print(f"\nBlog: {blog['name']}")
            print(f"URL: {blog['url']}")
            print(f"ID: {blog['id']}")

        # Save first blog ID
        blog_id = blogs[0]['id']
        with open('blog_config.txt', 'w') as f:
            f.write(blog_id)

        print(f"\nSaved blog ID to blog_config.txt: {blog_id}")
    else:
        print("No blogs found!")

except Exception as e:
    print(f"Error: {str(e)}")
    import traceback
    traceback.print_exc()
