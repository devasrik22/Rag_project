# RAG Document Analysis using LangChain

## 📌 Project Overview
This project implements a Retrieval-Augmented Generation (RAG) pipeline using:
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Groq LLM

The system loads documents, creates embeddings, stores them in a vector database, and answers user queries based on document context.

---

## 🚀 Features
- Document loading
- Text chunking
- Vector storage using ChromaDB
- Retrieval-based question answering
- LLM response generation

---

## 🛠 Installation

```bash
git clone https://github.com/devasrik22/Rag_project.git
cd Rag_project
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶ Run Project

```
python eg.py
```

---

## 📚 Tech Stack
- Python
- LangChain
- ChromaDB
- HuggingFace
- Groq