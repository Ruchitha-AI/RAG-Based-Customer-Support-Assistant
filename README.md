
# 🛍️ ShopEase: Agentic RAG Customer Support Assistant

### 🚀 Agentic AI Intern Project | Innomatics Research Labs

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![LangGraph](https://img.shields.io/badge/Orchestration-LangGraph-orange.svg)
![LLM](https://img.shields.io/badge/LLM-Llama_3.3_Groq-green.svg)
![VectorDB](https://img.shields.io/badge/VectorStore-ChromaDB-blue.svg)

---

## 📌 Project Overview

**ShopEase** is an intelligent, production-ready AI customer support assistant built using an **Agentic RAG (Retrieval-Augmented Generation)** framework.

Unlike traditional chatbots, this system **thinks, evaluates, and decides** before responding. It dynamically determines whether to:

* Answer confidently using retrieved knowledge
* Or escalate queries to a human for safety and accuracy

---

## ✨ Key Features

### 🤖 Agentic Intelligence

* Built using **LangGraph** for stateful, multi-step reasoning
* Enables **non-linear decision-making workflows**

### ⚡ High-Speed Inference

* Powered by **Llama 3.3 (70B)** via Groq
* Delivers **low-latency, real-time responses**

### 🧠 Context-Aware Retrieval

* Uses **HuggingFace embeddings (`all-MiniLM-L6-v2`)**
* Retrieves semantically relevant chunks from `knowledge_base.pdf`

### 🚦 Smart Routing & Guardrails

* Detects sensitive intents like:

  * Refund requests
  * Legal concerns
  * Urgent escalations
* Prevents hallucinations by enforcing **confidence-based decision logic**

## 🏗️ System Architecture

The system follows a **modular 3-layer architecture**:

### 1️⃣ Ingestion Layer

* Loads PDF documents
* Splits into chunks (1000 characters)
* Generates embeddings

### 2️⃣ Retrieval Layer

* Performs similarity search using **ChromaDB**
* Calculates confidence based on retrieved documents

### 3️⃣ Agentic Brain (LangGraph)

* Routes queries based on:

  * Intent
  * Confidence score
* Executes decision nodes (answer / escalate)

---

## 🚦 Decision Logic & Safety Guardrails

Every query passes through a **Conditional Router**:

* 🔍 **Intent Detection**
  Identifies risk keywords (`refund`, `urgent`, `manager`, etc.)

* 📊 **Confidence Check**
  Ensures sufficient supporting documents (`docs ≥ 2`)

* 🚨 **Escalation Path**
  If risk detected or confidence low → triggers `escalate_node`
  → avoids hallucinated responses

---

## 🛠️ Tech Stack

| Category      | Tools Used               |
| ------------- | ------------------------ |
| Language      | Python 3.12              |
| Orchestration | LangGraph, LangChain     |
| LLM           | Llama-3.3-70B (Groq API) |
| Embeddings    | all-MiniLM-L6-v2         |
| Vector Store  | ChromaDB                 |

---

## 🚀 Installation & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Ruchitha-AI/ShopEase-Agentic-RAG.git
cd ShopEase-Agentic-RAG
```

### 2️⃣ Environment Setup

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Ingest Documents

```bash
python data/ingest.py
```

### 5️⃣ Run the Agent

```bash
python data/graph.py
```

---

## 📈 Future Improvements

* Add **Streamlit UI / Web Interface**
* Integrate **real-time customer database APIs**
* Implement **feedback loop for continuous learning**
* Deploy using **Docker + Cloud (AWS/GCP)**

---

## 👩‍💻 About the Developer

**Ruchitha Penta**
🎓 B.Tech CSE (AI & ML)
🤖 Agentic AI Intern @ Innomatics Research Labs

Passionate about building:

* Intelligent AI systems
* Safe and reliable LLM applications
* Real-world scalable solutions

---
