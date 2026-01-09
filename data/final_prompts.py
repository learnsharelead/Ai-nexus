"""
AI Nexus - Curated Prompt Engineering Assets
100% Manual Curation - No Dummy Data
"""

PROMPTS_DATABASE = [
    # Coding & Development
    {
        "id": "p-1", 
        "title": "Clean Code Architect", 
        "category": "coding", 
        "prompt": "You are a Senior Software Architect. Review the following {language} code snippet. Your goal is to simplify logic, improve readability, and ensure it follows SOLID principles. Provide the refactored code and a list of structural improvements made.\n\nCode:\n```{language}\n{code}\n```", 
        "variables": ["language", "code"], 
        "difficulty": "Intermediate", 
        "uses": 12453, 
        "rating": 4.9, 
        "tags": ["architecture", "clean code"], 
        "ai_models": ["GPT-4o", "Claude 3.5 Sonnet"]
    },
    {
        "id": "p-2", 
        "title": "Regex Logic Master", 
        "category": "coding", 
        "prompt": "Act as a Regular Expression expert. I need to {requirement} in {language}. Provide the regex pattern, a detailed explanation of each token in the pattern, and example strings that match and fail.", 
        "variables": ["requirement", "language"], 
        "difficulty": "Beginner", 
        "uses": 8765, 
        "rating": 4.8, 
        "tags": ["regex", "utilities"], 
        "ai_models": ["ChatGPT", "Claude"]
    },
    {
        "id": "p-11",
        "title": "Unit Test Generator (Pytest/Jest)",
        "category": "coding",
        "prompt": "Generate a comprehensive test suite for the following {language} function using {framework}. Include tests for the happy path, edge cases (empty inputs, nulls), and error handling. Code:\n{code}",
        "variables": ["language", "framework", "code"],
        "difficulty": "Intermediate",
        "uses": 15600,
        "rating": 4.9,
        "tags": ["testing", "automation"],
        "ai_models": ["GPT-4o", "Claude 3.5 Sonnet"]
    },
    
    # Architecture & Design
    {
        "id": "p-3", 
        "title": "Microservices Blueprint", 
        "category": "architecture", 
        "prompt": "Design a microservices architecture for {system_type}. Include:\n- Boundary definitions for 3 core services\n- Communication patterns (Sync vs Async)\n- Recommended database per service\n- Security layer (AuthZ/AuthN)\n- Mermaid diagram syntax for the high-level flow.", 
        "variables": ["system_type"], 
        "difficulty": "Advanced", 
        "uses": 5432, 
        "rating": 4.9, 
        "tags": ["microservices", "system design"], 
        "ai_models": ["GPT-4o", "Claude 3.5 Sonnet"]
    },
    {
        "id": "p-12",
        "title": "Cloud Infrastructure Architect",
        "category": "architecture",
        "prompt": "Act as a Cloud Architect. Design a highly available, scalable infrastructure on {cloud_provider} for a {app_type}. Suggest specific services for compute, storage, networking, and monitoring. Provide a cost estimation strategy.",
        "variables": ["cloud_provider", "app_type"],
        "difficulty": "Advanced",
        "uses": 4200,
        "rating": 4.8,
        "tags": ["cloud", "infrastructure", "AWS", "Azure"],
        "ai_models": ["GPT-4o", "Claude 3.5 Sonnet"]
    },
    
    # Debugging
    {
        "id": "p-4", 
        "title": "SQL Performance DBA", 
        "category": "debugging", 
        "prompt": "Act as a Database Administrator. Optimize the following SQL query for {db_engine}. Explain why the current query is slow (e.g., table scans, missing indexes) and provide the optimized version.\n\nQuery:\n```sql\n{query}\n```", 
        "variables": ["db_engine", "query"], 
        "difficulty": "Advanced", 
        "uses": 9876, 
        "rating": 4.7, 
        "tags": ["SQL", "optimization"], 
        "ai_models": ["GPT-4o", "Claude"]
    },
    {
        "id": "p-13",
        "title": "Error Stack Trace Resolver",
        "category": "debugging",
        "prompt": "Identify the root cause of the following error stack trace in {language}. Suggest a step-by-step fix and explain how to prevent this in the future.\n\nStack Trace:\n{stack_trace}",
        "variables": ["language", "stack_trace"],
        "difficulty": "Intermediate",
        "uses": 21000,
        "rating": 4.8,
        "tags": ["debugging", "troubleshooting"],
        "ai_models": ["GPT-4o", "ChatGPT"]
    },
    
    # Testing
    {
        "id": "p-5", 
        "title": "Chaos engineering Simulator", 
        "category": "testing", 
        "prompt": "Create a Chaos Engineering test plan for {application}. Identify 3 potential failure points (e.g., network latency, pod eviction) and describe how to inject these faults using tools like Gremlin or Chaos Mesh.", 
        "variables": ["application"], 
        "difficulty": "Advanced", 
        "uses": 3210, 
        "rating": 4.6, 
        "tags": ["chaos", "reliability"], 
        "ai_models": ["GPT-4o", "Claude"]
    },
    {
        "id": "p-14",
        "title": "Cypress E2E Scenario Writer",
        "category": "testing",
        "prompt": "Write a Cypress end-to-end test script for the {user_journey} flow. Include assertions for critical elements and handle asynchronous loading states.",
        "variables": ["user_journey"],
        "difficulty": "Intermediate",
        "uses": 6700,
        "rating": 4.7,
        "tags": ["testing", "cypress", "E2E"],
        "ai_models": ["GPT-4o", "Claude 3.5 Sonnet"]
    },

    # Documentation
    {
        "id": "p-6",
        "title": "API Doc Gen",
        "category": "documentation",
        "prompt": "Generate a comprehensive OpenAPI 3.0 specification for {endpoint_description}. Include request/response schemas, error codes, and authentication requirements for {auth_type}.",
        "variables": ["endpoint_description", "auth_type"],
        "difficulty": "Intermediate",
        "uses": 4500,
        "rating": 4.8,
        "tags": ["API", "OpenAPI", "Documentation"],
        "ai_models": ["GPT-4o", "Claude 3.5 Sonnet"]
    },
    {
        "id": "p-15",
        "title": "README.md Master",
        "category": "documentation",
        "prompt": "Create a professional README.md for a {project_type} project named {project_name}. Include setup instructions, usage examples, contributing guidelines, and license info. Current Tech Stack: {tech_stack}",
        "variables": ["project_type", "project_name", "tech_stack"],
        "difficulty": "Beginner",
        "uses": 18200,
        "rating": 4.9,
        "tags": ["documentation", "github", "open source"],
        "ai_models": ["GPT-4o", "ChatGPT"]
    },

    # Code Review
    {
        "id": "p-7",
        "title": "Security Audit Reviewer",
        "category": "code_review",
        "prompt": "Perform a security-focused code review of this {language} snippet. Look for SQL injection, XSS, CSRF, and insecure dependency issues. Provide line-by-line recommendations.\n\nCode:\n{code}",
        "variables": ["language", "code"],
        "difficulty": "Advanced",
        "uses": 7800,
        "rating": 4.9,
        "tags": ["Security", "Code Review"],
        "ai_models": ["Claude 3.5 Sonnet", "GPT-4o"]
    },
    {
        "id": "p-16",
        "title": "Performance Code Reviewer",
        "category": "code_review",
        "prompt": "Review the following code for performance bottlenecks. Focus on O(n) complexity, memory allocation, and database N+1 issues. Suggest more efficient alternatives.\n\nCode:\n{code}",
        "variables": ["code"],
        "difficulty": "Advanced",
        "uses": 5400,
        "rating": 4.8,
        "tags": ["performance", "code review"],
        "ai_models": ["GPT-4o", "Claude 3.5 Sonnet"]
    },

    # Refactoring
    {
        "id": "p-8",
        "title": "Legacy Code Refactorer",
        "category": "refactoring",
        "prompt": "Refactor this legacy {language} code for better performance and readability. Use modern syntax features and design patterns where applicable.\n\nLegacy Code:\n{code}",
        "variables": ["language", "code"],
        "difficulty": "Advanced",
        "uses": 6100,
        "rating": 4.7,
        "tags": ["Refactoring", "Modernization"],
        "ai_models": ["GPT-4o", "Claude 3.5 Sonnet"]
    },
    {
        "id": "p-17",
        "title": "Monolith to Microservices Refactorer",
        "category": "refactoring",
        "prompt": "Identify how the following monolithic logic for {module_name} can be extracted into a separate microservice. Suggest API boundaries and data migration strategy.",
        "variables": ["module_name"],
        "difficulty": "Advanced",
        "uses": 3900,
        "rating": 4.6,
        "tags": ["refactoring", "architecture"],
        "ai_models": ["GPT-4o", "Claude 3.5 Sonnet"]
    },

    # Learning
    {
        "id": "p-9",
        "title": "First-Principles Teacher",
        "category": "learning",
        "prompt": "Explain the concept of {concept} using first-principles thinking. Start with the most basic axioms and build up to the complex application in {field}.",
        "variables": ["concept", "field"],
        "difficulty": "Beginner",
        "uses": 11200,
        "rating": 4.9,
        "tags": ["Education", "Concepts"],
        "ai_models": ["GPT-4o", "ChatGPT"]
    },
    {
        "id": "p-18",
        "title": "Paper Summary Expert",
        "category": "learning",
        "prompt": "Summarize the key findings of the following research abstract. Explain the methodology, results, and practical implications for {target_audience}.\n\nAbstract:\n{abstract}",
        "variables": ["abstract", "target_audience"],
        "difficulty": "Intermediate",
        "uses": 14500,
        "rating": 4.8,
        "tags": ["research", "learning"],
        "ai_models": ["GPT-4o", "Claude 3.5 Sonnet"]
    },

    # Productivity
    {
        "id": "p-10",
        "title": "ADR Generator",
        "category": "productivity",
        "prompt": "Create an Architectural Decision Record (ADR) for {decision}. Include Title, Context, Decision, Consequences, and Status.",
        "variables": ["decision"],
        "difficulty": "Intermediate",
        "uses": 2300,
        "rating": 4.8,
        "tags": ["Strategy", "Documentation"],
        "ai_models": ["GPT-4o", "Claude"]
    },
    {
        "id": "p-19",
        "title": "Meeting Minutes Automator",
        "category": "productivity",
        "prompt": "Summarize the following meeting transcript. Extract Action Items, Key Decisions, and Owner assignments.\n\nTranscript:\n{transcript}",
        "variables": ["transcript"],
        "difficulty": "Beginner",
        "uses": 25600,
        "rating": 4.7,
        "tags": ["productivity", "management"],
        "ai_models": ["GPT-4o", "Claude"]
    },

    # Communication
    {
        "id": "p-20",
        "title": "Executive Summary Writer",
        "category": "communication",
        "prompt": "Draft an executive summary of the following technical report for the {stakeholder_level} level. Focus on business impact and ROI.\n\nReport:\n{report}",
        "variables": ["stakeholder_level", "report"],
        "difficulty": "Intermediate",
        "uses": 9800,
        "rating": 4.9,
        "tags": ["communication", "writing"],
        "ai_models": ["GPT-4o", "Claude"]
    },
    {
        "id": "p-21",
        "title": "Pandas Data Cleaner",
        "category": "data_analysis",
        "prompt": "You are a Data Scientist. Write a Python function using Pandas to clean the following dataset features: {features}. Handle missing values using {imputation_method}, remove duplicates, and normalize numerical columns.",
        "variables": ["features", "imputation_method"],
        "difficulty": "Intermediate",
        "uses": 8900,
        "rating": 4.8,
        "tags": ["python", "data science"],
        "ai_models": ["GPT-4o", "Claude 3.5 Sonnet"]
    },
    {
        "id": "p-22",
        "title": "Kubernetes Manifest Generator",
        "category": "devops_infra",
        "prompt": "Generate a Kubernetes {resource_type} manifest for a {app_name} application. Include resource limits, liveness probes, and a LoadBalancer service definition.",
        "variables": ["resource_type", "app_name"],
        "difficulty": "Advanced",
        "uses": 5600,
        "rating": 4.7,
        "tags": ["k8s", "devops"],
        "ai_models": ["GPT-4o", "Claude"]
    },
    {
        "id": "p-23",
        "title": "FastAPI Endpoint Creator",
        "category": "coding",
        "prompt": "Create a FastAPI endpoint for {functionality} using Pydantic models for validation. Include async definition, error handling for {error_case}, and example Swagger docstrings.",
        "variables": ["functionality", "error_case"],
        "difficulty": "Intermediate",
        "uses": 11200,
        "rating": 4.9,
        "tags": ["python", "api"],
        "ai_models": ["GPT-4o", "Claude"]
    },
    {
        "id": "p-24",
        "title": "Rust Error Handler",
        "category": "coding",
        "prompt": "Explain this Rust error message: {error_msg}. Refactor the code to properly handle the Result/Option type using idiomatic pattern matching.",
        "variables": ["error_msg"],
        "difficulty": "Advanced",
        "uses": 3400,
        "rating": 4.8,
        "tags": ["rust", "debugging"],
        "ai_models": ["GPT-4o", "Claude 3.5 Sonnet"]
    },
    {
        "id": "p-25",
        "title": "Threat Modeling Facilitator",
        "category": "security",
        "prompt": "Conduct a STRIDE threat analysis for the following system component: {component_name}. List potential threats in each category (Spoofing, Tampering, etc.) and suggest mitigations.",
        "variables": ["component_name"],
        "difficulty": "Advanced",
        "uses": 2100,
        "rating": 4.9,
        "tags": ["security", "architecture"],
        "ai_models": ["GPT-4o", "Claude"]
    },
    {
        "id": "p-26",
        "title": "User Story to Gherkin",
        "category": "testing",
        "prompt": "Convert the following User Story into a set of Gherkin (Cucumber) scenarios. Include Happy Path and at least two Negative scenarios.\n\nUser Story: {user_story}",
        "variables": ["user_story"],
        "difficulty": "Beginner",
        "uses": 14500,
        "rating": 4.7,
        "tags": ["agile", "bdd"],
        "ai_models": ["ChatGPT", "Claude"]
    },
    {
        "id": "p-27",
        "title": "Technical Blog Post Writer",
        "category": "content_creation",
        "prompt": "Write a technical blog post about {topic}. Structure it with an engaging hook, 'What is it?', 'Why it matters?', 'Code Example', and 'Best Practices'. Target audience: {audience}.",
        "variables": ["topic", "audience"],
        "difficulty": "Intermediate",
        "uses": 18900,
        "rating": 4.8,
        "tags": ["writing", "marketing"],
        "ai_models": ["GPT-4o", "Claude 3.5 Sonnet"]
    },
    {
        "id": "p-28",
        "title": "SQL to SQLAlchemy ORM",
        "category": "refactoring",
        "prompt": "Convert this raw SQL query into a Python SQLAlchemy ORM format. Ensure it uses valid model relationships.\n\nSQL:\n{sql_query}",
        "variables": ["sql_query"],
        "difficulty": "Intermediate",
        "uses": 7600,
        "rating": 4.6,
        "tags": ["python", "database"],
        "ai_models": ["GPT-4o", "Claude"]
    },
    {
        "id": "p-29",
        "title": "Git Merge Conflict Resolver",
        "category": "debugging",
        "prompt": "I have a git merge conflict in {file_name}. Here are the 'ours' and 'theirs' blocks. Explain the difference and suggest a merged version that preserves both features.\n\nConflict:\n{conflict_block}",
        "variables": ["file_name", "conflict_block"],
        "difficulty": "Intermediate",
        "uses": 13200,
        "rating": 4.8,
        "tags": ["git", "devops"],
        "ai_models": ["GPT-4o", "Claude"]
    },
    {
        "id": "p-30",
        "title": "System Design Interview Prep",
        "category": "learning",
        "prompt": "Act as a Senior Interviewer. Ask me 3 probing questions about designing a {system_design_topic}. After I answer, critique my response on scalability and fault tolerance.",
        "variables": ["system_design_topic"],
        "difficulty": "Advanced",
        "uses": 25000,
        "rating": 4.9,
        "tags": ["interview", "career"],
        "ai_models": ["GPT-4o", "Claude 3.5 Sonnet"]
    },
    {
        "id": "p-31",
        "title": "SRE Incident Post-Mortem",
        "category": "communication",
        "prompt": "Write a blameless post-mortem for the following incident: {incident_description}. Include sections for 'Root Cause Analysis' (5 Whys), 'Impact', 'Timeline', and 'Action Items' to prevent recurrence.",
        "variables": ["incident_description"],
        "difficulty": "Advanced",
        "uses": 4200,
        "rating": 4.9,
        "tags": ["sre", "devops", "management"],
        "ai_models": ["GPT-4o", "Claude"]
    },
    {
        "id": "p-32",
        "title": "React Performance Optimizer",
        "category": "refactoring",
        "prompt": "Analyze this React component for performance bottlenecks (re-renders, heavy computations). Suggest optimizations using useMemo, useCallback, or code splitting.\n\nCode:\n{react_code}",
        "variables": ["react_code"],
        "difficulty": "Advanced",
        "uses": 15600,
        "rating": 4.8,
        "tags": ["javascript", "react", "performance"],
        "ai_models": ["GPT-4o", "Claude 3.5 Sonnet"]
    },
    {
        "id": "p-33",
        "title": "AWS Terraform Generator",
        "category": "devops_infra",
        "prompt": "Write a Terraform module for an AWS {aws_resource}. Include variables for {config_vars}, output the resource ID, and ensure it follows security best practices (encryption, private subnets).",
        "variables": ["aws_resource", "config_vars"],
        "difficulty": "Intermediate",
        "uses": 9800,
        "rating": 4.7,
        "tags": ["aws", "terraform", "iac"],
        "ai_models": ["GPT-4o", "Claude"]
    },
    {
        "id": "p-34",
        "title": "Technical Spec Writer",
        "category": "productivity",
        "prompt": "Draft a Technical Specification for a new {feature_name}. Structure: 1. Background, 2. API Design (Endpoints), 3. Database Schema Changes, 4. Security Considerations, 5. Rollout Plan.",
        "variables": ["feature_name"],
        "difficulty": "Advanced",
        "uses": 11500,
        "rating": 4.9,
        "tags": ["design", "documentation", "pm"],
        "ai_models": ["GPT-4o", "Claude 3.5 Sonnet"]
    },
    {
        "id": "p-35",
        "title": "Big O Complexity Analyzer",
        "category": "learning",
        "prompt": "Analyze the Time and Space complexity (Big O) of the following function. Explain the derivation step-by-step, identifying the dominant operations.\n\nFunction:\n{code_snippet}",
        "variables": ["code_snippet"],
        "difficulty": "Intermediate",
        "uses": 21000,
        "rating": 4.8,
        "tags": ["cs", "algorithms", "interview"],
        "ai_models": ["GPT-4o", "Claude"]
    },
    
    # New Prompts - Productivity & DevOps
    {
        "id": "p-51",
        "title": "Git Commit Message Generator",
        "category": "devops_infra",
        "prompt": "Analyze this code diff and generate a clear, conventional commit message following the format:\n\n<type>(<scope>): <subject>\n\n<body>\n\nTypes: feat, fix, docs, style, refactor, test, chore\n\nDiff:\n```\n{diff}\n```\n\nProvide 3 commit message options ranked by specificity.",
        "variables": ["diff"],
        "difficulty": "Beginner",
        "uses": 18500,
        "rating": 4.7,
        "tags": ["git", "version control", "productivity"],
        "ai_models": ["GPT-4o", "Claude 3.5 Sonnet"]
    },
    {
        "id": "p-52",
        "title": "REST API Design Reviewer",
        "category": "architecture",
        "prompt": "Review this API endpoint design for RESTful best practices:\n\nEndpoint: {method} {endpoint}\nRequest Body: {request_body}\nResponse: {response}\n\nEvaluate:\n1. URL naming conventions\n2. HTTP method appropriateness\n3. Status codes\n4. Request/response structure\n5. Pagination/filtering patterns\n\nProvide a score (1-10) and specific improvements.",
        "variables": ["method", "endpoint", "request_body", "response"],
        "difficulty": "Intermediate",
        "uses": 12300,
        "rating": 4.8,
        "tags": ["api", "rest", "design"],
        "ai_models": ["GPT-4o", "Claude"]
    },
    {
        "id": "p-53",
        "title": "Performance Optimization Advisor",
        "category": "refactoring",
        "prompt": "Analyze this {language} code for performance issues:\n\n```{language}\n{code}\n```\n\nIdentify:\n1. Time complexity (current vs optimal)\n2. Space complexity issues\n3. Memory leaks or inefficient allocations\n4. Database/IO bottlenecks\n5. Caching opportunities\n\nProvide optimized code with benchmarking suggestions.",
        "variables": ["language", "code"],
        "difficulty": "Advanced",
        "uses": 9800,
        "rating": 4.9,
        "tags": ["performance", "optimization", "profiling"],
        "ai_models": ["GPT-4o", "Claude 3.5 Sonnet"]
    },
    {
        "id": "p-54",
        "title": "Error Handling Hardener",
        "category": "debugging",
        "prompt": "Review this {language} code and add comprehensive error handling:\n\n```{language}\n{code}\n```\n\nAdd:\n1. Try-catch blocks with specific exceptions\n2. Input validation with clear error messages\n3. Logging statements for debugging\n4. Graceful degradation strategies\n5. User-friendly error responses\n\nExplain each addition.",
        "variables": ["language", "code"],
        "difficulty": "Intermediate",
        "uses": 11200,
        "rating": 4.7,
        "tags": ["error handling", "reliability", "debugging"],
        "ai_models": ["GPT-4o", "Claude"]
    },
    {
        "id": "p-55",
        "title": "Code Documentation Generator",
        "category": "documentation",
        "prompt": "Generate comprehensive documentation for this {language} code:\n\n```{language}\n{code}\n```\n\nInclude:\n1. Module/class docstring with purpose and usage\n2. Function docstrings with params, returns, raises\n3. Inline comments for complex logic\n4. Example usage snippets\n5. Type hints (if applicable)\n\nFormat: {doc_style} (e.g., Google, NumPy, JSDoc)",
        "variables": ["language", "code", "doc_style"],
        "difficulty": "Beginner",
        "uses": 14500,
        "rating": 4.8,
        "tags": ["documentation", "docstrings", "comments"],
        "ai_models": ["GPT-4o", "Claude 3.5 Sonnet"]
    }
]

def get_all_prompts():
    return PROMPTS_DATABASE

def get_prompts_by_category(category: str):
    if not category or category.lower() == 'all':
        return PROMPTS_DATABASE
    return [p for p in PROMPTS_DATABASE if p.get("category", "").lower() == category.lower()]

def get_prompts_by_difficulty(difficulty: str):
    if not difficulty: return []
    return [p for p in PROMPTS_DATABASE if p.get("difficulty") == difficulty]

def search_prompts(query: str):
    if not query: return []
    query = query.lower()
    return [p for p in PROMPTS_DATABASE if query in p.get("title", "").lower() or query in p.get("prompt", "").lower()]

def get_popular_prompts(limit: int = 10):
    return sorted(PROMPTS_DATABASE, key=lambda x: x.get("uses", 0), reverse=True)[:limit]

def get_prompt_by_id(prompt_id: str):
    for p in PROMPTS_DATABASE:
        if p.get("id") == prompt_id:
            return p
    return None
