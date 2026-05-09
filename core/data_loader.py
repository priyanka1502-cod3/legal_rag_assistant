from datasets import load_dataset


def load_cuad_documents(limit=30):
    dataset = load_dataset(
        "theatticusproject/cuad",
        split=f"train[:{limit}]",
        verification_mode="no_checks"
    )

    documents = []

    for idx, item in enumerate(dataset):
        text_parts = []

        try:
            pdf_obj = item.get("pdf")

            if pdf_obj is not None and hasattr(pdf_obj, "pages"):
                for page in pdf_obj.pages:
                    text = page.extract_text()
                    if text:
                        text_parts.append(text.strip())

            # fallback: check common text columns
            for key in ["text", "context", "contract", "document"]:
                if key in item and item[key]:
                    text_parts.append(str(item[key]))

            full_text = "\n".join(text_parts)

            if full_text.strip():
                documents.append({
                    "text": full_text,
                    "metadata": {
                        "doc_id": idx
                    }
                })

        except Exception as e:
            print(f"Skipping document {idx}: {e}")
            continue

    return documents