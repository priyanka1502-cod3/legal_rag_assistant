import os
from groq import Groq


GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_legal_answer(query, results):
    context = "\n\n".join(
        [f"Source {i+1}:\n{r['text'][:1200]}" for i, r in enumerate(results)]
    )

    system_prompt = """
You are a legal document intelligence assistant.
Use ONLY the provided contract context.
Do not give legal advice.
Do not hallucinate.
If the answer is not found in the context, say: "I could not find this information in the retrieved contract clauses."
Write in clear, professional language.
""".strip()

    user_prompt = f"""
Contract Context:
{context}

User Question:
{query}

Answer format:
Short Answer:
- ...

Relevant Clauses / Evidence:
- ...

Risk or Obligation Notes:
- ...
""".strip()

    try:
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.2,
            max_tokens=500,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Groq generation failed: {e}"