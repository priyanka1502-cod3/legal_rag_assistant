# ⚖️ Legal AI Contract Review Assistant

A production-style Legal AI system built using Retrieval-Augmented Generation (RAG), FAISS semantic search, CUAD legal contract datasets, and Groq-hosted Llama 3.

The system analyzes legal contracts, retrieves relevant clauses, performs evidence-grounded legal Q&A, and provides confidence-aware legal clause analysis.

---

# 🌐 Live Demo

🚀 https://huggingface.co/spaces/priyankkaa/legal-ai-contract-review-assistant

---

# 📸 Application Preview

## Legal Contract Analysis UI

<img width="1918" height="700" alt="image" src="https://github.com/user-attachments/assets/aeddd135-5504-4de8-9125-db9dd81599b4" />


## Evidence-Grounded Clause Retrieval

<img width="1853" height="950" alt="image" src="https://github.com/user-attachments/assets/9162ac79-af8a-4828-9ab2-80712ac35c45" />
<img width="1310" height="754" alt="image" src="https://github.com/user-attachments/assets/07ed570c-2a09-4d6a-81cd-e05d7b5e1630" />


---

# ✨ Features

- 📄 Legal contract document analysis
- 🔍 Semantic clause retrieval using FAISS
- 🧠 Groq-hosted Llama 3 answer generation
- ⚖️ Legal risk & obligation analysis
- 📚 Evidence-grounded legal responses
- 📊 Confidence assessment
- ⚠️ Hallucination-aware retrieval workflow
- 💻 Interactive Gradio-based legal assistant UI
- ☁️ Live deployment on Hugging Face Spaces

---

# 🏗️ System Architecture

```text
CUAD Contracts
      ↓
Text Extraction
      ↓
Chunking
      ↓
SentenceTransformer Embeddings
      ↓
FAISS Vector Store
      ↓
Semantic Retrieval
      ↓
Groq Llama 3
      ↓
Legal Analysis + Evidence + Confidence
```

---

# 🧠 Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| Vector Search | FAISS |
| Embeddings | SentenceTransformers |
| Dataset | CUAD |
| LLM | Groq Llama 3 |
| Frontend | Gradio |
| Deployment | Hugging Face Spaces |

---

# ⚙️ Core Capabilities

- Legal clause retrieval
- Contract semantic search
- Evidence-grounded legal Q&A
- Contract obligation analysis
- Legal risk identification
- Confidence-aware response generation
- Hallucination reduction workflow

---

# 📊 Evaluation Features

## Retrieval Accuracy (Hit@K)

Measures whether relevant legal clauses are retrieved successfully.

## Confidence Assessment

Estimates answer reliability using retrieval-context overlap.

## Hallucination Reduction

Grounds responses strictly within retrieved legal contract evidence.

---

# 💡 Example Questions

- Are there indemnification clauses?
- What liability limitations are mentioned?
- Are there termination conditions?
- What warranty disclaimers exist?
- Are there governing law clauses?
- Does the agreement mention arbitration?

---

# 🔥 Highlights

- Built an end-to-end Legal AI RAG pipeline
- Integrated FAISS semantic retrieval architecture
- Implemented Groq-hosted Llama 3 inference
- Designed evidence-grounded legal analysis workflow
- Deployed a production-style legal AI application

---

# 🚧 Future Improvements

- Clause highlighting
- Multi-contract comparison
- Streaming responses
- Legal PDF uploads
- Persistent vector databases
- LangGraph agent workflows
- Contract summarization reports

---

# ⚠️ Disclaimer

This application is for educational and research purposes only and does not provide legal advice.

---

# 👩‍💻 Author

Priyanka Choudhury

- GitHub: https://github.com/priyanka1502-cod3
- LinkedIn: https://www.linkedin.com/in/priyanka-choudhury-124b45101/
