"""
AI Nexus - Configuration Settings
"""

# Application Settings
APP_NAME = "AI Nexus"
APP_VERSION = "2.5.0"
APP_TAGLINE = "Enterprise Cognitive Architecture & Engineering System"

# Theme Colors
COLORS = {
    "primary": "#2563EB",
    "primary_light": "#60A5FA",
    "primary_dark": "#1E40AF",
    "secondary": "#10B981",
    "accent": "#F59E0B",
    "success": "#10B981",
    "warning": "#F59E0B",
    "error": "#EF4444",
    "background": "#0A0E1A",
    "surface": "#111827",
    "surface_light": "#1F2937",
    "text_primary": "#F9FAFB",
    "text_secondary": "#9CA3AF",
    "gradient_start": "#2563EB",
    "gradient_end": "#10B981",
}

# Role Archetypes
ROLE_ARCHETYPES = [
    {"id": "frontend_dev", "name": "Frontend Developer", "icon": "🎨", "category": "Engineering"},
    {"id": "backend_dev", "name": "Backend Developer", "icon": "⚙️", "category": "Engineering"},
    {"id": "fullstack_dev", "name": "Full-Stack Developer", "icon": "🔄", "category": "Engineering"},
    {"id": "mobile_dev", "name": "Mobile Developer", "icon": "📱", "category": "Engineering"},
    {"id": "devops", "name": "DevOps Engineer", "icon": "🔧", "category": "Engineering"},
    {"id": "ml_engineer", "name": "ML Engineer", "icon": "🤖", "category": "AI/ML"},
    {"id": "data_scientist", "name": "Data Scientist", "icon": "📊", "category": "AI/ML"},
    {"id": "data_analyst", "name": "Data Analyst", "icon": "📈", "category": "AI/ML"},
    {"id": "manual_tester", "name": "Manual Tester", "icon": "🔍", "category": "QA"},
    {"id": "automation_tester", "name": "Automation Tester", "icon": "🤖", "category": "QA"},
    {"id": "qa_lead", "name": "QA Lead", "icon": "👨‍💼", "category": "QA"},
    {"id": "scrum_master", "name": "Scrum Master", "icon": "🏃", "category": "Management"},
    {"id": "product_owner", "name": "Product Owner", "icon": "📋", "category": "Management"},
    {"id": "technical_pm", "name": "Technical PM", "icon": "📅", "category": "Management"},
    {"id": "engineering_manager", "name": "Engineering Manager", "icon": "👔", "category": "Management"},
    {"id": "ux_researcher", "name": "UX Researcher", "icon": "🔬", "category": "Design"},
    {"id": "ui_designer", "name": "UI Designer", "icon": "🎭", "category": "Design"},
    {"id": "product_designer", "name": "Product Designer", "icon": "✏️", "category": "Design"},
    {"id": "system_architect", "name": "System Architect", "icon": "🏗️", "category": "Architecture"},
    {"id": "security_engineer", "name": "Security Engineer", "icon": "🔒", "category": "Security"},
    {"id": "technical_writer", "name": "Technical Writer", "icon": "📝", "category": "Documentation"},
    {"id": "solutions_architect", "name": "Solutions Architect", "icon": "💡", "category": "Architecture"},
]

# Industry Verticals
INDUSTRY_VERTICALS = [
    {"id": "fintech", "name": "FinTech", "icon": "💰"},
    {"id": "healthtech", "name": "HealthTech", "icon": "🏥"},
    {"id": "ecommerce", "name": "E-commerce", "icon": "🛒"},
    {"id": "saas", "name": "SaaS", "icon": "☁️"},
    {"id": "gaming", "name": "Gaming", "icon": "🎮"},
    {"id": "edtech", "name": "EdTech", "icon": "📚"},
    {"id": "manufacturing", "name": "Manufacturing", "icon": "🏭"},
    {"id": "logistics", "name": "Logistics", "icon": "🚚"},
    {"id": "media", "name": "Media & Entertainment", "icon": "🎬"},
    {"id": "telecom", "name": "Telecom", "icon": "📡"},
    {"id": "real_estate", "name": "Real Estate", "icon": "🏢"},
    {"id": "automotive", "name": "Automotive", "icon": "🚗"},
]

