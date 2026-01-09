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
    }
}
