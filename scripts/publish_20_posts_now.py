"""
Publish 20 Blog Posts Immediately
Builds content base for AdSense approval
"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from trending_blogger import TrendingBlogger
from src.blogger_publisher import BloggerPublisher
from datetime import datetime
import time

def main():
    print("="*80)
    print("PUBLISHING 20 BLOG POSTS NOW")
    print("="*80)
    print("\nThis will take approximately 1-2 hours")
    print("Each post takes 3-5 minutes to generate with AI\n")

    # Get blog information
    print("Step 1: Getting blog information...")
    publisher = BloggerPublisher()
    publisher.authenticate()
    blogs = publisher.get_blogs()

    if not blogs:
        print("ERROR: No blogs found")
        return

    blog = blogs[0]
    print(f"Using blog: {blog['name']}")
    print(f"URL: {blog['url']}")

    # Initialize trending blogger
    print("\nStep 2: Initializing AI blog generator...")
    trending_blogger = TrendingBlogger(blog_id=blog['id'])

    # Define 20 trending topics (mix of evergreen and current)
    topics = [
        # AI & Machine Learning
        "Latest AI Development Tools and Frameworks in 2026",
        "Getting Started with Large Language Models",
        "Machine Learning Best Practices for Beginners",
        "Deep Learning Neural Networks Explained",
        "AI Ethics and Responsible AI Development",

        # Web Development
        "Modern Web Development with React and Next.js",
        "Building Progressive Web Apps in 2026",
        "RESTful API Design Best Practices",
        "Web Performance Optimization Techniques",
        "Full Stack Development Roadmap 2026",

        # Python Programming
        "Python for Data Science: A Complete Guide",
        "Advanced Python Programming Techniques",
        "Building Web Applications with Django",
        "Python Automation Scripts for Developers",
        "Python Best Practices and Code Style",

        # Cloud & DevOps
        "Cloud Computing Fundamentals and AWS Basics",
        "Docker and Kubernetes for Beginners",
        "CI/CD Pipeline Best Practices",
        "DevOps Tools and Workflows in 2026",
        "Microservices Architecture Explained"
    ]

    print(f"\nStep 3: Publishing {len(topics)} blog posts...")
    print("="*80)

    start_time = datetime.now()
    success_count = 0
    failed_count = 0

    for i, topic in enumerate(topics, 1):
        print(f"\n[{i}/{len(topics)}] Topic: {topic}")
        print("-"*80)

        try:
            # Generate and publish post
            post_start = datetime.now()
            success = trending_blogger.generate_and_publish_post(topic, i)
            post_duration = (datetime.now() - post_start).total_seconds() / 60

            if success:
                success_count += 1
                print(f"SUCCESS! Published in {post_duration:.1f} minutes")
            else:
                failed_count += 1
                print(f"FAILED after {post_duration:.1f} minutes")

            # Progress update
            remaining = len(topics) - i
            avg_time = (datetime.now() - start_time).total_seconds() / 60 / i
            est_remaining = remaining * avg_time

            print(f"Progress: {i}/{len(topics)} ({i/len(topics)*100:.0f}%)")
            print(f"Success: {success_count} | Failed: {failed_count}")
            print(f"Estimated time remaining: {est_remaining:.0f} minutes")

            # Small delay between posts (30 seconds)
            if i < len(topics):
                print("\nWaiting 30 seconds before next post...")
                time.sleep(30)

        except Exception as e:
            print(f"ERROR: {str(e)}")
            failed_count += 1

    # Final summary
    end_time = datetime.now()
    total_duration = (end_time - start_time).total_seconds() / 60

    print("\n" + "="*80)
    print("BATCH PUBLISHING COMPLETE")
    print("="*80)
    print(f"Successfully published: {success_count}/{len(topics)}")
    print(f"Failed: {failed_count}/{len(topics)}")
    print(f"Total time: {total_duration:.1f} minutes ({total_duration/60:.1f} hours)")
    print(f"Average per post: {total_duration/len(topics):.1f} minutes")
    print(f"\nYour blog now has {success_count} new posts!")
    print(f"Visit: {blog['url']}")
    print("="*80)

    # Next steps
    print("\nNEXT STEPS FOR ADSENSE APPROVAL:")
    print("1. Add About, Contact, and Privacy Policy pages")
    print("2. Improve blog theme/design")
    print("3. Let automated system continue (5 posts/day)")
    print("4. Wait 2-3 weeks for content to age")
    print("5. Get some traffic (share on social media)")
    print("6. Apply to AdSense again")
    print(f"\nWith {success_count} posts now + 5/day automated,")
    print("you'll have 50+ posts in 1 week, 100+ in 2 weeks!")

if __name__ == "__main__":
    main()
