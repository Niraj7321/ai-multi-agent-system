"""
Trending Topics Automated Blog Publisher
Automatically finds hot/trending topics and publishes SEO-optimized blog posts daily
"""
import sys
import io
import time
import schedule
import os
from datetime import datetime
from typing import List, Dict, Optional
import random
import requests
from bs4 import BeautifulSoup

# Fix Windows console encoding issues
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from src.crew_manager import CrewManager
from src.blogger_publisher import BloggerPublisher
from src.logger import logger


class TrendingTopicsFinder:
    """
    Finds trending and hot topics from various sources
    """

    def __init__(self):
        self.sources = {
            'github': self.get_github_trending,
            'hackernews': self.get_hackernews_trending,
            'reddit': self.get_reddit_trending,
            'google_trends': self.get_google_trends_topics
        }

    def get_github_trending(self) -> List[str]:
        """Get trending repositories from GitHub"""
        try:
            url = "https://github.com/trending"
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')

            trending_repos = []
            repos = soup.find_all('article', class_='Box-row')[:10]

            for repo in repos:
                try:
                    title_elem = repo.find('h2', class_='h3')
                    if title_elem:
                        repo_name = title_elem.get_text().strip().replace('\n', ' ')
                        desc_elem = repo.find('p', class_='col-9')
                        desc = desc_elem.get_text().strip() if desc_elem else ""

                        # Create topic from repo name and description
                        topic = f"{repo_name}: {desc}" if desc else repo_name
                        trending_repos.append(topic)
                except Exception as e:
                    continue

            return trending_repos[:5]
        except Exception as e:
            logger.warning(f"⚠️  Error fetching GitHub trends: {str(e)}")
            return []

    def get_hackernews_trending(self) -> List[str]:
        """Get trending stories from Hacker News"""
        try:
            url = "https://hacker-news.firebaseio.com/v0/topstories.json"
            response = requests.get(url, timeout=10)
            story_ids = response.json()[:10]

            trending_stories = []
            for story_id in story_ids[:5]:
                story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
                story_response = requests.get(story_url, timeout=5)
                story = story_response.json()

                if story and 'title' in story:
                    trending_stories.append(story['title'])

            return trending_stories
        except Exception as e:
            logger.warning(f"⚠️  Error fetching Hacker News trends: {str(e)}")
            return []

    def get_reddit_trending(self) -> List[str]:
        """Get trending topics from Reddit programming communities"""
        try:
            subreddits = ['programming', 'python', 'webdev', 'MachineLearning', 'datascience']
            trending_topics = []

            for subreddit in subreddits[:3]:
                url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=5"
                headers = {'User-Agent': 'TrendingBlogBot/1.0'}
                response = requests.get(url, headers=headers, timeout=10)

                if response.status_code == 200:
                    data = response.json()
                    posts = data.get('data', {}).get('children', [])

                    for post in posts[:2]:
                        title = post['data']['title']
                        trending_topics.append(title)

                time.sleep(1)  # Rate limiting

            return trending_topics[:5]
        except Exception as e:
            logger.warning(f"⚠️  Error fetching Reddit trends: {str(e)}")
            return []

    def get_google_trends_topics(self) -> List[str]:
        """Get trending search topics (simulated - you can integrate with pytrends)"""
        # Note: For real Google Trends, use pytrends library
        # This is a fallback with general trending tech topics
        trending_tech = [
            "AI Code Generation Tools 2026",
            "Quantum Computing Breakthroughs",
            "Web3 Development Tutorial",
            "Edge Computing Applications",
            "Serverless Architecture Best Practices",
            "DevOps Security Automation",
            "Low-Code Development Platforms",
            "API-First Development Approach",
            "Cloud Native Applications",
            "Microservices Design Patterns"
        ]
        return random.sample(trending_tech, min(5, len(trending_tech)))

    def get_all_trending_topics(self) -> List[str]:
        """
        Aggregate trending topics from all sources

        Returns:
            List of unique trending topics
        """
        all_topics = []

        logger.info("\n🔍 Searching for trending topics...")

        for source_name, source_func in self.sources.items():
            try:
                logger.info(f"  📡 Fetching from {source_name}...")
                topics = source_func()
                all_topics.extend(topics)
                logger.info(f"  ✅ Found {len(topics)} topics from {source_name}")
            except Exception as e:
                logger.warning(f"  ⚠️  Error with {source_name}: {str(e)}")

        # Remove duplicates while preserving order
        unique_topics = list(dict.fromkeys(all_topics))

        logger.info(f"\n✅ Total unique trending topics found: {len(unique_topics)}")
        return unique_topics


