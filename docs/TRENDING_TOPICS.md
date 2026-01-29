# 🔥 Trending Topics Automated Blog Publisher

Automatically discover **hot/trending topics** daily and publish SEO-optimized blog posts based on what's currently popular!

## 🌟 Features

### Trending Topic Discovery
- **GitHub Trending**: Latest trending repositories and projects
- **Hacker News**: Top stories from tech community
- **Reddit**: Hot topics from programming subreddits
- **Google Trends**: Popular search topics (with fallback)

### Intelligent Content Creation
- **Auto-refinement**: Converts raw trending topics into blog-friendly titles
- **SEO Optimization**: Automatically generates relevant tags/labels
- **Original Content**: 100% original, copyright-free blog posts
- **Keyword Extraction**: Smart keyword extraction for maximum SEO

### Automation
- **Daily Scheduling**: Publish at your chosen time automatically
- **Batch Processing**: Generate multiple posts in one run
- **Rate Limiting**: Respects API limits with delays
- **Error Handling**: Graceful fallbacks if trending sources fail

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

All required libraries (requests, beautifulsoup4, schedule) are included.

### 2. Run the Trending Blogger

```bash
python trending_blogger.py
```

### 3. Choose Your Mode

**Option 1: Run Once (Immediate)**
- Finds trending topics right now
- Publishes 5 posts immediately
- Perfect for testing or one-time bulk publishing

**Option 2: Schedule Daily**
- Finds trending topics every day
- Publishes at your specified time
- Keeps running in background

## 📋 How It Works

```
1. 🔍 Search Trending Sources
   ↓
   - GitHub trending repos
   - Hacker News top stories
   - Reddit hot posts
   - Google Trends topics
   ↓

2. 📝 Refine Topics
   ↓
   - "kubernetes/kubernetes"
   → "Complete Guide to Kubernetes 2026"
   ↓

3. 🏷️ Generate SEO Tags
   ↓
   - Extract keywords: Kubernetes, Container, DevOps
   - Add category tags: CloudComputing, Tutorial
   - Add year: 2026
   ↓

4. 🤖 AI Content Generation
   ↓
   - Research Agent: Gathers information
   - Writer Agent: Creates original blog post
   - Reviewer Agent: Quality assurance
   ↓

5. 🚀 Publish to Blogger
   ↓
   - SEO-optimized title
   - Relevant tags/labels
   - Original content
   - Live URL
```

## 📊 Trending Sources

### 1. GitHub Trending
- **What it finds**: Popular open-source projects
- **Example**: "GPT-4 Alternative: Open-Source Language Model"
- **Best for**: Developer tools, frameworks, libraries

### 2. Hacker News
- **What it finds**: Tech news and discussions
- **Example**: "Why Rust is Becoming Popular for Systems Programming"
- **Best for**: Tech trends, industry news, hot debates

### 3. Reddit Programming
- **What it finds**: Community discussions and questions
- **Subreddits**: r/programming, r/python, r/webdev, r/MachineLearning, r/datascience
- **Example**: "Best Practices for Python Async Programming"
- **Best for**: Tutorials, best practices, community interests

### 4. Google Trends (Fallback)
- **What it provides**: Backup trending tech topics
- **Example**: "Quantum Computing Breakthroughs 2026"
- **Best for**: When other sources are unavailable

## 🎯 Example Output

### Raw Trending Topic
```
"microsoft/vscode - Visual Studio Code with new AI features"
```

### Refined Blog Topic
```
"Complete Guide to Visual Studio Code AI Features 2026"
```

### Generated SEO Tags
```
['VSCode', 'VisualStudio', 'AI', 'Development', 'IDE', 'Microsoft', 'Tutorial', '2026']
```

### Published Blog Post
- **Title**: "Complete Guide to Visual Studio Code AI Features 2026"
- **Content**: 1500-2500 words, original, SEO-optimized
- **Tags**: 8 relevant tags for discovery
- **URL**: https://nrjai.blogspot.com/2026/01/vscode-ai-features.html

## 💡 Usage Examples

### Example 1: Test Run (Immediate)

```bash
python trending_blogger.py
# Select your blog
# Choose option 1
# Enter 5 posts (or any number)
```

**Result**: 5 trending blog posts published immediately

### Example 2: Daily Automation

```bash
python trending_blogger.py
# Select your blog
# Choose option 2
# Enter time: 08:00
# Enter 5 posts
```

**Result**: Every day at 8:00 AM:
1. Searches for trending topics
2. Generates 5 blog posts
3. Publishes to your blog automatically

### Example 3: High Volume Publishing

```bash
python trending_blogger.py
# Select your blog
# Choose option 1
# Enter 10 posts
```

**Result**: 10 trending blog posts in one batch

## 🔧 Customization

### Change Trending Sources

Edit `trending_blogger.py`:

```python
self.sources = {
    'github': self.get_github_trending,
    'hackernews': self.get_hackernews_trending,
    'reddit': self.get_reddit_trending,
    # Add your custom source:
    'custom': self.get_custom_trending
}
```

### Add Custom Subreddits

```python
subreddits = ['programming', 'python', 'webdev', 'MachineLearning', 'datascience',
              'javascript', 'docker', 'aws']  # Add more
```

### Customize Topic Refinement

```python
blog_style_prefixes = [
    "Complete Guide to",
    "Introduction to",
    "How to Use",
    "Mastering",
    "Deep Dive into",
    # Add your own styles
]
```

### Custom SEO Tag Rules

```python
def generate_seo_tags(self, topic: str) -> List[str]:
    tags = []
    # Your custom logic here
    tags.append('YourBrandTag')
    tags.extend(self.extract_keywords(topic))
    return tags
```

## 📈 SEO Benefits

