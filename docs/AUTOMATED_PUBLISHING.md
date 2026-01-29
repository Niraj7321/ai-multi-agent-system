# Automated Daily Blog Publishing

Automatically generate and publish 5 SEO-friendly blog posts to Blogger every day!

## Features

- **Automatic Content Generation**: Uses AI agents to create high-quality, original blog posts
- **SEO-Friendly**: Automatically generates relevant tags/labels for each post
- **Diverse Topics**: Covers 5 different categories (AI/ML, Python, Web Dev, Data Science, DevOps)
- **Scheduled Publishing**: Publish posts automatically at your chosen time daily
- **Rate Limiting**: Built-in delays to respect Blogger API limits
- **Copyright-Free**: All content is 100% original and copyright-free

## Installation

1. Install the required dependencies:
```bash
pip install schedule
```

Or install all dependencies:
```bash
pip install -r requirements.txt
```

2. Make sure you've completed the Blogger setup (see `BLOGGER_SETUP.md`)

## Usage

### Quick Start

Run the automated publisher:

```bash
python automated_blogger.py
```

You'll be prompted to:
1. Select your blog
2. Choose mode:
   - **Run once**: Publish 5 posts immediately
   - **Schedule daily**: Publish 5 posts every day at a specified time

### Mode 1: Run Once (Immediate Publishing)

Publishes 5 blog posts immediately:

```bash
python automated_blogger.py
# Select blog
# Choose option 1
```

**Use cases:**
- Test the system
- Bulk publish content for a new blog
- Catch up on missed days

### Mode 2: Schedule Daily Publishing

Publishes 5 blog posts automatically every day at your specified time:

```bash
python automated_blogger.py
# Select blog
# Choose option 2
# Enter time (e.g., 09:00 for 9 AM)
```

The scheduler will keep running in the background. **Keep the terminal/command prompt open.**

**Example schedule times:**
- `09:00` - 9:00 AM daily
- `14:30` - 2:30 PM daily
- `18:00` - 6:00 PM daily

### Running as Background Service (Windows)

To keep it running even after closing the terminal:

**Option 1: Using Task Scheduler**

1. Open Task Scheduler (`taskschd.msc`)
2. Create Basic Task:
   - Name: "Blogger Auto Publisher"
   - Trigger: Daily at your chosen time
   - Action: Start a program
   - Program: `python`
   - Arguments: `"C:\Users\Niraj\ai-multi-agent-system\automated_blogger.py"`
   - Start in: `C:\Users\Niraj\ai-multi-agent-system`

**Option 2: Using `pythonw` (Hidden Window)**

Create a batch file `start_blogger.bat`:
```batch
@echo off
cd C:\Users\Niraj\ai-multi-agent-system
pythonw automated_blogger.py
```

Add this batch file to Windows Startup folder.

## Customization

### Adding Your Own Topics

Edit `automated_blogger.py` and modify the `topic_categories` dictionary:

```python
self.topic_categories = {
    "Your Category": [
        "Your Topic 1",
        "Your Topic 2",
        # Add more topics...
    ],
    # Add more categories...
}
```

### Changing Number of Daily Posts

Modify the `get_daily_topics()` method to return more or fewer topics:

```python
if len(topics) == 10:  # Change 5 to 10 for 10 posts per day
    break
```

### Custom Scheduling

Use the `schedule` library for custom schedules:

```python
# Multiple times per day
schedule.every().day.at("09:00").do(auto_blogger.run_daily_batch)
schedule.every().day.at("15:00").do(auto_blogger.run_daily_batch)

# Specific days
schedule.every().monday.at("09:00").do(auto_blogger.run_daily_batch)
schedule.every().friday.at("14:00").do(auto_blogger.run_daily_batch)
```

### Tag Generation

Tags are automatically generated from:
- Category name (e.g., "AIMachineLearning")
- Keywords from topic (e.g., "Python", "Tutorial", "Guide")
- Year tag ("2026")
- Generic tags ("Programming", "Technology")

