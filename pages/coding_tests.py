"""
NrjAi Coding Tests & Examinations - Improved Version
Professional coding assessment platform with enhanced features
© 2024 NrjAi | All Rights Reserved
"""
import streamlit as st
import sys
from pathlib import Path
from datetime import datetime, timedelta
import json

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from src.coding_test_manager import CodingTestManager

# Page config
st.set_page_config(
    page_title="NrjAi - Coding Tests",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .test-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin-bottom: 1rem;
    }
    .question-card {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
    }
    .code-editor {
        font-family: 'Courier New', monospace;
        background: #282c34;
        color: #abb2bf;
        border-radius: 5px;
    }
    .test-stats {
        display: flex;
        justify-content: space-around;
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    .badge {
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.875rem;
        font-weight: 600;
    }
    .badge-easy { background: #d1f4e0; color: #0f5132; }
    .badge-medium { background: #fff3cd; color: #664d03; }
    .badge-hard { background: #f8d7da; color: #842029; }
    .badge-python { background: #e3f2fd; color: #0d47a1; }
    .badge-javascript { background: #fff9c4; color: #f57f17; }
    .badge-java { background: #ffe0b2; color: #e65100; }
    .badge-cpp { background: #f3e5f5; color: #4a148c; }
</style>
""", unsafe_allow_html=True)

# Initialize test manager
if 'test_manager' not in st.session_state:
    st.session_state.test_manager = CodingTestManager()

# Header
st.markdown("""
<div class="main-header">
    <h1>💻 NrjAi Coding Tests Platform</h1>
    <p>Professional Coding Assessment & Evaluation System</p>
    <p style="font-size: 0.85rem; opacity: 0.9;">© 2024 NrjAi | All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.image("https://via.placeholder.com/150x50/667eea/ffffff?text=NrjAi", use_container_width=True)
    st.markdown("### 🎯 Navigation")

    page = st.radio(
        "Select Section",
        ["🏠 Home", "📋 Browse Tests", "➕ Create Test", "✍️ Take Test", "📊 My Submissions", "🏆 Leaderboard"],
        label_visibility="collapsed"
    )

    st.divider()

    # Quick stats
    tests = st.session_state.test_manager.list_tests()
    st.markdown("### 📊 Quick Stats")
    st.metric("Total Tests", len(tests))
    st.metric("Languages", "4")
    st.metric("Active Users", "1,250+")

# Page: Home
if page == "🏠 Home":
    st.markdown("## 🏠 Welcome to NrjAi Coding Platform")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Available Tests", len(tests), "+5 this week")
    with col2:
        st.metric("Questions", sum(t['questions'] for t in tests), "+12")
    with col3:
        st.metric("Total Points", sum(t['total_points'] for t in tests))
    with col4:
        st.metric("Avg. Difficulty", "Medium")

    st.divider()

    # Featured tests
    st.markdown("### ⭐ Featured Tests")

    if tests:
        featured = tests[:3]  # Show first 3 tests
        for test in featured:
            with st.expander(f"🎯 {test['title']}", expanded=True):
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.markdown(f"**Questions:** {test['questions']}")
                with col2:
                    st.markdown(f"**Time:** {test['time_limit']} min")
                with col3:
                    st.markdown(f"**Points:** {test['total_points']}")
                with col4:
                    difficulty_class = f"badge badge-{test['difficulty']}"
                    st.markdown(f'<span class="{difficulty_class}">{test["difficulty"].upper()}</span>', unsafe_allow_html=True)

                st.write(f"**Created:** {test['created_at'][:10]}")

                if st.button(f"Start Test", key=f"home_start_{test['test_id']}", use_container_width=True, type="primary"):
                    st.session_state.selected_test_id = test['test_id']
                    st.session_state.page = "✍️ Take Test"
                    st.rerun()
    else:
        st.info("👋 No tests available yet. Create your first test to get started!")

    st.divider()

    # Features
    st.markdown("### 🚀 Platform Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        #### 💻 Multiple Languages
        - Python
        - JavaScript (Node.js)
        - Java
        - C++
        """)

    with col2:
        st.markdown("""
        #### ⚡ Instant Feedback
        - Automatic grading
        - Test case validation
        - Detailed results
        - Performance metrics
        """)

    with col3:
        st.markdown("""
        #### 🎯 Comprehensive Tools
        - Custom test creation
        - Code execution
        - Leaderboards
        - Progress tracking
        """)

# Page: Browse Tests
elif page == "📋 Browse Tests":
    st.markdown("## 📋 Available Coding Tests")

    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        filter_difficulty = st.selectbox("Filter by Difficulty", ["All", "Easy", "Medium", "Hard"])
    with col2:
        filter_language = st.selectbox("Filter by Language", ["All", "Python", "JavaScript", "Java", "C++"])
    with col3:
        search_query = st.text_input("🔍 Search tests", placeholder="Search by title...")

    st.divider()

    # Display tests
    if not tests:
        st.info("👋 No tests available. Create your first test in the 'Create Test' section!")
    else:
        filtered_tests = tests

        # Apply filters
        if filter_difficulty != "All":
            filtered_tests = [t for t in filtered_tests if t['difficulty'].lower() == filter_difficulty.lower()]

        if search_query:
            filtered_tests = [t for t in filtered_tests if search_query.lower() in t['title'].lower()]

        if not filtered_tests:
            st.warning("No tests match your filters.")
        else:
            st.markdown(f"**Showing {len(filtered_tests)} test(s)**")

            for test in filtered_tests:
                with st.container():
                    st.markdown(f"""
                    <div class="test-card">
                        <h3>🎯 {test['title']}</h3>
                        <p><strong>Test ID:</strong> <code>{test['test_id']}</code></p>
                    </div>
                    """, unsafe_allow_html=True)

                    col1, col2, col3, col4, col5 = st.columns(5)
                    with col1:
                        st.metric("Questions", test['questions'])
                    with col2:
                        st.metric("Time Limit", f"{test['time_limit']} min")
                    with col3:
                        st.metric("Total Points", test['total_points'])
                    with col4:
                        difficulty_class = f"badge badge-{test['difficulty']}"
                        st.markdown(f'<span class="{difficulty_class}">{test["difficulty"].upper()}</span>', unsafe_allow_html=True)
                    with col5:
                        if st.button("Take Test", key=f"browse_{test['test_id']}", use_container_width=True):
                            st.session_state.selected_test_id = test['test_id']
                            st.session_state.page = "✍️ Take Test"
                            st.rerun()

                    st.divider()

# Page: Create Test
elif page == "➕ Create Test":
    st.markdown("## ➕ Create New Coding Test")

    with st.form("create_test_form_improved"):
        # Test details
        st.markdown("### 📝 Test Details")

        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("Test Title *", placeholder="e.g., Python Programming Assessment")
        with col2:
            difficulty = st.selectbox("Difficulty Level *", ["easy", "medium", "hard"])

        description = st.text_area("Test Description *", placeholder="Describe what this test covers...", height=100)

        col1, col2, col3 = st.columns(3)
        with col1:
            time_limit = st.number_input("Time Limit (minutes)", min_value=5, max_value=240, value=60)
        with col2:
            passing_percentage = st.number_input("Passing %", min_value=0, max_value=100, value=60)
        with col3:
            tags_input = st.text_input("Tags", placeholder="Python, Algorithms, DS")

        st.divider()

        # Questions
        st.markdown("### ❓ Questions")
        num_questions = st.number_input("Number of Questions", min_value=1, max_value=15, value=3)

        questions = []
        for i in range(num_questions):
            with st.expander(f"📌 Question {i+1}", expanded=i==0):
                q_title = st.text_input(f"Question Title *", key=f"qti_{i}", placeholder="e.g., Reverse a String")
                q_description = st.text_area(f"Description *", key=f"qde_{i}", placeholder="Detailed question...", height=150)

                col1, col2 = st.columns(2)
                with col1:
                    q_language = st.selectbox(f"Language", ["python", "javascript", "java", "cpp"], key=f"qla_{i}")
                with col2:
                    q_points = st.number_input(f"Points", min_value=1, max_value=100, value=10, key=f"qpo_{i}")

                # Test cases
                st.markdown(f"**Test Cases**")
                num_test_cases = st.number_input(f"Number of Test Cases", min_value=1, max_value=10, value=3, key=f"qtc_{i}")

                test_cases = []
                for j in range(num_test_cases):
                    st.markdown(f"*Test Case {j+1}*")
                    col1, col2 = st.columns(2)
                    with col1:
                        tc_input = st.text_area(f"Input", key=f"ti_{i}_{j}", height=80)
                    with col2:
                        tc_output = st.text_area(f"Expected Output", key=f"to_{i}_{j}", height=80)

                    test_cases.append({
                        "input": tc_input,
                        "expected_output": tc_output
                    })

                questions.append({
                    "id": f"q{i+1}",
                    "title": q_title,
                    "description": q_description,
                    "language": q_language,
                    "points": q_points,
                    "test_cases": test_cases
                })

        submitted = st.form_submit_button("🚀 Create Test", use_container_width=True, type="primary")

        if submitted:
            if not title or not description:
                st.error("⚠️ Please fill in all required fields!")
            elif any(not q["title"] or not q["description"] for q in questions):
                st.error("⚠️ Please complete all question details!")
            else:
                tags = [tag.strip() for tag in tags_input.split(",")] if tags_input else []

                test_data = st.session_state.test_manager.create_test(
                    title=title,
                    description=description,
                    questions=questions,
                    time_limit_minutes=time_limit,
                    difficulty=difficulty,
                    tags=tags
                )

                st.success("✅ Test created successfully!")
                st.info(f"**Test ID:** `{test_data['test_id']}`")
                st.balloons()

# Page: Take Test
elif page == "✍️ Take Test":
    st.markdown("## ✍️ Take a Coding Test")

    if 'selected_test_id' not in st.session_state:
        st.warning("⚠️ Please select a test from the 'Browse Tests' page.")
        if st.button("📋 Go to Browse Tests", type="primary"):
            st.session_state.page = "📋 Browse Tests"
            st.rerun()
    else:
        test_data = st.session_state.test_manager.get_test(st.session_state.selected_test_id)

        if not test_data:
            st.error("❌ Test not found!")
            del st.session_state.selected_test_id
        else:
            # Test header
            st.markdown(f"""
            <div class="test-card">
                <h2>📝 {test_data['title']}</h2>
                <p>{test_data['description']}</p>
            </div>
            """, unsafe_allow_html=True)

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("⏱️ Time Limit", f"{test_data['time_limit_minutes']} min")
            with col2:
                st.metric("📝 Questions", test_data['num_questions'])
            with col3:
                st.metric("🎯 Total Points", test_data['total_points'])
            with col4:
                difficulty_class = f"badge badge-{test_data['difficulty']}"
                st.markdown(f'**Difficulty:** <span class="{difficulty_class}">{test_data["difficulty"].upper()}</span>', unsafe_allow_html=True)

            st.divider()

            # Candidate form
            with st.form("take_test_form_improved"):
                st.markdown("### 👤 Your Information")
                col1, col2 = st.columns(2)
                with col1:
                    candidate_name = st.text_input("Full Name *", placeholder="Enter your name")
                with col2:
                    candidate_email = st.text_input("Email *", placeholder="your.email@example.com")

                st.divider()

                # Questions
                st.markdown("### 🧩 Questions")
                answers = []

                for i, question in enumerate(test_data['questions']):
                    with st.container():
                        st.markdown(f"""
                        <div class="question-card">
                            <h3>Question {i+1}: {question['title']}</h3>
                            <p><strong>Language:</strong> <span class="badge badge-{question['language']}">{question['language'].upper()}</span> | <strong>Points:</strong> {question['points']}</p>
                        </div>
                        """, unsafe_allow_html=True)

                        st.markdown(question['description'])

                        st.markdown(f"**Your Code ({question['language'].upper()}):**")
                        code = st.text_area(
                            f"Write your solution here",
                            height=300,
                            key=f"code_{i}",
                            placeholder=f"# Write your {question['language']} code here...",
                            label_visibility="collapsed"
                        )

                        answers.append({
                            "question_id": question['id'],
                            "code": code,
                            "language": question['language']
                        })

                        st.divider()

                submit_button = st.form_submit_button("📥 Submit Test", use_container_width=True, type="primary")

                if submit_button:
                    if not candidate_name or not candidate_email:
                        st.error("⚠️ Please enter your name and email!")
                    elif any(not ans["code"].strip() for ans in answers):
                        st.warning("⚠️ Some questions are unanswered. Submit anyway?")
                    else:
                        submission_data = st.session_state.test_manager.submit_test(
                            test_id=st.session_state.selected_test_id,
                            candidate_name=candidate_name,
                            candidate_email=candidate_email,
                            answers=answers
                        )

                        st.session_state.submission_id = submission_data['submission_id']
                        st.success("✅ Test submitted successfully!")
                        st.info(f"**Submission ID:** `{submission_data['submission_id']}`")
                        st.balloons()

                        # Clear selected test
                        del st.session_state.selected_test_id

# Page: My Submissions
elif page == "📊 My Submissions":
    st.markdown("## 📊 My Test Submissions")

    st.info("💡 Enter your email to view your submissions")

    email = st.text_input("Your Email", placeholder="your.email@example.com")

    if email:
        # Get all submissions for this email (would need to implement this in manager)
        st.info("📋 Submissions feature coming soon! View results in 'Evaluate Submissions' for now.")
    else:
        st.info("👆 Enter your email to see your submissions")

# Page: Leaderboard
elif page == "🏆 Leaderboard":
    st.markdown("## 🏆 Leaderboard")

    st.info("🎯 Top performers across all tests")

    # Mock leaderboard data
    leaderboard = [
        {"rank": 1, "name": "Alice Johnson", "tests": 15, "avg_score": 95, "badge": "🏆"},
        {"rank": 2, "name": "Bob Smith", "tests": 12, "avg_score": 92, "badge": "🥈"},
        {"rank": 3, "name": "Charlie Brown", "tests": 18, "avg_score": 90, "badge": "🥉"},
        {"rank": 4, "name": "Diana Prince", "tests": 10, "avg_score": 88, "badge": "⭐"},
        {"rank": 5, "name": "Ethan Hunt", "tests": 14, "avg_score": 85, "badge": "⭐"},
    ]

    for entry in leaderboard:
        col1, col2, col3, col4 = st.columns([1, 3, 2, 2])
        with col1:
            st.markdown(f"### {entry['badge']}")
        with col2:
            st.markdown(f"**{entry['name']}**")
        with col3:
            st.markdown(f"Tests: {entry['tests']}")
        with col4:
            st.markdown(f"Avg Score: **{entry['avg_score']}%**")
        st.divider()

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #6b7280; padding: 2rem;">
    <p><strong>💻 NrjAi Coding Test Platform v2.0</strong></p>
    <p>Professional Coding Assessment & Evaluation</p>
    <p>© 2024 NrjAi | All Rights Reserved</p>
    <p style="margin-top: 1rem;">
        Python | JavaScript | Java | C++
    </p>
    <p style="font-size: 0.85rem; margin-top: 1rem;">
        Powered by <strong>NrjAi</strong> 🚀
    </p>
</div>
""", unsafe_allow_html=True)
