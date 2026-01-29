# 🎓 NrjAi - Complete AI-Powered Platform

**© 2024 NrjAi | All Rights Reserved**

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red.svg)](https://streamlit.io)
[![AI](https://img.shields.io/badge/AI-Powered-green.svg)](https://anthropic.com)

---

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the platform
streamlit run app.py
```

**Access:** http://localhost:8501

---

## 📁 Project Structure (Organized & Sorted)

```
ai-multi-agent-system/
├── 📄 app.py                              ⭐ Main Application
├── 📄 automated_blogger.py                🤖 Auto Blog Posting
├── 📄 run_background.py                   🔧 Service Manager
├── 📄 trending_blogger.py                 📰 Trending Blogger
├── 📄 trending_blogger_background.py      🌙 Background Service
│
├── 📂 agents/                             🤖 AI Agents (4 files)
├── 📂 pages/                              📱 UI Pages (2 files)
├── 📂 src/                                🔧 Core Code (7 files)
├── 📂 scripts/                            🛠️ Utilities (8 files)
├── 📂 docs/                               📚 Documentation (28 files)
└── 📂 [data directories]                  💾 Data Storage
```

**See:** [docs/PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md) for complete structure

---

## ✨ Features

### 🎓 Exam Preparation Platform
- **21 Competitive Exams** (STET, CTET, SSC, Banking, etc.)
- **525 Practice Sets** (21 exams × 25 sets each)
- **150 Questions per test** with real-time timer
- **100+ Computer Science questions** with randomization
- **50+ Mathematics questions** with variety
- **Subject-wise practice** (15+ subjects)
- **Class level selection** (Paper 1-4)
- **Performance analytics** & leaderboards

### 💻 Coding Assessment Platform
- **4 Programming Languages** (Python, JavaScript, Java, C++)
- **Auto-grading system** with test cases
- **Secure code execution** in sandbox
- **Instant feedback** on submissions
- **Test case validation**

### 📰 Automated Blog Publishing
- **AI-generated content** (Research → Write → Review)
- **Trending topics** from GitHub, Reddit, Hacker News
- **5 posts daily** at 09:00 (configurable)
- **SEO-optimized** with relevant tags
- **Background service** (24/7 operation)
- **Blogspot integration** (auto-publish)

---

## 🎯 Main Components

### 1. Exam Dashboard (`pages/nrjai_dashboard.py`)
Complete Testbook-style exam preparation:
- Home dashboard with statistics
- All exams browser (21 exams)
- Test-taking interface (MCQ)
- Subject & class selection
- Performance tracking
- Leaderboards

### 2. Coding Tests (`pages/coding_tests.py`)
Professional coding assessment:
- Test creation interface
- Code editor with syntax highlighting
- Multiple language support
- Automated test execution
- Results & leaderboard

### 3. Blog System (`trending_blogger.py`)
Automated blog publishing:
- Trending topic discovery
- AI content generation
- SEO optimization
- Scheduled publishing
- Background operation

---

## 📚 Documentation

### Getting Started:
- [README_NRJAI.md](docs/README_NRJAI.md) - Complete platform guide
- [QUICK_START_TESTING.md](docs/QUICK_START_TESTING.md) - Quick start
- [PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md) - File organization

### Features:
- [TESTBOOK_PLATFORM.md](docs/TESTBOOK_PLATFORM.md) - Exam platform
- [CODING_TESTS.md](docs/CODING_TESTS.md) - Coding tests
- [SUBJECT_SELECTION_GUIDE.md](docs/SUBJECT_SELECTION_GUIDE.md) - Subjects

### Blog System:
- [BLOGGER_SETUP.md](docs/BLOGGER_SETUP.md) - Setup guide
- [AUTOMATED_PUBLISHING.md](docs/AUTOMATED_PUBLISHING.md) - Auto-publish
- [BACKGROUND_SERVICE.md](docs/BACKGROUND_SERVICE.md) - Background service

### Fixes & Updates:
- [TODAYS_FIXES_SUMMARY.md](docs/TODAYS_FIXES_SUMMARY.md) - Recent fixes
- [CLEANUP_SUMMARY.md](docs/CLEANUP_SUMMARY.md) - Cleanup report

**All Documentation:** [docs/](docs/) folder (28 files)

---

## 🛠️ Utility Scripts

Located in [scripts/](scripts/) directory:

```bash
# Blog Service Management
python scripts/restart_blogger_service.py    # Restart blog service
python scripts/stop_blogger_service.py       # Stop blog service
python scripts/test_blogger_now.py           # Test publishing now

# Sample Data Creation
python scripts/create_competitive_exams.py   # Create exam samples
python scripts/create_sample_tests.py        # Create test samples

# Setup & Configuration
python scripts/setup_background.py           # Setup background service
python scripts/get_blog_id.py                # Get Blogger blog ID
```

---

## 📊 Statistics

### Platform Capabilities:
- ✅ **21 Competitive Exams** with 25 practice sets each
- ✅ **525 Total Practice Sets** available
- ✅ **150+ Unique Questions** per subject (CS, Math)
- ✅ **4 Programming Languages** supported
- ✅ **5 Blog Posts Daily** (automated)
- ✅ **100% Free** & open source approach

### Question Banks:
- 🎓 **Computer Science:** 100+ questions
- 🎓 **Mathematics:** 50+ questions
- 🎓 **Other Subjects:** 5-10 questions each
- 🎓 **Total:** 200+ unique questions

---

## 🔧 Technology Stack

**Backend:**
- Python 3.13
- CrewAI (Multi-agent AI)
- Anthropic Claude
- OpenAI

**Frontend:**
- Streamlit
- Custom CSS
- Responsive design

**APIs:**
- Google Blogger API
- Anthropic API
- OpenAI API

**Storage:**
- Local JSON files
- Secure data storage

---

## 🎮 How to Use

### 1. Run the Platform:
```bash
streamlit run app.py
```

### 2. Navigate Using Sidebar:
- **Testbook Dashboard** → Exam preparation
- **Coding Tests** → Programming assessments
- **Competitive Exams** → Exam management

### 3. Take Tests:
1. Go to "All Exams"
2. Select exam (e.g., STET)
3. Click "Start" on any practice set
4. Select class level (Paper 1-4)
5. Select subject (e.g., Computer Science)
6. Enter details and start test
7. Answer 150 questions
8. Submit and see results

### 4. Automated Blogging:
```bash
# Test immediately
python scripts/test_blogger_now.py

# Or wait for scheduled run (tomorrow 09:00)
# Background service publishes automatically
```

---

## 📈 Performance

### Exam Platform:
- **Fast Question Loading** - Optimized rendering
- **Smooth UI** - No unnecessary page refreshes
- **Randomization** - Different order every test
- **Scalable** - Supports 150+ questions smoothly

### Blog System:
- **3-5 minutes per post** - AI generation time
- **5 posts in 15-20 minutes** - Daily batch
- **Background operation** - No user interaction needed
- **Reliable** - Logging & error handling

---

## 🎯 Key Features

### Exam Platform:
✅ **Subject Selection** - 15+ subjects available
✅ **Class Level Selection** - Paper 1-4 options
✅ **Question Randomization** - Different order each test
✅ **Answer Shuffling** - Options in random positions
✅ **Real-time Timer** - Countdown during test
✅ **Question Palette** - Easy navigation
✅ **Mark for Review** - Flag difficult questions
✅ **Performance Analytics** - Track progress
✅ **Leaderboards** - Compare with others

### Coding Platform:
✅ **Multi-language Support** - Python, JS, Java, C++
✅ **Code Editor** - Syntax highlighting
✅ **Test Cases** - Automated validation
✅ **Auto-grading** - Instant results
✅ **Leaderboard** - Top performers
✅ **Secure Execution** - Sandboxed environment

### Blog System:
✅ **AI Content Generation** - High-quality posts
✅ **Trending Topics** - Auto-discovery
✅ **SEO Optimization** - Tags & formatting
✅ **Scheduled Publishing** - Daily at 09:00
✅ **Background Service** - Fully automated
✅ **Multiple Sources** - GitHub, Reddit, HN

---

## 🌟 Recent Updates

### Latest Fixes (Jan 22-23, 2026):
✅ **Blog Service Fixed** - Now publishes automatically
✅ **Questions Expanded** - 100+ CS, 50+ Math questions
✅ **UI Improved** - Smooth option selection
✅ **Code Organized** - Clean directory structure
✅ **Cache Cleaned** - Optimized performance

**See:** [docs/TODAYS_FIXES_SUMMARY.md](docs/TODAYS_FIXES_SUMMARY.md)

---

## 📦 Installation

### Requirements:
```bash
pip install -r requirements.txt
```

**Key Dependencies:**
- streamlit
- crewai
- anthropic
- openai
- google-auth
- google-api-python-client
- requests
- beautifulsoup4

### Configuration:
1. Set up `.env` file with API keys:
```env
ANTHROPIC_API_KEY=your-key
OPENAI_API_KEY=your-key
BLOGGER_BLOG_ID=your-blog-id
```

2. Set up Google OAuth for Blogger:
```bash
# Place credentials.json in root
# Run setup once:
python scripts/get_blog_id.py
```

---

## 🤝 Support

### Issues & Bugs:
Report in GitHub issues or check [docs/DEBUG_GUIDE.md](docs/DEBUG_GUIDE.md)

### Documentation:
Complete guides available in [docs/](docs/) folder

### Quick Help:
- **Exam Issues:** Check [docs/TEST_TAKING_GUIDE.md](docs/TEST_TAKING_GUIDE.md)
- **Blog Issues:** Check [docs/BLOGGER_SERVICE_FIX.md](docs/BLOGGER_SERVICE_FIX.md)
- **Code Issues:** Check [docs/DEBUG_GUIDE.md](docs/DEBUG_GUIDE.md)

---

## 📜 License

**© 2024 NrjAi | All Rights Reserved**

This platform is proprietary software owned by NrjAi.

### Terms:
- ✅ Personal use allowed
- ✅ Educational purposes
- ✅ Non-commercial use
- ❌ No redistribution without permission

---

## 🎉 Features at a Glance

| Feature | Status | Description |
|---------|--------|-------------|
| 🎓 Exam Platform | ✅ Working | 21 exams, 525 sets, 150 questions |
| 💻 Coding Tests | ✅ Working | 4 languages, auto-grading |
| 📰 Blog Publishing | ✅ Working | AI-generated, 5 posts/day |
| 🎯 Subject Selection | ✅ Working | 15+ subjects, class levels |
| 🔄 Question Randomization | ✅ Working | Different every test |
| ⏱️ Real-time Timer | ✅ Working | Countdown during tests |
| 📊 Analytics | ✅ Working | Performance tracking |
| 🏆 Leaderboards | ✅ Working | Rank comparison |
| 🌙 Background Service | ✅ Working | Automated publishing |
| 📚 Documentation | ✅ Complete | 28 detailed guides |

---

## 🚀 Getting Started

### 1. Clone/Download:
```bash
cd ai-multi-agent-system
```

### 2. Install:
```bash
pip install -r requirements.txt
```

### 3. Configure:
```bash
# Create .env file with API keys
# Set up Google OAuth credentials
```

### 4. Run:
```bash
streamlit run app.py
```

### 5. Navigate:
- Click **"Testbook Dashboard"** for exams
- Click **"Coding Tests"** for programming
- Background blog service runs automatically

---

## 📞 Quick Commands

```bash
# Run main app
streamlit run app.py

# Test blog publishing
python scripts/test_blogger_now.py

# Create sample data
python scripts/create_competitive_exams.py
python scripts/create_sample_tests.py

# Manage blog service
python scripts/restart_blogger_service.py
python scripts/stop_blogger_service.py

# Get help
cat docs/README_NRJAI.md
```

---

## 🎓 About NrjAi

**NrjAi** represents:
- **Nrj** - Energy, Power, Innovation
- **Ai** - Artificial Intelligence, Advancement

**Mission:** Energized by AI for Educational Excellence

**Vision:** Complete AI-powered platform for learning, testing, and content creation

---

**© 2024 NrjAi | All Rights Reserved**

**Status:** ✅ Organized, Optimized, Production-Ready

**Version:** 2.0 - Fully Organized Structure

**Last Updated:** 2026-01-23

---

**🌟 Star this project if you find it useful!**

**📖 Read [docs/README_NRJAI.md](docs/README_NRJAI.md) for complete guide**

**🚀 Ready to use - Start with `streamlit run app.py`**
