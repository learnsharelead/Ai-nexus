"""
AI Nexus - Comprehensive Tutorial Content Database
Production-ready tutorials with detailed, actionable content
"""

TUTORIAL_CONTENT = {
    "qw-1": {
        "title": "Production RAG in 10 Minutes",
        "sections": [
            {
                "title": "The RAG Blueprint",
                "content": """
Retrieval Augmented Generation (RAG) is the industry standard for grounding LLMs in your private data. This quick win walks you through the minimal production stack.

### The Stack
- **Vector DB:** Pinecone (Serverless)
- **Framework:** LangChain or LlamaIndex
- **Embedding Model:** text-embedding-3-small (OpenAI)
- **LLM:** GPT-4o-mini

### Core Implementation
```python
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_pinecone import PineconeVectorStore

# 1. Initialize
embeddings = OpenAIEmbeddings()
index_name = "nexus-docs"

# 2. Connect to Vector Store
vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)

# 3. Create Retrieval Chain
from langchain.chains import RetrievalQA
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4o-mini"),
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# 4. Query
response = qa_chain.invoke("How do I implement RAG?")
print(response["result"])
```

**Why this works:** It moves the complexity to the 'Retriever' layer, allowing the LLM to focus purely on synthesis.
                """
            }
        ],
        "quiz": [
            {
                "question": "What is the primary purpose of the Vector Database in RAG?",
                "options": ["Generate text", "Store and retrieve relevant context", "Fine-tune the model", "Compress data"],
                "correct": 1,
                "explanation": "Vector DBs store high-dimensional embeddings of your data, allowing for semantically similar context retrieval."
            }
        ]
    },
    
    "qw-2": {
        "title": "LLM Observability with LangSmith",
        "sections": [
            {
                "title": "Why Observability Matters",
                "content": """
Debugging LLM chains is hard because they are non-deterministic. LangSmith provides the "X-ray" for your AI applications.

### Setup
1. Create a LangSmith account at [smith.langchain.com](https://smith.langchain.com)
2. Export your API Key: `export LANGCHAIN_TRACING_V2=true`

### Key Features
- **Tracing:** See every step of your chain, including latencies and tokens used.
- **Feedback Loops:** Collect user 'thumbs up/down' directly into your datasets.
- **Unit Testing:** Run your chains against a fixed dataset of inputs/outputs.

### Code Example
```python
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Everything you run now will automatically show up in the LangSmith dashboard.
# No code changes required!
```
                """
            }
        ],
        "quiz": [
            {
                "question": "What environment variable enables LangChain tracing?",
                "options": ["DEBUG=TRUE", "LANGCHAIN_TRACING_V2=true", "AI_LOG_ENABLE=1", "LLM_WATCH=true"],
                "correct": 1,
                "explanation": "LANGCHAIN_TRACING_V2 is the official flag to pipe telemetry to the LangSmith platform."
            }
        ]
    },

    "qw-3": {
        "title": "Local LLMs with Ollama",
        "sections": [
            {
                "title": "Privacy-First AI",
                "content": """
Ollama allows you to run powerful models like Llama 3, Mistral, and Phi-3 locally on your laptop without an internet connection.

### Installation
- **macOS/Windows:** Download from [ollama.com](https://ollama.com)
- **Linux:** `curl -fsSL https://ollama.com/install.sh | sh`

### Usage
```bash
# Pull and run a model
ollama run llama3

# Run as a local API
ollama serve
```

### Python Integration
```python
import requests

response = requests.post('http://localhost:11434/api/generate', 
    json={"model": "llama3", "prompt": "Why is the sky blue?"})
print(response.json()['response'])
```
                """
            }
        ],
        "quiz": [
            {
                "question": "Which command downloads and starts an LLM in Ollama?",
                "options": ["ollama start", "ollama pull", "ollama run", "ollama launch"],
                "correct": 2,
                "explanation": "'ollama run' handles both downloading (if missing) and serving the model interactive prompt."
            }
        ]
    },

    "dd-1": {
        "title": "Architecting AI Agents",
        "sections": [
            {
                "title": "From Chains to Agents",
                "content": """
An agent is an LLM that uses reasoning to decide which actions (tools) to take to solve a problem.

### The ReAct Pattern
**Reason + Act.** The agent thinks about the state, decides on an action, observes the result, and repeats.

### Implementation with CrewAI
```python
from crewai import Agent, Task, Crew

# 1. Define Agent
researcher = Agent(
    role='Senior Researcher',
    goal='Uncover groundbreaking AI trends',
    backstory='You are a tech journalist at a top tier outlet.',
    tools=[search_tool],
    verbose=True
)

# 2. Define Task
task1 = Task(description='Search for GPT-5 rumors', agent=researcher)

# 3. Assemble Crew
crew = Crew(agents=[researcher], tasks=[task1])
result = crew.kickoff()
```
                """
            }
        ],
        "quiz": [
            {
                "question": "What does the 'Re' in ReAct stand for?",
                "options": ["Response", "Reasoning", "Retrieval", "Relational"],
                "correct": 1,
                "explanation": "ReAct stands for Reasoning and Acting, where the model verbalizes its reasoning before performing an action."
            }
        ]
    },

    "mt-1": {
        "title": "AI Engineering Mastery Track",
        "sections": [
            {
                "title": "Curriculum Overview",
                "content": """
This 20-hour track transforms you into a professional AI Engineer.

**Module 1: Advanced Prompting (4 Hours)**
- Meta-prompting
- Programmatic prompt generation
- Evaluation frameworks (Ragas, DeepEval)

**Module 2: RAG Architecture (6 Hours)**
- Hybrid search (Vector + Keyword)
- Multi-vector retrieval
- Lost-in-the-Middle mitigation

**Module 3: Deployment & MLOps (6 Hours)**
- Serving with vLLM and TGI
- Quantization (GGUF, AWQ, FP8)
- Autoscaling GPU clusters

**Module 4: Final Project (4 Hours)**
- Build and deploy a multi-agent system from scratch.
                """
            }
        ],
        "quiz": [
            {
                "question": "What is 'Quantization' in the context of LLMs?",
                "options": ["Adding more data", "Reducing the precision of weights to save memory", "Increasing the number of layers", "Translating code to Python"],
                "correct": 1,
                "explanation": "Quantization compresses models by using lower-precision data types (like 4-bit) for weights, allowing large models to run on smaller GPUs."
            }
        ]
    },

    "qw-4": {
        "title": "AI Unit Testing with Codium",
        "sections": [
            {
                "title": "Automated Test Generation",
                "content": """
CodiumAI analyzes your code behavior to generate meaningful tests, not just coverage fillers.

### How it works
1. **Analysis:** Codium scans your function logic and docstrings.
2. **Plan:** It proposes a test plan covering happy paths and edge cases.
3. **Generate:** It writes the test code in your preferred framework (Pytest/Jest).

### Example
For a `calculate_discount(price, user_tier)` function, Codium automatically suggests:
- `test_negative_price` (Edge Case)
- `test_vip_tier_max_discount` (Behavior)
- `test_invalid_tier_string` (Error Handling)
                """
            }
        ],
        "quiz": [
            {
                "question": "What distinguishes CodiumAI from standard autocomplete?",
                "options": ["It runs faster", "It analyzes behavior to suggest edge cases", "It only supports Python", "It is open source"],
                "correct": 1,
                "explanation": "Codium focuses on behavioral analysis to identify edge cases you might have missed, rather than just completing syntax."
            }
        ]
    },

    "qw-5": {
        "title": "Streamlining PRs with AI",
        "sections": [
            {
                "title": "The Perfect PR Description",
                "content": """
Stop writing "Fixed bugs" in your PRs. Use AI to scan your diffs and generate context-aware summaries.

### Tools
- **PR Agent:** Open source tool that connects to GitHub/GitLab.
- **GitHub Copilot Enterprise:** "Summarize this PR" feature.

### Structure of an AI-Generated PR
1. **Summary:** High-level intent.
2. **Walkthrough:** File-by-file breakdown of changes.
3. **Impact:** Potential risks or breaking changes.
                """
            }
        ],
        "quiz": [
            {
                "question": "What is a key benefit of AI-generated PR descriptions?",
                "options": ["They are always perfect", "They save time and ensure consistency", "They replace code review", "They deploy the code"],
                "correct": 1,
                "explanation": "AI ensures that every PR has a baseline of detailed documentation, saving developer time and helping reviewers understand the context."
            }
        ]
    },

    "dd-2": {
        "title": "Fine-Tuning Llama 3 for Logic",
        "sections": [
            {
                "title": "When to Fine-Tune?",
                "content": """
Don't fine-tune for knowledge; fine-tune for **behavior** and **format**.

### The LoRA Approach
Low-Rank Adaptation (LoRA) freezes the main model weights and trains a small adapter layer. This reduces VRAM requirements by 90%.

### Training Data Format (Alpaca)
```json
{
  "instruction": "Convert natural language to SQL.",
  "input": "Show me top users by spend.",
  "output": "SELECT user_id, SUM(amount) FROM orders GROUP BY user_id ORDER BY 2 DESC;"
}
```
                """
            }
        ],
        "quiz": [
            {
                "question": "What is the main advantage of LoRA fine-tuning?",
                "options": ["It makes the model larger", "It requires significantly less VRAM", "It removes the need for data", "It is faster at inference"],
                "correct": 1,
                "explanation": "LoRA trains only a tiny fraction of parameters (adapters), allowing you to fine-tune 70B parameter models on consumer hardware."
            }
        ]
    },

    "dd-3": {
        "title": "Vector Database Selection Guide",
        "sections": [
            {
                "title": "Comparing the Giants",
                "content": """
Choosing the right Vector DB is critical for RAG performance / cost.

### 1. Pinecone
- **Pros:** Fully managed, serverless, easy to scale.
- **Cons:** Closed source, data leaves your VPC (unless Enterprise).

### 2. Milvus / Zilliz
- **Pros:** Open source, highly scalable, rich features.
- **Cons:** Complex to manage self-hosted.

### 3. Weaviate
- **Pros:** Hybrid search out-of-the-box, module ecosystem.
- **Cons:** Steeper learning curve for GraphQL API.

### 4. Chroma
- **Pros:** Dead simple, runs locally/in-memory, open source.
- **Cons:** Less proven at massive scale.
                """
            }
        ],
        "quiz": [
            {
                "question": "Which Vector DB is best known for its easy-to-use Serverless mode?",
                "options": ["Milvus", "Pinecone", "Chroma", "Postgres"],
                "correct": 1,
                "explanation": "Pinecone pioneered the serverless vector database model, separating compute from storage for easy scaling."
            }
        ]
    },

    "dd-4": {
        "title": "AI Security & Guardrails",
        "sections": [
            {
                "title": "Protecting Your GenAI App",
                "content": """
LLMs are vulnerable to Prompt Injection and Jailbreaks. You need a firewall for your prompts.

### NeMo Guardrails (NVIDIA)
Define programmable rails using Colang.
```colang
define user ask about politics
  "Who should I vote for?"
  "What do you think of the president?"

define flow politics
  user ask about politics
  bot refuse to answer
```

### LLM Guard
An open-source library to scan inputs for toxicity, PII, and injections before they reach the model.
                """
            }
        ],
        "quiz": [
            {
                "question": "What is Prompt Injection?",
                "options": ["Adding context to a prompt", "Malicious input designed to override system instructions", "Fine-tuning a model", "Injecting data into a Vector DB"],
                "correct": 1,
                "explanation": "Prompt Injection occurs when a user input tricks the LLM into ignoring its developer-set constraints."
            }
        ]
    },

    "dd-5": {
        "title": "Advanced Prompt Engineering",
        "sections": [
            {
                "title": "Chain-of-Thought (CoT)",
                "content": """
Instead of asking for the answer, ask for the reasoning.

**Standard:** "Is 11 prime?"
**CoT:** "Think step by step. check if 11 is divisible by any number from 2 to sqrt(11). If no divisors found, it is prime."

### Self-Consistency
Generate 5 CoT reasoning paths and pick the answer that appears most often (majority vote). This dramatically increases accuracy on math/logic tasks.
                """
            }
        ],
        "quiz": [
            {
                "question": "How does Self-Consistency improve performance?",
                "options": ["It makes the model faster", "It uses majority voting across multiple reasoning paths", "It reduces token usage", "It fine-tunes the model"],
                "correct": 1,
                "explanation": "Self-Consistency generates multiple diverse reasoning chains and selects the final answer that is most consistent across them."
            }
        ]
    },

    "mt-2": {
        "title": "AI Product Management",
        "sections": [
            {
                "title": "Managing Probability",
                "content": """
AI PMs manage **probabilistic products**. Acceptance criteria are no longer binary (Pass/Fail) but statistical (Passes 90% of the time).

### Key Metrics
- **Pass@k:** Probability that at least one of top k outputs is correct.
- **Hallucination Rate:** Percentage of non-factual outputs.
- **Latency/Cost per Token:** Business viability constraints.

### The Evaluation Stack
You need a 'Golden Dataset' of Q&A pairs to run regression tests against every prompt change.
                """
            }
        ],
        "quiz": [
            {
                "question": "What is the biggest shift for PMs moving to AI products?",
                "options": ["Writing code", "Managing probabilistic vs deterministic outcomes", "Designing UI", "Hiring people"],
                "correct": 1,
                "explanation": "Traditional software is deterministic (Input A -> Output B). AI is probabilistic, requiring tolerance thresholds and statistical evaluation."
            }
        ]
    },

    "mt-3": {
        "title": "MLOps Professional",
        "sections": [
            {
                "title": "The MLOps Loop",
                "content": """
Code -> Data -> Train -> Evaluate -> Deploy -> Monitor -> Repeat.

### Feature Stores (Feast)
Serve consistent features to training and inference.

### Experiment Tracking (MLflow / Weights & Biases)
Log every hyperparameter configuration to reproduce results.

### Model Registry
Version control for your binary model artifacts. "Deploy v3.2.1 to production".
                """
            }
        ],
        "quiz": [
            {
                "question": "What is the purpose of a Feature Store?",
                "options": ["Store model weights", "Ensure consistency of input data between training and inference", "Track experiments", "Monitor costs"],
                "correct": 1,
                "explanation": "Feature Stores resolve 'training-serving skew' by ensuring the model sees exactly the same data definitions in production as it did during training."
            }
        ]
    },
    
    # Quick Wins Content (qw-6 to qw-10)
    "qw-6": {
        "title": "5 ChatGPT Prompts Every Developer Needs",
        "sections": [
            {
                "title": "Essential Developer Prompts",
                "content": """
These 5 prompts will transform your daily development workflow.

### 1. Code Explainer
```
Explain this code in simple terms, including what each part does:
[paste your code]
```

**Use Case:** Understanding legacy code or complex algorithms.

### 2. Bug Detective
```
I'm getting this error: [error message]
Here's my code: [code]
What's causing this and how do I fix it?
```

**Pro Tip:** Include the full stack trace for better results.

### 3. Code Optimizer
```
Review this code for performance issues and suggest optimizations:
[code]
Focus on: [time complexity / memory usage / readability]
```

### 4. Test Generator
```
Generate comprehensive unit tests for this function:
[function code]
Include edge cases and error scenarios.
```

### 5. Documentation Writer
```
Write clear documentation for this code including:
- Purpose and usage
- Parameters and return values
- Examples
[code]
```

**Time Saved:** ~2 hours per day using these prompts effectively.
                """
            }
        ],
        "quiz": [
            {
                "question": "What should you include when asking ChatGPT to debug code?",
                "options": ["Just the error message", "Full stack trace and relevant code", "Only the function name", "The entire codebase"],
                "correct": 1,
                "explanation": "Including both the full stack trace and relevant code gives ChatGPT the context needed to identify the root cause and suggest accurate fixes."
            }
        ]
    },

    "qw-7": {
        "title": "AI-Powered Regex Builder",
        "sections": [
            {
                "title": "Never Write Regex Again",
                "content": """
Let AI handle the complexity of regular expressions.

### The Prompt Template
```
Create a regex pattern that:
[describe what you want to match]

Test it against these examples:
Valid: [examples that should match]
Invalid: [examples that should NOT match]
```

### Real Examples

**Email Validation:**
```
Create a regex for validating email addresses.
Valid: user@example.com, john.doe@company.co.uk
Invalid: @example.com, user@, user@.com
```

**Result:**
```python
import re
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
```

**Extract Phone Numbers:**
```
Extract US phone numbers in formats:
(123) 456-7890
123-456-7890
123.456.7890
```

**Password Strength:**
```
Regex for password with:
- At least 8 characters
- One uppercase, one lowercase
- One digit, one special character
```

### Advanced: Explanation Request
```
Explain this regex pattern step by step:
^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$
```

AI will break down each component with clear explanations.
                """
            }
        ],
        "quiz": [
            {
                "question": "What's the best way to use AI for regex creation?",
                "options": ["Just ask for a pattern", "Provide examples of valid and invalid matches", "Copy from Stack Overflow", "Use trial and error"],
                "correct": 1,
                "explanation": "Providing concrete examples of what should and shouldn't match helps AI generate accurate regex patterns that meet your specific needs."
            }
        ]
    },

    "qw-8": {
        "title": "Auto-Generate Unit Tests with AI",
        "sections": [
            {
                "title": "Instant Test Coverage",
                "content": """
Generate comprehensive test suites in seconds.

### The Prompt Formula
```
Generate unit tests for this [language] function:
[paste function]

Include tests for:
1. Happy path scenarios
2. Edge cases
3. Error handling
4. Boundary conditions

Use [testing framework: pytest/jest/junit]
```

### Example: Python Function
```python
def calculate_discount(price, user_tier):
    if price < 0:
        raise ValueError("Price cannot be negative")
    
    discounts = {"bronze": 0.05, "silver": 0.10, "gold": 0.15}
    discount = discounts.get(user_tier, 0)
    return price * (1 - discount)
```

### AI-Generated Tests
```python
import pytest

def test_calculate_discount_bronze():
    assert calculate_discount(100, "bronze") == 95.0

def test_calculate_discount_silver():
    assert calculate_discount(100, "silver") == 90.0

def test_calculate_discount_gold():
    assert calculate_discount(100, "gold") == 85.0

def test_calculate_discount_invalid_tier():
    assert calculate_discount(100, "platinum") == 100.0

def test_calculate_discount_negative_price():
    with pytest.raises(ValueError):
        calculate_discount(-10, "gold")

def test_calculate_discount_zero_price():
    assert calculate_discount(0, "gold") == 0.0

def test_calculate_discount_large_price():
    assert calculate_discount(10000, "gold") == 8500.0
```

### Advanced: Test Data Generation
```
Generate realistic test data for testing this API endpoint:
[endpoint details]
Include: valid requests, malformed requests, edge cases
```
                """
            }
        ],
        "quiz": [
            {
                "question": "What types of tests should AI-generated test suites include?",
                "options": ["Only happy path", "Happy path, edge cases, and error handling", "Just one test", "Random tests"],
                "correct": 1,
                "explanation": "Comprehensive test suites should cover happy paths, edge cases, error handling, and boundary conditions to ensure robust code quality."
            }
        ]
    },

    "qw-9": {
        "title": "Debug Faster with AI Explanations",
        "sections": [
            {
                "title": "AI-Powered Debugging",
                "content": """
Turn cryptic errors into clear solutions.

### The Debug Prompt Template
```
I'm getting this error:
[full error message and stack trace]

Here's the relevant code:
[code snippet]

Context:
- What I'm trying to do: [goal]
- What I expected: [expected behavior]
- What's happening: [actual behavior]

Please explain the error and suggest a fix.
```

### Real Example: Python Error
```
I'm getting this error:
TypeError: unsupported operand type(s) for +: 'int' and 'str'

Code:
def calculate_total(items):
    total = 0
    for item in items:
        total = total + item['price']
    return total

items = [{'price': '10'}, {'price': '20'}]
result = calculate_total(items)
```

### AI Response
```
The error occurs because item['price'] is a string ('10'), 
not an integer. Python can't add strings to integers.

Fix:
def calculate_total(items):
    total = 0
    for item in items:
        total = total + int(item['price'])  # Convert to int
    return total

Better approach with error handling:
def calculate_total(items):
    total = 0
    for item in items:
        try:
            total += int(item['price'])
        except (ValueError, KeyError) as e:
            print(f"Invalid price for item: {e}")
    return total
```

### Advanced Debugging Prompts

**Performance Issues:**
```
This function is slow with large datasets:
[code]
Profile it and suggest optimizations.
```

**Memory Leaks:**
```
My application's memory usage keeps growing:
[code]
Identify potential memory leaks.
```

**Race Conditions:**
```
I'm getting inconsistent results in concurrent execution:
[code]
Check for race conditions and suggest thread-safe alternatives.
```
                """
            }
        ],
        "quiz": [
            {
                "question": "What information should you provide when asking AI to debug code?",
                "options": ["Just the error message", "Error, code, and context about what you're trying to do", "Only the function name", "The entire project"],
                "correct": 1,
                "explanation": "Providing the error message, relevant code, and context about your goal helps AI understand the problem and provide accurate, targeted solutions."
            }
        ]
    },

    "qw-10": {
        "title": "AI for SQL Query Optimization",
        "sections": [
            {
                "title": "Optimize Slow Queries",
                "content": """
Use AI to identify and fix SQL performance bottlenecks.

### The Optimization Prompt
```
Optimize this SQL query for better performance:
[paste query]

Table schemas:
[table structures and indexes]

Current execution time: [time]
Expected result: [description]
```

### Example: Slow Query
```sql
SELECT u.name, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.created_at > '2024-01-01'
GROUP BY u.name
ORDER BY order_count DESC;
```

### AI-Optimized Version
```sql
-- Add index on orders.created_at and orders.user_id
CREATE INDEX idx_orders_created_user ON orders(created_at, user_id);

-- Optimized query
SELECT u.name, COUNT(o.id) as order_count
FROM users u
INNER JOIN orders o ON u.id = o.user_id
WHERE o.created_at > '2024-01-01'
GROUP BY u.id, u.name  -- Include u.id for better grouping
ORDER BY order_count DESC;
```

**Improvements:**
- Changed LEFT JOIN to INNER JOIN (we filter on orders anyway)
- Added composite index
- Group by primary key for efficiency

### Query Explanation Prompt
```
Explain what this complex query does in simple terms:
[query]
```

### Index Suggestion Prompt
```
Given these tables and common queries:
Tables: [schemas]
Queries: [list of frequent queries]

Suggest optimal indexes.
```

### Query Generation
```
Generate a SQL query to:
[describe what you need]

Tables available:
- users (id, name, email, created_at)
- orders (id, user_id, total, created_at)
- products (id, name, price)
```

**Example Output:**
```sql
-- Get top 10 customers by total spending in 2024
SELECT 
    u.name,
    u.email,
    SUM(o.total) as total_spent,
    COUNT(o.id) as order_count
FROM users u
INNER JOIN orders o ON u.id = o.user_id
WHERE YEAR(o.created_at) = 2024
GROUP BY u.id, u.name, u.email
ORDER BY total_spent DESC
LIMIT 10;
```
                """
            }
        ],
        "quiz": [
            {
                "question": "What should you provide when asking AI to optimize a SQL query?",
                "options": ["Just the query", "Query, table schemas, and current performance metrics", "Only table names", "The database type"],
                "correct": 1,
                "explanation": "Providing the query, table schemas, indexes, and performance metrics helps AI understand the context and suggest targeted optimizations."
            }
        ]
    },

    # Deep Dive Content (dd-6 to dd-10)
    "dd-6": {
        "title": "Cursor IDE Masterclass",
        "sections": [
            {
                "title": "The AI-Native Code Editor",
                "content": """
Cursor is VS Code reimagined with AI at its core.

### Core Features

**1. Cmd+K: Inline Editing**
- Select code, press Cmd+K (Ctrl+K on Windows)
- Describe the change you want
- AI edits in place

**Example:**
```
Select a function → Cmd+K → "Add error handling and logging"
```

**2. Composer: Multi-File Editing**
- Cmd+I to open Composer
- Describe changes across multiple files
- AI understands your codebase structure

**Example:**
```
"Add a new user authentication endpoint with:
- Route in routes/auth.js
- Controller in controllers/authController.js  
- Validation middleware
- Unit tests"
```

**3. Chat with Codebase**
- @ mention files or folders
- Ask questions about your code
- Get contextual answers

**Example:**
```
@database/models.py How is user authentication implemented?
```

### Advanced Techniques

**Codebase Indexing:**
```
Settings → Features → Enable Codebase Indexing
```
This allows Cursor to understand your entire project.

**Custom Rules:**
Create `.cursorrules` file in project root:
```
- Use TypeScript strict mode
- Follow Airbnb style guide
- Add JSDoc comments to all functions
- Prefer functional components in React
```

**Tab Autocomplete:**
- More powerful than Copilot
- Understands recent edits
- Multi-line suggestions

### Workflow Example: Building a Feature

1. **Plan:** Chat with AI about architecture
2. **Scaffold:** Use Composer to create files
3. **Implement:** Cmd+K for inline edits
4. **Test:** Generate tests with AI
5. **Refactor:** Ask AI to improve code quality
                """
            }
        ],
        "quiz": [
            {
                "question": "What is Cursor's Composer feature used for?",
                "options": ["Writing music", "Multi-file editing across codebase", "Compiling code", "Creating databases"],
                "correct": 1,
                "explanation": "Composer (Cmd+I) allows you to make coordinated changes across multiple files by describing what you want at a high level."
            }
        ]
    },

    "dd-7": {
        "title": "GitHub Copilot Advanced Patterns",
        "sections": [
            {
                "title": "Beyond Basic Autocomplete",
                "content": """
Master advanced Copilot techniques for 10x productivity.

### 1. Prompt Files (.github/copilot-instructions.md)
```markdown
# Project Guidelines

## Code Style
- Use TypeScript with strict mode
- Prefer async/await over promises
- Add comprehensive error handling

## Testing
- Write tests for all public functions
- Use Jest for unit tests
- Aim for 80%+ coverage

## Documentation
- Add JSDoc comments
- Include usage examples
```

Copilot will follow these rules automatically!

### 2. Workspace Mode
```
Cmd+Shift+P → "Copilot: Open Chat"
Type: @workspace
```

Ask questions about your entire codebase:
```
@workspace How is authentication handled?
@workspace Where are API endpoints defined?
@workspace Show me all database models
```

### 3. Slash Commands in Chat

**/explain** - Explain selected code
```
Select complex function → /explain
```

**/fix** - Fix bugs
```
Select buggy code → /fix
```

**/tests** - Generate tests
```
Select function → /tests
```

**/doc** - Generate documentation
```
Select code → /doc
```

### 4. Context-Aware Completions

**Pattern: Comment-Driven Development**
```javascript
// Function to validate email and send welcome email
// Returns true if successful, throws error otherwise
async function registerUser(email, name) {
    // Copilot will suggest the implementation
}
```

**Pattern: Example-Driven**
```python
# Example usage:
# result = calculate_tax(income=50000, state="CA")
# result = {"federal": 5000, "state": 2500, "total": 7500}

def calculate_tax(income, state):
    # Copilot infers the structure from example
```

### 5. Copilot for CLI
```bash
# Install
gh extension install github/gh-copilot

# Use
gh copilot suggest "find all large files"
gh copilot explain "git rebase -i HEAD~3"
```

### Advanced Workflow

**1. Architecture Planning:**
```
// Create a REST API for a blog with:
// - Posts (CRUD)
// - Comments (nested under posts)
// - User authentication
// - Rate limiting
```

**2. Implementation:**
Let Copilot suggest the structure, then refine.

**3. Testing:**
```
// Generate comprehensive tests for the above API
```

**4. Documentation:**
```
// Generate API documentation in OpenAPI format
```
                """
            }
        ],
        "quiz": [
            {
                "question": "What is the purpose of .github/copilot-instructions.md?",
                "options": ["Store API keys", "Define project-specific guidelines for Copilot", "Configure GitHub Actions", "List dependencies"],
                "correct": 1,
                "explanation": "Copilot-instructions.md allows you to define project-specific coding standards and guidelines that Copilot will automatically follow."
            }
        ]
    },

    "dd-8": {
        "title": "Building with the Claude API",
        "sections": [
            {
                "title": "Production Claude Applications",
                "content": """
Claude excels at reasoning, coding, and long-context tasks.

### Setup
```python
pip install anthropic

import anthropic

client = anthropic.Anthropic(
    api_key="your-api-key"
)
```

### Basic Usage
```python
message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Explain quantum computing"}
    ]
)

print(message.content[0].text)
```

### System Prompts
```python
message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    system="You are a senior Python developer. Provide code with best practices.",
    messages=[
        {"role": "user", "content": "Create a REST API for user management"}
    ]
)
```

### Tool Use (Function Calling)
```python
tools = [
    {
        "name": "get_weather",
        "description": "Get current weather for a location",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City name"
                }
            },
            "required": ["location"]
        }
    }
]

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    tools=tools,
    messages=[
        {"role": "user", "content": "What's the weather in San Francisco?"}
    ]
)

# Handle tool calls
if message.stop_reason == "tool_use":
    tool_use = next(block for block in message.content if block.type == "tool_use")
    
    if tool_use.name == "get_weather":
        # Call your actual weather API
        weather_data = get_weather_api(tool_use.input["location"])
        
        # Send result back to Claude
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            tools=tools,
            messages=[
                {"role": "user", "content": "What's the weather in San Francisco?"},
                {"role": "assistant", "content": message.content},
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": tool_use.id,
                            "content": str(weather_data)
                        }
                    ]
                }
            ]
        )
```

### Streaming Responses
```python
with client.messages.stream(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Write a story"}]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

### Vision Capabilities
```python
import base64

with open("image.jpg", "rb") as f:
    image_data = base64.standard_b64encode(f.read()).decode("utf-8")

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": image_data
                    }
                },
                {
                    "type": "text",
                    "text": "Describe this image in detail"
                }
            ]
        }
    ]
)
```

### Best Practices

**1. Use System Prompts for Consistency**
**2. Implement Retry Logic**
```python
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def call_claude(prompt):
    return client.messages.create(...)
```

**3. Cache System Prompts (for cost savings)**
**4. Monitor Token Usage**
```python
print(f"Input tokens: {message.usage.input_tokens}")
print(f"Output tokens: {message.usage.output_tokens}")
```
                """
            }
        ],
        "quiz": [
            {
                "question": "What is Claude's tool use feature designed for?",
                "options": ["Image generation", "Function calling and external API integration", "Fine-tuning", "Data storage"],
                "correct": 1,
                "explanation": "Tool use allows Claude to call external functions and APIs, enabling it to perform actions beyond text generation like fetching data or executing code."
            }
        ]
    },

    "dd-9": {
        "title": "AI Image Generation for Developers",
        "sections": [
            {
                "title": "Integrating Image Generation APIs",
                "content": """
Add AI image generation to your applications.

### DALL-E 3 (OpenAI)
```python
from openai import OpenAI

client = OpenAI(api_key="your-key")

response = client.images.generate(
    model="dall-e-3",
    prompt="A futuristic city with flying cars, cyberpunk style",
    size="1024x1024",
    quality="standard",  # or "hd"
    n=1
)

image_url = response.data[0].url
```

### Stable Diffusion (Stability AI)
```python
import requests

url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

body = {
    "text_prompts": [
        {
            "text": "A serene mountain landscape at sunset",
            "weight": 1
        }
    ],
    "cfg_scale": 7,
    "height": 1024,
    "width": 1024,
    "samples": 1,
    "steps": 30
}

response = requests.post(url, headers=headers, json=body)
data = response.json()

# Save image
import base64
for i, image in enumerate(data["artifacts"]):
    with open(f"output_{i}.png", "wb") as f:
        f.write(base64.b64decode(image["base64"]))
```

### Midjourney (via API)
```python
# Using unofficial API wrapper
from midjourney_api import Midjourney

mj = Midjourney(token="your-token")

# Generate image
result = mj.imagine("a magical forest with glowing mushrooms --ar 16:9 --v 6")

# Get result
image_url = result.get_image_url()
```

### Prompt Engineering for Images

**Structure:**
```
[Subject] + [Style] + [Mood] + [Technical Parameters]
```

**Examples:**

**Product Photography:**
```
A sleek smartphone on a marble surface, 
professional product photography, 
studio lighting, 
high resolution, 
clean background
```

**UI Design:**
```
Modern dashboard interface for analytics app,
minimalist design,
blue and white color scheme,
flat design style,
4k resolution
```

**Character Design:**
```
A friendly robot character,
Pixar animation style,
warm lighting,
detailed textures,
white background
```

### Advanced Techniques

**Negative Prompts (Stable Diffusion):**
```python
body = {
    "text_prompts": [
        {"text": "beautiful landscape", "weight": 1},
        {"text": "people, buildings, cars", "weight": -1}  # Avoid these
    ]
}
```

**Image-to-Image:**
```python
# DALL-E
response = client.images.edit(
    image=open("input.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="Add a sunset sky",
    n=1,
    size="1024x1024"
)
```

**Variations:**
```python
response = client.images.create_variation(
    image=open("original.png", "rb"),
    n=3,
    size="1024x1024"
)
```

### Production Integration

**1. Async Generation:**
```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

async def generate_images(prompts):
    with ThreadPoolExecutor() as executor:
        loop = asyncio.get_event_loop()
        tasks = [
            loop.run_in_executor(executor, generate_single_image, prompt)
            for prompt in prompts
        ]
        return await asyncio.gather(*tasks)
```

**2. Caching:**
```python
import hashlib
import os

def get_or_generate_image(prompt):
    # Create hash of prompt
    prompt_hash = hashlib.md5(prompt.encode()).hexdigest()
    cache_path = f"cache/{prompt_hash}.png"
    
    if os.path.exists(cache_path):
        return cache_path
    
    # Generate new image
    image_url = generate_image(prompt)
    download_image(image_url, cache_path)
    return cache_path
```

**3. Cost Optimization:**
- Use lower resolution for previews
- Implement rate limiting
- Cache frequently requested images
- Use cheaper models for drafts
                """
            }
        ],
        "quiz": [
            {
                "question": "What is a negative prompt in image generation?",
                "options": ["A bad prompt", "Elements to avoid in the generated image", "A prompt that generates dark images", "An error message"],
                "correct": 1,
                "explanation": "Negative prompts specify elements that should NOT appear in the generated image, helping to refine and control the output."
            }
        ]
    },

    "dd-10": {
        "title": "API Testing with AI Assistants",
        "sections": [
            {
                "title": "Automated API Test Generation",
                "content": """
Use AI to generate comprehensive API test suites.

### From OpenAPI Spec
```
Given this OpenAPI specification:
[paste spec]

Generate a complete test suite using pytest that covers:
1. All endpoints
2. Success cases (200, 201, 204)
3. Error cases (400, 401, 403, 404, 500)
4. Edge cases
5. Authentication flows
```

### Example Output
```python
import pytest
import requests

BASE_URL = "https://api.example.com"
API_KEY = "test-key"

class TestUserAPI:
    
    def test_create_user_success(self):
        payload = {
            "name": "John Doe",
            "email": "john@example.com"
        }
        response = requests.post(
            f"{BASE_URL}/users",
            json=payload,
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        assert response.status_code == 201
        assert "id" in response.json()
        assert response.json()["email"] == payload["email"]
    
    def test_create_user_invalid_email(self):
        payload = {
            "name": "John Doe",
            "email": "invalid-email"
        }
        response = requests.post(
            f"{BASE_URL}/users",
            json=payload,
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        assert response.status_code == 400
        assert "error" in response.json()
    
    def test_create_user_unauthorized(self):
        payload = {
            "name": "John Doe",
            "email": "john@example.com"
        }
        response = requests.post(
            f"{BASE_URL}/users",
            json=payload
        )
        assert response.status_code == 401
    
    def test_get_user_success(self):
        user_id = "123"
        response = requests.get(
            f"{BASE_URL}/users/{user_id}",
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        assert response.status_code == 200
        assert response.json()["id"] == user_id
    
    def test_get_user_not_found(self):
        response = requests.get(
            f"{BASE_URL}/users/999999",
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        assert response.status_code == 404
```

### Contract Testing
```
Generate contract tests using Pact for this API:
[API details]

Include:
- Provider contract
- Consumer contract
- Verification tests
```

### Load Testing
```
Create a Locust load test script for this API:
Endpoint: POST /api/orders
Expected load: 100 requests/second
Test duration: 5 minutes

Include:
- Realistic user behavior
- Think time between requests
- Proper error handling
```

**AI-Generated Locust Script:**
```python
from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 3)
    
    def on_start(self):
        # Login
        response = self.client.post("/auth/login", json={
            "username": "test@example.com",
            "password": "password123"
        })
        self.token = response.json()["token"]
    
    @task(3)
    def create_order(self):
        self.client.post(
            "/api/orders",
            json={
                "items": [{"id": 1, "quantity": 2}],
                "total": 29.99
            },
            headers={"Authorization": f"Bearer {self.token}"}
        )
    
    @task(1)
    def get_orders(self):
        self.client.get(
            "/api/orders",
            headers={"Authorization": f"Bearer {self.token}"}
        )
```

### Mocking External APIs
```
Generate mock responses for this third-party API:
[API documentation]

Use responses library for Python
Include various scenarios: success, timeout, rate limit
```

### Security Testing
```
Generate security tests for this API:
- SQL injection attempts
- XSS attempts  
- Authentication bypass
- Rate limiting validation
- CORS configuration
```

### Advanced: AI-Powered Test Maintenance

**Update Tests After API Changes:**
```
The API has changed:
Old: POST /users (returns 200)
New: POST /users (returns 201 with Location header)

Update the test suite accordingly.
```

**Generate Test Data:**
```
Generate 100 realistic test users with:
- Valid email addresses
- Diverse names
- Various age ranges
- Different countries

Format as JSON array.
```
                """
            }
        ],
        "quiz": [
            {
                "question": "What should comprehensive API tests cover?",
                "options": ["Only success cases", "Success cases, error cases, edge cases, and auth flows", "Just one endpoint", "Only GET requests"],
                "correct": 1,
                "explanation": "Comprehensive API tests should cover all endpoints with success cases, various error scenarios, edge cases, and authentication/authorization flows."
            }
        ]
    },

    # Mastery Track Content (mt-4, mt-5)
    "mt-4": {
        "title": "Full-Stack AI Applications",
        "sections": [
            {
                "title": "Building Production AI Apps",
                "content": """
A comprehensive 30-hour track to build complete AI-powered applications.

### Module 1: Architecture (4 hours)

**Topics:**
- Microservices vs Monolith for AI apps
- API Gateway patterns
- Database selection (SQL vs NoSQL vs Vector)
- Caching strategies (Redis for LLM responses)
- Queue systems (Celery, RabbitMQ)

**Project:** Design architecture for an AI-powered customer support system

### Module 2: Frontend Integration (6 hours)

**React + AI:**
```javascript
import { useState } from 'react';

function AIChat() {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');
    const [streaming, setStreaming] = useState(false);

    const sendMessage = async () => {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: input })
        });

        const reader = response.body.getReader();
        const decoder = new TextDecoder();

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            
            const chunk = decoder.decode(value);
            setMessages(prev => [...prev, { text: chunk, role: 'assistant' }]);
        }
    };

    return (
        <div className="chat-container">
            {messages.map((msg, i) => (
                <div key={i} className={msg.role}>{msg.text}</div>
            ))}
            <input value={input} onChange={e => setInput(e.target.value)} />
            <button onClick={sendMessage}>Send</button>
        </div>
    );
}
```

### Module 3: Backend Development (8 hours)

**FastAPI + LangChain:**
```python
from fastapi import FastAPI, WebSocket
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

app = FastAPI()

@app.websocket("/ws/chat")
async def chat_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    llm = ChatOpenAI(model="gpt-4", streaming=True)
    memory = ConversationBufferMemory()
    chain = ConversationChain(llm=llm, memory=memory)
    
    while True:
        message = await websocket.receive_text()
        
        async for chunk in chain.astream({"input": message}):
            await websocket.send_text(chunk)
```

### Module 4: Database & Vector Stores (4 hours)

**Hybrid Storage:**
```python
from sqlalchemy import create_engine
from pinecone import Pinecone

# Traditional data
engine = create_engine('postgresql://...')

# Vector data
pc = Pinecone(api_key="...")
index = pc.Index("documents")

# Store document
def store_document(doc_id, text, metadata):
    # Store in PostgreSQL
    with engine.connect() as conn:
        conn.execute(
            "INSERT INTO documents (id, text, metadata) VALUES (%s, %s, %s)",
            (doc_id, text, metadata)
        )
    
    # Store embedding in Pinecone
    embedding = get_embedding(text)
    index.upsert([(doc_id, embedding, metadata)])
```

### Module 5: Authentication & Security (3 hours)

- JWT implementation
- API key management
- Rate limiting
- Input validation
- Prompt injection prevention

### Module 6: Deployment (5 hours)

**Docker Compose:**
```yaml
version: '3.8'
services:
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
  
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - DATABASE_URL=${DATABASE_URL}
    depends_on:
      - db
      - redis
  
  db:
    image: postgres:15
    volumes:
      - postgres_data:/var/lib/postgresql/data
  
  redis:
    image: redis:7
```

### Final Project (10 hours)

Build a complete AI-powered application:
- Document Q&A system
- User authentication
- Real-time chat
- Document upload
- Analytics dashboard
- Production deployment
                """
            }
        ],
        "quiz": [
            {
                "question": "Why use Redis in AI applications?",
                "options": ["Store user passwords", "Cache LLM responses to reduce costs and latency", "Replace the database", "Generate embeddings"],
                "correct": 1,
                "explanation": "Redis is ideal for caching LLM responses because it provides fast in-memory storage, reducing API costs and improving response times for repeated queries."
            }
        ]
    },

    "mt-5": {
        "title": "AI for QA Engineers",
        "sections": [
            {
                "title": "Transform Testing with AI",
                "content": """
An 18-hour comprehensive track for QA professionals.

### Module 1: AI-Powered Test Generation (4 hours)

**Automated Test Creation:**
```python
# Using AI to generate tests from user stories

user_story = '''
As a user, I want to reset my password
So that I can regain access if I forget it

Acceptance Criteria:
- User enters email address
- System sends reset link
- Link expires after 24 hours
- User sets new password
'''

# AI generates:
import pytest

class TestPasswordReset:
    
    def test_request_password_reset_valid_email(self):
        response = client.post('/auth/reset-password', json={
            'email': 'user@example.com'
        })
        assert response.status_code == 200
        assert 'Reset link sent' in response.json()['message']
    
    def test_request_password_reset_invalid_email(self):
        response = client.post('/auth/reset-password', json={
            'email': 'nonexistent@example.com'
        })
        # Should still return 200 for security
        assert response.status_code == 200
    
    def test_reset_link_expires_after_24_hours(self):
        # Generate reset token
        token = generate_reset_token('user@example.com')
        
        # Fast-forward time
        with freeze_time(datetime.now() + timedelta(hours=25)):
            response = client.post(f'/auth/reset-password/{token}', json={
                'new_password': 'NewSecure123!'
            })
            assert response.status_code == 400
            assert 'expired' in response.json()['error'].lower()
```

### Module 2: Visual Testing with AI (3 hours)

**AI-Powered Screenshot Comparison:**
```python
from playwright.sync_api import sync_playwright
from PIL import Image
import imagehash

def test_visual_regression():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://example.com')
        
        # Take screenshot
        page.screenshot(path='current.png')
        
        # Compare with baseline using perceptual hash
        baseline = Image.open('baseline.png')
        current = Image.open('current.png')
        
        baseline_hash = imagehash.phash(baseline)
        current_hash = imagehash.phash(current)
        
        difference = baseline_hash - current_hash
        assert difference < 5, f"Visual difference detected: {difference}"
```

### Module 3: Intelligent Test Data Generation (3 hours)

**AI-Generated Test Data:**
```python
# Prompt: Generate realistic test data for e-commerce

test_users = [
    {
        "name": "Sarah Johnson",
        "email": "sarah.j@email.com",
        "age": 28,
        "location": "New York, NY",
        "purchase_history": [
            {"product": "Laptop", "price": 1299.99, "date": "2024-01-15"},
            {"product": "Mouse", "price": 29.99, "date": "2024-01-15"}
        ]
    },
    # ... 99 more realistic users
]

# Use in tests
@pytest.mark.parametrize("user", test_users)
def test_user_checkout_flow(user):
    # Test with diverse, realistic data
    pass
```

### Module 4: AI-Assisted Bug Analysis (2 hours)

**Automated Bug Triage:**
```python
def analyze_bug_report(bug_description, stack_trace):
    prompt = f'''
    Analyze this bug report:
    
    Description: {bug_description}
    Stack Trace: {stack_trace}
    
    Provide:
    1. Severity (Critical/High/Medium/Low)
    2. Likely root cause
    3. Affected components
    4. Suggested fix
    5. Similar known issues
    '''
    
    analysis = call_llm(prompt)
    return analysis

# Auto-categorize and prioritize bugs
bug = {
    "description": "App crashes when uploading large files",
    "stack_trace": "..."
}

analysis = analyze_bug_report(bug["description"], bug["stack_trace"])
# AI suggests: Severity: High, Cause: Memory overflow, Fix: Implement chunked upload
```

### Module 5: Performance Testing (3 hours)

**AI-Optimized Load Patterns:**
```python
from locust import HttpUser, task, between
import random

class IntelligentUser(HttpUser):
    wait_time = between(1, 5)
    
    # AI suggests realistic user behavior patterns
    @task(5)  # 50% of traffic
    def browse_products(self):
        category = random.choice(['electronics', 'clothing', 'books'])
        self.client.get(f'/products?category={category}')
    
    @task(3)  # 30% of traffic
    def view_product(self):
        product_id = random.randint(1, 1000)
        self.client.get(f'/products/{product_id}')
    
    @task(2)  # 20% of traffic
    def add_to_cart(self):
        self.client.post('/cart', json={
            'product_id': random.randint(1, 1000),
            'quantity': random.randint(1, 3)
        })
```

### Module 6: Accessibility Testing (2 hours)

**AI-Powered A11y Checks:**
```python
from axe_selenium_python import Axe

def test_accessibility():
    driver.get('https://example.com')
    axe = Axe(driver)
    
    # Run accessibility scan
    results = axe.run()
    
    # AI analyzes violations and suggests fixes
    for violation in results['violations']:
        fix_suggestion = get_ai_fix_suggestion(violation)
        print(f"Issue: {violation['help']}")
        print(f"AI Suggestion: {fix_suggestion}")
```

### Module 7: Final Project (3 hours)

Build a complete AI-powered testing framework:
- Automated test generation from requirements
- Visual regression testing
- Performance monitoring
- Bug prediction
- Test maintenance automation
                """
            }
        ],
        "quiz": [
            {
                "question": "How can AI help with test maintenance?",
                "options": ["Delete all tests", "Auto-update tests when UI changes", "Make tests slower", "Remove assertions"],
                "correct": 1,
                "explanation": "AI can analyze UI changes and automatically update test selectors and assertions, reducing the manual effort required to maintain test suites."
            }
        ]
    },
    
    # NEW TUTORIAL CONTENT (January 2026)

    "dd-11": {
        "title": "LangGraph: Multi-Agent Orchestration",
        "sections": [
            {
                "title": "Introduction to LangGraph",
                "content": """
LangGraph is LangChain's framework for building stateful, multi-actor applications with LLMs. It extends LangChain Expression Language with the ability to coordinate multiple chains (or actors) across multiple steps of computation in a cyclic manner.

### Why LangGraph?

**Traditional Chains:** Linear, one-shot execution
```
Input → Chain → Output
```

**LangGraph:** Cyclic, stateful execution
```
Input → Agent 1 → State → Agent 2 → State → Agent 3 → Output
                    ↑                           ↓
                    └───────────────────────────┘
```

### Core Concepts

1. **State** - Shared data structure passed between nodes
2. **Nodes** - Individual agents or processing steps
3. **Edges** - Connections between nodes (conditional or fixed)
4. **Graph** - The overall workflow

### Installation
```bash
pip install langgraph langchain-openai
```
                """
            },
            {
                "title": "Building Your First Multi-Agent System",
                "content": """
Let's build a research assistant with specialized agents:

### Step 1: Define the State
```python
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI

class AgentState(TypedDict):
    messages: list
    research_data: str
    analysis: str
    final_report: str

llm = ChatOpenAI(model="gpt-4")
```

### Step 2: Create Agent Nodes
```python
def researcher_agent(state: AgentState):
    \"\"\"Gathers information\"\"\"
    prompt = f"Research this topic: {state['messages'][-1]}"
    research = llm.invoke(prompt).content
    return {"research_data": research}

def analyst_agent(state: AgentState):
    \"\"\"Analyzes the research\"\"\"
    prompt = f"Analyze this research: {state['research_data']}"
    analysis = llm.invoke(prompt).content
    return {"analysis": analysis}

def writer_agent(state: AgentState):
    \"\"\"Writes final report\"\"\"
    prompt = f"Write a report based on: {state['analysis']}"
    report = llm.invoke(prompt).content
    return {"final_report": report}
```

### Step 3: Build the Graph
```python
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("researcher", researcher_agent)
workflow.add_node("analyst", analyst_agent)
workflow.add_node("writer", writer_agent)

# Add edges
workflow.set_entry_point("researcher")
workflow.add_edge("researcher", "analyst")
workflow.add_edge("analyst", "writer")
workflow.add_edge("writer", END)

# Compile
app = workflow.compile()
```

### Step 4: Run the System
```python
result = app.invoke({
    "messages": ["Explain quantum computing"],
    "research_data": "",
    "analysis": "",
    "final_report": ""
})

print(result["final_report"])
```

### Conditional Routing
```python
def should_continue(state: AgentState):
    if len(state["research_data"]) < 100:
        return "researcher"  # Need more research
    return "analyst"  # Proceed to analysis

workflow.add_conditional_edges(
    "researcher",
    should_continue,
    {
        "researcher": "researcher",  # Loop back
        "analyst": "analyst"  # Move forward
    }
)
```

**Key Insight:** LangGraph enables complex workflows where agents can loop, branch, and collaborate based on state.
                """
            }
        ],
        "quiz": [
            {
                "question": "What is the main advantage of LangGraph over traditional LangChain chains?",
                "options": ["Faster execution", "Cyclic and stateful workflows", "Cheaper API costs", "Better prompts"],
                "correct": 1,
                "explanation": "LangGraph enables cyclic, stateful workflows where agents can loop back, branch conditionally, and maintain shared state across multiple steps."
            }
        ]
    },
    
    "dd-12": {
        "title": "CrewAI: Collaborative AI Agents",
        "sections": [
            {
                "title": "Introduction to CrewAI",
                "content": """
CrewAI is a framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks.

### Key Concepts

**Agents** - Autonomous units with specific roles and goals
**Tasks** - Assignments given to agents
**Crew** - A team of agents working together
**Process** - How tasks are executed (sequential or hierarchical)

### Installation
```bash
pip install crewai crewai-tools
```

### The CrewAI Philosophy
- **Role-Based:** Each agent has a specific role (researcher, writer, analyst)
- **Goal-Oriented:** Agents work towards defined objectives
- **Collaborative:** Agents can delegate and communicate
- **Autonomous:** Minimal human intervention needed
                """
            },
            {
                "title": "Building a Content Creation Crew",
                "content": """
Let's build a crew that researches, writes, and edits blog posts:

### Step 1: Define Agents
```python
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4")

# Researcher Agent
researcher = Agent(
    role='Research Analyst',
    goal='Find accurate, up-to-date information on given topics',
    backstory='''You are an expert researcher with a keen eye for 
    credible sources and relevant data. You excel at finding the 
    most important information quickly.''',
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Writer Agent
writer = Agent(
    role='Content Writer',
    goal='Create engaging, well-structured content',
    backstory='''You are a skilled writer who can transform research 
    into compelling narratives. You write with clarity and style.''',
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Editor Agent
editor = Agent(
    role='Content Editor',
    goal='Refine content for clarity, grammar, and impact',
    backstory='''You are a meticulous editor with an eye for detail. 
    You ensure every piece of content is polished and professional.''',
    verbose=True,
    allow_delegation=False,
    llm=llm
)
```

### Step 2: Define Tasks
```python
research_task = Task(
    description='''Research the topic: {topic}
    Find key points, statistics, and recent developments.
    Provide a comprehensive research summary.''',
    agent=researcher,
    expected_output="Detailed research summary with sources"
)

writing_task = Task(
    description='''Using the research provided, write a 500-word blog post 
    about {topic}. Make it engaging and informative.''',
    agent=writer,
    expected_output="Complete blog post draft"
)

editing_task = Task(
    description='''Edit the blog post for:
    - Grammar and spelling
    - Clarity and flow
    - Engagement and impact
    Provide the final polished version.''',
    agent=editor,
    expected_output="Final edited blog post"
)
```

### Step 3: Create the Crew
```python
crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, writing_task, editing_task],
    process=Process.sequential,  # Tasks run in order
    verbose=True
)
```

### Step 4: Run the Crew
```python
result = crew.kickoff(inputs={'topic': 'AI in Healthcare'})
print(result)
```

### Advanced: Hierarchical Process
```python
# Manager agent coordinates others
manager = Agent(
    role='Project Manager',
    goal='Coordinate the team and ensure quality output',
    backstory='''You are an experienced project manager who 
    knows how to get the best from your team.''',
    llm=llm,
    allow_delegation=True
)

crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, writing_task, editing_task],
    process=Process.hierarchical,
    manager_llm=llm,
    verbose=True
)
```

**Pro Tip:** Use `allow_delegation=True` to let agents delegate subtasks to each other!
                """
            }
        ],
        "quiz": [
            {
                "question": "What is the difference between Sequential and Hierarchical process in CrewAI?",
                "options": ["Sequential is faster", "Hierarchical uses a manager agent to coordinate", "Sequential uses more agents", "No difference"],
                "correct": 1,
                "explanation": "Hierarchical process uses a manager agent to coordinate and delegate tasks, while Sequential executes tasks in a fixed order."
            }
        ]
    },
    
    "qw-11": {
        "title": "Local LLM Setup: Complete Guide",
        "sections": [
            {
                "title": "Why Run LLMs Locally?",
                "content": """
Running Large Language Models locally offers several advantages:

### Benefits
✅ **Privacy** - Your data never leaves your machine
✅ **Cost** - No API fees, unlimited usage
✅ **Speed** - No network latency
✅ **Offline** - Works without internet
✅ **Customization** - Fine-tune models for your needs

### Use Cases
- Sensitive data processing (medical, legal, financial)
- Development and testing
- Learning and experimentation
- Cost-sensitive applications
- Offline environments

### Requirements
- **RAM:** 8GB minimum (16GB+ recommended)
- **Storage:** 10-50GB per model
- **GPU:** Optional but recommended (NVIDIA with CUDA or Apple Silicon)
                """
            },
            {
                "title": "Setting Up Ollama",
                "content": """
Ollama is the easiest way to run LLMs locally. Think of it as "Docker for LLMs".

### Installation

**macOS/Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows:**
Download from https://ollama.com/download

### Verify Installation
```bash
ollama --version
```

### Running Your First Model
```bash
# Pull Llama 3.2 (3B parameters - fast and capable)
ollama pull llama3.2

# Run interactively
ollama run llama3.2

# Try it out
>>> Write a Python function to calculate fibonacci numbers
```

### Popular Models
```bash
# Fast and efficient
ollama pull llama3.2        # Meta's latest (3B/7B)
ollama pull phi3            # Microsoft's efficient model
ollama pull gemma2          # Google's open model

# Code-specialized
ollama pull codellama       # Meta's code model
ollama pull deepseek-coder  # Excellent for coding

# Larger, more capable
ollama pull llama3.2:70b    # Requires 40GB+ RAM
ollama pull mixtral         # Mixture of Experts
```

### Model Sizes Guide
- **3B parameters** - 2GB RAM, fast responses
- **7B parameters** - 4GB RAM, good quality
- **13B parameters** - 8GB RAM, better quality
- **70B parameters** - 40GB RAM, GPT-4 class

### Using Ollama in Code
```python
import requests
import json

def query_ollama(prompt, model="llama3.2"):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(url, json=data)
    return response.json()["response"]

# Use it
result = query_ollama("Explain quantum computing in simple terms")
print(result)
```

### With LangChain
```python
from langchain_community.llms import Ollama

llm = Ollama(model="llama3.2")
response = llm.invoke("Write a haiku about coding")
print(response)
```

### Managing Models
```bash
# List installed models
ollama list

# Remove a model
ollama rm llama3.2

# Update a model
ollama pull llama3.2

# Show model info
ollama show llama3.2
```

**Pro Tip:** Start with `llama3.2` (3B) for testing, then upgrade to `llama3.2:7b` for better quality!
                """
            }
        ],
        "quiz": [
            {
                "question": "What is the minimum RAM recommended for running a 7B parameter model?",
                "options": ["2GB", "4GB", "8GB", "16GB"],
                "correct": 1,
                "explanation": "7B parameter models typically require about 4GB of RAM to run effectively."
            }
        ]
    },
    
    "dd-13": {
        "title": "Production RAG: From Prototype to Scale",
        "sections": [
            {
                "title": "RAG Architecture Overview",
                "content": """
Building a production-ready RAG system requires more than just basic vector search. Let's build it right.

### Production RAG Stack

**Components:**
1. **Document Processing** - Chunking, cleaning, metadata extraction
2. **Embedding** - Convert text to vectors
3. **Vector Store** - Store and search embeddings
4. **Retrieval** - Find relevant documents
5. **Generation** - LLM synthesizes answer
6. **Evaluation** - Measure quality

### Architecture Diagram
```
Documents → Chunking → Embedding → Vector DB
                                        ↓
User Query → Embedding → Search → Rerank → LLM → Answer
                                        ↑
                                   Metadata Filter
```
                """
            },
            {
                "title": "Advanced Chunking Strategies",
                "content": """
Chunking is critical - bad chunks = bad retrieval = bad answers.

### Strategy 1: Semantic Chunking
```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,  # Overlap prevents context loss
    separators=["\n\n", "\n", ". ", " ", ""],
    length_function=len
)

chunks = splitter.split_text(document)
```

### Strategy 2: Document-Aware Chunking
```python
# Preserve document structure
from langchain.text_splitter import MarkdownHeaderTextSplitter

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)
```

### Strategy 3: Sliding Window
```python
def sliding_window_chunks(text, window_size=500, step=250):
    chunks = []
    for i in range(0, len(text), step):
        chunk = text[i:i + window_size]
        if len(chunk) > 100:  # Minimum chunk size
            chunks.append(chunk)
    return chunks
```

### Adding Metadata
```python
from langchain.schema import Document

docs = [
    Document(
        page_content=chunk,
        metadata={
            "source": "docs/api.md",
            "section": "Authentication",
            "version": "v2.0",
            "last_updated": "2024-01-10"
        }
    )
    for chunk in chunks
]
```

**Best Practice:** Chunk size depends on your use case:
- **Q&A:** 500-1000 characters
- **Summarization:** 2000-4000 characters
- **Code:** Function/class level
                """
            },
            {
                "title": "Hybrid Search: Best of Both Worlds",
                "content": """
Combine dense (semantic) and sparse (keyword) search for better retrieval.

### Implementation with Pinecone
```python
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings

# Initialize
pc = Pinecone(api_key="your-key")
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Create hybrid index
index = pc.Index("hybrid-search")

# Add documents with both dense and sparse vectors
vectorstore = PineconeVectorStore(
    index=index,
    embedding=embeddings,
    text_key="text"
)

# Hybrid search
results = vectorstore.similarity_search(
    query="How do I authenticate?",
    k=5,
    filter={"section": "API"}  # Metadata filtering
)
```

### Reranking for Precision
```python
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CohereRerank

# Base retriever
base_retriever = vectorstore.as_retriever(search_kwargs={"k": 20})

# Reranker
compressor = CohereRerank(model="rerank-english-v2.0")

# Compression retriever
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=base_retriever
)

# Get top 5 after reranking
docs = compression_retriever.get_relevant_documents(
    "How do I authenticate?"
)
```

**Pro Tip:** Retrieve 20 documents, rerank to top 5 for best precision!
                """
            },
            {
                "title": "Evaluation Metrics",
                "content": """
Measure your RAG system's quality systematically.

### Key Metrics

**1. Retrieval Metrics**
- **Recall@K:** % of relevant docs in top K results
- **MRR (Mean Reciprocal Rank):** Position of first relevant doc
- **NDCG:** Normalized Discounted Cumulative Gain

**2. Generation Metrics**
- **Faithfulness:** Answer grounded in retrieved docs
- **Answer Relevance:** Answer addresses the question
- **Context Relevance:** Retrieved docs are relevant

### Using RAGAS Framework
```python
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_relevancy,
    context_recall
)

# Prepare evaluation data
eval_data = {
    "question": ["What is RAG?"],
    "answer": [generated_answer],
    "contexts": [[retrieved_doc1, retrieved_doc2]],
    "ground_truth": ["RAG is Retrieval Augmented Generation..."]
}

# Evaluate
result = evaluate(
    eval_data,
    metrics=[
        faithfulness,
        answer_relevancy,
        context_relevancy,
        context_recall
    ]
)

print(result)
```

### A/B Testing
```python
import random

def ab_test_rag(query, variant_a, variant_b, n_tests=100):
    results = {"a": [], "b": []}
    
    for _ in range(n_tests):
        variant = random.choice(["a", "b"])
        if variant == "a":
            answer = variant_a.query(query)
            results["a"].append(evaluate_answer(answer))
        else:
            answer = variant_b.query(query)
            results["b"].append(evaluate_answer(answer))
    
    return {
        "a_avg": sum(results["a"]) / len(results["a"]),
        "b_avg": sum(results["b"]) / len(results["b"])
    }
```

**Best Practice:** Continuously evaluate and iterate on your RAG system!
                """
            }
        ],
        "quiz": [
            {
                "question": "What is the purpose of reranking in RAG?",
                "options": ["Make it faster", "Improve precision by reordering results", "Reduce costs", "Add metadata"],
                "correct": 1,
                "explanation": "Reranking improves precision by using a more sophisticated model to reorder the initially retrieved documents, ensuring the most relevant ones are at the top."
            }
        ]
    },
    
    "dd-14": {
        "title": "AutoGen: Multi-Agent Conversations",
        "sections": [
            {
                "title": "Introduction to AutoGen",
                "content": """
AutoGen is Microsoft's framework for building multi-agent conversational systems. It enables complex workflows through agent collaboration.

### Key Features
- **Conversational Agents:** Agents that can chat with each other
- **Code Execution:** Agents can write and run code
- **Human-in-the-Loop:** Optional human feedback
- **Flexible Workflows:** Sequential, parallel, or custom patterns

### Installation
```bash
pip install pyautogen
```

### Core Concepts

**AssistantAgent** - AI agent that can reason and code
**UserProxyAgent** - Represents the user, can execute code
**GroupChat** - Multiple agents in conversation
**GroupChatManager** - Orchestrates group conversations
                """
            },
            {
                "title": "Building a Coding Assistant",
                "content": """
Let's build a system where agents collaborate to solve coding problems.

### Step 1: Configure LLM
```python
import autogen

config_list = [
    {
        "model": "gpt-4",
        "api_key": "your-openai-key"
    }
]

llm_config = {
    "config_list": config_list,
    "temperature": 0
}
```

### Step 2: Create Agents
```python
# Assistant that writes code
assistant = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config,
    system_message='''You are a helpful AI assistant.
    Solve tasks using your coding and language skills.
    Suggest Python code in markdown blocks.
    '''
)

# User proxy that executes code
user_proxy = autogen.UserProxyAgent(
    name="User",
    human_input_mode="NEVER",  # Fully autonomous
    max_consecutive_auto_reply=10,
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False  # Set True for safety
    }
)
```

### Step 3: Start Conversation
```python
user_proxy.initiate_chat(
    assistant,
    message='''Create a function to calculate the Fibonacci 
    sequence up to n terms. Then test it with n=10.'''
)
```

**What Happens:**
1. Assistant writes the code
2. User proxy executes it
3. If there's an error, assistant fixes it
4. Continues until task is complete

### Multi-Agent Collaboration
```python
# Planner agent
planner = autogen.AssistantAgent(
    name="Planner",
    system_message='''You are a planner. Break down complex 
    tasks into steps. Don't write code.''',
    llm_config=llm_config
)

# Coder agent
coder = autogen.AssistantAgent(
    name="Coder",
    system_message='''You are a coder. Implement the plan 
    with Python code.''',
    llm_config=llm_config
)

# Reviewer agent
reviewer = autogen.AssistantAgent(
    name="Reviewer",
    system_message='''You are a code reviewer. Check for bugs, 
    suggest improvements.''',
    llm_config=llm_config
)

# Executor
executor = autogen.UserProxyAgent(
    name="Executor",
    human_input_mode="NEVER",
    code_execution_config={"work_dir": "coding"}
)

# Group chat
groupchat = autogen.GroupChat(
    agents=[planner, coder, reviewer, executor],
    messages=[],
    max_round=12
)

manager = autogen.GroupChatManager(
    groupchat=groupchat,
    llm_config=llm_config
)

# Start
executor.initiate_chat(
    manager,
    message="Build a web scraper for news articles"
)
```

**Workflow:**
1. Planner creates a plan
2. Coder implements it
3. Executor runs the code
4. Reviewer checks quality
5. Iterate until complete

**Pro Tip:** Use `human_input_mode="TERMINATE"` to require human approval before code execution!
                """
            }
        ],
        "quiz": [
            {
                "question": "What is the role of UserProxyAgent in AutoGen?",
                "options": ["Write code", "Execute code and represent the user", "Review code", "Plan tasks"],
                "correct": 1,
                "explanation": "UserProxyAgent executes code written by AssistantAgent and represents the user in the conversation, optionally allowing human input."
            }
        ]
    }
}
