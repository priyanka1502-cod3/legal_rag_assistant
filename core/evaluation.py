def confidence_score(answer, results):
    if not answer or not results:
        return "Low confidence"

    context = " ".join([r["text"] for r in results]).lower()
    answer_words = set(answer.lower().split())

    overlap = len(answer_words & set(context.split()))
    score = overlap / max(len(answer_words), 1)

    if score < 0.25:
        return "Low confidence"
    elif score < 0.5:
        return "Medium confidence"
    else:
        return "High confidence"


def format_sources(results):
    sources = []

    for i, r in enumerate(results, start=1):
        metadata = r.get("metadata", {})
        doc_id = metadata.get("doc_id", "N/A")
        chunk_id = metadata.get("chunk_id", "N/A")
        distance = r.get("distance", 0)

        preview = r["text"][:450].replace("\n", " ").strip()

        sources.append(
            f"Source {i} | Document {doc_id} | Chunk {chunk_id} | Distance {distance:.4f}\n{preview}..."
        )

    return "\n\n".join(sources)