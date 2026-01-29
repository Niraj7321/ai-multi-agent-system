"""
Automated Daily Blog Publisher
Automatically generates and publishes 5 SEO-friendly blog posts daily to Blogger
"""
import sys
import io
import time
import schedule
from datetime import datetime
from typing import List, Dict
import random

# Fix Windows console encoding issues
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from src.crew_manager import CrewManager
from src.blogger_publisher import BloggerPublisher
from src.logger import logger


class AutomatedBlogger:
    """
    Automated blog publisher that generates and publishes content daily
    """

    def __init__(self, blog_id: str, use_anthropic: bool = True, model_name: str = "claude-sonnet-4-20250514"):
        """
        Initialize the automated blogger

        Args:
            blog_id: Your Blogger blog ID (get from blogger_publisher.get_blogs())
            use_anthropic: Use Anthropic Claude (True) or OpenAI (False)
            model_name: Model to use for content generation
        """
        self.blog_id = blog_id
        self.crew_manager = CrewManager(
            model_name=model_name,
            use_anthropic=use_anthropic,
            temperature=0.7
        )
        self.blogger_publisher = BloggerPublisher()
        self.blogger_publisher.authenticate()

        # SEO-friendly blog topics (you can customize this list)
        self.topic_categories = {
            "AI & Machine Learning": [
                "Introduction to Machine Learning for Beginners 2026",
                "Deep Learning vs Machine Learning: Complete Guide",
                "Natural Language Processing Applications in Business",
                "Computer Vision Projects for Beginners",
                "AI Ethics and Responsible AI Development",
                "Getting Started with TensorFlow and PyTorch",
                "Transformer Models Explained Simply",
                "AI in Healthcare: Current Applications",
                "Building Chatbots with GPT Models",
                "AutoML: Automated Machine Learning Guide"
            ],
            "Python Programming": [
                "Python Best Practices for Clean Code 2026",
                "Async Programming in Python Complete Guide",
                "Python Data Structures and Algorithms",
                "Building REST APIs with FastAPI",
                "Python for Data Analysis with Pandas",
                "Web Scraping with Python BeautifulSoup",
                "Python Testing with Pytest Guide",
                "Object-Oriented Programming in Python",
                "Python Decorators Explained with Examples",
                "Python Type Hints and Type Checking"
            ],
            "Web Development": [
                "React Best Practices 2026",
                "Building Progressive Web Apps (PWA)",
                "Modern CSS: Flexbox and Grid Layout",
                "JavaScript ES2026 New Features",
                "Node.js Performance Optimization",
                "Full Stack Development with Next.js",
                "RESTful API Design Best Practices",
                "GraphQL vs REST API Comparison",
                "Web Security Best Practices 2026",
                "Responsive Web Design Techniques"
            ],
            "Data Science": [
                "Data Science Project Workflow Guide",
                "Exploratory Data Analysis with Python",
                "Feature Engineering Techniques",
                "Time Series Forecasting Methods",
                "A/B Testing Statistical Analysis",
                "Data Visualization with Matplotlib",
                "SQL for Data Analysis Complete Guide",
                "Big Data Processing with Apache Spark",
                "Data Cleaning and Preprocessing",
                "Predictive Modeling Best Practices"
            ],
            "DevOps & Cloud": [
                "Docker for Beginners Complete Guide",
                "Kubernetes Deployment Strategies",
                "CI/CD Pipeline Setup with GitHub Actions",
                "AWS Cloud Services Overview 2026",
                "Infrastructure as Code with Terraform",
                "Microservices Architecture Patterns",
                "Container Orchestration Best Practices",
                "Cloud Cost Optimization Strategies",
                "Monitoring and Logging with ELK Stack",
                "GitOps Workflow Implementation"
            ]
        }

    def generate_seo_tags(self, topic: str, category: str) -> List[str]:
        """
        Generate SEO-friendly tags/labels for a blog post

        Args:
            topic: Blog post topic
            category: Topic category

        Returns:
            List of relevant tags
        """
        # Base category tag
        tags = [category.replace(" & ", " ").replace(" ", "")]

        # Extract keywords from topic
        keywords = topic.lower().split()
        common_words = {'a', 'an', 'the', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from', 'complete', 'guide', 'tutorial', 'introduction', '2026'}

        # Add meaningful keywords as tags
        for word in keywords:
            if word not in common_words and len(word) > 3:
                tags.append(word.capitalize())

        # Add year tag
        tags.append("2026")

        # Add generic relevant tags
        generic_tags = ["Tutorial", "Programming", "Technology", "Development", "Guide"]
        tags.extend(random.sample(generic_tags, min(2, len(generic_tags))))

        # Remove duplicates and limit to 8 tags (Blogger recommendation)
        return list(dict.fromkeys(tags))[:8]

    def get_daily_topics(self) -> List[Dict[str, str]]:
        """
        Get 5 diverse topics for today's blog posts

        Returns:
            List of dicts with 'topic', 'category', and 'tags'
        """
        topics = []
        used_topics = set()

        # Select one topic from each category to ensure diversity
        for category, category_topics in self.topic_categories.items():
            # Shuffle to get random topics each day
            available = [t for t in category_topics if t not in used_topics]
            if available:
                topic = random.choice(available)
                used_topics.add(topic)
                tags = self.generate_seo_tags(topic, category)

                topics.append({
                    'topic': topic,
                    'category': category,
                    'tags': tags
                })

            if len(topics) == 5:
                break

        return topics

    def generate_and_publish_post(self, topic: str, tags: List[str], post_number: int) -> bool:
        """
        Generate and publish a single blog post

        Args:
            topic: Blog post topic
            tags: SEO tags for the post
            post_number: Post number (1-5) for logging

        Returns:
            True if successful, False otherwise
        """
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\n{'='*80}")
            print(f"[{timestamp}] Generating Post #{post_number}/5: {topic}")
            print(f"{'='*80}")

            # Generate content
            print("🔬 Research Agent working...")
            result = self.crew_manager.execute_research_workflow(
                topic=topic,
                content_type="blog post"
            )

            if not result['success']:
                print(f"❌ Content generation failed: {result['message']}")
                return False

            print("✅ Content generated successfully!")

            # Extract title from content
            content = str(result['result'])
            lines = content.split('\n')
            title = lines[0].replace('#', '').strip() if lines else topic

            print(f"📝 Title: {title}")
            print(f"🏷️  Tags: {', '.join(tags)}")

            # Publish to Blogger
            print("🚀 Publishing to Blogger...")
            publish_result = self.blogger_publisher.publish_post(
                blog_id=self.blog_id,
                title=title,
                content=content,
                labels=tags,
                is_draft=False  # Publish immediately
            )

            if publish_result['success']:
                print(f"✅ Published successfully!")
                print(f"🔗 URL: {publish_result['url']}")
                logger.info(f"Published post #{post_number}: {title} - {publish_result['url']}")
                return True
            else:
                print(f"❌ Publishing failed: {publish_result['message']}")
                logger.error(f"Failed to publish post #{post_number}: {publish_result['message']}")
                return False

        except Exception as e:
            print(f"❌ Error: {str(e)}")
            logger.error(f"Error generating/publishing post #{post_number}: {str(e)}")
            return False

    def run_daily_batch(self):
        """
        Generate and publish 5 blog posts
        """
        start_time = datetime.now()
        print("\n" + "="*80)
        print(f"🤖 AUTOMATED BLOG PUBLISHER - Daily Batch Started")
        print(f"⏰ Time: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*80)

        # Get today's topics
        topics = self.get_daily_topics()

        success_count = 0
        failed_count = 0

        # Generate and publish each post
        for i, topic_data in enumerate(topics, 1):
            # Add delay between posts to avoid rate limiting (2 minutes)
            if i > 1:
                print(f"\n⏳ Waiting 2 minutes before next post to avoid rate limiting...")
                time.sleep(120)

            success = self.generate_and_publish_post(
                topic=topic_data['topic'],
                tags=topic_data['tags'],
                post_number=i
            )

            if success:
                success_count += 1
            else:
                failed_count += 1

        # Summary
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds() / 60

        print("\n" + "="*80)
        print(f"📊 DAILY BATCH SUMMARY")
        print("="*80)
        print(f"✅ Successfully published: {success_count}/5")
        print(f"❌ Failed: {failed_count}/5")
        print(f"⏱️  Total time: {duration:.1f} minutes")
        print(f"🕐 Completed at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*80 + "\n")

        logger.info(f"Daily batch completed: {success_count} successful, {failed_count} failed, {duration:.1f} minutes")

    def schedule_daily_posts(self, time_str: str = "09:00"):
        """
        Schedule daily blog posts at a specific time

        Args:
            time_str: Time in HH:MM format (24-hour) to run daily posts
        """
        print(f"\n🔔 Scheduling daily posts at {time_str} every day")
        print(f"📅 Blog ID: {self.blog_id}")
        print("⚙️  Press Ctrl+C to stop the scheduler\n")

        # Schedule the job
        schedule.every().day.at(time_str).do(self.run_daily_batch)

        # Run the scheduler loop
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
        except KeyboardInterrupt:
            print("\n\n👋 Scheduler stopped by user")


def main():
    """
    Main function to run the automated blogger
    """
    print("="*80)
    print("🤖 AUTOMATED DAILY BLOG PUBLISHER")
    print("="*80)
    print("\nThis tool will automatically generate and publish 5 SEO-friendly")
    print("blog posts to your Blogger blog every day.\n")

    # Step 1: Get blog ID
    print("Step 1: Getting your blog information...")
    publisher = BloggerPublisher()
    publisher.authenticate()
    blogs = publisher.get_blogs()

    if not blogs:
        print("❌ No blogs found. Please create a blog at blogger.com first.")
        return

    print(f"\n📚 Found {len(blogs)} blog(s):")
    for i, blog in enumerate(blogs, 1):
        print(f"  {i}. {blog['name']} - {blog['url']}")

    # Select blog
    if len(blogs) == 1:
        selected_blog = blogs[0]
        print(f"\n✅ Using blog: {selected_blog['name']}")
    else:
        choice = int(input(f"\nSelect blog (1-{len(blogs)}): ")) - 1
        selected_blog = blogs[choice]

    blog_id = selected_blog['id']

    # Step 2: Choose mode
    print("\n" + "="*80)
    print("Choose mode:")
    print("  1. Run once now (publish 5 posts immediately)")
    print("  2. Schedule daily (publish 5 posts every day at specified time)")
    print("="*80)

    mode = input("\nEnter choice (1 or 2): ").strip()

    # Initialize automated blogger
    auto_blogger = AutomatedBlogger(blog_id=blog_id)

    if mode == "1":
        # Run once
        print("\n🚀 Starting batch generation and publishing...")
        auto_blogger.run_daily_batch()
        print("\n✅ Done! All posts have been processed.")

    elif mode == "2":
        # Schedule daily
        time_input = input("\nEnter time to publish daily (HH:MM in 24-hour format, e.g., 09:00): ").strip()
        if not time_input:
            time_input = "09:00"

        print(f"\n✅ Will publish 5 posts daily at {time_input}")
        print("📝 The scheduler will keep running. Press Ctrl+C to stop.\n")

        auto_blogger.schedule_daily_posts(time_str=time_input)

    else:
        print("❌ Invalid choice. Exiting.")


if __name__ == "__main__":
    main()
