# 🤖 AI Multi-Agent Research Assistant

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Latest-green.svg)](https://www.crewai.com/)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-orange.svg)](https://www.langchain.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A production-ready **Multi-Agent AI System** built with **CrewAI**, **LangChain**, and **GPT-4** that demonstrates autonomous AI agents working together to research topics, create content, and perform quality assurance. This project showcases modern AI/ML engineering skills aligned with 2026 market demands.

## 🎯 Why This Project?

This project demonstrates **in-demand AI/ML skills for 2026**:

- ✅ **Multi-Agent Systems** - Trending architecture used by OpenAI, IBM for complex workflows
- ✅ **LLM Integration** - Working with GPT-4 and LangChain (19.7% of AI job postings require NLP)
- ✅ **Production Deployment** - Docker, environment management, and MLOps practices
- ✅ **Clean Code** - Modular architecture, logging, configuration management
- ✅ **Modern UI** - Streamlit interface for demonstrations
- ✅ **Portfolio-Ready** - End-to-end system showcasing real-world capabilities

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                  Streamlit UI                       │
│            (User Interface Layer)                   │
└────────────────┬────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────┐
│              CrewAI Manager                         │
│         (Orchestration Layer)                       │
└─────┬───────────────┬───────────────┬───────────────┘
      │               │               │
      ▼               ▼               ▼
┌──────────┐   ┌──────────┐   ┌──────────────┐
│ Research │   │  Writer  │   │   Reviewer   │
│  Agent   │──▶│  Agent   │──▶│    Agent     │
└──────────┘   └──────────┘   └──────────────┘
      │               │               │
      ▼               ▼               ▼
┌─────────────────────────────────────────────────────┐
│         LangChain + OpenAI GPT-4                    │
│            (LLM Backend)                            │
└─────────────────────────────────────────────────────┘
```

## 🚀 Features

### Multi-Agent Workflow

1. **Research Agent** 🔍
   - Conducts web searches and information gathering
   - Analyzes data from multiple sources
   - Extracts key insights and statistics

2. **Writer Agent** ✍️
   - Creates engaging, well-structured content
   - Transforms research into readable articles
   - Outputs in professional Markdown format

3. **Reviewer Agent** 🔎
   - Performs quality assurance checks
   - Verifies accuracy and completeness
   - Provides constructive feedback

### Key Capabilities

- 🎯 Autonomous agent coordination
- 🔄 Sequential task processing
- 📊 Real-time progress tracking
- 💾 Content export functionality
- 🐳 Docker deployment ready
- 📝 Comprehensive logging
- ⚙️ Configurable parameters

## 📋 Prerequisites

- Python 3.11 or higher
- OpenAI API key
- Docker (optional, for containerized deployment)

## 🛠️ Installation

### Option 1: Local Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd ai-multi-agent-system
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```

   Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   MODEL_NAME=gpt-4-turbo-preview
   TEMPERATURE=0.7
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

   The app will be available at `http://localhost:8501`

### Option 2: Docker Deployment

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

2. **Access the application**
   - URL: `http://localhost:8501`

3. **Stop the application**
   ```bash
   docker-compose down
   ```

## 📖 Usage

### Web Interface

1. Open the application in your browser
2. Enter your OpenAI API key in the sidebar (if not set in `.env`)
3. Configure model settings (optional)
4. Enter a research topic
5. Select content type (article, blog post, report, etc.)
6. Click "Start Research"
7. Monitor agent progress in real-time
8. Download the generated content

### Programmatic Usage

```python
from src.crew_manager import CrewManager

# Initialize manager
manager = CrewManager(
    model_name="gpt-4-turbo-preview",
    temperature=0.7,
    api_key="your-api-key"
)

# Execute workflow
result = manager.execute_research_workflow(
    topic="Artificial Intelligence in Healthcare 2026",
    content_type="article"
)

print(result["result"])
```

## 📁 Project Structure

```
ai-multi-agent-system/
├── agents/                 # Agent implementations
│   ├── __init__.py
│   ├── researcher.py      # Research agent
│   ├── writer.py          # Content writer agent
│   └── reviewer.py        # QA reviewer agent
├── src/                   # Core application code
│   ├── __init__.py
│   ├── crew_manager.py    # Crew orchestration
│   ├── config.py          # Configuration management
│   └── logger.py          # Logging setup
├── config/                # Configuration files
├── data/                  # Data storage
├── logs/                  # Application logs
├── tests/                 # Unit tests
├── app.py                 # Streamlit UI
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose setup
├── .env.example          # Environment template
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API key (required) | - |
| `MODEL_NAME` | LLM model to use | `gpt-4-turbo-preview` |
| `TEMPERATURE` | Model temperature (0-1) | `0.7` |
| `MAX_TOKENS` | Maximum tokens per request | `2000` |
| `LOG_LEVEL` | Logging level | `INFO` |
| `LOG_FILE` | Log file path | `./logs/app.log` |

### Model Options

- `gpt-4-turbo-preview` - Most capable (recommended)
- `gpt-4` - High quality
- `gpt-3.5-turbo` - Faster, more cost-effective

## 🧪 Testing

Run tests with pytest:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov=agents

# Run specific test file
pytest tests/test_crew_manager.py
```

## 📊 Performance Considerations

- **Execution Time**: Typically 2-5 minutes depending on topic complexity
- **API Costs**: ~$0.10-0.30 per workflow (using GPT-4)
- **Rate Limits**: Respects OpenAI rate limits automatically

## 🎓 Learning Resources

This project demonstrates skills from:
- [CrewAI Documentation](https://docs.crewai.com/)
- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Reference](https://platform.openai.com/docs/)

## 🚀 Future Enhancements

- [ ] Add vector database integration (Pinecone/Weaviate)
- [ ] Implement RAG for document-based research
- [ ] Add more specialized agents (Data Analyst, SEO Optimizer)
- [ ] Create REST API endpoints
- [ ] Add user authentication
- [ ] Implement caching for faster responses
- [ ] Add multi-language support
- [ ] Integrate with CI/CD pipeline

## 📝 Skills Demonstrated

This project showcases:

### Technical Skills
- ✅ Python programming (OOP, async, type hints)
- ✅ LLM integration and prompt engineering
- ✅ Multi-agent system architecture
- ✅ LangChain framework
- ✅ CrewAI orchestration
- ✅ API integration (OpenAI)
- ✅ Web development (Streamlit)
- ✅ Docker containerization
- ✅ Environment management
- ✅ Logging and monitoring
- ✅ Testing and documentation

### AI/ML Concepts
- ✅ Autonomous agents
- ✅ Task delegation and coordination
- ✅ Natural Language Processing
- ✅ Content generation
- ✅ Quality assurance automation

### Software Engineering
- ✅ Clean code architecture
- ✅ Configuration management
- ✅ Error handling
- ✅ Modular design
- ✅ Production-ready deployment

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👤 Author

**Your Name**
- Portfolio: [your-portfolio.com](https://your-portfolio.com)
- LinkedIn: [your-linkedin](https://linkedin.com/in/your-profile)
- GitHub: [@your-username](https://github.com/your-username)

## 🙏 Acknowledgments

- [CrewAI](https://www.crewai.com/) for the multi-agent framework
- [LangChain](https://www.langchain.com/) for LLM orchestration
- [Streamlit](https://streamlit.io/) for the web interface
- OpenAI for GPT-4 access

---

⭐ **Star this repository if you find it helpful for your AI/ML portfolio!**

Built with ❤️ to demonstrate modern AI/ML engineering skills aligned with 2026 market demands.
