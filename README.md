# 🚀 AI Nexus v2.6.0

> **Enterprise Cognitive Architecture & Engineering System**

AI Nexus is a comprehensive Streamlit-based platform for AI professionals to learn, discover tools, and master prompt engineering.

---

## ✨ Features

### 📚 Learning Hub
- **25+ Curated Tutorials** across Quick Wins, Deep Dives, and Mastery Tracks
- **Completion Tracking** with visual progress indicators
- **Role-based Recommendations** tailored to your profession
- **Tutorial Viewer** with step-by-step content

### 🔧 AI Tools Directory
- **47 Verified AI Tools** with detailed profiles
- **Category Filtering** (Code, Testing, DevOps, Design, etc.)
- **Global Search** across all content
- **Favorites System** to save tools to your library
- **Related Tools** recommendations

### 💡 Prompt Library
- **40+ Production-Ready Prompts** for developers
- **14 Categories** (Coding, Testing, Architecture, Security, etc.)
- **Prompt Lab** for testing and iterating
- **Technique Templates** with "Try This" functionality
- **Share Prompt** feature for collaboration

### 🔥 AI Hacks (NEW!)
- **10 Productivity Hacks** for AI tools
- **Curated Tips & Tricks** from ChatGPT, Claude, Cursor, Copilot, etc.
- **Time-Saving Metrics** for each hack
- **Step-by-Step Instructions** with examples
- **Filter by Category, Difficulty, Tool**

### 📰 AI Latest News (NEW!)
- **Real-Time News** from 8+ major AI sources
- **Auto-Updated** every 10 minutes via RSS feeds
- **Trending Topics** extraction
- **Filter by Source Type & Timeframe**
- **Direct Links** to full articles

### 📊 Dashboard
- **AI Score Tracking** based on assessments
- **Weekly Activity Chart** with real engagement data
- **Learning Progress Visualization**
- **Skill Distribution** radar chart
- **Achievements & Badges**
- **Data Export/Import** for workspace portability

### ⚡ Skills Assessment
- **10-Question Quiz** covering AI Engineering concepts
- **Instant Feedback** with explanations
- **Profile Integration** for score updates
- **Topics**: RAG, Fine-tuning, Prompting, Security, and more

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Database**: SQLite with SQLAlchemy (with Foreign Keys & Relationships)
- **Styling**: Custom CSS with Prism Vibrant Theme
- **Python**: 3.11+
- **Testing**: pytest

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/your-org/ai-nexus.git
cd ai-nexus

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

Or use the batch file on Windows:
```bash
run.bat
```

---

## 📁 Project Structure

```
AI Nexus/
├── app.py                 # Main application entry
├── config/
│   ├── settings.py        # Configuration & constants
│   └── enums.py           # Centralized enums (NEW)
├── data/
│   ├── final_assets.py    # AI tools database
│   ├── final_prompts.py   # Prompt library
│   ├── final_tutorials.py # Tutorial content
│   ├── ai_hacks.py        # AI productivity hacks (NEW)
│   └── ai_news.py         # Real-time news aggregator (NEW)
├── database/
│   ├── db.py              # Database connection & context manager
│   ├── models.py          # SQLAlchemy models with ForeignKeys
│   └── operations.py      # CRUD operations
├── pages/
│   ├── ai_tools_final.py  # Tools directory
│   ├── ai_hacks.py        # AI Hacks page (NEW)
│   ├── ai_news.py         # AI News page (NEW)
│   ├── assessment.py      # Skills quiz
│   ├── dashboard.py       # User dashboard
│   ├── learning_hub.py    # Tutorial browser
│   ├── prompt_library.py  # Prompt explorer
│   ├── tool_viewer.py     # Tool detail page
│   ├── tutorial_viewer.py # Tutorial reader
│   └── user_profile.py    # Profile management
├── scripts/               # Content management (NEW)
│   ├── update_all.py      # Update content
│   ├── validate_data.py   # Validate data files
│   └── content_report.py  # Generate reports
├── styles/
│   └── custom_css.py      # Theme & styling (with accessibility)
├── utils/
│   └── helpers.py         # Utility functions
├── tests/                 # Test suite (NEW)
│   ├── conftest.py        # Pytest fixtures
│   ├── test_tutorials.py  # Tutorial tests
│   ├── test_prompts.py    # Prompt tests
│   └── test_helpers.py    # Helper tests
├── docs/
│   ├── CONTENT_UPDATE_GUIDE.md  # Content update process (NEW)
│   ├── CONTENT_REPORT.md        # Latest content stats (NEW)
│   └── archive/           # Legacy documentation
├── requirements.txt       # Full dependencies
└── requirements-minimal.txt # Minimal dependencies
```

---

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_tutorials.py -v
```

---

## 📝 Content Management

Keep all content fresh and up-to-date using our content management scripts:

```bash
# Generate content report (shows stats and recommendations)
python scripts/content_report.py

# Validate all data files
python scripts/validate_data.py

# Update news cache and check freshness
python scripts/update_all.py
```

### Content Update Process

1. **Check Current Status:**
   ```bash
   python scripts/content_report.py
   ```

2. **Add New Content:**
   - Follow templates in `docs/CONTENT_UPDATE_GUIDE.md`
   - Add to appropriate data file (`ai_hacks.py`, `final_tutorials.py`, etc.)

3. **Validate:**
   ```bash
   python scripts/validate_data.py
   ```

4. **Test Locally:**
   ```bash
   streamlit run app.py
   ```

5. **Commit:**
   ```bash
   git add -A
   git commit -m "Content update: Added X items"
   ```

### Content Goals

- 📚 Tutorials: 25 → 50 → 100
- 💡 Prompts: 40 → 100 → 200
- 🛠️ Tools: 47 → 75 → 150
- 🔥 Hacks: 10 → 25 → 50
- 📰 News: Auto-updated every 10 minutes

See `docs/CONTENT_UPDATE_GUIDE.md` for detailed instructions.

---

## 🎨 Theme: Prism Vibrant

- **Primary Gradient**: `#6366F1` → `#EC4899`
- **High Contrast** text for accessibility
- **Glassmorphism** cards with subtle shadows
- **Smooth Animations** on card load
- **Accessibility**: Reduced motion support, high contrast mode

---

## 📝 Version History

### v2.6.0 (Current)
- ✅ Fixed critical dashboard rendering bug
- ✅ Added ForeignKey constraints to database models
- ✅ Timezone-aware datetime handling
- ✅ Context manager for database sessions
- ✅ Removed cache-clearing anti-pattern
- ✅ Added accessibility CSS improvements
- ✅ Created centralized enums module
- ✅ Added comprehensive test suite
- ✅ Enhanced run.bat with error handling

### v2.5.0
- ✅ Global Search across all content
- ✅ Assessment Engine (10 questions)
- ✅ Data Import/Export
- ✅ Real Activity Tracking
- ✅ Tip of the Day
- ✅ Tool Viewer enhancements
- ✅ Quick Actions on Home
- ✅ 6 new AI tools

### v2.4.0
- Initial release with core features

---

## 🔧 Development

### Code Quality
```bash
# Format code (if using black)
black .

# Type checking (if using mypy)
mypy .

# Lint (if using ruff)
ruff check .
```

### Database Reset
```bash
python -c "from database.db import reset_db; reset_db()"
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Run tests (`pytest`)
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

---

## 📄 License

MIT License - See LICENSE file for details.

---

**Built with ❤️ for AI Professionals**
