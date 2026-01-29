"""
NrjAi - Complete Exam Preparation Platform
All Competitive Exams with 25 Practice Sets Each
© 2024 NrjAi | All Rights Reserved
"""
import streamlit as st
import sys
from pathlib import Path
from datetime import datetime, timedelta
import json
from typing import Dict, List, Any

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from src.competitive_exam_manager import CompetitiveExamManager

# Initialize
if 'exam_manager' not in st.session_state:
    st.session_state.exam_manager = CompetitiveExamManager()

st.set_page_config(
    page_title="NrjAi - Exam Preparation",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for NrjAi branding
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
    .exam-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border-left: 4px solid #667eea;
        transition: transform 0.2s;
    }
    .exam-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .stat-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
    }
    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.2rem;
    }
    .badge-new { background: #10b981; color: white; }
    .badge-trending { background: #f59e0b; color: white; }
    .badge-popular { background: #3b82f6; color: white; }
    .badge-free { background: #8b5cf6; color: white; }
    .practice-set-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 0.5rem;
        border-left: 3px solid #667eea;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🎓 NrjAi - Complete Exam Preparation Platform</h1>
    <p>All Competitive Exams | 25 Practice Sets Each | Free Forever</p>
    <p style="font-size: 0.85rem; opacity: 0.9;">© 2024 NrjAi | All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.image("https://via.placeholder.com/150x50/667eea/ffffff?text=NrjAi", width='stretch')
    st.markdown("### 🎯 Quick Navigation")

    # Initialize nav_page in session state if not exists
    if 'nav_page' not in st.session_state:
        st.session_state.nav_page = "🏠 Home Dashboard"

    # Use session state for page selection
    page = st.radio(
        "Select",
        ["🏠 Home Dashboard", "📚 All Exams", "✍️ Take Test", "📊 My Performance", "🏆 Leaderboard", "❓ Daily Quiz"],
        index=["🏠 Home Dashboard", "📚 All Exams", "✍️ Take Test", "📊 My Performance", "🏆 Leaderboard", "❓ Daily Quiz"].index(st.session_state.nav_page) if st.session_state.nav_page in ["🏠 Home Dashboard", "📚 All Exams", "✍️ Take Test", "📊 My Performance", "🏆 Leaderboard", "❓ Daily Quiz"] else 0
    )

    # Update session state when radio button changes
    if page != st.session_state.nav_page:
        st.session_state.nav_page = page
        st.rerun()

# Use session state for page rendering (not the radio button value)
page = st.session_state.nav_page

# Exam database with 25 practice sets each
EXAM_TYPES = {
    "Teaching Exams": {
        "exams": [
            {
                "name": "STET (State TET)",
                "icon": "👨‍🏫",
                "description": "State Teacher Eligibility Test",
                "papers": ["Paper 1 (Classes 1-5)", "Paper 2 (Classes 6-8)", "Paper 3 (Classes 9-10)", "Paper 4 (Classes 11-12)"],
                "duration": 150,
                "questions": 150,
                "marks": 150,
                "subjects": ["Child Development", "Mathematics", "Science", "Social Studies", "Language", "English", "Hindi", "Computer Science", "Physics", "Chemistry", "Biology", "History", "Geography", "Economics", "Political Science"]
            },
            {
                "name": "CTET (Central TET)",
                "icon": "🎓",
                "description": "Central Teacher Eligibility Test",
                "papers": ["Paper 1 (Classes 1-5)", "Paper 2 (Classes 6-8)"],
                "duration": 150,
                "questions": 150,
                "marks": 150,
                "subjects": ["Child Development", "Language I", "Language II", "Mathematics", "EVS", "Science", "Social Studies", "English", "Hindi"]
            },
            {
                "name": "UPTET",
                "icon": "📚",
                "description": "UP Teacher Eligibility Test",
                "papers": ["Paper 1 (Classes 1-5)", "Paper 2 (Classes 6-8)"],
                "duration": 150,
                "questions": 150,
                "marks": 150,
                "subjects": ["Child Development", "Languages", "Mathematics", "Science", "Social Studies", "English", "Hindi", "Computer Science"]
            }
        ]
    },
    "Civil Services": {
        "exams": [
            {
                "name": "BPSC (Bihar PSC)",
                "icon": "🏛️",
                "description": "Bihar Public Service Commission",
                "papers": ["Prelims", "Mains"],
                "duration": 120,
                "questions": 150,
                "marks": 200,
                "subjects": ["General Studies", "Current Affairs", "History", "Geography", "Polity"]
            },
            {
                "name": "UPSC (IAS/IPS)",
                "icon": "🎯",
                "description": "Union Public Service Commission",
                "papers": ["Prelims", "Mains"],
                "duration": 120,
                "questions": 100,
                "marks": 200,
                "subjects": ["General Studies", "CSAT", "Optional Subjects", "Essay"]
            },
            {
                "name": "State PSC",
                "icon": "🏢",
                "description": "All State Public Service Commissions",
                "papers": ["Prelims", "Mains"],
                "duration": 120,
                "questions": 150,
                "marks": 200,
                "subjects": ["General Studies", "State Specific", "Current Affairs"]
            }
        ]
    },
    "SSC Exams": {
        "exams": [
            {
                "name": "SSC CGL",
                "icon": "📊",
                "description": "Combined Graduate Level",
                "papers": ["Tier 1", "Tier 2"],
                "duration": 60,
                "questions": 100,
                "marks": 200,
                "subjects": ["Reasoning", "Math", "English", "General Awareness"]
            },
            {
                "name": "SSC CHSL",
                "icon": "📝",
                "description": "Combined Higher Secondary Level",
                "papers": ["Tier 1", "Tier 2"],
                "duration": 60,
                "questions": 100,
                "marks": 200,
                "subjects": ["Reasoning", "Math", "English", "General Awareness"]
            },
            {
                "name": "SSC MTS",
                "icon": "🔧",
                "description": "Multi Tasking Staff",
                "papers": ["Paper 1"],
                "duration": 90,
                "questions": 100,
                "marks": 100,
                "subjects": ["Reasoning", "Math", "English", "General Awareness"]
            }
        ]
    },
    "Banking Exams": {
        "exams": [
            {
                "name": "IBPS PO",
                "icon": "🏦",
                "description": "Probationary Officer",
                "papers": ["Prelims", "Mains"],
                "duration": 60,
                "questions": 100,
                "marks": 100,
                "subjects": ["Reasoning", "Math", "English", "Banking Awareness", "Computer"]
            },
            {
                "name": "IBPS Clerk",
                "icon": "💼",
                "description": "Clerical Cadre",
                "papers": ["Prelims", "Mains"],
                "duration": 60,
                "questions": 100,
                "marks": 100,
                "subjects": ["Reasoning", "Math", "English", "Banking Awareness", "Computer"]
            },
            {
                "name": "SBI PO",
                "icon": "🏛️",
                "description": "State Bank PO",
                "papers": ["Prelims", "Mains"],
                "duration": 60,
                "questions": 100,
                "marks": 100,
                "subjects": ["Reasoning", "Math", "English", "Banking Awareness", "Computer"]
            },
            {
                "name": "RBI Grade B",
                "icon": "💰",
                "description": "Reserve Bank Officer",
                "papers": ["Phase 1", "Phase 2"],
                "duration": 120,
                "questions": 200,
                "marks": 200,
                "subjects": ["General Awareness", "English", "Reasoning", "Math", "Finance"]
            }
        ]
    },
    "Railway Exams": {
        "exams": [
            {
                "name": "RRB NTPC",
                "icon": "🚂",
                "description": "Non-Technical Popular Categories",
                "papers": ["Stage 1", "Stage 2"],
                "duration": 90,
                "questions": 100,
                "marks": 100,
                "subjects": ["Math", "Reasoning", "General Awareness", "General Science"]
            },
            {
                "name": "RRB Group D",
                "icon": "🚆",
                "description": "Group D Posts",
                "papers": ["CBT"],
                "duration": 90,
                "questions": 100,
                "marks": 100,
                "subjects": ["Math", "Reasoning", "General Awareness", "General Science"]
            },
            {
                "name": "RRB JE",
                "icon": "⚙️",
                "description": "Junior Engineer",
                "papers": ["Stage 1", "Stage 2"],
                "duration": 90,
                "questions": 100,
                "marks": 100,
                "subjects": ["Technical", "General Awareness", "Math", "Reasoning"]
            }
        ]
    },
    "Defense Exams": {
        "exams": [
            {
                "name": "NDA",
                "icon": "⚔️",
                "description": "National Defence Academy",
                "papers": ["Math", "GAT"],
                "duration": 150,
                "questions": 120,
                "marks": 300,
                "subjects": ["Mathematics", "English", "Physics", "Chemistry", "GK"]
            },
            {
                "name": "CDS",
                "icon": "🎖️",
                "description": "Combined Defence Services",
                "papers": ["English", "GK", "Math"],
                "duration": 120,
                "questions": 100,
                "marks": 100,
                "subjects": ["English", "General Knowledge", "Mathematics"]
            },
            {
                "name": "AFCAT",
                "icon": "✈️",
                "description": "Air Force Common Admission Test",
                "papers": ["AFCAT"],
                "duration": 120,
                "questions": 100,
                "marks": 300,
                "subjects": ["General Awareness", "Verbal", "Numerical", "Reasoning"]
            }
        ]
    },
    "Other Exams": {
        "exams": [
            {
                "name": "GATE",
                "icon": "🔬",
                "description": "Graduate Aptitude Test in Engineering",
                "papers": ["Technical Paper"],
                "duration": 180,
                "questions": 65,
                "marks": 100,
                "subjects": ["Engineering Subject", "Aptitude", "Math"]
            },
            {
                "name": "Police Constable",
                "icon": "👮",
                "description": "State Police Recruitment",
                "papers": ["Written Test"],
                "duration": 120,
                "questions": 100,
                "marks": 100,
                "subjects": ["Reasoning", "GK", "Math", "Hindi/English"]
            },
            {
                "name": "LIC AAO",
                "icon": "💼",
                "description": "Life Insurance Corporation",
                "papers": ["Prelims", "Mains"],
                "duration": 60,
                "questions": 100,
                "marks": 100,
                "subjects": ["Reasoning", "Math", "English", "Insurance Awareness"]
            }
        ]
    }
}

# Main content based on selection
if page == "🏠 Home Dashboard":
    # Welcome section
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### 👋 Welcome to NrjAi!")
        st.write("Your complete exam preparation platform with 25 practice sets for every exam")
    with col2:
        if st.button("🎯 Browse All Exams", use_container_width=True, type="primary"):
            st.session_state.nav_page = "📚 All Exams"
            st.rerun()

    st.divider()

    # Quick stats
    st.markdown("### 📊 Platform Overview")
    col1, col2, col3, col4 = st.columns(4)

    total_exams = sum(len(cat["exams"]) for cat in EXAM_TYPES.values())
    total_practice_sets = total_exams * 25

    with col1:
        st.markdown('<div class="stat-box">', unsafe_allow_html=True)
        st.metric("Exam Types", f"{total_exams}")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="stat-box">', unsafe_allow_html=True)
        st.metric("Practice Sets", f"{total_practice_sets}")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="stat-box">', unsafe_allow_html=True)
        st.metric("Categories", f"{len(EXAM_TYPES)}")
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="stat-box">', unsafe_allow_html=True)
        st.metric("Status", "100% Free")
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # Featured exam categories
    st.markdown("### 🎯 Exam Categories")

    for category_name, category_data in EXAM_TYPES.items():
        with st.expander(f"📚 {category_name} ({len(category_data['exams'])} Exams)", expanded=False):
            cols = st.columns(3)
            for idx, exam in enumerate(category_data['exams']):
                with cols[idx % 3]:
                    st.markdown(f"""
                    <div class="exam-card">
                        <h2 style="text-align: center;">{exam['icon']}</h2>
                        <h4 style="text-align: center;">{exam['name']}</h4>
                        <p style="text-align: center; color: #6b7280; font-size: 0.9rem;">
                            {exam['description']}<br>
                            <strong>25 Practice Sets</strong>
                        </p>
                    </div>
                    """, unsafe_allow_html=True)

                    if st.button(f"View {exam['name']}", key=f"home_{exam['name']}", use_container_width=True):
                        st.session_state.selected_exam = exam['name']
                        st.session_state.nav_page = "📚 All Exams"
                        st.rerun()

elif page == "📚 All Exams":
    st.markdown("### 📚 All Competitive Exams with 25 Practice Sets")

    # Search and filter
    col1, col2 = st.columns([3, 1])
    with col1:
        search = st.text_input("🔍 Search exams", placeholder="Type exam name...")
    with col2:
        category_filter = st.selectbox("Filter by Category", ["All"] + list(EXAM_TYPES.keys()))

    st.divider()

    # Display exams by category
    for category_name, category_data in EXAM_TYPES.items():
        if category_filter != "All" and category_filter != category_name:
            continue

        st.markdown(f"## 📖 {category_name}")
        st.write(f"**{len(category_data['exams'])} Exams | 25 Practice Sets Each**")

        for exam in category_data['exams']:
            if search and search.lower() not in exam['name'].lower():
                continue

            with st.expander(f"{exam['icon']} {exam['name']} - {exam['description']}", expanded=False):
                # Exam details
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Duration", f"{exam['duration']} min")
                with col2:
                    st.metric("Questions", exam['questions'])
                with col3:
                    st.metric("Total Marks", exam['marks'])
                with col4:
                    st.markdown('<span class="badge badge-free">FREE</span>', unsafe_allow_html=True)

                st.markdown(f"**Papers:** {', '.join(exam['papers'])}")
                st.markdown(f"**Subjects:** {', '.join(exam['subjects'])}")

                st.divider()

                # 25 Practice Sets
                st.markdown("### 📝 25 Practice Sets Available")

                # Display in groups of 5
                for row in range(5):
                    cols = st.columns(5)
                    for col_idx, col in enumerate(cols):
                        set_num = row * 5 + col_idx + 1
                        with col:
                            st.markdown(f"""
                            <div class="practice-set-card">
                                <p style="text-align: center; margin: 0;">
                                    <strong>Set {set_num}</strong><br>
                                    <small>{exam['questions']} Qs</small>
                                </p>
                            </div>
                            """, unsafe_allow_html=True)

                            if st.button(f"Start", key=f"{exam['name']}_set_{set_num}", use_container_width=True):
                                st.session_state.selected_exam_for_test = exam
                                st.session_state.selected_set_number = set_num
                                st.session_state.nav_page = "✍️ Take Test"
                                st.rerun()

                st.divider()

                # Additional options
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button(f"📊 View All Sets", key=f"view_all_{exam['name']}", use_container_width=True):
                        st.info(f"Showing all 25 practice sets for {exam['name']}")
                with col2:
                    if st.button(f"📈 My Progress", key=f"progress_{exam['name']}", use_container_width=True):
                        st.info("Progress tracking coming soon!")
                with col3:
                    if st.button(f"📥 Download PDF", key=f"download_{exam['name']}", use_container_width=True):
                        st.info("PDF download feature coming soon!")

        st.divider()

elif page == "✍️ Take Test":
    # Check if exam is selected
    if 'selected_exam_for_test' not in st.session_state:
        st.warning("⚠️ Please select a practice set from the 'All Exams' page to start your test.")
        if st.button("📚 Go to All Exams", use_container_width=True, type="primary"):
            st.session_state.nav_page = "📚 All Exams"
            st.rerun()
    else:
        exam = st.session_state.selected_exam_for_test
        set_num = st.session_state.selected_set_number

        # Initialize test state
        if 'test_started' not in st.session_state:
            st.session_state.test_started = False
        if 'current_question' not in st.session_state:
            st.session_state.current_question = 0
        if 'answers' not in st.session_state:
            st.session_state.answers = {}
        if 'marked_for_review' not in st.session_state:
            st.session_state.marked_for_review = set()
        if 'class_level_selected' not in st.session_state:
            st.session_state.class_level_selected = False
        if 'subject_selected' not in st.session_state:
            st.session_state.subject_selected = False

        st.markdown(f"### ✍️ {exam['icon']} {exam['name']} - Practice Set {set_num}")

        # Step 1: Class Level Selection (for teaching exams)
        if not st.session_state.class_level_selected:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        padding: 2rem; border-radius: 10px; color: white; margin-bottom: 2rem;">
                <h3>📚 Step 1: Select Class Level</h3>
                <p>Choose which class level you want to prepare for</p>
            </div>
            """, unsafe_allow_html=True)

            # Check if this is a teaching exam with papers
            if "papers" in exam and len(exam["papers"]) > 0:
                st.markdown("### Available Papers/Class Levels:")

                # Display paper options
                for paper in exam["papers"]:
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.info(f"📄 **{paper}**")
                    with col2:
                        if st.button("Select", key=f"paper_{paper}", use_container_width=True, type="primary"):
                            st.session_state.selected_paper = paper
                            st.session_state.class_level_selected = True
                            st.rerun()
            else:
                # For non-teaching exams, skip class level selection
                st.session_state.selected_paper = "General"
                st.session_state.class_level_selected = True
                st.rerun()

        # Step 2: Subject Selection
        elif not st.session_state.subject_selected:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        padding: 2rem; border-radius: 10px; color: white; margin-bottom: 2rem;">
                <h3>📖 Step 2: Select Subject</h3>
                <p>Choose the subject you want to practice</p>
            </div>
            """, unsafe_allow_html=True)

            st.info(f"📄 Selected: **{st.session_state.selected_paper}**")
            st.divider()

            st.markdown("### Available Subjects:")

            # Display subject options based on exam
            if "subjects" in exam:
                # Create a grid layout for subjects (3 columns)
                subjects = exam["subjects"]
                cols_per_row = 3

                for i in range(0, len(subjects), cols_per_row):
                    cols = st.columns(cols_per_row)
                    for j, col in enumerate(cols):
                        if i + j < len(subjects):
                            subject = subjects[i + j]
                            with col:
                                # Subject icon mapping
                                subject_icons = {
                                    "Child Development": "👶",
                                    "Mathematics": "🔢",
                                    "Science": "🔬",
                                    "Social Studies": "🌍",
                                    "Language": "📝",
                                    "English": "🔤",
                                    "Hindi": "🇮🇳",
                                    "Computer Science": "💻",
                                    "Physics": "⚛️",
                                    "Chemistry": "🧪",
                                    "Biology": "🧬",
                                    "History": "📜",
                                    "Geography": "🗺️",
                                    "Economics": "💰",
                                    "Political Science": "🏛️",
                                    "Commerce": "📊",
                                    "Accountancy": "📈",
                                    "Business Studies": "💼",
                                    "General Knowledge": "🧠",
                                    "Current Affairs": "📰",
                                    "Reasoning": "💭",
                                    "EVS": "🌱",
                                    "Language I": "📖",
                                    "Language II": "📚"
                                }

                                icon = subject_icons.get(subject, "📘")

                                st.markdown(f"""
                                <div style="background: #f8f9fa; padding: 1rem; border-radius: 8px;
                                            text-align: center; border: 2px solid #667eea; margin-bottom: 1rem;">
                                    <p style="font-size: 2rem; margin: 0;">{icon}</p>
                                    <p style="margin: 0.5rem 0;"><strong>{subject}</strong></p>
                                </div>
                                """, unsafe_allow_html=True)

                                if st.button("Choose", key=f"subject_{subject}", use_container_width=True, type="primary"):
                                    st.session_state.selected_subject = subject
                                    st.session_state.subject_selected = True
                                    st.rerun()

            st.divider()

            # Back button
            if st.button("⬅️ Back to Class Level", use_container_width=True):
                st.session_state.class_level_selected = False
                st.rerun()

        # Step 3: Candidate Details and Test
        elif not st.session_state.test_started:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        padding: 2rem; border-radius: 10px; color: white; margin-bottom: 2rem;">
                <h3>📋 Step 3: Enter Your Details</h3>
                <p>Selected: {st.session_state.selected_paper} | Subject: {st.session_state.selected_subject}</p>
            </div>
            """, unsafe_allow_html=True)

            # Show selected options
            col1, col2 = st.columns(2)
            with col1:
                st.success(f"📄 **Class Level:** {st.session_state.selected_paper}")
            with col2:
                st.success(f"📖 **Subject:** {st.session_state.selected_subject}")

            st.divider()

            col1, col2 = st.columns(2)
            with col1:
                candidate_name = st.text_input("Full Name *", placeholder="Enter your full name")
            with col2:
                candidate_email = st.text_input("Email *", placeholder="your.email@example.com")

            col3, col4 = st.columns(2)
            with col3:
                candidate_roll = st.text_input("Roll Number (Optional)", placeholder="e.g., 2024001")
            with col4:
                candidate_phone = st.text_input("Phone Number (Optional)", placeholder="10-digit number")

            st.divider()

            # Exam instructions
            st.markdown("### 📜 Exam Instructions")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.info(f"⏱️ **Duration**\n\n{exam['duration']} minutes")
            with col2:
                st.info(f"📝 **Questions**\n\n{exam['questions']} MCQs")
            with col3:
                st.info(f"🎯 **Total Marks**\n\n{exam['marks']} marks")

            st.markdown("""
            **Important Points:**
            - ✅ Each question has 4 options (A, B, C, D)
            - ✅ Only one option is correct
            - ✅ Negative marking: 0.25 marks for wrong answer
            - ✅ You can mark questions for review
            - ✅ Test will auto-submit after time expires
            - ✅ Make sure you have stable internet connection
            """)

            st.divider()

            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("⬅️ Back to Subjects", use_container_width=True):
                    st.session_state.subject_selected = False
                    st.rerun()
            with col2:
                if st.button("🚀 Start Test Now", use_container_width=True, type="primary"):
                    if not candidate_name or not candidate_email:
                        st.error("⚠️ Please enter your name and email to continue")
                    else:
                        st.session_state.test_started = True
                        st.session_state.candidate_name = candidate_name
                        st.session_state.candidate_email = candidate_email
                        st.session_state.candidate_roll = candidate_roll
                        st.session_state.start_time = datetime.now()
                        st.success("✅ Test started! Good luck!")
                        st.rerun()
            with col3:
                pass  # Empty column for spacing

        # Test started - show questions
        else:
            # Calculate remaining time
            elapsed = (datetime.now() - st.session_state.start_time).seconds
            remaining_seconds = exam['duration'] * 60 - elapsed
            remaining_minutes = remaining_seconds // 60
            remaining_secs = remaining_seconds % 60

            # Top bar with timer and progress
            col1, col2, col3 = st.columns([2, 2, 1])
            with col1:
                st.markdown(f"**Candidate:** {st.session_state.candidate_name}")
            with col2:
                if remaining_seconds > 0:
                    st.markdown(f"⏱️ **Time Remaining:** {remaining_minutes:02d}:{remaining_secs:02d}")
                else:
                    st.error("⏰ Time's Up! Submitting test...")
                    # Auto-submit logic would go here
            with col3:
                st.markdown(f"**Q {st.session_state.current_question + 1}/{exam['questions']}**")

            st.progress((st.session_state.current_question + 1) / exam['questions'])

            # Show selected options at top
            st.info(f"📄 **{st.session_state.selected_paper}** | 📖 **{st.session_state.selected_subject}**")

            st.divider()

            # Generate subject-specific questions
            selected_subject = st.session_state.selected_subject

            # Subject-specific question templates
            subject_questions = {
                "Computer Science": [
                    # Basic Computer Knowledge
                    {"q": "What does CPU stand for?", "opts": ["Central Processing Unit", "Central Program Unit", "Computer Personal Unit", "Central Processor Universal"], "ans": "A"},
                    {"q": "What is the brain of the computer called?", "opts": ["CPU", "RAM", "Hard Disk", "Monitor"], "ans": "A"},
                    {"q": "What is the full form of RAM?", "opts": ["Random Access Memory", "Read Access Memory", "Run Access Memory", "Rapid Access Memory"], "ans": "A"},
                    {"q": "Which is the smallest unit of data in a computer?", "opts": ["Bit", "Byte", "Nibble", "Word"], "ans": "A"},
                    {"q": "What is 1 GB equal to?", "opts": ["1024 MB", "1000 MB", "1024 KB", "1000 KB"], "ans": "A"},
                    {"q": "What is the speed of a processor measured in?", "opts": ["GHz", "GB", "MB", "KB"], "ans": "A"},
                    {"q": "What is 1 KB equal to?", "opts": ["1024 Bytes", "1000 Bytes", "1024 Bits", "1000 Bits"], "ans": "A"},
                    {"q": "Which is the fastest memory?", "opts": ["Cache Memory", "RAM", "Hard Disk", "ROM"], "ans": "A"},
                    {"q": "What does ROM stand for?", "opts": ["Read Only Memory", "Random Only Memory", "Read Online Memory", "Random Open Memory"], "ans": "A"},
                    {"q": "Which type of memory is volatile?", "opts": ["RAM", "ROM", "Hard Disk", "SSD"], "ans": "A"},

                    # Input/Output Devices
                    {"q": "Which device is used to input data into a computer?", "opts": ["Keyboard", "Monitor", "Speaker", "Printer"], "ans": "A"},
                    {"q": "Which of the following is an output device?", "opts": ["Monitor", "Keyboard", "Mouse", "Scanner"], "ans": "A"},
                    {"q": "Which is both input and output device?", "opts": ["Touch Screen", "Keyboard", "Monitor", "Printer"], "ans": "A"},
                    {"q": "What is a scanner used for?", "opts": ["Input images to computer", "Print documents", "Display text", "Store data"], "ans": "A"},
                    {"q": "Which device converts digital to analog signals?", "opts": ["Modem", "Scanner", "Printer", "Monitor"], "ans": "A"},

                    # Programming Languages
                    {"q": "Which programming language is known as the mother of all languages?", "opts": ["C", "Assembly", "COBOL", "FORTRAN"], "ans": "A"},
                    {"q": "What is the extension of a Python file?", "opts": [".py", ".python", ".pt", ".p"], "ans": "A"},
                    {"q": "Which company developed Java programming language?", "opts": ["Sun Microsystems", "Microsoft", "Apple", "IBM"], "ans": "A"},
                    {"q": "Which language is used for web development?", "opts": ["JavaScript", "C++", "Java", "COBOL"], "ans": "A"},
                    {"q": "Which language is used for Android app development?", "opts": ["Kotlin", "Swift", "Ruby", "Perl"], "ans": "A"},
                    {"q": "What does OOP stand for?", "opts": ["Object Oriented Programming", "Only Object Programming", "Objective Oriented Programming", "Object Order Programming"], "ans": "A"},
                    {"q": "Which is a low-level programming language?", "opts": ["Assembly", "Python", "Java", "JavaScript"], "ans": "A"},
                    {"q": "Which language is used for iOS development?", "opts": ["Swift", "Kotlin", "Python", "Ruby"], "ans": "A"},
                    {"q": "What is Python known for?", "opts": ["Easy syntax and readability", "Game development", "Mobile apps", "Hardware programming"], "ans": "A"},
                    {"q": "Which language uses indentation for code blocks?", "opts": ["Python", "Java", "C++", "JavaScript"], "ans": "A"},

                    # Web Technologies
                    {"q": "HTML stands for?", "opts": ["Hyper Text Markup Language", "High Text Machine Language", "Hyperlinks and Text Markup Language", "Home Tool Markup Language"], "ans": "A"},
                    {"q": "What does WWW stand for?", "opts": ["World Wide Web", "Wide World Web", "Web World Wide", "World Web Wide"], "ans": "A"},
                    {"q": "What does URL stand for?", "opts": ["Uniform Resource Locator", "Universal Resource Locator", "Uniform Reference Locator", "Universal Reference Locator"], "ans": "A"},
                    {"q": "Which protocol is used for web pages?", "opts": ["HTTP", "FTP", "SMTP", "POP3"], "ans": "A"},
                    {"q": "What does CSS stand for?", "opts": ["Cascading Style Sheets", "Computer Style Sheets", "Creative Style Sheets", "Colorful Style Sheets"], "ans": "A"},
                    {"q": "Which tag is used for hyperlinks in HTML?", "opts": ["<a>", "<link>", "<href>", "<url>"], "ans": "A"},
                    {"q": "What is the default port for HTTP?", "opts": ["80", "443", "21", "25"], "ans": "A"},
                    {"q": "What is the default port for HTTPS?", "opts": ["443", "80", "8080", "3000"], "ans": "A"},
                    {"q": "Which language makes web pages interactive?", "opts": ["JavaScript", "HTML", "CSS", "XML"], "ans": "A"},
                    {"q": "What does AJAX stand for?", "opts": ["Asynchronous JavaScript and XML", "Advanced Java and XML", "Automatic JavaScript and XML", "Active Java and XML"], "ans": "A"},

                    # Networking
                    {"q": "Which protocol is used for sending emails?", "opts": ["SMTP", "HTTP", "FTP", "TCP"], "ans": "A"},
                    {"q": "What does IP stand for in IP address?", "opts": ["Internet Protocol", "Internal Protocol", "Internet Process", "Internal Process"], "ans": "A"},
                    {"q": "Which device connects multiple networks?", "opts": ["Router", "Hub", "Switch", "Modem"], "ans": "A"},
                    {"q": "What is the range of Class C IP address?", "opts": ["192.0.0.0 to 223.255.255.255", "128.0.0.0 to 191.255.255.255", "1.0.0.0 to 126.255.255.255", "224.0.0.0 to 239.255.255.255"], "ans": "A"},
                    {"q": "Which protocol is used for file transfer?", "opts": ["FTP", "HTTP", "SMTP", "POP3"], "ans": "A"},
                    {"q": "What does DNS stand for?", "opts": ["Domain Name System", "Dynamic Name System", "Domain Network System", "Data Name System"], "ans": "A"},
                    {"q": "Which layer is responsible for routing in OSI model?", "opts": ["Network Layer", "Transport Layer", "Data Link Layer", "Session Layer"], "ans": "A"},
                    {"q": "What is the full form of LAN?", "opts": ["Local Area Network", "Large Area Network", "Long Area Network", "Limited Area Network"], "ans": "A"},
                    {"q": "Which topology uses a single cable?", "opts": ["Bus Topology", "Star Topology", "Ring Topology", "Mesh Topology"], "ans": "A"},
                    {"q": "What is the maximum speed of Wi-Fi 6?", "opts": ["9.6 Gbps", "5 Gbps", "1 Gbps", "100 Mbps"], "ans": "A"},

                    # Operating Systems
                    {"q": "What does OS stand for?", "opts": ["Operating System", "Open System", "Operational Software", "Online System"], "ans": "A"},
                    {"q": "Which is an example of system software?", "opts": ["Windows", "MS Word", "Chrome", "Photoshop"], "ans": "A"},
                    {"q": "Which OS is open source?", "opts": ["Linux", "Windows", "macOS", "iOS"], "ans": "A"},
                    {"q": "What is the kernel in OS?", "opts": ["Core of OS", "User interface", "Application layer", "File system"], "ans": "A"},
                    {"q": "Which scheduling algorithm gives priority to shortest job?", "opts": ["SJF", "FCFS", "Round Robin", "Priority"], "ans": "A"},
                    {"q": "What is virtual memory?", "opts": ["Hard disk used as RAM", "Extra RAM", "Cache memory", "ROM"], "ans": "A"},
                    {"q": "Which command shows directory contents in Linux?", "opts": ["ls", "dir", "show", "list"], "ans": "A"},
                    {"q": "What is multitasking in OS?", "opts": ["Running multiple tasks simultaneously", "Running one task", "Switching between users", "Booting system"], "ans": "A"},
                    {"q": "Which file system is used by Windows?", "opts": ["NTFS", "ext4", "FAT", "HFS+"], "ans": "A"},
                    {"q": "What is the purpose of device drivers?", "opts": ["Interface between OS and hardware", "Run applications", "Manage files", "Control network"], "ans": "A"},

                    # Database & Data Structures
                    {"q": "What does SQL stand for?", "opts": ["Structured Query Language", "Simple Query Language", "Standard Query Language", "System Query Language"], "ans": "A"},
                    {"q": "Which is a NoSQL database?", "opts": ["MongoDB", "MySQL", "Oracle", "PostgreSQL"], "ans": "A"},
                    {"q": "What is a primary key?", "opts": ["Unique identifier for records", "Foreign key", "Index", "Constraint"], "ans": "A"},
                    {"q": "Which data structure uses LIFO?", "opts": ["Stack", "Queue", "Tree", "Graph"], "ans": "A"},
                    {"q": "Which data structure uses FIFO?", "opts": ["Queue", "Stack", "Tree", "Graph"], "ans": "A"},
                    {"q": "What is the time complexity of binary search?", "opts": ["O(log n)", "O(n)", "O(n²)", "O(1)"], "ans": "A"},
                    {"q": "Which is faster: Array or Linked List for access?", "opts": ["Array", "Linked List", "Both same", "Depends on size"], "ans": "A"},
                    {"q": "What is a hash table?", "opts": ["Key-value data structure", "Linear structure", "Tree structure", "Graph structure"], "ans": "A"},

                    # Number Systems & Binary
                    {"q": "What is the binary representation of decimal 5?", "opts": ["101", "110", "011", "100"], "ans": "A"},
                    {"q": "What is the binary representation of decimal 10?", "opts": ["1010", "1001", "1100", "0110"], "ans": "A"},
                    {"q": "What is hexadecimal A equal to in decimal?", "opts": ["10", "11", "15", "16"], "ans": "A"},
                    {"q": "How many bits in a byte?", "opts": ["8", "4", "16", "32"], "ans": "A"},
                    {"q": "What is octal number system base?", "opts": ["8", "10", "16", "2"], "ans": "A"},

                    # Software & Security
                    {"q": "What is malware?", "opts": ["Malicious software", "Good software", "System software", "Application software"], "ans": "A"},
                    {"q": "What does VPN stand for?", "opts": ["Virtual Private Network", "Very Private Network", "Virtual Public Network", "Valid Private Network"], "ans": "A"},
                    {"q": "Which is an antivirus software?", "opts": ["Norton", "Chrome", "Windows", "MS Office"], "ans": "A"},
                    {"q": "What is phishing?", "opts": ["Fake emails to steal data", "Computer virus", "Firewall attack", "DDoS attack"], "ans": "A"},
                    {"q": "What does HTTPS provide?", "opts": ["Secure communication", "Fast browsing", "File download", "Email service"], "ans": "A"},

                    # Miscellaneous
                    {"q": "Which key is used to refresh a webpage?", "opts": ["F5", "F1", "F12", "Ctrl+R"], "ans": "A"},
                    {"q": "What is cloud computing?", "opts": ["Internet-based computing", "Local computing", "Mobile computing", "Desktop computing"], "ans": "A"},
                    {"q": "Who is called the father of computers?", "opts": ["Charles Babbage", "Alan Turing", "Bill Gates", "Steve Jobs"], "ans": "A"},
                    {"q": "What is AI?", "opts": ["Artificial Intelligence", "Automated Intelligence", "Advanced Intelligence", "Applied Intelligence"], "ans": "A"},
                    {"q": "What does IoT stand for?", "opts": ["Internet of Things", "Internet of Technology", "Internal of Things", "International of Technology"], "ans": "A"},
                    {"q": "What is machine learning?", "opts": ["Computer learning from data", "Manual programming", "Hardware learning", "Network learning"], "ans": "A"},
                    {"q": "Which company developed Windows?", "opts": ["Microsoft", "Apple", "Google", "IBM"], "ans": "A"},
                    {"q": "What is open source software?", "opts": ["Free and modifiable code", "Paid software", "Closed software", "Trial software"], "ans": "A"},
                    {"q": "What is Git used for?", "opts": ["Version control", "Web browsing", "Video editing", "Gaming"], "ans": "A"},
                    {"q": "What does API stand for?", "opts": ["Application Programming Interface", "Applied Programming Interface", "Automatic Programming Interface", "Advanced Programming Interface"], "ans": "A"},
                ],
                "Mathematics": [
                    # Arithmetic
                    {"q": "What is 15 + 25?", "opts": ["40", "35", "45", "50"], "ans": "A"},
                    {"q": "What is 48 - 19?", "opts": ["29", "27", "31", "33"], "ans": "A"},
                    {"q": "What is 8 × 7?", "opts": ["56", "54", "48", "64"], "ans": "A"},
                    {"q": "What is 100 ÷ 5?", "opts": ["20", "15", "25", "30"], "ans": "A"},
                    {"q": "What is 12 × 12?", "opts": ["144", "124", "156", "132"], "ans": "A"},
                    {"q": "What is 75 + 38?", "opts": ["113", "103", "123", "93"], "ans": "A"},
                    {"q": "What is 200 - 87?", "opts": ["113", "123", "103", "93"], "ans": "A"},
                    {"q": "What is 25 × 4?", "opts": ["100", "90", "110", "120"], "ans": "A"},
                    {"q": "What is 144 ÷ 12?", "opts": ["12", "14", "10", "16"], "ans": "A"},
                    {"q": "What is 50% of 200?", "opts": ["100", "50", "150", "75"], "ans": "A"},

                    # Fractions & Decimals
                    {"q": "What is 1/2 + 1/4?", "opts": ["3/4", "2/4", "1/4", "1/2"], "ans": "A"},
                    {"q": "What is 0.5 × 10?", "opts": ["5", "0.05", "50", "0.5"], "ans": "A"},
                    {"q": "What is 3/4 as a decimal?", "opts": ["0.75", "0.5", "0.25", "0.85"], "ans": "A"},
                    {"q": "What is 25% as a fraction?", "opts": ["1/4", "1/2", "1/3", "2/5"], "ans": "A"},
                    {"q": "What is 2.5 + 3.7?", "opts": ["6.2", "5.2", "7.2", "6.0"], "ans": "A"},

                    # Geometry
                    {"q": "What is the area of a square with side 5cm?", "opts": ["25 cm²", "20 cm²", "30 cm²", "10 cm²"], "ans": "A"},
                    {"q": "What is the perimeter of a rectangle with length 10cm and width 5cm?", "opts": ["30 cm", "25 cm", "50 cm", "15 cm"], "ans": "A"},
                    {"q": "How many sides does a hexagon have?", "opts": ["6", "5", "7", "8"], "ans": "A"},
                    {"q": "What is the sum of angles in a triangle?", "opts": ["180°", "90°", "360°", "270°"], "ans": "A"},
                    {"q": "What is the value of π (pi) approximately?", "opts": ["3.14", "2.14", "4.14", "5.14"], "ans": "A"},
                    {"q": "What is the area of a circle with radius 7cm (π=22/7)?", "opts": ["154 cm²", "144 cm²", "164 cm²", "134 cm²"], "ans": "A"},
                    {"q": "What is the circumference of a circle with radius 7cm?", "opts": ["44 cm", "49 cm", "42 cm", "56 cm"], "ans": "A"},
                    {"q": "How many degrees in a right angle?", "opts": ["90°", "180°", "45°", "360°"], "ans": "A"},

                    # Algebra
                    {"q": "If x + 5 = 12, what is x?", "opts": ["7", "8", "6", "5"], "ans": "A"},
                    {"q": "What is 2x when x = 3?", "opts": ["6", "5", "9", "3"], "ans": "A"},
                    {"q": "If 3x = 15, what is x?", "opts": ["5", "4", "6", "3"], "ans": "A"},
                    {"q": "What is x² when x = 4?", "opts": ["16", "8", "12", "20"], "ans": "A"},
                    {"q": "If y = 2x + 1 and x = 3, what is y?", "opts": ["7", "6", "8", "5"], "ans": "A"},

                    # Powers & Roots
                    {"q": "What is the square root of 144?", "opts": ["12", "14", "10", "16"], "ans": "A"},
                    {"q": "What is the square root of 81?", "opts": ["9", "7", "11", "8"], "ans": "A"},
                    {"q": "What is 2³?", "opts": ["8", "6", "9", "4"], "ans": "A"},
                    {"q": "What is 5²?", "opts": ["25", "20", "30", "10"], "ans": "A"},
                    {"q": "What is the cube of 3?", "opts": ["27", "9", "18", "36"], "ans": "A"},
                    {"q": "What is the square root of 100?", "opts": ["10", "11", "9", "12"], "ans": "A"},

                    # Number Theory
                    {"q": "Which is a prime number?", "opts": ["7", "8", "9", "10"], "ans": "A"},
                    {"q": "What is the LCM of 4 and 6?", "opts": ["12", "24", "8", "6"], "ans": "A"},
                    {"q": "What is the HCF of 12 and 18?", "opts": ["6", "3", "9", "12"], "ans": "A"},
                    {"q": "Which number is divisible by 3?", "opts": ["27", "25", "26", "28"], "ans": "A"},
                    {"q": "What is the next prime number after 7?", "opts": ["11", "9", "10", "13"], "ans": "A"},

                    # Percentages & Ratios
                    {"q": "What is 20% of 500?", "opts": ["100", "150", "50", "200"], "ans": "A"},
                    {"q": "What is the ratio of 10 to 5?", "opts": ["2:1", "1:2", "5:1", "1:5"], "ans": "A"},
                    {"q": "If 30% students passed, what % failed?", "opts": ["70%", "60%", "80%", "50%"], "ans": "A"},
                    {"q": "What is 10% of 1000?", "opts": ["100", "10", "1000", "50"], "ans": "A"},

                    # Word Problems
                    {"q": "A book costs ₹150 and you pay ₹200. What is the change?", "opts": ["₹50", "₹40", "₹60", "₹30"], "ans": "A"},
                    {"q": "If a car travels 60km in 1 hour, how far in 3 hours?", "opts": ["180 km", "120 km", "240 km", "150 km"], "ans": "A"},
                    {"q": "5 apples cost ₹25. What is the cost of 1 apple?", "opts": ["₹5", "₹4", "₹6", "₹3"], "ans": "A"},
                    {"q": "A train leaves at 10:00 and arrives at 13:00. How long is the journey?", "opts": ["3 hours", "2 hours", "4 hours", "5 hours"], "ans": "A"},
                ],
                "Science": [
                    {"q": "What is the chemical symbol for water?", "opts": ["H2O", "O2", "CO2", "H2"], "ans": "A"},
                    {"q": "Which planet is known as the Red Planet?", "opts": ["Mars", "Venus", "Jupiter", "Saturn"], "ans": "A"},
                    {"q": "What is the speed of light?", "opts": ["3×10^8 m/s", "3×10^6 m/s", "3×10^9 m/s", "3×10^7 m/s"], "ans": "A"},
                    {"q": "What is the largest organ in the human body?", "opts": ["Skin", "Heart", "Liver", "Brain"], "ans": "A"},
                    {"q": "What gas do plants absorb from the atmosphere?", "opts": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen"], "ans": "A"},
                ],
                "English": [
                    {"q": "What is the past tense of 'go'?", "opts": ["Went", "Gone", "Going", "Goes"], "ans": "A"},
                    {"q": "Which is a pronoun?", "opts": ["He", "Run", "Beautiful", "Quickly"], "ans": "A"},
                    {"q": "What is a synonym for 'happy'?", "opts": ["Joyful", "Sad", "Angry", "Worried"], "ans": "A"},
                    {"q": "Which article is used before 'hour'?", "opts": ["An", "A", "The", "No article"], "ans": "A"},
                    {"q": "What is the plural of 'child'?", "opts": ["Children", "Childs", "Childes", "Childrens"], "ans": "A"},
                ],
                "History": [
                    {"q": "Who was the first President of India?", "opts": ["Dr. Rajendra Prasad", "Jawaharlal Nehru", "Mahatma Gandhi", "Sardar Patel"], "ans": "A"},
                    {"q": "In which year did India gain independence?", "opts": ["1947", "1950", "1942", "1945"], "ans": "A"},
                    {"q": "Who wrote the Indian National Anthem?", "opts": ["Rabindranath Tagore", "Bankim Chandra", "Subhash Bose", "Bhagat Singh"], "ans": "A"},
                    {"q": "What was the capital of the Mauryan Empire?", "opts": ["Pataliputra", "Delhi", "Ujjain", "Varanasi"], "ans": "A"},
                    {"q": "Who is known as the Father of the Indian Constitution?", "opts": ["Dr. B.R. Ambedkar", "Jawaharlal Nehru", "Mahatma Gandhi", "Sardar Patel"], "ans": "A"},
                ],
                "Geography": [
                    {"q": "What is the capital of India?", "opts": ["New Delhi", "Mumbai", "Kolkata", "Chennai"], "ans": "A"},
                    {"q": "Which is the longest river in India?", "opts": ["Ganga", "Yamuna", "Godavari", "Brahmaputra"], "ans": "A"},
                    {"q": "How many states are there in India?", "opts": ["28", "29", "30", "27"], "ans": "A"},
                    {"q": "Which is the highest mountain peak in India?", "opts": ["Kanchenjunga", "K2", "Nanda Devi", "Mount Everest"], "ans": "A"},
                    {"q": "Which ocean is to the south of India?", "opts": ["Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean"], "ans": "A"},
                ],
                "Child Development": [
                    {"q": "According to Piaget, which stage occurs from ages 2-7?", "opts": ["Preoperational", "Sensorimotor", "Concrete Operational", "Formal Operational"], "ans": "A"},
                    {"q": "What is the most critical period for brain development?", "opts": ["0-6 years", "6-12 years", "12-18 years", "18-24 years"], "ans": "A"},
                    {"q": "Who proposed the theory of Multiple Intelligences?", "opts": ["Howard Gardner", "Jean Piaget", "Lev Vygotsky", "Erik Erikson"], "ans": "A"},
                    {"q": "What does ZPD stand for in child development?", "opts": ["Zone of Proximal Development", "Zero Point Development", "Zonal Physical Development", "Zone of Primary Development"], "ans": "A"},
                    {"q": "At what age do children typically start walking?", "opts": ["12-15 months", "6-9 months", "18-24 months", "24-30 months"], "ans": "A"},
                ],
            }

            # Get questions for selected subject or use default
            if selected_subject in subject_questions:
                base_questions = subject_questions[selected_subject]
            else:
                # Default questions if subject not found
                base_questions = [
                    {"q": f"Sample question for {selected_subject}", "opts": ["Option A", "Option B", "Option C", "Option D"], "ans": "A"}
                ]

            # Generate full question set with randomization to reduce repetition
            import random
            sample_questions = []

            # Create a larger pool by repeating base questions
            question_pool = []
            num_repeats = (exam['questions'] // len(base_questions)) + 1

            for repeat in range(num_repeats):
                shuffled_questions = base_questions.copy()
                random.shuffle(shuffled_questions)
                question_pool.extend(shuffled_questions)

            # Take only what we need
            question_pool = question_pool[:exam['questions']]

            # Generate questions with shuffled options
            for i, base_q in enumerate(question_pool):
                # Shuffle the options
                options_list = base_q['opts'].copy()
                correct_answer_text = base_q['opts'][ord(base_q['ans']) - ord('A')]
                random.shuffle(options_list)

                # Find new position of correct answer
                new_correct_index = options_list.index(correct_answer_text)
                new_correct_letter = chr(ord('A') + new_correct_index)

                sample_questions.append({
                    "id": i,
                    "text": f"Question {i+1} ({selected_subject}): {base_q['q']}",
                    "options": {
                        "A": options_list[0],
                        "B": options_list[1],
                        "C": options_list[2],
                        "D": options_list[3]
                    },
                    "correct": new_correct_letter,
                    "marks": 1
                })

            current_q = sample_questions[st.session_state.current_question]

            # Display question
            st.markdown(f"""
            <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px; border-left: 4px solid #667eea;">
                <h4>Question {current_q['id'] + 1}</h4>
                <p style="font-size: 1.1rem;">{current_q['text']}</p>
                <p style="color: #666; margin-top: 1rem;"><strong>Marks:</strong> {current_q['marks']} | <strong>Negative:</strong> 0.25</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### Select Your Answer:")

            # Get current saved answer
            selected_answer = st.session_state.answers.get(current_q['id'], None)

            # Function to save answer (defined outside loop)
            def save_answer_callback(q_id, opt):
                """Save answer to session state"""
                st.session_state.answers[q_id] = opt

            # Create clickable option buttons - SIMPLE AND RELIABLE
            for option_key, option_text in current_q['options'].items():
                # Check if this option is currently selected
                is_selected = (selected_answer == option_key)

                # Add selection indicator to button text
                button_label = f"{'✅ ' if is_selected else '⭕ '}{option_key}. {option_text}"
                button_type = "primary" if is_selected else "secondary"

                # Create button with absolutely unique key
                button_key = f"question_{current_q['id']}_option_{option_key}_pos_{st.session_state.current_question}"

                # Button with on_click callback to save answer
                # This saves the answer without changing the question
                st.button(
                    button_label,
                    key=button_key,
                    use_container_width=True,
                    type=button_type,
                    help=f"Select option {option_key}",
                    on_click=save_answer_callback,
                    args=(current_q['id'], option_key)
                )

            # Show currently selected answer
            st.divider()
            if selected_answer:
                st.success(f"✓ Your Answer: **{selected_answer}**")
            else:
                st.info("💡 Click any option above to select your answer")

            # DEBUG INFO - Shows what's actually saved
            with st.expander("🔍 Debug Info (Click to see saved answers)", expanded=False):
                st.write(f"**Current Question ID:** {current_q['id']}")
                st.write(f"**Question Number:** {st.session_state.current_question + 1}")
                st.write(f"**Saved Answer:** {st.session_state.answers.get(current_q['id'], 'None')}")
                st.write(f"**Total Answers Saved:** {len(st.session_state.answers)}")
                if len(st.session_state.answers) > 0:
                    st.write("**All Saved Answers:**")
                    for q_id, ans in sorted(st.session_state.answers.items()):
                        st.write(f"  Question {q_id}: {ans}")

            st.divider()

            # Navigation buttons
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                if st.session_state.current_question > 0:
                    if st.button("⬅️ Previous", use_container_width=True):
                        # Answer is already saved, just move back
                        st.session_state.current_question -= 1
                        st.rerun()

            with col2:
                if st.button("🔖 Mark for Review", use_container_width=True):
                    if current_q['id'] in st.session_state.marked_for_review:
                        st.session_state.marked_for_review.remove(current_q['id'])
                    else:
                        st.session_state.marked_for_review.add(current_q['id'])
                    st.rerun()

            with col3:
                if st.button("⏭️ Clear Selection", use_container_width=True):
                    # Clear the answer for this question
                    if current_q['id'] in st.session_state.answers:
                        del st.session_state.answers[current_q['id']]
                    st.rerun()

            with col4:
                if st.session_state.current_question < exam['questions'] - 1:
                    if st.button("➡️ Next", use_container_width=True, type="primary"):
                        # Answer is already saved, just move forward
                        st.session_state.current_question += 1
                        st.rerun()

            st.divider()

            # Question palette
            st.markdown("### 📊 Question Palette")
            st.markdown("""
            <div style="padding: 0.5rem; background: #f8f9fa; border-radius: 5px; margin-bottom: 1rem;">
                <span style="color: #28a745;">🟢 Green: Answered</span> |
                <span style="color: #ffc107;">🟡 Yellow: Marked for Review</span> |
                <span style="color: #6c757d;">⚪ Gray: Not Visited</span>
            </div>
            """, unsafe_allow_html=True)

            # Display questions in grid (10 per row)
            questions_per_row = 10
            for row_start in range(0, exam['questions'], questions_per_row):
                cols = st.columns(questions_per_row)
                for i, col in enumerate(cols):
                    q_num = row_start + i
                    if q_num < exam['questions']:
                        with col:
                            # Determine status and styling
                            is_answered = q_num in st.session_state.answers
                            is_marked = q_num in st.session_state.marked_for_review
                            is_current = q_num == st.session_state.current_question

                            # Set label and button type based on status
                            if is_answered:
                                label = f"✓ {q_num + 1}"
                                btn_type = "primary"  # Blue/Green - Answered
                            elif is_marked:
                                label = f"🔖 {q_num + 1}"
                                btn_type = "secondary"  # Yellow - Marked
                            else:
                                label = f"{q_num + 1}"
                                btn_type = "secondary"  # Gray - Not visited

                            # Clickable button for navigation
                            if st.button(
                                label,
                                key=f"palette_{q_num}",
                                use_container_width=True,
                                type=btn_type,
                                help=f"Jump to question {q_num + 1}"
                            ):
                                st.session_state.current_question = q_num
                                st.rerun()

            st.divider()

            # Submit section
            st.markdown("### 📤 Submit Test")

            answered = len(st.session_state.answers)
            not_answered = exam['questions'] - answered
            marked = len(st.session_state.marked_for_review)

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Answered", answered, f"{(answered/exam['questions']*100):.0f}%")
            with col2:
                st.metric("Not Answered", not_answered)
            with col3:
                st.metric("Marked for Review", marked)

            if not_answered > 0:
                st.warning(f"⚠️ You have {not_answered} unanswered questions!")

            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("📥 Submit Test", use_container_width=True, type="primary"):
                    # Calculate results
                    correct_count = 0
                    wrong_count = 0

                    for q in sample_questions:
                        if q['id'] in st.session_state.answers:
                            if st.session_state.answers[q['id']] == q['correct']:
                                correct_count += 1
                            else:
                                wrong_count += 1

                    total_marks = correct_count * 1 - wrong_count * 0.25
                    percentage = (total_marks / exam['marks']) * 100

                    # Store results
                    st.session_state.test_completed = True
                    st.session_state.correct_answers = correct_count
                    st.session_state.wrong_answers = wrong_count
                    st.session_state.total_marks = total_marks
                    st.session_state.percentage = percentage

                    st.success("✅ Test submitted successfully!")
                    st.rerun()

        # Show results if test completed
        if 'test_completed' in st.session_state and st.session_state.test_completed:
            st.balloons()

            st.markdown("""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        padding: 2rem; border-radius: 10px; color: white; text-align: center; margin-bottom: 2rem;">
                <h2>🎉 Test Completed!</h2>
                <p>Congratulations on completing the test. Here are your results:</p>
            </div>
            """, unsafe_allow_html=True)

            # Results summary
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Correct Answers", st.session_state.correct_answers, f"✅")
            with col2:
                st.metric("Wrong Answers", st.session_state.wrong_answers, "❌")
            with col3:
                st.metric("Total Marks", f"{st.session_state.total_marks:.2f}", f"Out of {exam['marks']}")
            with col4:
                st.metric("Percentage", f"{st.session_state.percentage:.2f}%",
                         "🏆" if st.session_state.percentage >= 75 else "👍")

            st.divider()

            # Grade
            if st.session_state.percentage >= 90:
                grade = "A+"
                remark = "Outstanding! 🏆"
            elif st.session_state.percentage >= 80:
                grade = "A"
                remark = "Excellent! 🌟"
            elif st.session_state.percentage >= 70:
                grade = "B+"
                remark = "Very Good! 👏"
            elif st.session_state.percentage >= 60:
                grade = "B"
                remark = "Good! 👍"
            elif st.session_state.percentage >= 50:
                grade = "C"
                remark = "Average - Keep Practicing! 💪"
            else:
                grade = "F"
                remark = "Need Improvement - Don't Give Up! 📚"

            st.markdown(f"""
            <div style="background: #f8f9fa; padding: 2rem; border-radius: 10px; text-align: center;">
                <h3>Your Grade: {grade}</h3>
                <p style="font-size: 1.2rem; color: #667eea;"><strong>{remark}</strong></p>
            </div>
            """, unsafe_allow_html=True)

            st.divider()

            # Action buttons
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("🔄 Take Another Test", use_container_width=True):
                    # Reset test state including new selections
                    for key in ['test_started', 'current_question', 'answers', 'marked_for_review',
                               'test_completed', 'selected_exam_for_test', 'selected_set_number',
                               'class_level_selected', 'subject_selected', 'selected_paper', 'selected_subject']:
                        if key in st.session_state:
                            del st.session_state[key]
                    st.session_state.nav_page = "📚 All Exams"
                    st.rerun()
            with col2:
                if st.button("📊 View Performance", use_container_width=True):
                    st.session_state.nav_page = "📊 My Performance"
                    st.rerun()
            with col3:
                if st.button("🏠 Go to Home", use_container_width=True):
                    st.session_state.nav_page = "🏠 Home Dashboard"
                    st.rerun()

elif page == "📊 My Performance":
    st.markdown("### 📊 Your Performance Analytics")

    # Overall stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Tests Taken", "47", "+12 this month")
    with col2:
        st.metric("Average Score", "72.5%", "+5.3%")
    with col3:
        st.metric("Time Spent", "85h 30m", "+18h")
    with col4:
        st.metric("Overall Rank", "#124", "↑23")

    st.divider()

    # Exam-wise performance
    st.markdown("### 📈 Performance by Exam")

    performance_data = [
        {"exam": "STET", "sets_attempted": 18, "avg_score": 75, "best": 92, "accuracy": 78},
        {"exam": "BPSC", "sets_attempted": 12, "avg_score": 68, "best": 85, "accuracy": 71},
        {"exam": "SSC CGL", "sets_attempted": 10, "avg_score": 73, "best": 88, "accuracy": 76},
        {"exam": "IBPS PO", "sets_attempted": 7, "avg_score": 70, "best": 82, "accuracy": 73}
    ]

    for perf in performance_data:
        with st.expander(f"📊 {perf['exam']} Performance"):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Sets Attempted", f"{perf['sets_attempted']}/25")
            with col2:
                st.metric("Average Score", f"{perf['avg_score']}%")
            with col3:
                st.metric("Best Score", f"{perf['best']}%")
            with col4:
                st.metric("Accuracy", f"{perf['accuracy']}%")

            st.progress(perf['sets_attempted'] / 25)
            st.caption(f"{25 - perf['sets_attempted']} practice sets remaining")

elif page == "🏆 Leaderboard":
    st.markdown("### 🏆 Top Performers")

    tab1, tab2 = st.tabs(["🌟 Overall", "🎯 By Exam"])

    with tab1:
        st.markdown("#### Overall Top 10")

        top_performers = [
            {"rank": 1, "name": "Rahul Kumar", "score": "94.2%", "tests": 120, "badge": "🏆"},
            {"rank": 2, "name": "Priya Singh", "score": "92.8%", "tests": 115, "badge": "🥈"},
            {"rank": 3, "name": "Amit Sharma", "score": "91.5%", "tests": 110, "badge": "🥉"},
            {"rank": 4, "name": "Neha Gupta", "score": "90.2%", "tests": 105, "badge": "⭐"},
            {"rank": 5, "name": "Vikas Yadav", "score": "89.7%", "tests": 100, "badge": "⭐"},
        ]

        for performer in top_performers:
            col1, col2, col3, col4 = st.columns([1, 3, 2, 2])
            with col1:
                st.markdown(f"### {performer['badge']}")
            with col2:
                st.markdown(f"**{performer['name']}**")
            with col3:
                st.markdown(f"Score: **{performer['score']}**")
            with col4:
                st.markdown(f"{performer['tests']} tests")
            st.divider()

    with tab2:
        exam_type = st.selectbox("Select Exam", ["STET", "CTET", "BPSC", "SSC CGL", "IBPS PO"])
        st.info(f"Showing top performers for {exam_type}")

elif page == "❓ Daily Quiz":
    st.markdown("### ❓ Daily Free Quiz")

    st.success("🎁 Take one free quiz daily!")

    quiz_topics = [
        "🧠 General Knowledge (10 Questions)",
        "🔢 Mathematics (10 Questions)",
        "💭 Reasoning (10 Questions)",
        "📰 Current Affairs (10 Questions)",
        "🏛️ Indian Polity (10 Questions)",
        "🌍 Geography (10 Questions)"
    ]

    selected_quiz = st.selectbox("Choose Topic", quiz_topics)

    st.markdown(f"""
    ### {selected_quiz}

    **Format:**
    - 10 Multiple Choice Questions
    - 10 minutes duration
    - Instant results with explanations
    - Track your daily progress
    """)

    if st.button("🚀 Start Daily Quiz", use_container_width=True, type="primary"):
        st.balloons()
        st.success("Starting your daily quiz...")

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #6b7280; padding: 2rem;">
    <p><strong>🎓 NrjAi - Your Complete Exam Preparation Platform</strong></p>
    <p>All Competitive Exams | 25 Practice Sets Each | 100% Free Forever</p>
    <p>© 2024 NrjAi | All Rights Reserved | Preparing Students for Success</p>
    <p style="margin-top: 1rem;">
        STET | CTET | BPSC | UPSC | SSC | Banking | Railway | Defense | GATE | Police
    </p>
    <p style="font-size: 0.85rem; margin-top: 1rem;">
        Developed & Powered by <strong>NrjAi</strong> 🚀
    </p>
</div>
""", unsafe_allow_html=True)
