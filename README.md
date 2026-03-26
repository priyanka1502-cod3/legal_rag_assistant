# Legal Document RAG Assistant

A production-style Retrieval-Augmented Generation (RAG) system for answering questions from legal contract documents using FAISS, Sentence Transformers, FLAN-T5, and Gradio.

---

## 🚀 Overview

This project builds an end-to-end legal document assistant using the **CUAD (Contract Understanding Atticus Dataset)**.

It extracts text from contract PDFs, converts them into embeddings, retrieves relevant chunks using FAISS, and generates context-aware answers using an LLM.

---

## ✨ Features

* 📄 PDF contract processing
* 🔍 Semantic search with FAISS
* 🧠 LLM-based answer generation (FLAN-T5)
* 🧩 Text chunking with overlap
* 📊 Retrieval & answer evaluation
* ⚠️ Hallucination detection
* 📈 Confidence scoring
* 💻 Interactive Gradio UI

---

## 🏗️ Architecture

```
PDF Contracts → Text Extraction → Chunking → Embeddings → FAISS Index
        → Retrieval → Context → FLAN-T5 → Answer + Confidence
```

---

## 🧠 Tech Stack

* Python
* Hugging Face Datasets
* Sentence Transformers (`all-MiniLM-L6-v2`)
* FAISS
* Transformers (`google/flan-t5-base`)
* pdfplumber
* Gradio
* PyTorch

---

## 📊 Evaluation

This project evaluates RAG performance using:

### 1. Retrieval Accuracy (Hit@K)

Checks if relevant clauses are retrieved.

### 2. Answer Accuracy

Checks if expected keywords appear in answers.

### 3. Hallucination Score

Measures overlap between generated answer and retrieved context.

---

## 💡 Example Questions

* Are there indemnification clauses?
* What
