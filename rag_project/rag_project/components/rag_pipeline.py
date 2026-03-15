import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline


vector_db = None
retriever = None
llm = None

UPLOAD_FOLDER = "uploaded_files"


def load_llm():
    global llm

    pipe = pipeline(
        "text2text-generation",
        model="google/flan-t5-small",
        max_length=256
    )

    llm = HuggingFacePipeline(pipeline=pipe)


def process_document(file_path):

    global vector_db
    global retriever

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_db = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory="chroma_db"
    )

    vector_db.persist()

    retriever = vector_db.as_retriever(search_kwargs={"k": 3})


def load_existing_documents():

    global retriever

    if not os.path.exists(UPLOAD_FOLDER):
        return

    files = os.listdir(UPLOAD_FOLDER)

    for file in files:
        if file.endswith(".pdf"):
            file_path = os.path.join(UPLOAD_FOLDER, file)
            process_document(file_path)
            break


def ask_question(question):

    global retriever
    global llm

    if retriever is None:
        load_existing_documents()

    if retriever is None:
        return "Please upload a document first."

    if llm is None:
        load_llm()

    # Use the standard retriever API and handle empty results.
    try:
        docs = retriever.get_relevant_documents(question)
    except AttributeError:
        # Fallback for retrievers that may expose invoke
        docs = retriever.invoke(question)

    if not docs:
        return "No relevant passages found in uploaded documents. Please upload a different document or ask another question."

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an AI assistant.

Use ONLY the context below to answer the question.

Context:
{context}

Question:
{question}

Answer in a short clear sentence.
"""

    response = llm.invoke(prompt)

    if isinstance(response, list) and response:
        # Some wrappers return a list of text results.
        response = response[0]

    return str(response)