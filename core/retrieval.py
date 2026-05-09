import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


class LegalRetriever:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.embedding_model = SentenceTransformer(model_name)
        self.index = None
        self.chunked_docs = []

    def build_index(self, chunked_docs):
        self.chunked_docs = chunked_docs

        texts = [doc["text"] for doc in chunked_docs]
        embeddings = self.embedding_model.encode(texts, normalize_embeddings=True)

        embedding_matrix = np.array(embeddings).astype("float32")
        dimension = embedding_matrix.shape[1]

        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embedding_matrix)

        return len(chunked_docs)

    def retrieve(self, query, top_k=5):
        if self.index is None:
            return []

        query_embedding = self.embedding_model.encode([query], normalize_embeddings=True)
        query_embedding = np.array(query_embedding).astype("float32")

        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for idx, distance in zip(indices[0], distances[0]):
            if idx == -1:
                continue

            results.append({
                "text": self.chunked_docs[idx]["text"],
                "metadata": self.chunked_docs[idx].get("metadata", {}),
                "distance": float(distance)
            })

        return results