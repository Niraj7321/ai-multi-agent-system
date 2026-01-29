# Blogger/Blogspot Integration Setup Guide

## Overview

This guide will help you set up automatic publishing to Blogger (Blogspot) from the AI Multi-Agent System. Once configured, you can generate blog posts and publish them directly to your Blogger blog with a single click.

## Prerequisites

- A Google account
- A Blogger/Blogspot blog (create one at [blogger.com](https://www.blogger.com) if needed)
- Python 3.8 or higher

## Step 1: Install Required Packages

Install the Google API dependencies:

```bash
pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client markdown
```

Or install all dependencies:

```bash
pip install -r requirements.txt
```

## Step 2: Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)

2. Create a new project:
   - Click "Select a project" dropdown at the top
   - Click "New Project"
   - Enter project name: "AI Blog Publisher" (or any name)
   - Click "Create"

3. Select your newly created project from the dropdown

## Step 3: Enable Blogger API

1. In the Google Cloud Console, go to "APIs & Services" > "Library"

2. Search for "Blogger API v3"

3. Click on "Blogger API v3" and click "Enable"

## Step 4: Create OAuth 2.0 Credentials

1. Go to "APIs & Services" > "Credentials"

2. Click "Create Credentials" > "OAuth client ID"

3. If prompted, configure the OAuth consent screen:
   - Choose "External" user type
   - Fill in required fields:
     - App name: "AI Blog Publisher"
     - User support email: Your email
     - Developer contact email: Your email
   - Click "Save and Continue"
   - Skip "Scopes" section (click "Save and Continue")
   - Add test users: Add your own email
   - Click "Save and Continue"

4. Create OAuth Client ID:
   - Application type: "Desktop app"
   - Name: "AI Blog Publisher Desktop"
   - Click "Create"

5. Download the credentials:
   - Click "Download JSON" button
   - Save the file as `credentials.json` in your project root directory:
     ```
     c:\Users\Niraj\ai-multi-agent-system\credentials.json
     ```

## Step 5: First-Time Authentication

When you first use the Blogger integration, you'll need to authenticate:

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Generate a blog post and click "Publish to Blogger"

3. A browser window will open asking you to:
   - Sign in with your Google account
   - Grant permission to access your Blogger blogs
   - You may see a warning "This app isn't verified" - click "Advanced" > "Go to AI Blog Publisher (unsafe)"

4. After authorization, a `token.pickle` file will be created in your project directory
   - This file stores your authentication token
   - You won't need to authenticate again unless you delete this file

## Step 6: Using the Blogger Integration

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Generate a blog post:
   - Enter your topic
   - Select "blog post" as content type
   - Click "Start Research"
   - Wait for the blog post to be generated

3. Publish to Blogger:
   - In the "Blogger Publishing" section, you'll see a list of your blogs
   - Select the blog you want to publish to
   - (Optional) Add labels/tags (comma-separated)
   - Choose whether to publish immediately or save as draft
   - Click "Publish to Blogger"

4. View your published post:
   - After successful publication, you'll see a success message with the post URL
   - Click the URL to view your post on Blogger

## File Structure

After setup, your project should have these files:

```
ai-multi-agent-system/
├── credentials.json          # Google OAuth credentials (keep private!)
├── token.pickle             # Authentication token (auto-generated, keep private!)
├── src/
│   └── blogger_publisher.py # Blogger API integration
├── app.py                   # Streamlit UI with Blogger controls
└── .gitignore              # Should include credentials.json and token.pickle
```

## Security Notes

**IMPORTANT:** Keep your credentials secure!

1. Add to `.gitignore`:
   ```
   credentials.json
   token.pickle
   *.pickle
   ```

2. Never commit these files to version control

3. The `credentials.json` file contains your OAuth client credentials

4. The `token.pickle` file contains your authenticated session

## Troubleshooting

### "Credentials file not found" error

- Make sure `credentials.json` is in the project root directory
- Check the file name is exactly `credentials.json` (case-sensitive)

### "Access blocked: This app's request is invalid"

- Make sure you enabled the Blogger API in Google Cloud Console
- Check that you added your email as a test user in OAuth consent screen

### "Token has expired"

- Delete the `token.pickle` file
- Authenticate again by running the app

### "Blog not found" error

- Make sure you have at least one blog on Blogger
- Try refreshing the blog list in the UI

### Permission denied error

- Check that you granted all required permissions during authentication
- Re-authenticate by deleting `token.pickle` and trying again

## Features

The Blogger integration supports:

- List all your Blogger blogs
- Publish posts immediately or save as drafts
- Add labels/tags to posts
- Convert Markdown to HTML automatically
- Update existing posts
- Delete posts
- View published post URLs

## API Quotas

Google Blogger API has usage quotas:

- Free tier: 50,000 requests per day
- Sufficient for most personal and small business use cases
- Monitor usage in Google Cloud Console > "APIs & Services" > "Dashboard"

## Additional Resources

- [Blogger API Documentation](https://developers.google.com/blogger)
- [Google OAuth 2.0 Guide](https://developers.google.com/identity/protocols/oauth2)
- [Python Quickstart for Blogger](https://developers.google.com/blogger/docs/3.0/getting_started)

## Support

For issues or questions:
- Check the error logs in the Streamlit app
- Review the troubleshooting section above
- Open an issue on the GitHub repository
