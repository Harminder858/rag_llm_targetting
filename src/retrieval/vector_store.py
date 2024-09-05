import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class VectorStore:
    def __init__(self):
        self.vectors = {}

    def add_vector(self, key, vector):
        self.vectors[key] = vector

    def search(self, query_vector, top_k=5):
        similarities = {k: cosine_similarity([query_vector], [v])[0][0] for k, v in self.vectors.items()}
        return sorted(similarities.items(), key=lambda x: x[1], reverse=True)[:top_k]

vector_store = VectorStore()

def add_to_vector_store(key, vector):
    vector_store.add_vector(key, vector)

def search_vector_store(query_vector, top_k=5):
    return vector_store.search(query_vector, top_k)