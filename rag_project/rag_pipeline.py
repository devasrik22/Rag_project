import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

db = None

# ✅ Chat history storage
chat_history = []


# ✅ Process PDF and store embeddings
def process_pdf(file_path):
    global db

    # Load PDF
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(docs)

    # Create embeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # Store in Chroma DB
    db = Chroma.from_documents(chunks, embeddings)


# ✅ Ask question with chat history memory
def ask_question(query):
    global db, chat_history

    if db is None:
        return "Please upload a document first."

    # Chat history
    history_text = ""
    for q, a in chat_history:
        history_text += f"User: {q}\nAssistant: {a}\n"

    final_query = history_text + f"User: {query}"

    # Retrieve docs
    docs = db.similarity_search(final_query)
    context = " ".join([doc.page_content for doc in docs])

    # ✅ FIXED INDENTATION
    llm = ChatGroq(
        model_name="openai/gpt-oss-120b",
        temperature=0
    )

    prompt = f"""
You are a helpful AI assistant.

Use the following context to answer the question.

Context:
{context}

Conversation so far:
{history_text}

User Question:
{query}

Answer clearly:
"""

    try:
        print("LLM CALLED")

        response = llm.invoke(prompt)

        print("LLM RESPONSE:", response)

        answer = response.content

    except Exception as e:
        print("ERROR:", e)
        return "Model error. Please try again."

    # Save history
    chat_history.append((query, answer))

    if len(chat_history) > 5:
        chat_history.pop(0)

    return answer