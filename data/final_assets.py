"""
AI Nexus - Curated Technical Assets
100% Manual Curation - No Dummy Data
"""

AI_TOOLS_DATABASE = [
    # Code Generation & Assistance
    {"id": "github-copilot", "name": "GitHub Copilot", "category": "coding", "icon": "🤖", "description": "AI pair programmer that suggests code and functions in real-time", "rating": 4.8, "pricing": "Paid", "pricing_details": "$19/mo individual, $39/mo business", "features": ["Code completion", "Multi-language", "IDE integration", "Chat interface"], "integrations": ["VS Code", "JetBrains", "Neovim", "Visual Studio"], "best_for": ["All Developers"], "url": "https://github.com/features/copilot", "is_featured": True},
    {"id": "cursor", "name": "Cursor", "category": "coding", "icon": "⚡", "description": "AI-first code editor built for pair programming with AI", "rating": 4.7, "pricing": "Freemium", "pricing_details": "Free tier, Pro $20/mo", "features": ["AI code editing", "Codebase Q&A", "Multi-file edits", "Custom models"], "integrations": ["Git", "GitHub", "Extensions"], "best_for": ["All Developers"], "url": "https://cursor.sh", "is_featured": True},
    {"id": "langchain", "name": "LangChain", "category": "coding", "icon": "🦜", "description": "Framework for building applications with LLMs through chaining.", "rating": 4.8, "pricing": "Free", "pricing_details": "Open Source", "features": ["Chains", "Agents", "Memory", "Retrieval"], "integrations": ["Python", "OpenAI", "Anthropic"], "best_for": ["AI Engineers"], "url": "https://langchain.com", "is_featured": True},
    {"id": "llamaindex", "name": "LlamaIndex", "category": "coding", "icon": "🦙", "description": "Data framework for LLM applications to connect private data.", "rating": 4.6, "pricing": "Free", "pricing_details": "Open Source", "features": ["Data connectors", "Indices", "Query engine"], "integrations": ["Pinecone", "Milvus"], "best_for": ["Enterprise AI"], "url": "https://llamaindex.ai", "is_featured": False},
    
    # Testing & QA
    {"id": "testim", "name": "Testim", "category": "testing", "icon": "🧪", "description": "AI-powered test authoring and execution platform", "rating": 4.5, "pricing": "Paid", "pricing_details": "Custom pricing", "features": ["Smart locators", "Self-healing tests", "Parallel execution", "CI/CD integration"], "integrations": ["Jenkins", "CircleCI", "GitHub Actions"], "best_for": ["QA Teams"], "url": "https://www.testim.io", "is_featured": True},
    {"id": "applitools", "name": "Applitools", "category": "testing", "icon": "👁️", "description": "Visual AI for test automation with smart visual comparisons", "rating": 4.6, "pricing": "Freemium", "pricing_details": "Free tier available", "features": ["Visual testing", "Cross-browser", "Auto maintenance", "Root cause analysis"], "integrations": ["Selenium", "Cypress", "Playwright"], "best_for": ["UI/UX Teams"], "url": "https://applitools.com", "is_featured": True},
    {"id": "mabl", "name": "mabl", "category": "testing", "icon": "🔍", "description": "Intelligent test automation for agile teams", "rating": 4.4, "pricing": "Paid", "pricing_details": "Custom pricing", "features": ["Auto-healing", "Insights", "API testing", "Performance"], "integrations": ["GitHub", "GitLab", "Slack"], "best_for": ["Agile Teams"], "url": "https://www.mabl.com", "is_featured": False},
    {"id": "functionize", "name": "Functionize", "category": "testing", "icon": "🔬", "description": "AI-powered software testing platform", "rating": 4.3, "pricing": "Paid", "pricing_details": "Custom pricing", "features": ["ML test creation", "Self-healing", "Natural language", "API testing"], "integrations": ["CI/CD tools", "Jira", "Slack"], "best_for": ["Enterprise QA"], "url": "https://www.functionize.com", "is_featured": False},
    {"id": "katalon", "name": "Katalon AI", "category": "testing", "icon": "🤖", "description": "All-in-one test automation with AI capabilities", "rating": 4.3, "pricing": "Freemium", "pricing_details": "Free tier, paid plans", "features": ["Record & playback", "Self-healing", "Analytics", "Cross-platform"], "integrations": ["Jira", "Jenkins", "Git"], "best_for": ["Cross-platform testing"], "url": "https://katalon.com", "is_featured": False},

    # Data Analysis
    {"id": "pinecone", "name": "Pinecone", "category": "data_analysis", "icon": "🌲", "description": "Vector database for high-performance AI applications.", "rating": 4.7, "pricing": "Freemium", "pricing_details": "Free tier available", "features": ["Vector search", "Serverless", "Scalable"], "integrations": ["LangChain", "LlamaIndex"], "best_for": ["Data Scientists"], "url": "https://pinecone.io", "is_featured": True},
    {"id": "julius", "name": "Julius AI", "category": "data_analysis", "icon": "📊", "description": "AI data analyst that creates visualizations from your data", "rating": 4.5, "pricing": "Freemium", "pricing_details": "Free tier, Pro $20/mo", "features": ["Data analysis", "Visualizations", "Natural language", "Python code"], "integrations": ["File upload", "Databases"], "best_for": ["Data analysts"], "url": "https://julius.ai", "is_featured": True},

    # Infrastructure
    {"id": "weights-biases", "name": "Weights & Biases", "category": "devops_infra", "icon": "📈", "description": "Developer tools for machine learning to track experiments.", "rating": 4.7, "pricing": "Freemium", "pricing_details": "Free for individuals", "features": ["Experiment tracking", "Version control", "Artifacts"], "integrations": ["PyTorch", "Hugging Face"], "best_for": ["MLOps Engineers"], "url": "https://wandb.ai", "is_featured": False},

    # Prototyping
    {"id": "v0-dev", "name": "v0.dev", "category": "design_prototyping", "icon": "✨", "description": "Generative UI by Vercel for building components with text.", "rating": 4.9, "pricing": "Freemium", "pricing_details": "Free tier, $20/mo Pro", "features": ["Generative UI", "React code", "Tailwind styling"], "integrations": ["Next.js", "Vercel"], "best_for": ["Frontend Developers"], "url": "https://v0.dev", "is_featured": True},
    {"id": "streamlit", "name": "Streamlit", "category": "design_prototyping", "icon": "🎈", "description": "The fastest way to build and share data apps.", "rating": 4.8, "pricing": "Free", "pricing_details": "Open Source", "features": ["Fast UI", "Python-based", "Interactive"], "integrations": ["Python", "Snowflake"], "best_for": ["Data Developers"], "url": "https://streamlit.io", "is_featured": True},

    # Documentation
    {"id": "mintlify", "name": "Mintlify", "category": "documentation", "icon": "📚", "description": "AI-powered documentation platform for developers", "rating": 4.5, "pricing": "Freemium", "pricing_details": "Free tier, Pro $120/mo", "features": ["Auto-generated docs", "Search", "Beautiful themes", "API docs"], "integrations": ["GitHub", "GitLab", "OpenAPI"], "best_for": ["API documentation"], "url": "https://mintlify.com", "is_featured": True},
    {"id": "swimm", "name": "Swimm", "category": "documentation", "icon": "🏊", "description": "AI documentation that stays in sync with code", "rating": 4.4, "pricing": "Freemium", "pricing_details": "Free for small teams", "features": ["Code-coupled docs", "Auto-sync", "IDE integration", "Snippets"], "integrations": ["VS Code", "JetBrains", "GitHub"], "best_for": ["Code documentation"], "url": "https://swimm.io", "is_featured": False},

    # Design
    {"id": "midjourney", "name": "Midjourney", "category": "design_prototyping", "icon": "🎨", "description": "AI image generation for stunning visual assets", "rating": 4.9, "pricing": "Paid", "pricing_details": "$10-60/mo", "features": ["Image generation", "Variations", "Upscaling", "Styles"], "integrations": ["Discord"], "best_for": ["Visual designers"], "url": "https://midjourney.com", "is_featured": True},
    {"id": "figma-ai", "name": "Figma AI", "category": "design_prototyping", "icon": "🎭", "description": "AI features built into Figma for faster design", "rating": 4.4, "pricing": "Included", "pricing_details": "With Figma subscription", "features": ["Layer renaming", "Auto layout", "Content generation", "Search"], "integrations": ["Figma"], "best_for": ["UI designers"], "url": "https://figma.com", "is_featured": False},

    # Research
    {"id": "perplexity", "name": "Perplexity AI", "category": "research_learning", "icon": "🔍", "description": "AI-powered search engine with cited answers", "rating": 4.7, "pricing": "Freemium", "pricing_details": "Free tier, Pro $20/mo", "features": ["Search", "Citations", "Focus modes", "File analysis"], "integrations": ["API", "Mobile apps"], "best_for": ["Researchers"], "url": "https://perplexity.ai", "is_featured": True},
    {"id": "elicit", "name": "Elicit", "category": "research_learning", "icon": "📚", "description": "AI research assistant for academic papers", "rating": 4.4, "pricing": "Freemium", "pricing_details": "Free tier, Plus $10/mo", "features": ["Paper search", "Summarization", "Data extraction", "Analysis"], "integrations": ["Export"], "best_for": ["Academic researchers"], "url": "https://elicit.org", "is_featured": False},

    # Communication
    {"id": "otter-ai", "name": "Otter.ai", "category": "communication", "icon": "🦦", "description": "AI meeting transcription and note-taking", "rating": 4.5, "pricing": "Freemium", "pricing_details": "Free tier, Pro $16.99/mo", "features": ["Transcription", "Speaker ID", "Summaries", "Search"], "integrations": ["Zoom", "Meet", "Teams"], "best_for": ["Meeting-heavy professionals"], "url": "https://otter.ai", "is_featured": True},
    {"id": "grammarly", "name": "Grammarly", "category": "communication", "icon": "✒️", "description": "AI writing assistant for grammar, tone, and clarity", "rating": 4.7, "pricing": "Freemium", "pricing_details": "Free tier, Premium $12/mo", "features": ["Grammar check", "Tone detection", "Plagiarism", "Rewriting"], "integrations": ["Browser", "Desktop", "Mobile"], "best_for": ["All professionals"], "url": "https://grammarly.com", "is_featured": True},

    # Productivity
    {"id": "chatgpt", "name": "ChatGPT", "category": "productivity", "icon": "💭", "description": "OpenAI's conversational AI assistant", "rating": 4.8, "pricing": "Freemium", "pricing_details": "Free tier, Plus $20/mo", "features": ["Conversations", "Code", "Analysis", "Vision", "Web browsing"], "integrations": ["API", "Plugins"], "best_for": ["Everyone"], "url": "https://chat.openai.com", "is_featured": True},
    {"id": "claude", "name": "Claude", "category": "productivity", "icon": "🤖", "description": "Anthropic's helpful, harmless, and honest AI assistant", "rating": 4.7, "pricing": "Freemium", "pricing_details": "Free tier, Pro $20/mo", "features": ["Long context", "Analysis", "Coding", "Writing"], "integrations": ["API"], "best_for": ["Long-form tasks"], "url": "https://claude.ai", "is_featured": True},

    # Project Management
    {"id": "motion", "name": "Motion", "category": "project_management", "icon": "📅", "description": "AI calendar and project management that auto-schedules your day", "rating": 4.6, "pricing": "Paid", "pricing_details": "$34/mo", "features": ["Auto-scheduling", "Task management", "Calendar blocking", "Team coordination"], "integrations": ["Google Calendar", "Outlook", "Zoom"], "best_for": ["Busy professionals"], "url": "https://www.usemotion.com", "is_featured": True},
    {"id": "notion-ai", "name": "Notion AI", "category": "project_management", "icon": "📒", "description": "AI writing and knowledge assistant in Notion", "rating": 4.5, "pricing": "Add-on", "pricing_details": "$8/mo per member", "features": ["Content generation", "Summarization", "Action items", "Translation"], "integrations": ["Notion workspace"], "best_for": ["Teams using Notion"], "url": "https://notion.so/product/ai", "is_featured": False},

    # Content Creation
    {"id": "jasper", "name": "Jasper", "category": "content_creation", "icon": "✍️", "description": "AI content generation for marketing teams", "rating": 4.4, "pricing": "Paid", "pricing_details": "$49/mo starter", "features": ["Long-form", "Templates", "Brand voice", "Images"], "integrations": ["Chrome", "API"], "best_for": ["Marketing teams"], "url": "https://jasper.ai", "is_featured": False},
    {"id": "copy-ai", "name": "Copy.ai", "category": "content_creation", "icon": "📝", "description": "AI-powered copywriting for every business case", "rating": 4.5, "pricing": "Freemium", "pricing_details": "Free tier, Pro $36/mo", "features": ["Workflows", "Brand voice", "Content creation", "Analytics"], "integrations": ["Browser", "API"], "best_for": ["Content writers"], "url": "https://copy.ai", "is_featured": True},

    # Security
    {"id": "snyk", "name": "Snyk", "category": "security", "icon": "🛡️", "description": "Developer security platform with AI-powered fixes", "rating": 4.6, "pricing": "Freemium", "pricing_details": "Free tier available", "features": ["Vulnerability scanning", "Auto-fix", "SCA", "Container security"], "integrations": ["GitHub", "GitLab", "IDEs"], "best_for": ["Security-conscious teams"], "url": "https://snyk.io", "is_featured": True},
    {"id": "checkmarx", "name": "Checkmarx", "category": "security", "icon": "🔍", "description": "Enterprise application security testing with AI insights", "rating": 4.4, "pricing": "Paid", "pricing_details": "Enterprise pricing", "features": ["SAST", "DAST", "API Security", "IAST"], "integrations": ["Azure DevOps", "Jenkins", "GitHub"], "best_for": ["Enterprise security"], "url": "https://checkmarx.com", "is_featured": False},

    # DevOps
    {"id": "harness-ai", "name": "Harness AI", "category": "devops_infra", "icon": "🔧", "description": "AI-native software delivery platform", "rating": 4.4, "pricing": "Paid", "pricing_details": "Custom pricing", "features": ["CI/CD", "Cost management", "Feature flags", "Deployment verification"], "integrations": ["Cloud providers", "Git"], "best_for": ["Enterprise DevOps"], "url": "https://harness.io", "is_featured": True},
    {"id": "kubecost", "name": "Kubecost", "category": "devops_infra", "icon": "☸️", "description": "AI-powered Kubernetes cost monitoring and optimization", "rating": 4.5, "pricing": "Freemium", "pricing_details": "Free for small clusters", "features": ["Cost allocation", "Optimization", "Alerts"], "integrations": ["Kubernetes", "AWS", "GCP"], "best_for": ["Cloud FinOps"], "url": "https://kubecost.com", "is_featured": False},

    # Data Analysis
    {"id": "great-expectations", "name": "Great Expectations", "category": "data_analysis", "icon": "📏", "description": "AI-ready data quality and validation framework", "rating": 4.7, "pricing": "Free", "pricing_details": "Open Source", "features": ["Data profiling", "Expectations", "Validation"], "integrations": ["Pandas", "Spark", "SQLAlchemy"], "best_for": ["Data Engineers"], "url": "https://greatexpectations.io", "is_featured": False},

    # Research & Models
    {"id": "hugging-face", "name": "Hugging Face", "category": "research_learning", "icon": "🤗", "description": "The community hub for AI models, datasets, and demos.", "rating": 4.9, "pricing": "Freemium", "pricing_details": "Free, Enterprise Hub", "features": ["Model Hub", "Datasets", "Spaces", "Inference API"], "integrations": ["Python", "PyTorch", "TensorFlow"], "best_for": ["AI Researchers"], "url": "https://huggingface.co", "is_featured": True},
    {"id": "replicate", "name": "Replicate", "category": "devops_infra", "icon": "🚀", "description": "Run open-source models with a cloud API.", "rating": 4.7, "pricing": "Pay-as-you-go", "pricing_details": "Per second billing", "features": ["Model hosting", "Fine-tuning", "API access"], "integrations": ["Python", "Node.js", "Next.js"], "best_for": ["AI App Developers"], "url": "https://replicate.com", "is_featured": True},

    # Creative & Media
    {"id": "elevenlabs", "name": "ElevenLabs", "category": "content_creation", "icon": "🎙️", "description": "The most realistic AI voice generator and text-to-speech.", "rating": 4.8, "pricing": "Freemium", "pricing_details": "Free tier, Starter $5/mo", "features": ["Voice cloning", "Dubbing", "Speech synthesis"], "integrations": ["API"], "best_for": ["Content Creators"], "url": "https://elevenlabs.io", "is_featured": True},
    {"id": "leonardo-ai", "name": "Leonardo.ai", "category": "design_prototyping", "icon": "👾", "description": "Generative AI platform for game assets and concept art.", "rating": 4.6, "pricing": "Freemium", "pricing_details": "Free daily tokens", "features": ["Image generation", "Canvas editor", "3D textures"], "integrations": ["Web"], "best_for": ["Game Designers"], "url": "https://leonardo.ai", "is_featured": False},

    # Infrastructure & Deployment
    {"id": "vercel", "name": "Vercel", "category": "devops_infra", "icon": "▲", "description": "Frontend Cloud for building and deploying the best web experiences.", "rating": 4.9, "pricing": "Freemium", "pricing_details": "Free for hobbyists, Pro $20/mo", "features": ["Global Edge", "Serverless", "Analytics"], "integrations": ["GitHub", "GitLab"], "best_for": ["Frontend Developers"], "url": "https://vercel.com", "is_featured": True},
    {"id": "terraform", "name": "Terraform", "category": "devops_infra", "icon": "🏗️", "description": "Infrastructure as Code tool for building, changing, and versioning infrastructure.", "rating": 4.8, "pricing": "Free", "pricing_details": "Open Source", "features": ["IaC", "Multi-cloud", "Automation"], "integrations": ["AWS", "Azure", "GCP"], "best_for": ["DevOps Engineers"], "url": "https://www.terraform.io", "is_featured": False},
    
    # Code Assistance
    {"id": "tabnine", "name": "Tabnine", "category": "coding", "icon": "💻", "description": "Private and secure AI code assistant for teams", "rating": 4.5, "pricing": "Freemium", "pricing_details": "$12/mo pro", "features": ["Local models", "Team learning", "Secure"], "integrations": ["VS Code", "IntelliJ"], "best_for": ["Privacy-focused teams"], "url": "https://tabnine.com", "is_featured": False},
    {"id": "codeium", "name": "Codeium", "category": "coding", "icon": "🦸", "description": "Free AI Code Completion & Chat for developers.", "rating": 4.7, "pricing": "Free", "pricing_details": "Free for individuals", "features": ["Autocomplete", "Chat", "Search"], "integrations": ["VS Code", "JetBrains", "Vim"], "best_for": ["Individual Developers"], "url": "https://codeium.com", "is_featured": False},

    # New AI Platforms & APIs
    {"id": "gemini", "name": "Google Gemini", "category": "productivity", "icon": "💎", "description": "Google's most capable AI model, built for multimodal reasoning.", "rating": 4.8, "pricing": "Freemium", "pricing_details": "Free tier, Advanced $20/mo", "features": ["Multimodal", "Code generation", "Long context", "Workspace integration"], "integrations": ["Google Workspace", "Android"], "best_for": ["Google ecosystem users"], "url": "https://gemini.google.com", "is_featured": True},
    {"id": "anthropic-api", "name": "Anthropic API", "category": "coding", "icon": "🧠", "description": "Access Claude models via API for building AI applications.", "rating": 4.8, "pricing": "Pay-as-you-go", "pricing_details": "Per token pricing", "features": ["Claude 3", "Long context", "Tool use", "Vision"], "integrations": ["Python", "Node.js", "REST"], "best_for": ["AI Developers"], "url": "https://docs.anthropic.com", "is_featured": True},
    {"id": "openrouter", "name": "OpenRouter", "category": "devops_infra", "icon": "🔀", "description": "Unified API to access 100+ LLMs from multiple providers.", "rating": 4.6, "pricing": "Pay-as-you-go", "pricing_details": "Pass-through pricing", "features": ["Model routing", "Fallbacks", "Cost tracking", "Rate limits"], "integrations": ["OpenAI SDK compatible"], "best_for": ["Multi-model apps"], "url": "https://openrouter.ai", "is_featured": False},
    {"id": "modal", "name": "Modal", "category": "devops_infra", "icon": "⚡", "description": "Serverless platform for running AI/ML workloads at scale.", "rating": 4.7, "pricing": "Pay-as-you-go", "pricing_details": "Per second compute", "features": ["Serverless GPU", "Fast cold starts", "Python native"], "integrations": ["Python", "Hugging Face"], "best_for": ["ML Engineers"], "url": "https://modal.com", "is_featured": True},
    {"id": "runpod", "name": "RunPod", "category": "devops_infra", "icon": "🏃", "description": "Cloud GPU platform for AI training and inference.", "rating": 4.5, "pricing": "Pay-as-you-go", "pricing_details": "$0.39/hr GPU", "features": ["On-demand GPUs", "Serverless", "Templates"], "integrations": ["Docker", "Jupyter"], "best_for": ["AI Training"], "url": "https://runpod.io", "is_featured": False},
    {"id": "groq", "name": "Groq", "category": "productivity", "icon": "🚀", "description": "Ultra-fast LLM inference with specialized hardware.", "rating": 4.7, "pricing": "Freemium", "pricing_details": "Free tier, pay-as-you-go", "features": ["Fast inference", "Low latency", "Llama models"], "integrations": ["OpenAI SDK compatible"], "best_for": ["Speed-critical apps"], "url": "https://groq.com", "is_featured": True},
]

def get_all_tools():
    return AI_TOOLS_DATABASE

def get_tools_by_category(category: str):
    if not category or category.lower() == 'all':
        return AI_TOOLS_DATABASE
    return [t for t in AI_TOOLS_DATABASE if t.get("category", "").lower() == category.lower()]

def get_featured_tools():
    return [t for t in AI_TOOLS_DATABASE if t.get("is_featured", False)]

def search_tools(query: str):
    if not query: return []
    query = query.lower()
    return [t for t in AI_TOOLS_DATABASE if query in t.get("name", "").lower() or query in t.get("description", "").lower()]

def get_tool_by_id(tool_id: str):
    for tool in AI_TOOLS_DATABASE:
        if tool.get("id") == tool_id:
            return tool
    return None