Modify `generate_seo_tags()` to customize tag generation.

## SEO Best Practices

The automated publisher follows SEO best practices:

✅ **SEO-Friendly Titles**: Clear, keyword-rich titles
✅ **Structured Content**: H1, H2, H3 hierarchy
✅ **Relevant Tags**: 5-8 tags per post
✅ **Code Examples**: Practical code snippets
✅ **Internal Structure**: Problem → Solution → Conclusion
✅ **Word Count**: 1500-2500 words per post
✅ **Fresh Content**: New posts daily

## Rate Limiting

The system includes built-in rate limiting:
- **2-minute delay** between posts
- Total time for 5 posts: ~10-15 minutes
- Respects Google Blogger API quotas (50,000 requests/day)

## Monitoring & Logs

Logs are automatically saved to:
```
logs/app.log
```

Check logs for:
- Successful publishes
- Failed attempts
- Error messages
- Published URLs

## Troubleshooting

### "No blogs found"
- Make sure you've created a blog at blogger.com
- Check your OAuth authentication (delete `token.pickle` and re-authenticate)

### "Rate limit exceeded"
- Increase delay between posts in `generate_and_publish_post()`
- Reduce number of daily posts

### "Authentication failed"
- Delete `token.pickle`
- Re-run the script to re-authenticate
- Check your `credentials.json` is valid

### Posts not publishing at scheduled time
- Make sure the script is still running
- Check system time is correct
- Verify the time format (24-hour: HH:MM)

## Example Output

```
================================================================================
🤖 AUTOMATED BLOG PUBLISHER - Daily Batch Started
⏰ Time: 2026-01-21 09:00:00
================================================================================

================================================================================
[2026-01-21 09:00:05] Generating Post #1/5: Introduction to Machine Learning...
================================================================================
🔬 Research Agent working...
✅ Content generated successfully!
📝 Title: Introduction to Machine Learning for Beginners 2026
🏷️  Tags: AIMachineLearning, Introduction, Machine, Learning, Beginners, 2026
🚀 Publishing to Blogger...
✅ Published successfully!
🔗 URL: https://nrjai.blogspot.com/2026/01/introduction-to-machine-learning.html

⏳ Waiting 2 minutes before next post...

[Continues for posts #2-5...]

================================================================================
📊 DAILY BATCH SUMMARY
================================================================================
✅ Successfully published: 5/5
❌ Failed: 0/5
⏱️  Total time: 12.3 minutes
🕐 Completed at: 2026-01-21 09:12:18
================================================================================
```

## Advanced Usage

### Custom Content Types

Generate different content types:

```python
# In automated_blogger.py, modify the execute_research_workflow call:
result = self.crew_manager.execute_research_workflow(
    topic=topic,
    content_type="article"  # or "report", "white paper"
)
```

### Save as Drafts First

To review before publishing:

```python
# In automated_blogger.py, modify publish_post call:
publish_result = self.blogger_publisher.publish_post(
    blog_id=self.blog_id,
    title=title,
    content=content,
    labels=tags,
    is_draft=True  # Save as draft instead
)
```

Then manually publish from Blogger dashboard.

## API Quotas

Google Blogger API quotas:
- **Free tier**: 50,000 requests per day
- **Per post**: ~3-5 API calls
- **Daily limit**: ~10,000-16,000 posts (you're using 5)

You're well within the free tier limits!

## Support

For issues or questions:
- Check the logs: `logs/app.log`
- Review `BLOGGER_SETUP.md` for authentication issues
- Check Google Cloud Console for API quota usage

## Tips for Success

1. **Start with "Run once" mode** to test the system
2. **Review first few posts** manually before scheduling
3. **Monitor logs regularly** for any issues
4. **Customize topics** to match your niche
5. **Keep terminal open** when using scheduled mode (or use Task Scheduler)
6. **Backup credentials.json** securely

---

**Happy Automated Blogging! 🚀📝**
