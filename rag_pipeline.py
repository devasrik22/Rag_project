import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Setup paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_DB_DIR = os.path.join(BASE_DIR, "..", "milestone1", "chroma_db")
COLLECTION_NAME = "milestone1_collection"
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

def initialize_vector_store():
    """
    Initializes and returns the Chroma vector store.
    """
    if not os.path.exists(CHROMA_DB_DIR):
        raise FileNotFoundError(f"ChromaDB directory not found at {CHROMA_DB_DIR}. Please run milestone 1 first.")
        
    print(f"Loading embeddings ({EMBEDDING_MODEL_NAME})...")
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME,
        model_kwargs={'device': 'cpu'}
    )
    
    print(f"Loading Chroma Vector Store from {CHROMA_DB_DIR}...")
    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=CHROMA_DB_DIR
    )
    return vector_store

def initialize_llm():
    """
    Initializes and returns the ChatGroq model.
    """
    api_key = os.getenv("Groq_API_KEY")
    if not api_key or api_key == "your_groq_api_key_here":
        raise ValueError("Groq_API_KEY not found or is invalid in the environment variables.")
        
    print("Initializing ChatGroq LLM...")
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=api_key,
        temperature=0.3
    )
    return llm

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def build_rag_chain(vector_store, llm):
    """
    Builds the Retrieval-Augmented Generation chain using LCEL.
    """
    print("Building Retrieval QA Chain...")
    # Retrieve top 3 relevant chunks
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    
    # System prompt for the QA
    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer the question. "
        "If you don't know the answer, say that you don't know. "
        "Use three sentences maximum and keep the answer concise."
        "\n\nContext:"
        "\n{context}"
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}")
    ])
    
    rag_chain_from_docs = (
        RunnablePassthrough.assign(context=(lambda x: format_docs(x["context"])))
        | prompt
        | llm
        | StrOutputParser()
    )
    
    rag_chain_with_source = RunnableParallel(
        {"context": retriever, "input": RunnablePassthrough()}
    ).assign(answer=rag_chain_from_docs)
    
    return rag_chain_with_source

def query_rag(rag_chain, query: str):
    """
    Executes a query against the RAG chain and prints the answer and source citations.
    """
    print(f"\n--- Query: {query} ---")
    response = rag_chain.invoke(query)
    
    answer = response.get("answer", "No answer generated.")
    context_docs = response.get("context", [])
    
    print("\n[Answer]:")
    print(answer)
    print("\n[Sources Cited]:")
    
    if not context_docs:
        print("No sources found.")
    else:
        # Avoid duplicate source citations by collecting them in a set/dict
        sources_seen = set()
        for i, doc in enumerate(context_docs):
            source = doc.metadata.get("source", "Unknown")
            page = doc.metadata.get("page", "N/A")
            cite_key = f"{source} (Page: {page})"
            if cite_key not in sources_seen:
                sources_seen.add(cite_key)
                # Print a clean basename if possible
                source_basename = os.path.basename(source) if source != "Unknown" else source
                print(f"- {source_basename} (Page: {page})")
            
    print("-" * 50)

def main():
    try:
        vector_store = initialize_vector_store()
        llm = initialize_llm()
        rag_chain = build_rag_chain(vector_store, llm)
        
        print("\nPipeline Ready. Running Sample Queries...\n")
        
        # Test queries
        test_queries = [
            "What is generative AI?",
            "What are some applications of LLMs?",
            "What are the main topics discussed in the document?"
        ]
        
        for q in test_queries:
            query_rag(rag_chain, q)
            
    except Exception as e:
        print(f"\n[Error]: {e}")

if __name__ == "__main__":
    main()
