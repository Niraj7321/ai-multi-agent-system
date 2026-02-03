"""
NrjAi - AI Multi-Agent System
© 2024 NrjAi | All Rights Reserved
"""
import streamlit as st
import os
from pathlib import Path
import sys
from io import BytesIO

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from src.crew_manager import CrewManager
from src.logger import logger
from src.blogger_publisher import BloggerPublisher

# Page config
st.set_page_config(
    page_title="NrjAi - AI Multi-Agent System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS
st.markdown(
    """
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1E88E5;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .agent-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
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
    """Display application header"""
    st.markdown('<p class="main-header">🎓 NrjAi - AI Multi-Agent System</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header">Generate Original, Copyright-Free Content | Research • Write • Review</p>',
        unsafe_allow_html=True,
    )
    st.caption("© 2024 NrjAi | All Rights Reserved")


def display_sidebar():
    """Display sidebar with configuration"""
    with st.sidebar:
        st.title("⚙️ Configuration")

        # Provider selection
        use_anthropic = st.checkbox(
            "Use Anthropic Claude",
            value=os.getenv("USE_ANTHROPIC", "").lower() == "true",
            help="Use Claude instead of GPT"
        )

        # API Key input
        api_key_label = "Anthropic API Key" if use_anthropic else "OpenAI API Key"
        api_key_env = "ANTHROPIC_API_KEY" if use_anthropic else "OPENAI_API_KEY"
        api_key = st.text_input(
            api_key_label,
            type="password",
            value=os.getenv(api_key_env, ""),
            help=f"Enter your {api_key_label}",
        )

        # Model selection
        if use_anthropic:
            model_options = [
                "claude-sonnet-4-20250514",
                "claude-opus-4-20250514",
                "claude-sonnet-3-7-20250219",
                "claude-haiku-3-5-20241022"
            ]
            default_model = "claude-sonnet-4-20250514"
        else:
            model_options = ["gpt-4-turbo-preview", "gpt-4", "gpt-3.5-turbo"]
            default_model = "gpt-4-turbo-preview"

        model_name = st.selectbox(
            "Model",
            model_options,
            index=0,
            help="Select the LLM model to use",
        )

        # Temperature slider
        temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=1.0,
            value=0.7,
            step=0.1,
            help="Controls randomness in output",
        )

        st.divider()

        # Agent information
        st.title("🤵 Agents")

        with st.expander("👨‍🔬 Research Agent"):
            st.write(
                """
                **Role:** Senior Research Analyst

                **Capabilities:**
                - Web search and information gathering
                - Data analysis and extraction
                - Source verification
                """
            )

        with st.expander("✍️ Writer Agent"):
            st.write(
                """
                **Role:** Senior Content Writer

                **Capabilities:**
                - Content creation and structuring
                - Clear and engaging writing
                - Markdown formatting
                """
            )

        with st.expander("🔍 Reviewer Agent"):
            st.write(
                """
                **Role:** Quality Assurance Specialist

                **Capabilities:**
                - Accuracy verification
                - Quality assessment
                - Constructive feedback
                """
            )

        with st.expander("🎨 Presentation Agent"):
            st.write(
                """
                **Role:** Senior Presentation Designer

                **Capabilities:**
                - Convert text to slides
                - Structure content for presentations
                - Create engaging slide decks
                - Visual hierarchy design
                """
            )

        return api_key, model_name, temperature, use_anthropic


def main():
    """Main application function"""
    init_session_state()
    display_header()
    api_key, model_name, temperature, use_anthropic = display_sidebar()

    # Main content area
    st.divider()

    # Input section
    col1, col2 = st.columns([3, 1])

    with col1:
        topic = st.text_input(
            "🔍 Research Topic",
            placeholder="e.g., Artificial Intelligence in Healthcare 2026",
            help="Enter the topic you want to research and create content about",
        )

    with col2:
        content_type = st.selectbox(
            "📝 Content Type",
            ["blog post", "article", "report", "white paper", "presentation"],
            help="Choose content format - presentation creates slide decks"
        )

    # Execute button
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        execute_button = st.button(
            "🚀 Start Research", use_container_width=True, type="primary"
        )

    # Execution logic
    if execute_button:
        if not topic:
            st.error("⚠️ Please enter a research topic")
            return

        if not api_key:
            st.error("⚠️ Please enter your OpenAI API key in the sidebar")
            return

        st.session_state.is_running = True

        # Progress section
        with st.status("🔄 Multi-Agent Workflow in Progress...", expanded=True) as status:
            try:
                # Initialize crew manager
                st.write("🔧 Initializing AI agents...")
                manager = CrewManager(
                    model_name=model_name,
                    temperature=temperature,
                    api_key=api_key,
                    use_anthropic=use_anthropic
                )

                # Execute workflow based on content type
                if content_type == "presentation":
                    st.write("👨‍🔬 Research Agent is gathering information...")
                    st.write("✍️ Writer Agent is creating content...")
                    st.write("🎨 Presentation Agent is designing slides...")
                    result = manager.execute_presentation_workflow(topic)
                else:
                    st.write("👨‍🔬 Research Agent is gathering information...")
                    st.write("✍️ Writer Agent is creating content...")
                    st.write("🔍 Reviewer Agent is performing quality check...")
                    result = manager.execute_research_workflow(topic, content_type)

                st.session_state.execution_result = result
                st.session_state.is_running = False

                if result["success"]:
                    status.update(
                        label="✅ Workflow Completed Successfully!", state="complete"
                    )
                else:
                    status.update(label="❌ Workflow Failed", state="error")

            except Exception as e:
                logger.error(f"Error during execution: {str(e)}")
                st.session_state.is_running = False
                status.update(label="❌ Error Occurred", state="error")
                st.error(f"Error: {str(e)}")

    # Display results
    if st.session_state.execution_result:
        result = st.session_state.execution_result

        st.divider()
        st.subheader("📊 Results")

        if result["success"]:
            # Display the final output
            st.success(result["message"])

            # Create tabs for different outputs
            tab1, tab2 = st.tabs(["📄 Final Content", "📋 Workflow Details"])

            with tab1:
                # Convert CrewOutput to string
                output_text = str(result["result"])
                st.markdown(output_text)

                # Export options
                if result['content_type'] == "presentation":
                    st.subheader("📥 Export Presentation")

                    col1, col2, col3, col4 = st.columns(4)

                    with col1:
                        # Markdown download
                        st.download_button(
                            label="📝 Markdown",
                            data=output_text,
                            file_name=f"{result['topic'].replace(' ', '_')}.md",
                            mime="text/markdown",
                            use_container_width=True
                        )

                    with col2:
                        # PowerPoint export
                        try:
                            from src.presentation_exporter import export_presentation
                            pptx_data = export_presentation(output_text, 'pptx', result['topic'])
                            st.download_button(
                                label="📊 PowerPoint",
                                data=pptx_data,
                                file_name=f"{result['topic'].replace(' ', '_')}.pptx",
                                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                                use_container_width=True
                            )
                        except Exception as e:
                            st.button("📊 PowerPoint", disabled=True, use_container_width=True, help=f"Install python-pptx: {str(e)}")

                    with col3:
                        # HTML export
                        try:
                            from src.presentation_exporter import export_presentation
                            html_data = export_presentation(output_text, 'html', result['topic'])
                            st.download_button(
                                label="🌐 HTML",
                                data=html_data,
                                file_name=f"{result['topic'].replace(' ', '_')}.html",
                                mime="text/html",
                                use_container_width=True
                            )
                        except Exception as e:
                            st.button("🌐 HTML", disabled=True, use_container_width=True, help=f"Install markdown: {str(e)}")

                    with col4:
                        # PDF export
                        try:
                            from src.presentation_exporter import export_presentation
                            pdf_data = export_presentation(output_text, 'pdf', result['topic'])
                            st.download_button(
                                label="📄 PDF",
                                data=pdf_data,
                                file_name=f"{result['topic'].replace(' ', '_')}.pdf",
                                mime="application/pdf",
                                use_container_width=True
                            )
                        except Exception as e:
                            st.button("📄 PDF", disabled=True, use_container_width=True, help=f"Install weasyprint: {str(e)}")

                    # Export All button with multiprocessing
                    st.markdown("---")
                    st.markdown("**⚡ Quick Export (Multiprocessing):**")

                    if st.button("🚀 Export to All Formats (Parallel)", type="primary", use_container_width=True):
                        try:
                            from src.presentation_exporter import export_presentation_parallel
                            import zipfile
                            from datetime import datetime

                            with st.spinner("Exporting to all formats in parallel... ⚡"):
                                # Export to all formats simultaneously using multiprocessing
                                exports = export_presentation_parallel(
                                    output_text,
                                    result['topic'],
                                    formats=['pptx', 'html', 'pdf']
                                )

                                # Create ZIP file with all exports
                                zip_buffer = BytesIO()
                                with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                                    base_name = result['topic'].replace(' ', '_')

                                    # Add Markdown
                                    zip_file.writestr(f"{base_name}.md", output_text)

                                    # Add PowerPoint
                                    if 'pptx' in exports and not isinstance(exports['pptx'], str):
                                        zip_file.writestr(f"{base_name}.pptx", exports['pptx'].read())

                                    # Add HTML
                                    if 'html' in exports:
                                        zip_file.writestr(f"{base_name}.html", exports['html'])

                                    # Add PDF
                                    if 'pdf' in exports and not isinstance(exports['pdf'], str):
                                        zip_file.writestr(f"{base_name}.pdf", exports['pdf'].read())

                                zip_buffer.seek(0)

                                st.success("✅ Exported to all formats! Download ZIP file below:")
                                st.download_button(
                                    label="📦 Download All Formats (ZIP)",
                                    data=zip_buffer,
                                    file_name=f"{result['topic'].replace(' ', '_')}_all_formats.zip",
                                    mime="application/zip",
                                    use_container_width=True
                                )

                                st.info("⚡ **Multiprocessing:** All formats exported simultaneously (3x faster!)")

                        except Exception as e:
                            st.error(f"Error during parallel export: {str(e)}")

                else:
                    # Standard content download
                    st.download_button(
                        label="📥 Download Content",
                        data=output_text,
                        file_name=f"{result['topic'].replace(' ', '_')}.md",
                        mime="text/markdown",
                    )

            with tab2:
                st.json(
                    {
                        "topic": result["topic"],
                        "content_type": result["content_type"],
                        "status": "Success",
                    }
                )

            # Blogger Publishing Section (only for blog posts)
            if result.get("content_type") == "blog post":
                st.divider()
                st.subheader("📝 Publish to Blogger")

                col1, col2 = st.columns([2, 1])

                with col1:
                    st.info("📌 Publish your blog post directly to Blogger/Blogspot")

                with col2:
                    if st.button("🔑 Connect to Blogger", use_container_width=True):
                        try:
                            with st.spinner("Authenticating with Blogger..."):
                                st.session_state.blogger_publisher = BloggerPublisher()
                                st.session_state.blogger_publisher.authenticate()
                                st.session_state.user_blogs = st.session_state.blogger_publisher.get_blogs()

                                if st.session_state.user_blogs:
                                    st.success(f"✅ Connected! Found {len(st.session_state.user_blogs)} blog(s)")
                                else:
                                    st.warning("⚠️ No blogs found. Create a blog at blogger.com first.")
                        except FileNotFoundError as e:
                            st.error(str(e))
                            st.info("📖 See BLOGGER_SETUP.md for setup instructions")
                        except Exception as e:
                            st.error(f"❌ Authentication failed: {str(e)}")

                # Show publishing controls if authenticated
                if st.session_state.user_blogs:
                    st.markdown("---")

                    col1, col2 = st.columns(2)

                    with col1:
                        # Blog selection
                        blog_names = [f"{blog['name']} ({blog['url']})" for blog in st.session_state.user_blogs]
                        selected_blog_idx = st.selectbox(
                            "Select Blog",
                            range(len(blog_names)),
                            format_func=lambda x: blog_names[x],
                            help="Choose which blog to publish to"
                        )
                        selected_blog = st.session_state.user_blogs[selected_blog_idx]

                        # Labels/tags
                        labels_input = st.text_input(
                            "Labels/Tags (optional)",
                            placeholder="e.g., AI, Tutorial, Python",
                            help="Comma-separated tags for your post"
                        )
                        labels = [label.strip() for label in labels_input.split(",")] if labels_input else None

                    with col2:
                        # Draft vs Publish
                        is_draft = st.checkbox(
                            "Save as Draft",
                            value=False,
                            help="Save as draft instead of publishing immediately"
                        )

                        st.write("")  # Spacing
                        st.write("")  # Spacing

                        # Publish button
                        if st.button("🚀 Publish to Blogger", use_container_width=True, type="primary"):
                            try:
                                with st.spinner("Publishing to Blogger..."):
                                    # Extract title from content (first line/heading)
                                    output_text = str(result["result"])
                                    lines = output_text.split("\n")
                                    title = lines[0].replace("#", "").strip() if lines else result["topic"]

                                    # Publish the post
                                    publish_result = st.session_state.blogger_publisher.publish_post(
                                        blog_id=selected_blog['id'],
                                        title=title,
                                        content=output_text,
                                        labels=labels,
                                        is_draft=is_draft
                                    )

                                    st.session_state.publish_result = publish_result

                                    if publish_result['success']:
                                        st.success(f"✅ {publish_result['message']}")
                                        st.markdown(f"**Post URL:** [{publish_result['url']}]({publish_result['url']})")
                                        st.balloons()
                                    else:
                                        st.error(f"❌ {publish_result['message']}")

                            except Exception as e:
                                st.error(f"❌ Publishing failed: {str(e)}")

                    # Show last publish result
                    if st.session_state.publish_result:
                        st.divider()
                        with st.expander("📊 Last Publish Details"):
                            st.json(st.session_state.publish_result)

        else:
            st.error(result["message"])

    # Footer
    st.divider()
    st.markdown(
        """
        <div style='text-align: center; color: #666; padding: 2rem 0;'>
            <p>Built with CrewAI, LangChain, and Streamlit | Multi-Agent AI System Demo</p>
            <p>✅ All generated content is 100% original and copyright-free</p>
            <p>⭐ Showcase project for AI/ML Engineer Portfolio</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
