import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

CHROMA_PATH = os.path.join(os.path.dirname(__file__), "..", "chroma_db")
DATA_PATH = os.path.join(os.path.dirname(__file__), "knowledge_base.pdf")

def ingest_pdf():
    # 1. Load the PDF
    print("📄 Loading PDF...")
    if not os.path.exists(DATA_PATH):
        print(f"❌ Error: File not found at {DATA_PATH}")
        return

    loader = PyPDFLoader(DATA_PATH)
    documents = loader.load()
    print(f"✅ Loaded {len(documents)} pages")

    # 2. Split text into chunks
    print("✂️ Splitting text into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(documents)

    # 3. Create Embeddings
    print("🧠 Generating embeddings...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # 4. Save to Chroma DB
    print(f"📦 Saving {len(chunks)} chunks to {CHROMA_PATH}...")
    db = Chroma.from_documents(chunks, embeddings, persist_directory=CHROMA_PATH)
    
    print("🚀 Done! Your database is ready.")

if __name__ == "__main__":
    ingest_pdf()
def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)