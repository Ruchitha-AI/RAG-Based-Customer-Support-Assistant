ShopEase: Agentic RAG Customer Support Assistant
🚀 Agentic AI Intern Project | Innomatics Research Labs
📌 Project Overview
ShopEase is a high-performance AI support agent designed to move beyond simple chatbots. Built using an Agentic RAG (Retrieval-Augmented Generation) framework, this system doesn't just retrieve data; it evaluates its own confidence and uses internal logic to decide whether to answer a customer or escalate the request to a human supervisor.

Key Capabilities:
Agentic Orchestration: Uses LangGraph to manage complex state transitions and non-linear decision-making.

High-Speed Reasoning: Powered by Llama 3.3 (70B) via the Groq LPU for sub-second response times.

Intelligent Routing: Automated safety guardrails detect high-risk intents (Refunds, Legal) and trigger escalation protocols.

Context-Aware Retrieval: Semantic search via HuggingFace Embeddings ensures the AI is grounded in the knowledge_base.pdf.

🏗️ System Architecture
The project follows a modular, three-tier architecture:

Ingestion Layer: Loads PDF data, performs recursive character splitting (1000-char chunks), and creates vector embeddings.

Retrieval Layer: Conducts similarity searches in ChromaDB and calculates a metadata-based confidence score.

Agentic Brain: A LangGraph state machine that routes queries based on intent and retrieval quality.

🚦 Decision Logic & Safety Guardrails
To ensure enterprise-grade reliability, the agent passes every query through a Conditional Router:

Intent Check: Scans for "Risk Keywords" (refund, manager, urgent).

Confidence Threshold: Checks if the vector search yielded sufficient supporting evidence (docs >= 2).

Escalation Path: If risks are detected or confidence is low, the system bypasses the LLM and triggers the escalate_node to prevent hallucinations.

🛠️ Tech Stack
Core: Python 3.12

AI Orchestration: LangGraph, LangChain

Inference: Groq API (Llama-3.3-70b-versatile)

Embeddings: all-MiniLM-L6-v2

Storage: ChromaDB (Vector Store)

🚀 Installation & Usage
Clone the Repository:

Bash
git clone https://github.com/Ruchitha-AI/ShopEase-Agentic-RAG.git
cd ShopEase-Agentic-RAG
Environment Setup:
Create a .env file in the root directory:

Code snippet
GROQ_API_KEY=your_groq_api_key_here
Install Requirements:

Bash
pip install -r requirements.txt
Process Documents:

Bash
python data/ingest.py
Launch the Agent:

Bash
python data/graph.py
