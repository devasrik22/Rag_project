from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

import os
import shutil

# Startup Cleanup
if os.path.exists("./chroma_db"):
    shutil.rmtree("./chroma_db")
    print("Old vector database removed.")

# 1️⃣ Load PDFs
loader = DirectoryLoader(
    path="data",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

documents = loader.load()
print("Loaded documents:", len(documents))

# 2️⃣ Split Text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=3000,
    chunk_overlap=200
)

split_docs = text_splitter.split_documents(documents)
print("After splitting:", len(split_docs))

for doc in split_docs:
    doc.metadata = {}
    
# 3️⃣ Create Embeddings
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 4️⃣ Store in Chroma Vector DB
vector_store = Chroma.from_documents(
    documents=split_docs,
    embedding=embedding_model,
    persist_directory="./chroma_db",
    collection_name="fresh_session"
)
vector_store.persist()
print("Vector database created successfully!")