### Trending Topics = More Traffic
- **Timely Content**: Write about what people are searching NOW
- **High Relevance**: Topics already proven popular
- **Social Buzz**: Trending topics get more shares
- **Search Volume**: Higher search traffic for popular topics

### Smart Tag Generation
- **Keyword-Rich**: Tags extracted from trending topics
- **Category Tags**: Auto-categorized (AI, Python, Web, etc.)
- **Year Tags**: Current year for freshness
- **Generic Tags**: Technology, Tutorial, etc.

### Content Quality
- **Original**: AI-generated, not copied
- **Comprehensive**: 1500-2500 words
- **Structured**: Proper H1, H2, H3 hierarchy
- **Code Examples**: Practical tutorials

## ⏰ Recommended Schedule

### For New Blogs (Growth Phase)
- **Frequency**: 5-10 posts per day
- **Times**: 9:00 AM, 2:00 PM (two batches)
- **Goal**: Build content library quickly

### For Established Blogs (Maintenance)
- **Frequency**: 3-5 posts per day
- **Time**: 9:00 AM daily
- **Goal**: Keep content fresh and relevant

### For High Authority Blogs
- **Frequency**: 2-3 posts per day
- **Time**: 8:00 AM daily
- **Goal**: Quality over quantity

## 🛡️ Rate Limiting & Safety

### Built-in Protection
- **2-minute delay** between posts
- **1-second delay** between Reddit requests
- **Timeout limits** on all HTTP requests
- **Error handling** with fallbacks

### API Quotas
- **Blogger API**: 50,000 requests/day (you'll use ~50/day)
- **GitHub**: No authentication required for trending
- **Reddit**: Public API, rate-limited automatically
- **Hacker News**: Free Firebase API

## 📝 Logs & Monitoring

### Log File Location
```
logs/app.log
```

### What's Logged
- ✅ Successful publishes with URLs
- ❌ Failed attempts with errors
- 🔍 Trending topics found
- ⏱️ Time taken per post
- 📊 Daily batch summaries

### Example Log Entry
```
2026-01-21 09:05:23 - INFO - Published trending post #1: Complete Guide to GPT-4 Alternatives 2026 - https://nrjai.blogspot.com/...
```

## 🚨 Troubleshooting

### "No trending topics found"
- **Cause**: Network issues or source changes
- **Solution**: Script uses fallback topics automatically
- **Prevention**: Check internet connection

### "Rate limit exceeded"
- **Cause**: Too many requests too fast
- **Solution**: Increase delay between posts
- **Fix**: Edit `time.sleep(120)` to `time.sleep(180)`

### "Publishing failed"
- **Cause**: Blogger API issues
- **Solution**: Check authentication (delete token.pickle)
- **Retry**: Run the script again

### "Connection timeout"
- **Cause**: Slow network or website down
- **Solution**: Script has timeout protection
- **Effect**: Skips that source and continues

## 🔮 Advanced Features

### Integrate Google Trends API

Install pytrends:
```bash
pip install pytrends
```

Add to `trending_blogger.py`:
```python
from pytrends.request import TrendReq

def get_real_google_trends(self):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=['programming', 'AI', 'python'])
    data = pytrend.interest_over_time()
    # Extract trending topics
    return trending_topics
```

### Filter by Category

Only publish AI-related topics:
```python
def filter_topics(self, topics: List[str]) -> List[str]:
    ai_keywords = ['ai', 'machine learning', 'neural', 'gpt', 'llm']
    return [t for t in topics if any(kw in t.lower() for kw in ai_keywords)]
```

### Schedule Multiple Times

```python
schedule.every().day.at("09:00").do(lambda: trending_blogger.run_daily_batch(5))
schedule.every().day.at("15:00").do(lambda: trending_blogger.run_daily_batch(3))
```

## 📊 Performance Expectations

### Generation Time
- **Per post**: 2-3 minutes
- **5 posts**: 10-15 minutes total
- **10 posts**: 20-30 minutes total

### Success Rate
- **Typical**: 95-100% success rate
- **With errors**: 80-90% (network issues)
- **Fallback**: Always has backup topics

### SEO Impact
- **Within 1 week**: Posts indexed by Google
- **Within 1 month**: Ranking for long-tail keywords
- **Within 3 months**: Noticeable traffic increase

## 🎓 Best Practices

1. **Run test batch first**: Try 2-3 posts before scheduling
2. **Monitor first week**: Check logs daily initially
3. **Adjust timing**: Find best time for your audience
4. **Diversify sources**: Enable all trending sources
5. **Review content**: Spot-check generated posts
6. **Track analytics**: Use Google Analytics/Search Console
7. **Adjust volume**: Start with 3-5 posts, increase gradually

## 🆚 Comparison: Trending vs Fixed Topics

### Trending Topics Blogger
✅ **Always relevant and timely**
✅ **Higher search volume**
✅ **More social shares**
✅ **Follows industry news**
✅ **Adapts to tech changes**

### Fixed Topics Blogger
❌ Topics may become outdated
❌ Lower search volume potential
❌ Less viral potential
✅ More predictable content
✅ Better for niche focus

**Recommendation**: Use BOTH
- **Morning**: Trending topics (70% of posts)
- **Afternoon**: Fixed topics (30% of posts)

## 🎯 Next Steps

1. **Test the system**:
   ```bash
   python trending_blogger.py
   ```

2. **Review first posts**: Check quality and SEO

3. **Schedule daily run**: Set your preferred time

4. **Monitor performance**: Track traffic and rankings

5. **Optimize**: Adjust based on analytics

---

**🔥 Start Publishing Trending Content Today!**

Your blog will always have fresh, relevant, SEO-optimized content about the hottest topics in tech!
