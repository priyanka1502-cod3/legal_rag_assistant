def chunk_text(text, chunk_size=1000, overlap=200):
    chunks = []

    text = " ".join(text.split())

    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks


def create_chunks(documents):
    chunked_docs = []

    for doc in documents:
        chunks = chunk_text(doc["text"])

        for i, chunk in enumerate(chunks):
            chunked_docs.append({
                "text": chunk,
                "metadata": {
                    **doc["metadata"],
                    "chunk_id": i
                }
            })

    return chunked_docs