class TrendingBlogger:
    """
    Automated blogger that creates posts based on trending topics
    """

    def __init__(self, blog_id: str, use_anthropic: bool = True, model_name: str = "claude-sonnet-4-20250514"):
        """
        Initialize the trending blogger

        Args:
            blog_id: Your Blogger blog ID
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
        self.trending_finder = TrendingTopicsFinder()
        self.unsplash_api_key = os.getenv('UNSPLASH_ACCESS_KEY')

    def get_topic_image(self, topic: str) -> Optional[str]:
        """
        Fetch a relevant image from Unsplash based on topic

        Args:
            topic: Blog topic/keywords

        Returns:
            Image URL or None if not found
        """
        if not self.unsplash_api_key or self.unsplash_api_key == 'your_unsplash_access_key_here':
            logger.warning("⚠️  Unsplash API key not configured. Skipping image.")
            return None

        try:
            # Extract keywords for image search
            keywords = self.extract_keywords(topic)
            search_query = ' '.join(keywords[:3])  # Use top 3 keywords

            logger.info(f"🖼️  Searching for image: '{search_query}'")

            # Unsplash API search
            url = "https://api.unsplash.com/search/photos"
            headers = {
                "Authorization": f"Client-ID {self.unsplash_api_key}"
            }
            params = {
                "query": search_query,
                "per_page": 1,
                "orientation": "landscape"
            }

            response = requests.get(url, headers=headers, params=params, timeout=10)

            if response.status_code == 200:
                data = response.json()
                if data['results']:
                    image_url = data['results'][0]['urls']['regular']
                    photographer = data['results'][0]['user']['name']
                    logger.info(f"✅ Found image by {photographer}")
                    return image_url
                else:
                    logger.warning(f"⚠️  No images found for '{search_query}'")
                    return None
            else:
                logger.warning(f"⚠️  Unsplash API error: {response.status_code}")
                return None

        except Exception as e:
            logger.warning(f"⚠️  Error fetching image: {str(e)}")
            return None

    def extract_keywords(self, topic: str) -> List[str]:
        """
        Extract keywords from topic for SEO tags

        Args:
            topic: Topic string

        Returns:
            List of keywords
        """
        # Remove common words
        common_words = {
            'a', 'an', 'the', 'in', 'on', 'at', 'to', 'for', 'of', 'with',
            'by', 'from', 'and', 'or', 'but', 'is', 'are', 'was', 'were',
            'how', 'what', 'why', 'when', 'where', 'which', '2026', '2025'
        }

        # Split and clean
        words = topic.lower().replace(':', ' ').replace('-', ' ').split()
        keywords = [w.capitalize() for w in words if w not in common_words and len(w) > 3]

        return keywords[:5]

    def generate_seo_tags(self, topic: str) -> List[str]:
        """
        Generate SEO-friendly tags from trending topic

        Args:
            topic: Trending topic

        Returns:
            List of SEO tags
        """
        tags = []

        # Extract keywords from topic
        keywords = self.extract_keywords(topic)
        tags.extend(keywords)

        # Add category-based tags
        tech_categories = {
            'ai': ['AI', 'MachineLearning', 'ArtificialIntelligence'],
            'python': ['Python', 'Programming', 'PythonDev'],
            'web': ['WebDevelopment', 'WebDev', 'JavaScript'],
            'data': ['DataScience', 'Analytics', 'BigData'],
            'cloud': ['Cloud', 'DevOps', 'CloudComputing'],
            'security': ['Cybersecurity', 'Security', 'InfoSec']
        }

        topic_lower = topic.lower()
        for category, category_tags in tech_categories.items():
            if category in topic_lower:
                tags.extend(category_tags[:2])
                break

        # Add generic tags
        tags.extend(['Technology', 'Tutorial', '2026', 'Trending'])

        # Remove duplicates and limit to 8
        unique_tags = list(dict.fromkeys(tags))[:8]
        return unique_tags

    def refine_topic_for_blog(self, raw_topic: str) -> str:
        """
        Refine raw trending topic into a blog-friendly title

        Args:
            raw_topic: Raw topic from trending sources

        Returns:
            Refined blog topic
        """
        # Clean up the topic
        topic = raw_topic.strip()

        # If it's too long, extract main subject
        if len(topic) > 100:
            # Take first sentence or first 100 chars
            topic = topic.split('.')[0][:100]

        # Make it more blog-friendly
        blog_style_prefixes = [
            "Complete Guide to",
            "Introduction to",
            "Getting Started with",
            "Understanding",
            "Building with",
            "Mastering"
        ]

        # If it doesn't have a blog-style format, add one randomly
        if not any(prefix.lower() in topic.lower() for prefix in ['guide', 'tutorial', 'how to', 'introduction']):
            prefix = random.choice(blog_style_prefixes)
            topic = f"{prefix} {topic}"

        # Add year for SEO
        if '2026' not in topic and '2025' not in topic:
            topic = f"{topic} 2026"

        return topic

    def generate_and_publish_post(self, topic: str, post_number: int) -> bool:
        """
        Generate and publish a blog post for a trending topic

        Args:
            topic: Trending topic
            post_number: Post number for logging

        Returns:
            True if successful, False otherwise
        """
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            logger.info(f"\n{'='*80}")
            logger.info(f"[{timestamp}] Post #{post_number}/5")
            logger.info(f"📰 Trending Topic: {topic}")
            logger.info(f"{'='*80}")

            # Refine topic for blog
            blog_topic = self.refine_topic_for_blog(topic)
            logger.info(f"📝 Blog Topic: {blog_topic}")

            # Generate SEO tags
            tags = self.generate_seo_tags(topic)
            logger.info(f"🏷️  Tags: {', '.join(tags)}")

            # Generate content
            logger.info("\n🔬 AI Agents working...")
            result = self.crew_manager.execute_research_workflow(
                topic=blog_topic,
                content_type="blog post"
            )

            if not result['success']:
                logger.error(f"❌ Content generation failed: {result['message']}")
                return False

            logger.info("✅ Content generated successfully!")

            # Extract title from content
            content = str(result['result'])
            lines = content.split('\n')
            title = lines[0].replace('#', '').strip() if lines else blog_topic

            logger.info(f"📰 Final Title: {title}")

            # Get featured image (disabled for faster publishing)
            # image_url = self.get_topic_image(blog_topic)
            image_url = None

            # Publish to Blogger
            logger.info("🚀 Publishing to Blogger...")
            publish_result = self.blogger_publisher.publish_post(
                blog_id=self.blog_id,
                title=title,
                content=content,
                labels=tags,
                image_url=image_url,
                is_draft=False
            )

            if publish_result['success']:
                logger.info(f"✅ Published successfully!")
                logger.info(f"🔗 URL: {publish_result['url']}")
                logger.info(f"Published trending post #{post_number}: {title} - {publish_result['url']}")
                return True
            else:
                logger.error(f"❌ Publishing failed: {publish_result['message']}")
                logger.error(f"Failed to publish trending post #{post_number}: {publish_result['message']}")
                return False

        except Exception as e:
            logger.error(f"❌ Error: {str(e)}")
            logger.error(f"Error with trending post #{post_number}: {str(e)}")
            return False

    def run_daily_batch(self, num_posts: int = 5):
        """
        Find trending topics and publish blog posts

        Args:
            num_posts: Number of posts to publish (default: 5)
        """
        start_time = datetime.now()
        logger.info("="*80)
        logger.info(f"🔥 TRENDING TOPICS BLOG PUBLISHER - Daily Batch Started")
        logger.info(f"⏰ Time: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info("="*80)

        # Find trending topics
        trending_topics = self.trending_finder.get_all_trending_topics()

        if not trending_topics:
            logger.warning("⚠️  No trending topics found. Using fallback topics.")
            trending_topics = [
                "Latest AI Development Tools and Frameworks",
                "Modern Web Development Best Practices",
                "Python Data Analysis Techniques",
                "Cloud Computing Trends 2026",
                "DevOps Automation Strategies"
            ]

        # Select topics for today
        selected_topics = random.sample(trending_topics, min(num_posts, len(trending_topics)))

        logger.info(f"\n📋 Selected {len(selected_topics)} topics for today:")
        for i, topic in enumerate(selected_topics, 1):
            logger.info(f"  {i}. {topic[:80]}...")

        success_count = 0
        failed_count = 0

        # Generate and publish each post
        for i, topic in enumerate(selected_topics, 1):
            # Add delay between posts (30 seconds for faster batch publishing)
            if i > 1:
                logger.info(f"\n⏳ Waiting 30 seconds before next post...")
                time.sleep(30)

            success = self.generate_and_publish_post(topic, i)

            if success:
                success_count += 1
            else:
                failed_count += 1

        # Summary
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds() / 60

        logger.info("\n" + "="*80)
        logger.info(f"📊 DAILY BATCH SUMMARY")
        logger.info("="*80)
        logger.info(f"✅ Successfully published: {success_count}/{num_posts}")
        logger.info(f"❌ Failed: {failed_count}/{num_posts}")
        logger.info(f"⏱️  Total time: {duration:.1f} minutes")
        logger.info(f"🕐 Completed at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info("="*80 + "\n")

        logger.info(f"Trending batch completed: {success_count} successful, {failed_count} failed, {duration:.1f} minutes")

    def schedule_daily_posts(self, time_str: str = "09:00", num_posts: int = 5):
        """
        Schedule daily trending blog posts

        Args:
            time_str: Time in HH:MM format (24-hour)
            num_posts: Number of posts per day
        """
        print(f"\n🔔 Scheduling {num_posts} trending posts daily at {time_str}")
        print(f"📅 Blog ID: {self.blog_id}")
        print("⚙️  Press Ctrl+C to stop the scheduler\n")

        # Schedule the job
        schedule.every().day.at(time_str).do(lambda: self.run_daily_batch(num_posts))

        # Run the scheduler loop
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)
        except KeyboardInterrupt:
            print("\n\n👋 Scheduler stopped by user")


def main():
    """
    Main function
    """
    print("="*80)
    print("🔥 TRENDING TOPICS AUTOMATED BLOG PUBLISHER")
    print("="*80)
    print("\nAutomatically finds hot/trending topics and publishes SEO-optimized")
    print("blog posts based on what's currently popular!\n")

    # Get blog ID
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

    # Choose mode
    print("\n" + "="*80)
    print("Choose mode:")
    print("  1. Run once now (find trending topics & publish 5 posts)")
    print("  2. Schedule daily (find trending topics & publish daily)")
    print("="*80)

    mode = input("\nEnter choice (1 or 2): ").strip()

    # Number of posts
    num_posts = input("\nHow many posts per day? (default: 5): ").strip()
    num_posts = int(num_posts) if num_posts else 5

    # Initialize trending blogger
    trending_blogger = TrendingBlogger(blog_id=blog_id)

    if mode == "1":
        # Run once
        print(f"\n🚀 Finding trending topics and publishing {num_posts} posts...")
        trending_blogger.run_daily_batch(num_posts)
        print("\n✅ Done! All posts have been processed.")

    elif mode == "2":
        # Schedule daily
        time_input = input("\nEnter time to publish daily (HH:MM, e.g., 09:00): ").strip()
        if not time_input:
            time_input = "09:00"

        print(f"\n✅ Will find trending topics and publish {num_posts} posts daily at {time_input}")
        print("📝 The scheduler will keep running. Press Ctrl+C to stop.\n")

        trending_blogger.schedule_daily_posts(time_str=time_input, num_posts=num_posts)

    else:
        print("❌ Invalid choice. Exiting.")


if __name__ == "__main__":
    main()
