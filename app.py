import gradio as gr

from core.data_loader import load_cuad_documents
from core.chunking import create_chunks
from core.retrieval import LegalRetriever
from core.generation import generate_legal_answer
from core.evaluation import confidence_score, format_sources


retriever = LegalRetriever()
is_index_ready = False


def build_legal_index(limit):
    global is_index_ready

    documents = load_cuad_documents(limit=int(limit))

    if not documents:
        return "No documents loaded from CUAD dataset."

    chunks = create_chunks(documents)
    total_chunks = retriever.build_index(chunks)

    is_index_ready = True

    return f"Loaded {len(documents)} legal documents and indexed {total_chunks} contract chunks."


def ask_legal_question(query, top_k):
    if not is_index_ready:
        return "Please build the legal document index first.", ""

    if not query.strip():
        return "Please enter a legal contract question.", ""

    results = retriever.retrieve(query, top_k=int(top_k))

    if not results:
        return "No relevant contract clauses found.", ""

    answer = generate_legal_answer(query, results)
    confidence = confidence_score(answer, results)
    sources = format_sources(results)

    final_answer = f"""### Answer
{answer}

---

### Confidence
{confidence}
"""

    return final_answer, sources


sample_questions = [
    "Are there indemnification clauses?",
    "What warranty disclaimer clauses are mentioned?",
    "Are there limitation of liability clauses?",
    "What governing law clauses are mentioned?",
    "Are there third-party beneficiary clauses?"
]


with gr.Blocks(theme=gr.themes.Soft(), title="Legal AI Contract Review Assistant") as demo:
    gr.Markdown("# Legal AI Contract Review Assistant")
    gr.Markdown(
        "Analyze legal contract clauses using Retrieval-Augmented Generation, "
        "FAISS vector search, CUAD contract data, and Groq Llama 3."
    )

    with gr.Row():
        limit = gr.Slider(
            minimum=5,
            maximum=50,
            value=20,
            step=5,
            label="Number of CUAD Contracts to Load"
        )

    build_btn = gr.Button("Build Legal Document Index")
    build_status = gr.Textbox(label="Indexing Status", interactive=False)

    build_btn.click(
        fn=build_legal_index,
        inputs=limit,
        outputs=build_status
    )

    query = gr.Textbox(
        label="Ask a Legal Contract Question",
        placeholder="Example: Are there indemnification clauses?"
    )

    top_k = gr.Slider(
        minimum=1,
        maximum=10,
        value=5,
        step=1,
        label="Top-K Retrieved Clauses"
    )

    ask_btn = gr.Button("Ask")

    answer = gr.Markdown(label="Answer")
    sources = gr.Textbox(label="Retrieved Contract Clauses", lines=16)

    ask_btn.click(
        fn=ask_legal_question,
        inputs=[query, top_k],
        outputs=[answer, sources]
    )

    gr.Examples(
        examples=[[q, 5] for q in sample_questions],
        inputs=[query, top_k]
    )

    gr.Markdown(
        """
        ---
        Built with CUAD, FAISS, Sentence Transformers, Groq Llama 3, and Gradio.
        This tool is for contract analysis assistance only and does not provide legal advice.
        """
    )


demo.launch(server_name="0.0.0.0", server_port=7860)