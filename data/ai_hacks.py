"""
AI Nexus - AI Hacks Database
Curated productivity hacks, tips, and tricks for AI tools
"""

AI_HACKS = [
    {
        "id": "hack-1",
        "title": "ChatGPT Memory Hack: Custom Instructions",
        "category": "Productivity",
        "difficulty": "Beginner",
        "tool": "ChatGPT",
        "icon": "🧠",
        "description": "Use Custom Instructions to make ChatGPT remember your preferences across all conversations.",
        "hack": """
**The Problem:** Repeating context in every ChatGPT conversation wastes time.

**The Solution:** Set up Custom Instructions once, use forever.

**How to Do It:**
1. Go to Settings → Custom Instructions
2. In "What would you like ChatGPT to know about you?":
   - Your role (e.g., "I'm a Python backend developer")
   - Your tech stack
   - Your preferences (code style, verbosity level)
3. In "How would you like ChatGPT to respond?":
   - "Always provide code with comments"
   - "Explain trade-offs for different approaches"
   - "Use Python 3.11+ syntax"

**Example Custom Instruction:**
```
I'm a senior full-stack developer working with:
- Backend: Python (FastAPI), PostgreSQL
- Frontend: React, TypeScript
- DevOps: Docker, AWS

When answering:
- Provide production-ready code with error handling
- Explain performance implications
- Suggest testing strategies
- Use type hints in Python
```

**Impact:** Saves 2-3 minutes per conversation, 100+ hours/year.
        """,
        "tags": ["ChatGPT", "Productivity", "Setup"],
        "time_saved": "2-3 min per chat",
        "difficulty_level": 1
    },
    {
        "id": "hack-2",
        "title": "Claude Projects: Persistent Context",
        "category": "Workflow",
        "difficulty": "Intermediate",
        "tool": "Claude",
        "icon": "📁",
        "description": "Use Claude Projects to maintain context across multiple conversations for complex projects.",
        "hack": """
**The Problem:** Losing context when switching between Claude conversations.

**The Solution:** Claude Projects (Pro feature) maintains persistent knowledge.

**How to Use:**
1. Create a new Project for each codebase/domain
2. Upload key files:
   - README.md
   - Architecture docs
   - API schemas
   - Style guides
3. All conversations in that Project have access to these files

**Pro Tip - Project Setup Template:**
```markdown
# Project: [Name]

## Tech Stack
- Languages: Python 3.11, TypeScript
- Frameworks: FastAPI, React
- Database: PostgreSQL

## Code Style
- Use type hints
- Max line length: 100
- Follow PEP 8

## Architecture
[Paste your architecture diagram or description]
```

**Impact:** 10x faster onboarding for complex projects.
        """,
        "tags": ["Claude", "Projects", "Context"],
        "time_saved": "10+ min per session",
        "difficulty_level": 2
    },
    {
        "id": "hack-3",
        "title": "Cursor: Multi-File Editing with @-mentions",
        "category": "Coding",
        "difficulty": "Beginner",
        "tool": "Cursor",
        "icon": "⚡",
        "description": "Use @-mentions to reference multiple files in a single Cursor prompt.",
        "hack": """
**The Problem:** Editing related files requires multiple prompts.

**The Solution:** Reference multiple files with @ in Cursor.

**Syntax:**
```
@filename.py @another.py refactor the authentication logic to use the new User model
```

**Advanced Usage:**
```
@models/user.py @api/auth.py @tests/test_auth.py 
Update the User model to include 2FA, update the auth endpoint, 
and add comprehensive tests
```

**Pro Tips:**
- Use `@folder/` to reference entire directories
- Use `@docs` to reference documentation
- Combine with Cmd+K for inline edits

**Real Example:**
```
@backend/models.py @backend/schemas.py @backend/crud.py
Add a 'last_login' timestamp field to the User model and update 
all related code
```

**Impact:** 5x faster for multi-file refactoring.
        """,
        "tags": ["Cursor", "Multi-file", "Refactoring"],
        "time_saved": "5+ min per refactor",
        "difficulty_level": 1
    },
    {
        "id": "hack-4",
        "title": "GitHub Copilot: Slash Commands",
        "category": "Coding",
        "difficulty": "Beginner",
        "tool": "GitHub Copilot",
        "icon": "🤖",
        "description": "Use slash commands in Copilot Chat for instant, context-aware actions.",
        "hack": """
**The Problem:** Typing out full prompts for common tasks.

**The Solution:** Copilot Slash Commands.

**Essential Commands:**
- `/explain` - Explain selected code
- `/fix` - Fix bugs in selection
- `/tests` - Generate unit tests
- `/doc` - Generate documentation
- `/optimize` - Suggest performance improvements

**Advanced Commands:**
- `/new` - Scaffold new files/components
- `/newNotebook` - Create Jupyter notebook
- `/terminal` - Explain terminal commands

**Workflow Example:**
1. Select buggy function
2. Type `/fix`
3. Review suggestion
4. Type `/tests` to add tests
5. Type `/doc` to document

**Pro Tip - Chain Commands:**
```
1. /fix (fix the bug)
2. /tests (add tests)
3. /optimize (improve performance)
4. /doc (document changes)
```

**Impact:** 10x faster for routine coding tasks.
        """,
        "tags": ["Copilot", "Commands", "Shortcuts"],
        "time_saved": "30+ sec per task",
        "difficulty_level": 1
    },
    {
        "id": "hack-5",
        "title": "Prompt Chaining: Break Complex Tasks",
        "category": "Prompting",
        "difficulty": "Advanced",
        "tool": "Any LLM",
        "icon": "🔗",
        "description": "Chain multiple focused prompts instead of one complex prompt for better results.",
        "hack": """
**The Problem:** Complex prompts produce mediocre results.

**The Solution:** Break into sequential, focused prompts.

**Bad Approach (Single Prompt):**
```
Build a REST API for a todo app with authentication, CRUD operations,
database models, tests, and documentation
```

**Good Approach (Chained Prompts):**

**Prompt 1 - Architecture:**
```
Design the architecture for a todo REST API with:
- User authentication
- CRUD operations
- PostgreSQL database
Provide: folder structure, tech stack, data models
```

**Prompt 2 - Models:**
```
Based on the architecture above, create SQLAlchemy models for:
- User (with password hashing)
- Todo (with user relationship)
Include: timestamps, constraints, indexes
```

**Prompt 3 - API Endpoints:**
```
Create FastAPI endpoints for the Todo model:
- POST /todos (create)
- GET /todos (list with pagination)
- GET /todos/{id} (detail)
- PUT /todos/{id} (update)
- DELETE /todos/{id} (delete)
Include: authentication, validation, error handling
```

**Prompt 4 - Tests:**
```
Generate pytest tests for the Todo endpoints covering:
- Happy paths
- Edge cases
- Authentication failures
- Validation errors
```

**Why This Works:**
- Each prompt has clear, focused scope
- LLM can dedicate full context window to one task
- Easier to review and iterate
- Better code quality

**Impact:** 3x better code quality, 2x faster iteration.
        """,
        "tags": ["Prompting", "Strategy", "Quality"],
        "time_saved": "Varies",
        "difficulty_level": 3
    },
    {
        "id": "hack-6",
        "title": "Perplexity: Research Mode for Deep Dives",
        "category": "Research",
        "difficulty": "Beginner",
        "tool": "Perplexity",
        "icon": "🔍",
        "description": "Use Perplexity's Pro Search for comprehensive research with citations.",
        "hack": """
**The Problem:** ChatGPT hallucinates, Google is cluttered with SEO spam.

**The Solution:** Perplexity Pro Search with Focus modes.

**Focus Modes:**
- **Academic** - Peer-reviewed papers only
- **Writing** - Long-form, detailed responses
- **Math** - Step-by-step calculations
- **Video** - YouTube content summaries
- **Reddit** - Community discussions

**Research Workflow:**
1. Start with Academic mode for foundational knowledge
2. Switch to Reddit mode for real-world experiences
3. Use Writing mode for comprehensive summary

**Example Query:**
```
Focus: Academic
"What are the latest advances in RAG (Retrieval Augmented Generation) 
for reducing hallucinations in LLMs?"
```

**Pro Tips:**
- Use "site:arxiv.org" for research papers
- Use "site:github.com" for code examples
- Ask for "comparison table" for feature comparisons

**Impact:** 10x faster research with verified sources.
        """,
        "tags": ["Perplexity", "Research", "Citations"],
        "time_saved": "20+ min per research task",
        "difficulty_level": 1
    },
    {
        "id": "hack-7",
        "title": "Notion AI: Database Auto-Fill",
        "category": "Productivity",
        "difficulty": "Intermediate",
        "tool": "Notion",
        "icon": "📊",
        "description": "Use Notion AI to automatically populate database properties.",
        "hack": """
**The Problem:** Manually filling database properties is tedious.

**The Solution:** Notion AI auto-fill with custom prompts.

**Setup:**
1. Create a Notion database (e.g., "Meeting Notes")
2. Add AI-powered properties:
   - Summary (AI-generated)
   - Action Items (AI-extracted)
   - Key Decisions (AI-identified)
   - Next Steps (AI-suggested)

**AI Property Prompts:**

**Summary Property:**
```
Summarize this meeting note in 2-3 sentences focusing on 
outcomes and decisions
```

**Action Items Property:**
```
Extract all action items from this note as a bulleted list.
Format: "- [Owner] Task (Due date if mentioned)"
```

**Key Decisions Property:**
```
List all decisions made in this meeting as bullet points
```

**Workflow:**
1. Paste meeting transcript
2. AI auto-fills all properties
3. Review and edit if needed

**Impact:** 5 minutes saved per meeting note.
        """,
        "tags": ["Notion", "Automation", "Databases"],
        "time_saved": "5 min per note",
        "difficulty_level": 2
    },
    {
        "id": "hack-8",
        "title": "Midjourney: Consistent Character with --cref",
        "category": "Design",
        "difficulty": "Advanced",
        "tool": "Midjourney",
        "icon": "🎨",
        "description": "Use character reference (--cref) to maintain consistent characters across images.",
        "hack": """
**The Problem:** Generating multiple images of the same character produces inconsistent results.

**The Solution:** Midjourney's --cref parameter.

**How It Works:**
1. Generate your base character image
2. Copy the image URL
3. Use --cref [URL] in subsequent prompts

**Example:**
```
Base Prompt:
"professional headshot of a female software engineer, 
short black hair, glasses, confident smile --v 6"

Save the URL: https://cdn.midjourney.com/abc123.png

Subsequent Prompts:
"same character coding at a desk --cref https://cdn.midjourney.com/abc123.png"
"same character presenting at a conference --cref https://cdn.midjourney.com/abc123.png"
```

**Advanced: Character Weight (--cw)**
- `--cw 0` - Loose reference (face only)
- `--cw 50` - Moderate (default)
- `--cw 100` - Strict (face, hair, clothing)

**Pro Tip - Style Reference:**
Combine with `--sref` for consistent art style:
```
portrait --cref [character_url] --sref [style_url] --cw 100
```

**Impact:** Professional-quality character consistency for branding.
        """,
        "tags": ["Midjourney", "Design", "Consistency"],
        "time_saved": "Hours of iteration",
        "difficulty_level": 3
    },
    {
        "id": "hack-9",
        "title": "Gemini: Upload PDFs for Analysis",
        "category": "Research",
        "difficulty": "Beginner",
        "tool": "Gemini",
        "icon": "📄",
        "description": "Upload PDFs directly to Gemini for instant analysis and Q&A.",
        "hack": """
**The Problem:** Reading long PDFs is time-consuming.

**The Solution:** Upload to Gemini for instant insights.

**What You Can Do:**
- Summarize research papers
- Extract key findings
- Compare multiple documents
- Generate study guides
- Find specific information

**Example Prompts:**

**For Research Papers:**
```
Summarize this paper's methodology, key findings, and limitations.
Create a table comparing it to [other paper].
```

**For Contracts/Legal:**
```
Extract all deadlines and obligations.
Identify potential risks or red flags.
Explain in simple terms.
```

**For Technical Docs:**
```
Create a step-by-step implementation guide.
Extract all API endpoints and their parameters.
```

**Pro Tip - Multi-Document Analysis:**
Upload multiple PDFs and ask:
```
Compare the approaches in these 3 papers.
Which one is most suitable for [your use case]?
```

**Impact:** 10x faster document analysis.
        """,
        "tags": ["Gemini", "PDF", "Analysis"],
        "time_saved": "30+ min per document",
        "difficulty_level": 1
    },
    {
        "id": "hack-10",
        "title": "V0.dev: Component-to-Code in Seconds",
        "category": "Development",
        "difficulty": "Beginner",
        "tool": "V0.dev",
        "icon": "⚛️",
        "description": "Generate production-ready React components from text descriptions.",
        "hack": """
**The Problem:** Building UI components from scratch is slow.

**The Solution:** V0.dev generates React + Tailwind components instantly.

**How to Use:**
1. Describe your component in plain English
2. V0 generates code + live preview
3. Iterate with follow-up prompts
4. Copy code to your project

**Example Prompts:**

**Simple Component:**
```
Create a pricing card with:
- Title
- Price (large, bold)
- Feature list with checkmarks
- CTA button
- Hover effect
Use Tailwind CSS and shadcn/ui
```

**Complex Component:**
```
Build a dashboard analytics card showing:
- Metric name and value
- Percentage change (green if positive, red if negative)
- Sparkline chart
- Time period selector
Make it responsive and accessible
```

**Pro Tips:**
- Specify "shadcn/ui" for consistent design system
- Ask for "TypeScript" for type safety
- Request "responsive" for mobile support
- Say "accessible" for ARIA labels

**Iteration Example:**
```
Initial: "Create a login form"
Refine: "Add password strength indicator"
Refine: "Add social login buttons"
Refine: "Make it dark mode compatible"
```

**Impact:** 10x faster UI development.
        """,
        "tags": ["V0.dev", "React", "UI"],
        "time_saved": "30+ min per component",
        "difficulty_level": 1
    },
    {
        "id": "hack-11",
        "title": "Gemini 2.0 Flash: Thinking Mode for Complex Problems",
        "category": "Prompting",
        "difficulty": "Intermediate",
        "tool": "Gemini",
        "icon": "💭",
        "description": "Use Gemini 2.0 Flash's thinking mode for better reasoning on complex problems.",
        "hack": """
**The Problem:** LLMs rush to answers without proper reasoning.

**The Solution:** Gemini 2.0 Flash's extended thinking mode.

**How to Enable:**
1. Use Gemini 2.0 Flash Thinking Experimental model
2. Add "Think step by step" or "Show your reasoning" to prompts
3. Model will show its thought process before answering

**Example Prompts:**

**For Code Debugging:**
```
I have a bug in this Python function. Think through what could be wrong:
[paste code]

Show your reasoning process, then provide the fix.
```

**For Architecture Decisions:**
```
I need to choose between microservices and monolith for a new project.
Think through the tradeoffs considering:
- Team size: 5 developers
- Expected scale: 10K users initially
- Timeline: 3 months to MVP

Show your reasoning, then recommend an approach.
```

**For Algorithm Design:**
```
Design an algorithm to find duplicates in a large dataset.
Think through different approaches, analyze time/space complexity,
then recommend the best solution.
```

**Why It Works:**
- Model explicitly shows reasoning steps
- Catches logical errors early
- Produces more accurate results
- Helps you understand the thought process

**Impact:** 50% fewer errors on complex problems.
        """,
        "tags": ["Gemini", "Reasoning", "Thinking"],
        "time_saved": "10+ min per complex problem",
        "difficulty_level": 2
    },
    {
        "id": "hack-12",
        "title": "Cursor Composer: Multi-File Code Generation",
        "category": "Coding",
        "difficulty": "Advanced",
        "tool": "Cursor",
        "icon": "🎼",
        "description": "Use Cursor Composer to generate entire features across multiple files simultaneously.",
        "hack": """
**The Problem:** Building features requires editing many files manually.

**The Solution:** Cursor Composer (Cmd+Shift+I) generates across files.

**How to Use:**
1. Press Cmd+Shift+I (or Ctrl+Shift+I on Windows)
2. Describe the feature you want to build
3. Composer will create/edit multiple files automatically

**Example Prompts:**

**Feature: User Authentication:**
```
Add user authentication to this app:
- Create User model with email/password
- Add login/signup endpoints
- Create JWT token generation
- Add authentication middleware
- Update existing routes to require auth
```

**Feature: API Endpoint:**
```
Create a new /api/products endpoint:
- Add Product model
- Create CRUD operations
- Add validation
- Write tests
- Update API documentation
```

**Feature: UI Component:**
```
Add a dark mode toggle:
- Create theme context
- Add toggle component
- Update all components to use theme
- Persist preference in localStorage
```

**Pro Tips:**
- Be specific about file structure
- Mention testing requirements
- Request documentation updates
- Ask for error handling

**Workflow:**
1. Open Composer (Cmd+Shift+I)
2. Describe feature comprehensively
3. Review proposed changes
4. Accept or iterate
5. Test the generated code

**Impact:** 10x faster feature development.
        """,
        "tags": ["Cursor", "Composer", "Multi-file"],
        "time_saved": "30+ min per feature",
        "difficulty_level": 3
    },
    {
        "id": "hack-13",
        "title": "Windsurf: Cascade for Autonomous Coding",
        "category": "Coding",
        "difficulty": "Advanced",
        "tool": "Windsurf",
        "icon": "🌊",
        "description": "Use Windsurf's Cascade mode for autonomous multi-step coding tasks.",
        "hack": """
**The Problem:** Complex tasks require constant back-and-forth with AI.

**The Solution:** Windsurf Cascade - AI that works autonomously.

**How It Works:**
1. Open Windsurf IDE
2. Activate Cascade mode (Cmd+L)
3. Give high-level task
4. AI autonomously plans and executes

**Example Tasks:**

**Refactor Codebase:**
```
Refactor this codebase to use TypeScript:
- Convert all .js files to .ts
- Add proper type definitions
- Fix all type errors
- Update tests
```

**Add Feature:**
```
Add real-time notifications:
- Set up WebSocket connection
- Create notification service
- Add UI components
- Implement persistence
- Write integration tests
```

**Fix Bug:**
```
There's a memory leak in the data processing module.
Find it, fix it, and add monitoring to prevent future leaks.
```

**What Makes Cascade Special:**
- Plans multi-step approach
- Executes autonomously
- Handles errors and retries
- Asks for clarification when needed
- Shows progress in real-time

**Best Practices:**
- Start with clear, high-level goals
- Let Cascade plan the approach
- Review changes before committing
- Provide feedback for iteration

**Impact:** 5x faster on complex, multi-step tasks.
        """,
        "tags": ["Windsurf", "Cascade", "Autonomous"],
        "time_saved": "1+ hour per complex task",
        "difficulty_level": 3
    },
    {
        "id": "hack-14",
        "title": "Bolt.new: Full-Stack App in Minutes",
        "category": "Development",
        "difficulty": "Beginner",
        "tool": "Bolt.new",
        "icon": "⚡",
        "description": "Generate complete full-stack applications with Bolt.new's AI-powered builder.",
        "hack": """
**The Problem:** Setting up a new project takes hours.

**The Solution:** Bolt.new generates full-stack apps instantly.

**How to Use:**
1. Go to bolt.new
2. Describe your app idea
3. AI generates complete codebase
4. Deploy with one click

**Example Prompts:**

**SaaS App:**
```
Create a task management SaaS:
- User authentication
- Project and task CRUD
- Team collaboration
- Real-time updates
- Stripe integration
Use Next.js, Prisma, PostgreSQL
```

**E-commerce:**
```
Build an e-commerce store:
- Product catalog
- Shopping cart
- Checkout with Stripe
- Order management
- Admin dashboard
Use React, Node.js, MongoDB
```

**Dashboard:**
```
Create an analytics dashboard:
- Data visualization with charts
- Real-time metrics
- Export to PDF
- User permissions
Use Vue.js, Express, PostgreSQL
```

**What You Get:**
- Complete file structure
- Frontend + Backend code
- Database schema
- Authentication setup
- Deployment configuration
- Live preview

**Pro Tips:**
- Be specific about tech stack
- Mention third-party integrations
- Request specific features
- Iterate with follow-up prompts

**Impact:** Ship MVPs in hours instead of weeks.
        """,
        "tags": ["Bolt.new", "Full-stack", "Rapid"],
        "time_saved": "10+ hours per project",
        "difficulty_level": 1
    },
    {
        "id": "hack-15",
        "title": "Replit Agent: Natural Language to App",
        "category": "Development",
        "difficulty": "Beginner",
        "tool": "Replit",
        "icon": "🤖",
        "description": "Use Replit Agent to build and deploy apps using natural language.",
        "hack": """
**The Problem:** Non-developers can't build apps.

**The Solution:** Replit Agent understands natural language.

**How to Use:**
1. Open Replit
2. Click "Create with Agent"
3. Describe your app in plain English
4. Agent builds, tests, and deploys

**Example Requests:**

**Simple App:**
```
Build a weather app that shows current weather for any city.
Use a free weather API and make it mobile-friendly.
```

**Game:**
```
Create a snake game with:
- Score tracking
- High score persistence
- Difficulty levels
- Mobile controls
```

**Tool:**
```
Build a markdown to HTML converter with:
- Live preview
- Syntax highlighting
- Export functionality
- Dark mode
```

**What Agent Does:**
- Chooses appropriate tech stack
- Writes all code
- Handles dependencies
- Fixes bugs automatically
- Deploys to production

**Iteration:**
```
User: "Add user authentication"
Agent: *implements auth system*

User: "Make it work offline"
Agent: *adds service worker*

User: "Add dark mode"
Agent: *implements theme toggle*
```

**Best For:**
- Prototypes
- Learning projects
- Internal tools
- Side projects

**Impact:** Build apps without coding knowledge.
        """,
        "tags": ["Replit", "Agent", "No-code"],
        "time_saved": "Full project time",
        "difficulty_level": 1
    },
    {
        "id": "hack-16",
        "title": "Ollama: Run LLMs Locally for Free",
        "category": "Development",
        "difficulty": "Intermediate",
        "tool": "Ollama",
        "icon": "🦙",
        "description": "Run powerful LLMs locally with Ollama for privacy and cost savings.",
        "hack": """
**The Problem:** API costs add up, privacy concerns with cloud LLMs.

**The Solution:** Run models locally with Ollama.

**Setup:**
```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull a model
ollama pull llama3.2

# Run the model
ollama run llama3.2
```

**Popular Models:**
- `llama3.2` - Meta's latest (3B, 7B, 70B)
- `codellama` - Code-specialized
- `mistral` - Fast and capable
- `phi3` - Microsoft's efficient model
- `gemma2` - Google's open model

**Use Cases:**

**Code Assistant:**
```bash
ollama run codellama
>>> Explain this Python function: [paste code]
```

**Local RAG:**
```python
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2")
response = llm.invoke("Summarize this document: " + doc_text)
```

**API Server:**
```bash
# Ollama runs API server on localhost:11434
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "Why is the sky blue?"
}'
```

**Advantages:**
- ✅ Free (no API costs)
- ✅ Private (data stays local)
- ✅ Fast (no network latency)
- ✅ Offline (works without internet)
- ✅ Customizable (fine-tune models)

**System Requirements:**
- 8GB RAM minimum (16GB+ recommended)
- GPU optional (faster with CUDA/Metal)
- 10-50GB disk space per model

**Impact:** $0 API costs, complete privacy.
        """,
        "tags": ["Ollama", "Local", "Privacy"],
        "time_saved": "API costs eliminated",
        "difficulty_level": 2
    },
    {
        "id": "hack-17",
        "title": "LangChain: Build AI Chains Visually",
        "category": "Development",
        "difficulty": "Advanced",
        "tool": "LangChain",
        "icon": "⛓️",
        "description": "Use LangChain Expression Language (LCEL) to build complex AI workflows.",
        "hack": """
**The Problem:** Complex AI workflows are hard to build and maintain.

**The Solution:** LangChain's composable chains.

**Basic Chain:**
```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Define components
llm = ChatOpenAI(model="gpt-4")
prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")
output_parser = StrOutputParser()

# Chain them together
chain = prompt | llm | output_parser

# Use it
result = chain.invoke({"topic": "programming"})
```

**Advanced: RAG Chain:**
```python
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.runnables import RunnablePassthrough

# Setup
vectorstore = Chroma.from_documents(documents, OpenAIEmbeddings())
retriever = vectorstore.as_retriever()

# RAG Chain
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | output_parser
)

# Query
answer = rag_chain.invoke("What is the capital of France?")
```

**Multi-Step Chain:**
```python
# Step 1: Research
research_chain = research_prompt | llm | output_parser

# Step 2: Analyze
analysis_chain = analysis_prompt | llm | output_parser

# Step 3: Summarize
summary_chain = summary_prompt | llm | output_parser

# Combine
full_chain = (
    research_chain
    | {"research": RunnablePassthrough()}
    | analysis_chain
    | {"analysis": RunnablePassthrough()}
    | summary_chain
)
```

**Use Cases:**
- Document Q&A
- Data extraction
- Content generation
- Code analysis
- Multi-agent systems

**Impact:** Build production AI apps 10x faster.
        """,
        "tags": ["LangChain", "Chains", "RAG"],
        "time_saved": "Hours per AI feature",
        "difficulty_level": 3
    },
    {
        "id": "hack-18",
        "title": "Anthropic Console: Prompt Optimization",
        "category": "Prompting",
        "difficulty": "Intermediate",
        "tool": "Claude",
        "icon": "🎯",
        "description": "Use Anthropic Console's prompt optimizer to improve your prompts automatically.",
        "hack": """
**The Problem:** Writing effective prompts is hard.

**The Solution:** Anthropic Console's built-in optimizer.

**How to Use:**
1. Go to console.anthropic.com
2. Write your prompt
3. Click "Optimize Prompt"
4. Get improved version with explanations

**Example Optimization:**

**Before (Vague):**
```
Write code for a login system
```

**After (Optimized):**
```
You are an expert full-stack developer. Create a secure login system with:

Requirements:
- User registration with email validation
- Password hashing (bcrypt)
- JWT token authentication
- Rate limiting (5 attempts per minute)
- Password reset functionality

Tech Stack:
- Backend: Node.js + Express
- Database: PostgreSQL
- Frontend: React

Provide:
1. Database schema
2. API endpoints with validation
3. Frontend login component
4. Security best practices

Use TypeScript and include error handling.
```

**Optimization Techniques Applied:**
- ✅ Added role context
- ✅ Specified requirements clearly
- ✅ Defined tech stack
- ✅ Requested structured output
- ✅ Added constraints

**Console Features:**
- **Prompt Library** - Save and reuse prompts
- **Version Control** - Track prompt iterations
- **A/B Testing** - Compare prompt variations
- **Analytics** - See token usage and costs
- **Workbench** - Test prompts interactively

**Pro Tips:**
- Use examples in prompts
- Specify output format
- Add constraints
- Request step-by-step reasoning
- Include edge cases

**Impact:** 3x better prompt quality, fewer iterations.
        """,
        "tags": ["Anthropic", "Console", "Optimization"],
        "time_saved": "15+ min per prompt",
        "difficulty_level": 2
    },
    {
        "id": "hack-19",
        "title": "OpenAI Playground: Temperature Tuning",
        "category": "Prompting",
        "difficulty": "Beginner",
        "tool": "ChatGPT",
        "icon": "🌡️",
        "description": "Master temperature settings in OpenAI Playground for optimal outputs.",
        "hack": """
**The Problem:** AI outputs are too random or too predictable.

**The Solution:** Tune temperature for your use case.

**Temperature Scale:**
- **0.0-0.3** - Deterministic, factual, consistent
- **0.4-0.7** - Balanced creativity and accuracy
- **0.8-1.0** - Creative, varied, unpredictable
- **1.0+** - Highly creative, experimental

**Use Cases by Temperature:**

**Temperature 0.0-0.2 (Factual):**
```
Use for:
- Code generation
- Data extraction
- Technical documentation
- Math problems
- Translations

Example: "Extract all email addresses from this text"
```

**Temperature 0.5-0.7 (Balanced):**
```
Use for:
- General Q&A
- Explanations
- Summaries
- Business writing
- Tutorials

Example: "Explain how JWT authentication works"
```

**Temperature 0.8-1.0 (Creative):**
```
Use for:
- Creative writing
- Brainstorming
- Marketing copy
- Story generation
- Unique ideas

Example: "Write a creative product description for..."
```

**Playground Settings:**
```
Temperature: 0.7
Top P: 1.0
Frequency Penalty: 0.0
Presence Penalty: 0.0
Max Tokens: 2000
```

**Pro Tips:**
- Lower temperature for production code
- Higher temperature for ideation
- Use Top P with temperature for fine control
- Test different settings in Playground
- Save presets for different tasks

**Advanced: Frequency Penalty:**
- Reduces repetition
- Range: 0.0 to 2.0
- Use 0.5-1.0 for varied outputs

**Impact:** Perfect outputs for every use case.
        """,
        "tags": ["OpenAI", "Temperature", "Playground"],
        "time_saved": "Multiple iterations avoided",
        "difficulty_level": 1
    },
    {
        "id": "hack-20",
        "title": "Hugging Face Spaces: Deploy AI Apps Free",
        "category": "Development",
        "difficulty": "Intermediate",
        "tool": "Hugging Face",
        "icon": "🤗",
        "description": "Deploy AI applications for free using Hugging Face Spaces.",
        "hack": """
**The Problem:** Deploying AI apps is expensive and complex.

**The Solution:** Hugging Face Spaces - free hosting for AI apps.

**Setup:**
1. Go to huggingface.co/spaces
2. Click "Create new Space"
3. Choose framework (Gradio/Streamlit/Static)
4. Push your code
5. App is live!

**Example: Gradio App:**
```python
import gradio as gr
from transformers import pipeline

# Load model
classifier = pipeline("sentiment-analysis")

def analyze(text):
    result = classifier(text)[0]
    return f"{result['label']}: {result['score']:.2f}"

# Create interface
demo = gr.Interface(
    fn=analyze,
    inputs=gr.Textbox(placeholder="Enter text..."),
    outputs="text",
    title="Sentiment Analyzer"
)

demo.launch()
```

**Example: Streamlit App:**
```python
import streamlit as st
from transformers import pipeline

st.title("Text Summarizer")

text = st.text_area("Enter text to summarize:")

if st.button("Summarize"):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=130, min_length=30)
    st.write(summary[0]['summary_text'])
```

**Popular Use Cases:**
- Image generation
- Text classification
- Object detection
- Speech recognition
- Translation
- Question answering

**Features:**
- ✅ Free hosting
- ✅ GPU support (paid tier)
- ✅ Custom domains
- ✅ API access
- ✅ Embed anywhere
- ✅ Version control

**Deployment:**
```bash
# Clone your space
git clone https://huggingface.co/spaces/username/space-name

# Add files
git add app.py requirements.txt

# Push to deploy
git push
```

**Pro Tips:**
- Use Gradio for quick demos
- Use Streamlit for dashboards
- Add README.md for documentation
- Use secrets for API keys
- Enable analytics

**Impact:** Deploy AI apps in minutes, not days.
        """,
        "tags": ["Hugging Face", "Deployment", "Free"],
        "time_saved": "Hours of deployment work",
        "difficulty_level": 2
    }
]


def get_all_hacks():
    """Get all AI hacks"""
    return AI_HACKS


def get_hacks_by_category(category):
    """Get hacks filtered by category"""
    if category == "All":
        return AI_HACKS
    return [h for h in AI_HACKS if h['category'].lower() == category.lower()]


def get_hacks_by_tool(tool):
    """Get hacks filtered by tool"""
    if tool == "All":
        return AI_HACKS
    return [h for h in AI_HACKS if h['tool'].lower() == tool.lower()]


def get_hacks_by_difficulty(difficulty):
    """Get hacks filtered by difficulty"""
    if difficulty == "All":
        return AI_HACKS
    return [h for h in AI_HACKS if h['difficulty'].lower() == difficulty.lower()]


def search_hacks(query):
    """Search hacks by title, description, or tags"""
    if not query:
        return []
    
    query = query.lower()
    results = []
    
    for hack in AI_HACKS:
        if (query in hack['title'].lower() or 
            query in hack['description'].lower() or
            query in hack['hack'].lower() or
            any(query in tag.lower() for tag in hack['tags'])):
            results.append(hack)
    
    return results
