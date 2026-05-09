from datasets import load_dataset
import pdfplumber
import tempfile


def load_cuad_documents(limit=30):
    dataset = load_dataset(
        "theatticusproject/cuad",
        split=f"train[:{limit}]",
        verification_mode="no_checks"
    )

    documents = []

    for idx, item in enumerate(dataset):
        pdf_obj = item["pdf"]

        try:
            with tempfile.NamedTemporaryFile(suffix=".pdf") as tmp:
                tmp.write(pdf_obj)
                tmp.flush()

                text_parts = []

                with pdfplumber.open(tmp.name) as pdf:
                    for page in pdf.pages:
                        text = page.extract_text()
                        if text:
                            text_parts.append(text.strip())

                full_text = "\n".join(text_parts)

                if full_text.strip():
                    documents.append({
                        "text": full_text,
                        "metadata": {
                            "doc_id": idx
                        }
                    })

        except Exception:
            continue

    return documents