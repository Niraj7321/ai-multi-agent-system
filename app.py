"""
NrjAi - AI Multi-Agent System
Advanced Content Generation Platform
© 2024 NrjAi | All Rights Reserved
"""
import streamlit as st
import os
from pathlib import Path
import sys
from io import BytesIO
import zipfile

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from src.crew_manager import CrewManager
from src.logger import logger
from src.blogger_publisher import BloggerPublisher

# Page config - Modern & Colorful
st.set_page_config(
    page_title="NrjAi - AI Multi-Agent System",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Advanced Custom CSS with Modern Design
st.markdown(
    """
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    /* Main App Styling */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        font-family: 'Poppins', sans-serif;
        position: relative;
    }

    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background:
            radial-gradient(circle at 20% 50%, rgba(102, 126, 234, 0.2) 0%, transparent 50%),
            radial-gradient(circle at 80% 50%, rgba(118, 75, 162, 0.2) 0%, transparent 50%);
        pointer-events: none;
        z-index: -1;
    }

    /* Main Content Area */
    .main {
        background: rgba(255, 255, 255, 0.92) !important;
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
    }

    /* Header Styling */
    .main-header {
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(135deg, #5568d3 0%, #6a4c93 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        animation: fadeIn 1s ease-in;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
    }

    .sub-header {
        font-size: 1.3rem;
        text-align: center;
        color: #2c3e50;
        margin-bottom: 2rem;
        font-weight: 400;
        text-shadow: 0 1px 2px rgba(255,255,255,0.8);
    }

    .highlight {
        color: #5568d3;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    /* Agent Cards with Glassmorphism */
    .agent-card {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.15);
        transition: all 0.3s ease;
    }

    .agent-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(31, 38, 135, 0.25);
    }

    /* Feature Cards */
    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
    }

    .feature-card:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.6);
    }

    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }

    .feature-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .feature-desc {
        font-size: 1rem;
        opacity: 0.9;
    }

    /* Stats Counter */
    .stat-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(245, 87, 108, 0.4);
        border: 2px solid rgba(255, 255, 255, 0.3);
        transition: all 0.3s ease;
    }

    .stat-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(245, 87, 108, 0.5);
    }

    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

    .stat-label {
        font-size: 1rem;
        opacity: 1;
        margin-top: 0.5rem;
        font-weight: 600;
        text-shadow: 0 1px 2px rgba(0,0,0,0.15);
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        border: none;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 30px rgba(102, 126, 234, 0.6);
    }

    /* Input Fields */
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        padding: 0.75rem;
        transition: all 0.3s ease;
    }

    .stTextInput>div>div>input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 70%, #f093fb 100%);
        box-shadow: 2px 0 20px rgba(0,0,0,0.2);
    }

    [data-testid="stSidebar"]::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background:
            radial-gradient(circle at 50% 20%, rgba(255, 255, 255, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 50% 80%, rgba(240, 147, 251, 0.2) 0%, transparent 50%);
        pointer-events: none;
    }

    [data-testid="stSidebar"] * {
        color: white !important;
        position: relative;
        z-index: 1;
    }

    /* Success/Error Messages */
    .stSuccess {
        background-color: #d4edda;
        border-color: #c3e6cb;
        border-radius: 10px;
    }

    .stError {
        background-color: #f8d7da;
        border-color: #f5c6cb;
        border-radius: 10px;
    }

    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-30px); }
        to { opacity: 1; transform: translateX(0); }
    }

    /* Progress Bar */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }

    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
        margin: 2rem 0;
    }

    /* Expander */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
        border-radius: 10px;
        font-weight: 600;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        background: rgba(102, 126, 234, 0.05);
        border-radius: 15px;
        padding: 0.5rem;
    }

    .stTabs [data-baseweb="tab"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        border: 2px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
    }

    .stTabs [data-baseweb="tab"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }

    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, #5568d3 0%, #6a4c93 100%);
        box-shadow: 0 6px 25px rgba(102, 126, 234, 0.5);
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def init_session_state():
    """Initialize session state variables"""
    if "execution_result" not in st.session_state:
        st.session_state.execution_result = None
    if "is_running" not in st.session_state:
        st.session_state.is_running = False
    if "blogger_publisher" not in st.session_state:
        st.session_state.blogger_publisher = None
    if "user_blogs" not in st.session_state:
        st.session_state.user_blogs = []
    if "publish_result" not in st.session_state:
        st.session_state.publish_result = None


def display_header():
    """Display modern animated header"""
    st.markdown(
        '<p class="main-header">🚀 NrjAi - AI Multi-Agent System</p>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<p class="sub-header">Powered by <span class="highlight">4 AI Agents</span> • Research • Write • Review • Present</p>',
        unsafe_allow_html=True,
    )

    # Feature Highlights
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">🔬</div>
            <div class="stat-label">Research Agent</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="stat-box" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">
            <div class="stat-number">✍️</div>
            <div class="stat-label">Writer Agent</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="stat-box" style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);">
            <div class="stat-number">🔍</div>
            <div class="stat-label">Review Agent</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="stat-box" style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);">
            <div class="stat-number">🎨</div>
            <div class="stat-label">Presentation Agent</div>
        </div>
        """, unsafe_allow_html=True)


def display_sidebar():
    """Display modern sidebar with configuration"""
    with st.sidebar:
        st.title("⚙️ Configuration")
        st.caption("Configure your AI agents")

        st.divider()

        # Provider selection with icon
        use_anthropic = st.checkbox(
            "🤖 Use Anthropic Claude",
            value=os.getenv("USE_ANTHROPIC", "").lower() == "true",
            help="Use Claude instead of GPT for better results"
        )

        # API Key input with modern styling
        api_key_label = "🔑 Anthropic API Key" if use_anthropic else "🔑 OpenAI API Key"
        api_key_env = "ANTHROPIC_API_KEY" if use_anthropic else "OPENAI_API_KEY"
        api_key = st.text_input(
            api_key_label,
            type="password",
            value=os.getenv(api_key_env, ""),
            help=f"Enter your API key securely",
        )

        # Model selection with descriptions
        if use_anthropic:
            model_options = {
                "claude-sonnet-4-20250514": "Claude Sonnet 4 - Best Balance",
                "claude-opus-4-20250514": "Claude Opus 4 - Most Powerful",
                "claude-sonnet-3-7-20250219": "Claude Sonnet 3.7 - Fast",
                "claude-haiku-3-5-20241022": "Claude Haiku 3.5 - Fastest"
            }
        else:
            model_options = {
                "gpt-4-turbo-preview": "GPT-4 Turbo - Best Balance",
                "gpt-4": "GPT-4 - Most Capable",
                "gpt-3.5-turbo": "GPT-3.5 Turbo - Fastest"
            }

        model_name = st.selectbox(
            "🧠 AI Model",
            list(model_options.keys()),
            format_func=lambda x: model_options[x],
            help="Select the AI model to power your agents",
        )

        # Temperature slider with icon
        temperature = st.slider(
            "🌡️ Temperature",
            min_value=0.0,
            max_value=1.0,
            value=0.7,
            step=0.1,
            help="Higher = More creative | Lower = More focused",
        )

        st.divider()

        # Agent Information with modern cards
        st.title("🤵 AI Agent Team")
        st.caption("Your intelligent workforce")

        agents_info = [
            {
                "icon": "👨‍🔬",
                "title": "Research Agent",
                "role": "Senior Research Analyst",
                "skills": ["Web Research", "Data Analysis", "Fact Checking"]
            },
            {
                "icon": "✍️",
                "title": "Writer Agent",
                "role": "Senior Content Writer",
                "skills": ["Content Creation", "SEO Writing", "Storytelling"]
            },
            {
                "icon": "🔍",
                "title": "Reviewer Agent",
                "role": "Quality Assurance Specialist",
                "skills": ["Quality Control", "Accuracy Check", "Feedback"]
            },
            {
                "icon": "🎨",
                "title": "Presentation Agent",
                "role": "Presentation Designer",
                "skills": ["Slide Design", "Visual Layout", "Export to PPTX/PDF"]
            }
        ]

        for agent in agents_info:
            with st.expander(f"{agent['icon']} {agent['title']}"):
                st.markdown(f"**Role:** {agent['role']}")
                st.markdown("**Skills:**")
                for skill in agent['skills']:
                    st.markdown(f"• {skill}")

        st.divider()

        # Footer
        st.caption("© 2024 NrjAi | All Rights Reserved")
        st.caption("Version 2.0 - Advanced Edition")

        return api_key, model_name, temperature, use_anthropic


def main():
    """Main application function"""
    init_session_state()
    display_header()
    api_key, model_name, temperature, use_anthropic = display_sidebar()

    st.divider()

    # Main Content Tabs
    tab1, tab2, tab3 = st.tabs(["📝 Generate Content", "📊 Publish to Blog", "ℹ️ About"])

    with tab1:
        # Input section with modern design
        st.markdown("### 🎯 What would you like to create?")

        col1, col2 = st.columns([3, 1])

        with col1:
            topic = st.text_input(
                "🔍 Research Topic",
                placeholder="e.g., Artificial Intelligence in Healthcare 2026",
                help="Enter any topic and let our AI agents do the research",
                label_visibility="collapsed"
            )

        with col2:
            content_type = st.selectbox(
                "📝 Format",
                ["blog post", "article", "report", "white paper", "presentation"],
                help="Choose your output format",
                label_visibility="collapsed"
            )

        # Execute button with modern styling
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            execute_button = st.button(
                "🚀 Generate Content",
                use_container_width=True,
                type="primary",
                help="Start the multi-agent workflow"
            )

        # Execution logic
        if execute_button:
            if not topic:
                st.error("⚠️ Please enter a research topic")
                return

            if not api_key:
                st.error("⚠️ Please enter your API key in the sidebar")
                return

            st.session_state.is_running = True

            # Modern progress display
            with st.status("🔄 AI Agents Working...", expanded=True) as status:
                try:
                    # Initialize crew manager
                    st.write("🔧 Initializing AI agent team...")
                    manager = CrewManager(
                        model_name=model_name,
                        temperature=temperature,
                        api_key=api_key,
                        use_anthropic=use_anthropic
                    )

                    # Execute workflow based on content type
                    if content_type == "presentation":
                        st.write("👨‍🔬 **Research Agent** gathering information...")
                        st.write("✍️ **Writer Agent** creating content...")
                        st.write("🎨 **Presentation Agent** designing slides...")
                        result = manager.execute_presentation_workflow(topic)
                    else:
                        st.write("👨‍🔬 **Research Agent** analyzing topic...")
                        st.write("✍️ **Writer Agent** crafting content...")
                        st.write("🔍 **Reviewer Agent** checking quality...")
                        result = manager.execute_research_workflow(topic, content_type)

                    st.session_state.execution_result = result
                    status.update(label="✅ Content Generated Successfully!", state="complete")

                except Exception as e:
                    status.update(label="❌ Error Occurred", state="error")
                    st.error(f"Error: {str(e)}")
                    logger.error(f"Execution error: {str(e)}")
                    st.session_state.is_running = False
                    return

        # Display results with modern cards
        if st.session_state.execution_result:
            result = st.session_state.execution_result

            if result["success"]:
                st.success("✅ Your content is ready!")

                # Result card
                st.markdown("### 📄 Generated Content")

                col1, col2, col3 = st.columns([1, 1, 1])
                with col1:
                    st.metric("Type", result['content_type'].title())
                with col2:
                    st.metric("Topic", result['topic'][:30] + "...")
                with col3:
                    st.metric("Status", "✅ Complete")

                output_text = str(result["result"])

                # Display content in styled container
                with st.expander("👁️ View Content", expanded=True):
                    st.markdown(output_text)

                st.divider()

                # Download section with multiple options
                st.markdown("### 📥 Download Options")

                if result['content_type'] == "presentation":
                    # Presentation exports
                    col1, col2, col3, col4 = st.columns(4)

                    with col1:
                        st.download_button(
                            label="📝 Markdown",
                            data=output_text,
                            file_name=f"{result['topic']}.md",
                            mime="text/markdown",
                            use_container_width=True
                        )

                    with col2:
                        try:
                            from src.presentation_exporter import export_presentation
                            pptx_data = export_presentation(output_text, 'pptx', result['topic'])
                            st.download_button(
                                label="📊 PowerPoint",
                                data=pptx_data,
                                file_name=f"{result['topic']}.pptx",
                                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                                use_container_width=True
                            )
                        except Exception as e:
                            st.warning("PowerPoint export unavailable")

                    with col3:
                        try:
                            from src.presentation_exporter import export_presentation
                            html_data = export_presentation(output_text, 'html', result['topic'])
                            st.download_button(
                                label="🌐 HTML",
                                data=html_data,
                                file_name=f"{result['topic']}.html",
                                mime="text/html",
                                use_container_width=True
                            )
                        except Exception as e:
                            st.warning("HTML export unavailable")

                    with col4:
                        try:
                            from src.presentation_exporter import export_presentation
                            pdf_data = export_presentation(output_text, 'pdf', result['topic'])
                            st.download_button(
                                label="📄 PDF",
                                data=pdf_data,
                                file_name=f"{result['topic']}.pdf",
                                mime="application/pdf",
                                use_container_width=True
                            )
                        except Exception as e:
                            st.warning("PDF export unavailable")

                    # Export all button
                    st.divider()
                    if st.button("🚀 Export to All Formats (Parallel)", type="primary", use_container_width=True):
                        try:
                            from src.presentation_exporter import export_presentation_parallel

                            with st.spinner("Exporting to all formats..."):
                                exports = export_presentation_parallel(output_text, result['topic'])

                                # Create ZIP file
                                zip_buffer = BytesIO()
                                with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                                    base_name = result['topic'].replace(' ', '_').replace('/', '_')[:50]

                                    zip_file.writestr(f"{base_name}.md", output_text)

                                    if 'pptx' in exports and not isinstance(exports['pptx'], str):
                                        zip_file.writestr(f"{base_name}.pptx", exports['pptx'].read())

                                    if 'html' in exports:
                                        zip_file.writestr(f"{base_name}.html", exports['html'])

                                    if 'pdf' in exports and not isinstance(exports['pdf'], str):
                                        zip_file.writestr(f"{base_name}.pdf", exports['pdf'].read())

                                zip_buffer.seek(0)

                                st.download_button(
                                    label="📦 Download All Formats (ZIP)",
                                    data=zip_buffer,
                                    file_name=f"{base_name}_all_formats.zip",
                                    mime="application/zip",
                                    use_container_width=True
                                )

                                st.success("✅ All formats exported successfully!")
                        except Exception as e:
                            st.error(f"Export error: {str(e)}")
                else:
                    # Regular content export
                    col1, col2 = st.columns(2)
                    with col1:
                        st.download_button(
                            label="📝 Download Markdown",
                            data=output_text,
                            file_name=f"{result['topic']}.md",
                            mime="text/markdown",
                            use_container_width=True
                        )
                    with col2:
                        st.download_button(
                            label="📄 Download Text",
                            data=output_text,
                            file_name=f"{result['topic']}.txt",
                            mime="text/plain",
                            use_container_width=True
                        )
            else:
                st.error(f"❌ {result['message']}")

    with tab2:
        st.markdown("### 📤 Publish to Blogger")
        st.info("💡 Connect your Blogger account to publish content directly")

        # Blogger configuration
        with st.expander("⚙️ Configure Blogger"):
            st.markdown("""
            **Setup Instructions:**
            1. Go to [Google Cloud Console](https://console.cloud.google.com/)
            2. Create OAuth 2.0 credentials
            3. Download credentials.json
            4. Place it in the project root
            5. Authorize the app
            """)

        if st.button("📊 View My Blogs"):
            try:
                if st.session_state.blogger_publisher is None:
                    st.session_state.blogger_publisher = BloggerPublisher()

                blogs = st.session_state.blogger_publisher.get_user_blogs()
                st.session_state.user_blogs = blogs

                if blogs:
                    st.success(f"✅ Found {len(blogs)} blog(s)")
                    for blog in blogs:
                        with st.expander(f"📝 {blog['name']}"):
                            st.write(f"**URL:** {blog['url']}")
                            st.write(f"**Posts:** {blog.get('posts', {}).get('totalItems', 0)}")
                else:
                    st.warning("No blogs found")
            except Exception as e:
                st.error(f"Error: {str(e)}")

        # Publish section
        if st.session_state.execution_result and st.session_state.user_blogs:
            result = st.session_state.execution_result

            if result["success"] and result['content_type'] != "presentation":
                st.divider()
                st.markdown("### 📤 Publish Content")

                blog_choice = st.selectbox(
                    "Select Blog",
                    options=[blog['name'] for blog in st.session_state.user_blogs],
                )

                post_title = st.text_input(
                    "Post Title",
                    value=result['topic']
                )

                if st.button("🚀 Publish to Blogger", type="primary"):
                    try:
                        selected_blog = next(
                            b for b in st.session_state.user_blogs if b['name'] == blog_choice
                        )

                        with st.spinner("Publishing..."):
                            published = st.session_state.blogger_publisher.publish_post(
                                blog_id=selected_blog['id'],
                                title=post_title,
                                content=str(result['result']),
                            )

                            if published:
                                st.success(f"✅ Published to {blog_choice}")
                                st.balloons()
                            else:
                                st.error("❌ Publishing failed")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")

    with tab3:
        st.markdown("### ℹ️ About NrjAi")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🤖</div>
                <div class="feature-title">4 AI Agents</div>
                <div class="feature-desc">Collaborative intelligence working for you</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <div class="feature-title">Lightning Fast</div>
                <div class="feature-desc">Parallel processing for maximum speed</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <div class="feature-title">Multiple Formats</div>
                <div class="feature-desc">Export to PowerPoint, PDF, HTML, Markdown</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🎨</div>
                <div class="feature-title">Beautiful Design</div>
                <div class="feature-desc">Professional templates ready to use</div>
            </div>
            """, unsafe_allow_html=True)

        st.divider()

        st.markdown("### 🚀 Features")
        features = [
            "✅ Research any topic with AI-powered web search",
            "✅ Generate blog posts, articles, reports, white papers",
            "✅ Create professional presentations with slide export",
            "✅ Multi-format export (PPTX, PDF, HTML, Markdown)",
            "✅ Parallel processing for 3-5x faster generation",
            "✅ Quality review by dedicated AI agent",
            "✅ Direct publishing to Blogger platform",
            "✅ Modern, colorful, responsive UI"
        ]

        for feature in features:
            st.markdown(feature)

        st.divider()
        st.markdown("**© 2024 NrjAi | All Rights Reserved**")
        st.markdown("Built with ❤️ using Streamlit, CrewAI, and Claude/GPT")


if __name__ == "__main__":
    main()
