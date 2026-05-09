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
    formatted = []

    for i, r in enumerate(results, 1):
        distance = round(r["distance"], 4)

        source = f"""
📄 Source {i}
━━━━━━━━━━━━━━━━━━
• Similarity Score: {distance}
• Document ID: {r['metadata'].get('doc_id')}
• Chunk ID: {r['metadata'].get('chunk_id')}

Clause Preview:
{r['text'][:500]}

"""

        formatted.append(source)

    return "\n".join(formatted)