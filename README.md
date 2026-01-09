# 🚀 AI Nexus v2.5.0

> **Enterprise Cognitive Architecture & Engineering System**

AI Nexus is a comprehensive Streamlit-based platform for AI professionals to learn, discover tools, and master prompt engineering.

---

## ✨ Features

### 📚 Learning Hub
- **35+ Curated Tutorials** across Quick Wins, Deep Dives, and Mastery Tracks
- **Completion Tracking** with visual progress indicators
- **Role-based Recommendations** tailored to your profession
- **Tutorial Viewer** with step-by-step content

### 🔧 AI Tools Directory
- **35 Verified AI Tools** with detailed profiles
- **Category Filtering** (Code, Testing, DevOps, Design, etc.)
- **Global Search** across all content
- **Favorites System** to save tools to your library
- **Related Tools** recommendations

### 💡 Prompt Library
- **50+ Production-Ready Prompts** for developers
- **14 Categories** (Coding, Testing, Architecture, Security, etc.)
- **Prompt Lab** for testing and iterating
- **Technique Templates** with "Try This" functionality
- **Share Prompt** feature for collaboration

### 📊 Dashboard
- **AI Score Tracking** based on assessments
- **Weekly Activity Chart** with real engagement data
- **Learning Progress Visualization**
- **Data Export/Import** for workspace portability

### ⚡ Skills Assessment
- **10-Question Quiz** covering AI Engineering concepts
- **Instant Feedback** with explanations
- **Profile Integration** for score updates
- **Topics**: RAG, Fine-tuning, Prompting, Security, and more

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Database**: SQLite with SQLAlchemy
- **Styling**: Custom CSS with Prism Vibrant Theme
- **Python**: 3.11+

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

---

## 📁 Project Structure

```
AI Nexus/
├── app.py                 # Main application entry
├── config/
│   └── settings.py        # Configuration & constants
├── data/
│   ├── final_assets.py    # AI tools database
│   ├── final_prompts.py   # Prompt library
│   └── final_tutorials.py # Tutorial content
├── database/
│   ├── models.py          # SQLAlchemy models
│   └── operations.py      # CRUD operations
├── pages/
│   ├── ai_tools_final.py  # Tools directory
│   ├── assessment.py      # Skills quiz
│   ├── dashboard.py       # User dashboard
│   ├── learning_hub.py    # Tutorial browser
│   ├── prompt_library.py  # Prompt explorer
│   ├── tool_viewer.py     # Tool detail page
│   ├── tutorial_viewer.py # Tutorial reader
│   └── user_profile.py    # Profile management
├── styles/
│   └── custom_css.py      # Theme & styling
├── utils/
│   └── helpers.py         # Utility functions
├── docs/
│   └── archive/           # Legacy documentation
└── requirements.txt
```

---

## 🎨 Theme: Prism Vibrant

- **Primary Gradient**: `#6366F1` → `#EC4899`
- **High Contrast** text for accessibility
- **Glassmorphism** cards with subtle shadows
- **Smooth Animations** on card load

---

## 📝 Version History

### v2.5.0 (Current)
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

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## 📄 License

MIT License - See LICENSE file for details.

---

**Built with ❤️ for AI Professionals**
