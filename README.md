# 🚀 NrjAi - AI Multi-Agent Content Platform

**© 2024 NrjAi | All Rights Reserved**

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red.svg)](https://streamlit.io)
[![AI](https://img.shields.io/badge/AI-Powered-green.svg)](https://anthropic.com)
[![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-purple.svg)](https://crewai.com)

---

## 🎨 Modern UI with Advanced Design

**Beautiful, Colorful Interface with Maximum Readability:**
- 🌈 Gradient backgrounds (Purple, Pink, Blue)
- ⚪ Solid white content areas for excellent contrast
- 🔤 Pure black text for maximum visibility
- 💫 Glassmorphism effects on cards
- 🎯 Professional typography with Poppins font
- ✨ Smooth animations and hover effects

---

## 📸 Screenshots & Demo

### 🤖 AI Multi-Agent Content Generator
![AI Multi-Agent System](images/screenshots/ai-multiagent-dashboard.png)
*Research, Write, Review, and Convert to Presentations with 4 AI agents*

### 📰 Automated Blog Publishing
![Blog Publishing](images/screenshots/blog-publisher.png)
*Automated blog posting with trending topics*

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

## ✨ Core Features

### 🤖 AI Multi-Agent Content Generation
- **4 AI Agents Working Together:**
  - 🔍 **Research Agent** - Deep web research and fact-gathering
  - ✍️ **Writer Agent** - Professional content creation
  - 👁️ **Reviewer Agent** - Quality assurance and editing
  - 🎨 **Presentation Agent** - Slide creation and formatting
- **Multiple Content Types:**
  - 📝 Blog posts and articles
  - 🎨 Professional presentations
  - 📊 Research reports
  - 📰 Content with citations
- **Advanced AI Models:**
  - Anthropic Claude Sonnet 4.5
  - OpenAI GPT-4
  - CrewAI orchestration

### 🎨 AI Presentation Generator
- **Text-to-Slides Conversion** - Turn any topic into professional slides
- **Professional Templates v2.0:**
  - Strict formatting standards
  - Action-oriented titles
  - Concise bullet points (5-10 words)
  - Visual element suggestions
  - 10-15 slides per presentation
- **Multiple Export Formats:**
  - 📊 **PowerPoint (.pptx)** - Ready to present
  - 🌐 **HTML** - Web-based slideshow
  - 📄 **PDF** - Printable format
  - 📝 **Markdown** - Edit and customize
- **⚡ Multiprocessing Export:**
  - Export to all formats **simultaneously**
  - **2-3x faster** than sequential export
  - One-click ZIP download with all formats
- **Export Quality:**
  - Perfect PowerPoint compatibility
  - Clean HTML rendering
  - High-quality PDF output
  - Human-readable Markdown

### 📰 Automated Blog Publishing
- **AI-Generated Content** (Research → Write → Review)
- **Trending Topics** from GitHub, Reddit, Hacker News
- **Scheduled Publishing** (configurable timing)
- **SEO-Optimized** with relevant tags
- **Background Service** (24/7 operation)
- **Blogspot Integration** (auto-publish)

---

## 🎯 Main Components

### 1. AI Multi-Agent System (`app.py`)
Core content generation platform:
- Modern, colorful UI with gradient backgrounds
- 4 AI agents working in parallel
- Real-time progress tracking
- Multiple content type support
- Professional presentation generation

### 2. Presentation Exporter (`src/presentation_exporter.py`)
Multi-format export system:
- PowerPoint generation (python-pptx)
- HTML slideshow creation
- PDF rendering (weasyprint)
- Markdown formatting
- Multiprocessing support for parallel export

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
- [PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md) - File organization
- [QUICK_START_TESTING.md](docs/QUICK_START_TESTING.md) - Quick start

### Presentation Features:
- [PRESENTATION_EXPORT_GUIDE.md](docs/PRESENTATION_EXPORT_GUIDE.md) - Export guide
- [PRESENTATION_TEMPLATE_V2.md](docs/PRESENTATION_TEMPLATE_V2.md) - Template standards
- [MULTIPROCESSING_FEATURES.md](docs/MULTIPROCESSING_FEATURES.md) - Parallel processing
- [PARALLEL_AGENTS_GUIDE.md](docs/PARALLEL_AGENTS_GUIDE.md) - Batch processing

### Blog System:
- [BLOGGER_SETUP.md](docs/BLOGGER_SETUP.md) - Setup guide
- [AUTOMATED_PUBLISHING.md](docs/AUTOMATED_PUBLISHING.md) - Auto-publish
- [BACKGROUND_SERVICE.md](docs/BACKGROUND_SERVICE.md) - Background service

### Fixes & Updates:
- [TODAYS_FIXES_SUMMARY.md](docs/TODAYS_FIXES_SUMMARY.md) - Recent fixes
- [CLEANUP_SUMMARY.md](docs/CLEANUP_SUMMARY.md) - Cleanup report

**All Documentation:** [docs/](docs/) folder (30+ files)

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

## 📊 Platform Statistics

### Content Generation:
- ✅ **4 AI Agents** working collaboratively
- ✅ **Multiple Content Types** (blogs, presentations, reports)
- ✅ **4 Export Formats** for presentations
- ✅ **2-3x Faster** export with multiprocessing
- ✅ **Professional Quality** templates and formatting
- ✅ **Automated Publishing** with background service

### AI Models:
- 🤖 **Anthropic Claude Sonnet 4.5** - Primary model
- 🤖 **OpenAI GPT-4** - Alternative model
- 🤖 **CrewAI** - Multi-agent orchestration
- 🤖 **Parallel Processing** - Simultaneous operations

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

### 2. Generate Content:

**For Blog Posts:**
1. Select "blog" from Content Type dropdown
2. Enter your topic (e.g., "AI in Healthcare 2026")
3. Click "Start Research"
4. Wait 3-5 minutes for AI agents to work
5. Review and publish to Blogger

**For Presentations:**
1. Select "presentation" from Content Type dropdown
2. Enter your topic (e.g., "Python Best Practices")
3. Click "Start Research"
4. Wait 3-5 minutes for generation
5. Choose export format:
   - 📊 PowerPoint (.pptx)
   - 🌐 HTML slideshow
   - 📄 PDF document
   - 📝 Markdown source
   - 🚀 All formats (parallel export)

### 3. Automated Blogging:
```bash
# Test immediately
python scripts/test_blogger_now.py

# Or wait for scheduled run
# Background service publishes automatically
```

---

## 📈 Performance

### Content Generation:
- **3-5 minutes** - Blog post generation time
- **3-5 minutes** - Presentation creation time
- **Multi-agent Parallel Processing** - All agents work simultaneously
- **Real-time Progress** - Live status updates

### Presentation Export:
- **Sequential Export:** ~45 seconds (all formats)
- **Parallel Export:** ~20 seconds (all formats)
- **Speedup:** 2-3x faster with multiprocessing
- **Quality:** Professional-grade output

### Blog System:
- **3-5 minutes per post** - AI generation time
- **Background operation** - No user interaction needed
- **Reliable** - Logging & error handling
- **Scheduled Publishing** - Automated daily posts

---

## 🎯 Key Features

### AI Content Generation:
✅ **Multi-Agent System** - 4 AI agents working in parallel
✅ **Research Agent** - Deep web research and fact-gathering
✅ **Writer Agent** - Professional content creation
✅ **Reviewer Agent** - Quality assurance and editing
✅ **Presentation Agent** - Slide creation and formatting
✅ **Real-time Progress** - Live status updates
✅ **Multiple Content Types** - Blogs, presentations, reports
✅ **High Quality Output** - Professional-grade content

### Presentation Features:
✅ **Professional Templates v2.0** - Strict formatting standards
✅ **Multi-format Export** - PowerPoint, HTML, PDF, Markdown
✅ **Parallel Processing** - 2-3x faster export
✅ **10-15 Slides** - Perfect presentation length
✅ **Visual Suggestions** - Chart/Image/Diagram recommendations
✅ **Action-oriented Titles** - Descriptive and compelling
✅ **Concise Bullets** - 5-10 words maximum
✅ **Export-ready** - Perfect PowerPoint compatibility

### Blog System:
✅ **AI Content Generation** - High-quality posts
✅ **Trending Topics** - Auto-discovery
✅ **SEO Optimization** - Tags & formatting
✅ **Scheduled Publishing** - Configurable timing
✅ **Background Service** - Fully automated
✅ **Multiple Sources** - GitHub, Reddit, HN

### Modern UI:
✅ **Gradient Backgrounds** - Beautiful purple-pink gradients
✅ **Maximum Contrast** - Pure black text on white
✅ **Glassmorphism** - Modern card effects
✅ **Professional Typography** - Poppins font family
✅ **Smooth Animations** - Polished interactions
✅ **Responsive Design** - Works on all devices

---

## 🌟 Recent Updates

### Latest Updates (February 2026):
✅ **Modern UI Redesign** - Beautiful gradient backgrounds with maximum contrast
✅ **Text Visibility** - Pure black text on solid white backgrounds
✅ **Presentation Templates v2.0** - Professional slide formatting standards
✅ **Multiprocessing Export** - 2-3x faster parallel export to all formats
✅ **Streamlined Features** - Focused on core AI content generation
✅ **Enhanced Typography** - Poppins font with optimized sizing
✅ **Glassmorphism Effects** - Modern card designs with blur effects

**UI Improvements:**
- Solid white content area for maximum readability
- Black text (#000000) everywhere for perfect contrast
- Gradient backgrounds (Purple → Pink)
- Bold labels (1.1rem, weight 700)
- Smooth animations and hover effects

**See:** [docs/PRESENTATION_TEMPLATE_V2.md](docs/PRESENTATION_TEMPLATE_V2.md)

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
| 🤖 Multi-Agent System | ✅ Working | 4 AI agents in parallel |
| 🎨 Presentation Generator | ✅ Working | Professional slide decks |
| 📊 Multi-format Export | ✅ Working | PowerPoint, HTML, PDF, Markdown |
| ⚡ Parallel Processing | ✅ Working | 2-3x faster exports |
| 📰 Blog Publishing | ✅ Working | AI-generated content |
| 🌈 Modern UI | ✅ Working | Gradient backgrounds, max contrast |
| 🎯 Template v2.0 | ✅ Working | Professional formatting standards |
| 🔍 Research Agent | ✅ Working | Deep web research |
| ✍️ Writer Agent | ✅ Working | Professional content creation |
| 👁️ Reviewer Agent | ✅ Working | Quality assurance |
| 🌙 Background Service | ✅ Working | Automated publishing |
| 📚 Documentation | ✅ Complete | 30+ detailed guides |

---

## 🚀 Getting Started

### 1. Clone/Download:
```bash
cd ai-multi-agent-system
```

### 2. Install:
```bash
pip install -r requirements.txt

# For presentation export features:
pip install python-pptx weasyprint markdown2
# Or run: install_presentation_exports.bat
```

### 3. Configure:
```bash
# Create .env file with API keys
ANTHROPIC_API_KEY=your-key
OPENAI_API_KEY=your-key
BLOGGER_BLOG_ID=your-blog-id

# Set up Google OAuth credentials (optional, for blog publishing)
```

### 4. Run:
```bash
streamlit run app.py
```

### 5. Generate Content:
- **Blog Posts:** Select "blog" → Enter topic → Start Research
- **Presentations:** Select "presentation" → Enter topic → Start Research → Export
- **Background Blogging:** Runs automatically (configurable)

---

## 📞 Quick Commands

```bash
# Run main app
streamlit run app.py

# Install presentation export libraries
install_presentation_exports.bat
# Or: pip install python-pptx weasyprint markdown2

# Test blog publishing
python scripts/test_blogger_now.py

# Manage blog service
python scripts/restart_blogger_service.py
python scripts/stop_blogger_service.py

# Get help
cat docs/README_NRJAI.md
cat docs/PRESENTATION_EXPORT_GUIDE.md
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

**Status:** ✅ Modern UI, Professional Templates, Production-Ready

**Version:** 3.0 - Advanced AI Content Platform

**Last Updated:** 2026-02-04

---

**🌟 Key Highlights:**
- 🎨 Modern gradient UI with maximum readability
- 🤖 4 AI agents working in parallel
- 📊 Professional presentation generation
- ⚡ Multi-format export with multiprocessing
- 📰 Automated blog publishing

---

**🌟 Star this project if you find it useful!**

**📖 Documentation:**
- [Complete Guide](docs/README_NRJAI.md)
- [Presentation Export](docs/PRESENTATION_EXPORT_GUIDE.md)
- [Template Standards](docs/PRESENTATION_TEMPLATE_V2.md)

**🚀 Ready to use - Start with `streamlit run app.py`**
