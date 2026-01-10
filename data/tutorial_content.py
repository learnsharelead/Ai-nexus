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
    
    # NEW TUTORIAL CONTENT (January 2026)
    "dd-8": {
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
    
    "dd-9": {
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
    backstory="""You are an expert researcher with a keen eye for 
    credible sources and relevant data. You excel at finding the 
    most important information quickly.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Writer Agent
writer = Agent(
    role='Content Writer',
    goal='Create engaging, well-structured content',
    backstory="""You are a skilled writer who can transform research 
    into compelling narratives. You write with clarity and style.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Editor Agent
editor = Agent(
    role='Content Editor',
    goal='Refine content for clarity, grammar, and impact',
    backstory="""You are a meticulous editor with an eye for detail. 
    You ensure every piece of content is polished and professional.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)
```

### Step 2: Define Tasks
```python
research_task = Task(
    description="""Research the topic: {topic}
    Find key points, statistics, and recent developments.
    Provide a comprehensive research summary.""",
    agent=researcher,
    expected_output="Detailed research summary with sources"
)

writing_task = Task(
    description="""Using the research provided, write a 500-word blog post 
    about {topic}. Make it engaging and informative.""",
    agent=writer,
    expected_output="Complete blog post draft"
)

editing_task = Task(
    description="""Edit the blog post for:
    - Grammar and spelling
    - Clarity and flow
    - Engagement and impact
    Provide the final polished version.""",
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
    backstory="""You are an experienced project manager who 
    knows how to get the best from your team.""",
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
    
    "dd-10": {
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
    
    "dd-11": {
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
    system_message="""You are a helpful AI assistant.
    Solve tasks using your coding and language skills.
    Suggest Python code in markdown blocks.
    """
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
    message="""Create a function to calculate the Fibonacci 
    sequence up to n terms. Then test it with n=10."""
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
    system_message="""You are a planner. Break down complex 
    tasks into steps. Don't write code.""",
    llm_config=llm_config
)

# Coder agent
coder = autogen.AssistantAgent(
    name="Coder",
    system_message="""You are a coder. Implement the plan 
    with Python code.""",
    llm_config=llm_config
)

# Reviewer agent
reviewer = autogen.AssistantAgent(
    name="Reviewer",
    system_message="""You are a code reviewer. Check for bugs, 
    suggest improvements.""",
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
