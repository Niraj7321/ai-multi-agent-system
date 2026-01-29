"""
Blogger Publisher - Automatically publish blog posts to Blogger/Blogspot
"""
import os
from typing import Dict, Any, Optional
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pickle
from src.logger import logger


class BloggerPublisher:
    """
    Publisher for automatically posting content to Blogger/Blogspot
    """

    # If modifying these scopes, delete the token.pickle file
    SCOPES = ['https://www.googleapis.com/auth/blogger']

    def __init__(self, credentials_path: Optional[str] = None):
        """
        Initialize Blogger Publisher

        Args:
            credentials_path: Path to Google OAuth credentials JSON file
        """
        self.credentials_path = credentials_path or os.getenv('GOOGLE_CREDENTIALS_PATH', 'credentials.json')
        self.token_path = 'token.pickle'
        self.creds = None
        self.service = None

    def authenticate(self) -> bool:
        """
        Authenticate with Google Blogger API

        Returns:
            bool: True if authentication successful
        """
        # Check if we have saved credentials
        if os.path.exists(self.token_path):
            with open(self.token_path, 'rb') as token:
                self.creds = pickle.load(token)

        # If there are no (valid) credentials available, let the user log in
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                if not os.path.exists(self.credentials_path):
                    raise FileNotFoundError(
                        f"Google credentials file not found at: {self.credentials_path}\n"
                        "Please download OAuth credentials from Google Cloud Console"
                    )

                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_path, self.SCOPES)
                self.creds = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open(self.token_path, 'wb') as token:
                pickle.dump(self.creds, token)

        # Build the service
        self.service = build('blogger', 'v3', credentials=self.creds)
        return True

    def get_blogs(self) -> list:
        """
        Get list of user's blogs

        Returns:
            list: List of blogs with id, name, and url
        """
        if not self.service:
            self.authenticate()

        try:
            blogs = self.service.blogs().listByUser(userId='self').execute()
            return [
                {
                    'id': blog['id'],
                    'name': blog['name'],
                    'url': blog['url']
                }
                for blog in blogs.get('items', [])
            ]
        except HttpError as error:
            print(f'An error occurred: {error}')
            return []

    def publish_post(
        self,
        blog_id: str,
        title: str,
        content: str,
        labels: Optional[list] = None,
        image_url: Optional[str] = None,
        is_draft: bool = False
    ) -> Dict[str, Any]:
        """
        Publish a blog post to Blogger

        Args:
            blog_id: The ID of the blog
            title: Post title
            content: Post content (HTML or plain text)
            labels: List of labels/tags for the post
            image_url: Optional featured image URL to add at top of post
            is_draft: Whether to save as draft (default: False - publish immediately)

        Returns:
            Dict containing success status, post URL, and message
        """
        if not self.service:
            self.authenticate()

        # Convert Markdown to HTML if needed
        if content.startswith('#'):
            content = self._markdown_to_html(content)

        # Add featured image at top of content if provided
        if image_url:
            image_html = f'''
<div style="text-align: center; margin-bottom: 30px;">
    <img src="{image_url}"
         alt="{title}"
         style="width: 100%; max-width: 800px; height: auto; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" />
</div>
'''
            content = image_html + content
            logger.info(f"🖼️  Featured image added to post")

        post_data = {
            'title': title,
            'content': content
        }

        if labels:
            post_data['labels'] = labels
            logger.info(f"📌 Adding labels to post: {labels}")
        else:
            logger.warning("⚠️ No labels provided for this post")

        # Log the complete post data being sent
        logger.info(f"📤 Post data being sent to Blogger API:")
        logger.info(f"   Title: {post_data.get('title', 'N/A')}")
        logger.info(f"   Labels: {post_data.get('labels', 'None')}")
        logger.info(f"   Content length: {len(content)} characters")

        try:
            if is_draft:
                # Save as draft
                post = self.service.posts().insert(
                    blogId=blog_id,
                    body=post_data,
                    isDraft=True
                ).execute()
            else:
                # Publish immediately
                post = self.service.posts().insert(
                    blogId=blog_id,
                    body=post_data
                ).execute()

            # Log what was actually saved
            logger.info(f"✅ Post published successfully!")
            logger.info(f"   Post ID: {post.get('id')}")
            logger.info(f"   URL: {post.get('url')}")
            logger.info(f"   Labels in response: {post.get('labels', 'None returned')}")

            return {
                'success': True,
                'post_id': post['id'],
                'url': post['url'],
                'title': post['title'],
                'labels': post.get('labels', []),
                'status': 'draft' if is_draft else 'published',
                'message': f"Post {'saved as draft' if is_draft else 'published'} successfully!"
            }

        except HttpError as error:
            return {
                'success': False,
                'message': f"Error publishing post: {error}"
            }

    def _markdown_to_html(self, markdown_text: str) -> str:
        """
        Convert Markdown to HTML for Blogger

        Args:
            markdown_text: Markdown formatted text

        Returns:
            str: HTML formatted text
        """
        try:
            import markdown
            html = markdown.markdown(
                markdown_text,
                extensions=[
                    'fenced_code',
                    'codehilite',
                    'tables',
                    'nl2br'
                ]
            )
            return html
        except ImportError:
            # If markdown library not available, do basic conversion
            html = markdown_text.replace('\n\n', '</p><p>')
            html = html.replace('\n', '<br>')
            html = f'<p>{html}</p>'

            # Convert code blocks
            import re
            html = re.sub(r'```(\w+)?\n(.*?)```', r'<pre><code>\2</code></pre>', html, flags=re.DOTALL)

            # Convert bold
            html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)

            # Convert headings
            html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
            html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
            html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)

            return html

    def update_post(
        self,
        blog_id: str,
        post_id: str,
        title: Optional[str] = None,
        content: Optional[str] = None,
        labels: Optional[list] = None
    ) -> Dict[str, Any]:
        """
        Update an existing blog post

        Args:
            blog_id: The ID of the blog
            post_id: The ID of the post to update
            title: New title (optional)
            content: New content (optional)
            labels: New labels (optional)

        Returns:
            Dict containing success status and message
        """
        if not self.service:
            self.authenticate()

        try:
            # Get existing post
            post = self.service.posts().get(blogId=blog_id, postId=post_id).execute()

            # Update fields
            if title:
                post['title'] = title
            if content:
                if content.startswith('#'):
                    content = self._markdown_to_html(content)
                post['content'] = content
            if labels:
                post['labels'] = labels

            # Update the post
            updated_post = self.service.posts().update(
                blogId=blog_id,
                postId=post_id,
                body=post
            ).execute()

            return {
                'success': True,
                'post_id': updated_post['id'],
                'url': updated_post['url'],
                'message': 'Post updated successfully!'
            }

        except HttpError as error:
            return {
                'success': False,
                'message': f"Error updating post: {error}"
            }

    def delete_post(self, blog_id: str, post_id: str) -> Dict[str, Any]:
        """
        Delete a blog post

        Args:
            blog_id: The ID of the blog
            post_id: The ID of the post to delete

        Returns:
            Dict containing success status and message
        """
        if not self.service:
            self.authenticate()

        try:
            self.service.posts().delete(blogId=blog_id, postId=post_id).execute()

            return {
                'success': True,
                'message': 'Post deleted successfully!'
            }

        except HttpError as error:
            return {
                'success': False,
                'message': f"Error deleting post: {error}"
            }


if __name__ == "__main__":
    # Example usage
    publisher = BloggerPublisher()

    # Authenticate
    publisher.authenticate()

    # Get list of blogs
    blogs = publisher.get_blogs()
    print("Your blogs:")
    for blog in blogs:
        print(f"  - {blog['name']}: {blog['url']} (ID: {blog['id']})")

    # Publish a test post
    if blogs:
        blog_id = blogs[0]['id']
        result = publisher.publish_post(
            blog_id=blog_id,
            title="Test Post from AI Multi-Agent System",
            content="# Hello World\n\nThis is a test post generated automatically!",
            labels=['test', 'automation'],
            is_draft=True  # Save as draft for testing
        )
        print(f"\nPublish result: {result}")