# Tech Stacks
TECH_STACKS = {
    "languages": ["Python", "JavaScript", "TypeScript", "Java", "C#", "Go", "Rust", "Ruby", "PHP", "Swift", "Kotlin"],
    "frontend": ["React", "Angular", "Vue.js", "Next.js", "Svelte", "HTML/CSS", "Tailwind"],
    "backend": ["Node.js", "Django", "FastAPI", "Spring Boot", ".NET", "Express.js", "Flask"],
    "databases": ["PostgreSQL", "MongoDB", "MySQL", "Redis", "Elasticsearch", "DynamoDB"],
    "cloud": ["AWS", "Azure", "GCP", "Heroku", "Vercel", "DigitalOcean"],
    "tools": ["Docker", "Kubernetes", "Jenkins", "GitHub Actions", "Terraform", "Ansible"],
    "design": ["Figma", "Sketch", "Adobe XD", "Photoshop", "Illustrator", "InVision"],
    "pm_tools": ["Jira", "Asana", "Trello", "Linear", "Monday.com", "Notion"],
}

# Learning Styles
LEARNING_STYLES = [
    {"id": "video", "name": "Video Courses", "icon": "🎥", "description": "Learn through watching video tutorials"},
    {"id": "text", "name": "Text & Documentation", "icon": "📖", "description": "Learn through reading articles and docs"},
    {"id": "interactive", "name": "Interactive Labs", "icon": "💻", "description": "Learn by doing in sandbox environments"},
    {"id": "project", "name": "Project-Based", "icon": "🛠️", "description": "Learn by building real projects"},
    {"id": "social", "name": "Social Learning", "icon": "👥", "description": "Learn through community and discussion"},
]

# Skill Levels
SKILL_LEVELS = [
    {"id": "beginner", "name": "Beginner", "description": "New to AI tools", "range": (0, 25)},
    {"id": "intermediate", "name": "Intermediate", "description": "Some experience with AI", "range": (26, 50)},
    {"id": "advanced", "name": "Advanced", "description": "Regular AI user", "range": (51, 75)},
    {"id": "expert", "name": "Expert", "description": "AI power user", "range": (76, 100)},
]

# Learning Path Types
LEARNING_PATHS = [
    {"id": "quick_wins", "name": "Quick Wins", "duration": "5-10 min", "icon": "⚡"},
    {"id": "deep_dives", "name": "Deep Dives", "duration": "30-60 min", "icon": "🔥"},
    {"id": "mastery_tracks", "name": "Mastery Tracks", "duration": "10-20 hours", "icon": "🎯"},
    {"id": "certifications", "name": "Certifications", "duration": "50-100 hours", "icon": "🏆"},
]

# AI Tool Categories
AI_TOOL_CATEGORIES = [
    {"id": "code_generation", "name": "Code Generation & Assistance", "icon": "💻"},
    {"id": "testing_qa", "name": "Testing & QA", "icon": "🧪"},
    {"id": "project_management", "name": "Project Management", "icon": "📋"},
    {"id": "documentation", "name": "Documentation", "icon": "📝"},
    {"id": "design_prototyping", "name": "Design & Prototyping", "icon": "🎨"},
    {"id": "data_analysis", "name": "Data Analysis", "icon": "📊"},
    {"id": "communication", "name": "Communication", "icon": "💬"},
    {"id": "devops_infra", "name": "DevOps & Infrastructure", "icon": "🔧"},
    {"id": "security", "name": "Security", "icon": "🔒"},
    {"id": "research_learning", "name": "Research & Learning", "icon": "🔬"},
    {"id": "productivity", "name": "Productivity", "icon": "⚡"},
    {"id": "content_creation", "name": "Content Creation", "icon": "✍️"},
]

# Prompt Categories (Synced with final_prompts.py)
PROMPT_CATEGORIES = [
    {"id": "coding", "name": "Coding & Development", "icon": "💻"},
    {"id": "debugging", "name": "Debugging & Troubleshooting", "icon": "🐛"},
    {"id": "testing", "name": "Testing & QA", "icon": "🧪"},
    {"id": "documentation", "name": "Documentation", "icon": "📝"},
    {"id": "architecture", "name": "System Architecture", "icon": "🏗️"},
    {"id": "code_review", "name": "Code Review", "icon": "👀"},
    {"id": "refactoring", "name": "Refactoring", "icon": "🔄"},
    {"id": "learning", "name": "Learning & Explanation", "icon": "📚"},
    {"id": "productivity", "name": "Productivity", "icon": "⚡"},
    {"id": "communication", "name": "Communication", "icon": "💬"},
    {"id": "devops_infra", "name": "DevOps & Infrastructure", "icon": "🔧"},
    {"id": "security", "name": "Security", "icon": "🔒"},
    {"id": "content_creation", "name": "Content Creation", "icon": "✍️"},
    {"id": "data_analysis", "name": "Data Analysis", "icon": "📊"},
]
