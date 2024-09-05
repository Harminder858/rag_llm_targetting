from src.models.embeddings import get_embedding
from src.retrieval.vector_store import search_vector_store

def analyze_context(user_id):
    # In a real scenario, you'd fetch user data from a database
    user_data = f"User {user_id} is interested in technology and sports."
    
    # Get embedding for user data
    user_embedding = get_embedding(user_data)
    
    # Search for similar contexts
    similar_contexts = search_vector_store(user_embedding)
    
    # Analyze the similar contexts
    context = {
        "interests": ["technology", "sports"],
        "similar_users": [context[0] for context in similar_contexts],
        "similarity_scores": [context[1] for context in similar_contexts]
    }
    
    return context