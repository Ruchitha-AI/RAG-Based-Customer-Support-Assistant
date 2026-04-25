import os
import sys
from dotenv import load_dotenv
from typing import TypedDict, Literal
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, END

# ─── 1. Setup Paths and Environment ──────────────────────────────
# We look in the current folder AND the parent folder for .env
load_dotenv() # Looks in data/
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env")) # Looks in root

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("❌ API Key NOT found. Checking paths...")
    print(f"Looked in: {os.getcwd()}")
else:
    print("✅ Key loaded successfully!")

# Ensure the 'data' directory is in the system path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from retriever import retrieve_context

# ─── 2. State Definition ──────────────────────────────────────────
class GraphState(TypedDict):
    query: str
    context: str
    answer: str
    confidence: str 
    needs_escalation: bool

# ─── 3. LLM Setup ──────────────────────────────────────────────────
# We pass the api_key explicitly to avoid any more GroqErrors
llm = ChatGroq(
    api_key=api_key,
    model_name="llama-3.3-70b-versatile"
)

# ─── 4. Nodes ─────────────────────────────────────────────────────
def retrieve_node(state: GraphState) -> GraphState:
    print("🔍 Searching knowledge base...")
    context, confidence = retrieve_context(state["query"])
    return {**state, "context": context, "confidence": confidence}

def generate_node(state: GraphState) -> GraphState:
    print("🤖 Generating AI response...")
    prompt = f"""You are a ShopEase support assistant. Use the context to answer.
    Context: {state['context']}
    Question: {state['query']}
    Answer:"""
    response = llm.invoke(prompt)
    return {**state, "answer": response.content, "needs_escalation": False}

def escalate_node(state: GraphState) -> GraphState:
    print("⚠️ Escalating to human...")
    return {**state, "answer": "⚠️ This query has been escalated to a human agent.", "needs_escalation": True}

# ─── 5. Router Logic ──────────────────────────────────────────────
def route_query(state: GraphState) -> Literal["generate", "escalate"]:
    return "generate" 
    query = state["query"].lower()
    confidence = state.get("confidence", "low")
    
    escalation_keywords = ["refund", "legal", "urgent", "speak to human", "manager"]
    
    if any(kw in query for kw in escalation_keywords) or confidence == "low":
        return "escalate"
    return "generate"

# ─── 6. Build Graph ───────────────────────────────────────────────
workflow = StateGraph(GraphState)
workflow.add_node("retrieve", retrieve_node)
workflow.add_node("generate", generate_node)
workflow.add_node("escalate", escalate_node)

workflow.set_entry_point("retrieve")
workflow.add_conditional_edges(
    "retrieve", 
    route_query, 
    {"generate": "generate", "escalate": "escalate"}
)
workflow.add_edge("generate", END)
workflow.add_edge("escalate", END)

app = workflow.compile()

# ─── 7. Execution ──────────────────────────────────────────────────
if __name__ == "__main__":
    if not api_key:
        print("❌ Final check: Still no API key. Please save your .env file!")
    else:
        print("🚀 Agentic RAG is Online! (Type 'exit' to quit)")
        
        while True:
            user_query = input("\n👤 YOU: ")
            
            if user_query.lower() in ["exit", "quit", "q"]:
                print("👋 Goodbye!")
                break
            
            inputs = {"query": user_query} 
            
            # This runs the graph for your specific question
            for output in app.stream(inputs):
                for key, value in output.items():
                    # We only want to print the final response to the user
                    if "answer" in value and value["answer"]:
                        print(f"\n🤖 AI: {value['answer']}")