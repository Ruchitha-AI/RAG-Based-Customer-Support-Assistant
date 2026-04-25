# retriever.py
from ingest import load_vectorstore

def retrieve_context(query: str, k: int = 4):
    """
    Retrieve top-k relevant chunks from ChromaDB.
    Returns (context_text, confidence_level)
    """
    try:
        # 1. Load the database using the function in ingest.py
        vectorstore = load_vectorstore()
        
        # 2. Set up the retriever
        retriever = vectorstore.as_retriever(search_kwargs={"k": k})
        
        # 3. Fetch documents
        docs = retriever.invoke(query)

        if not docs:
            return "No relevant information found.", "low"

        # 4. Build context string
        context = "\n\n".join([doc.page_content for doc in docs])

        # 5. Simple confidence check
        confidence = "high" if len(docs) >= 2 else "low"

        return context, confidence
        
    except Exception as e:
        print(f"❌ Error during retrieval: {e}")
        return f"Error retrieving context: {str(e)}", "low"