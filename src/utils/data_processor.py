import json
from src.models.embeddings import get_embedding
from src.retrieval.vector_store import add_to_vector_store

def process_user_data(file_path='src/data/user_profiles.json'):
    with open(file_path, 'r') as f:
        user_data = json.load(f)
    
    for user in user_data['users']:
        user_text = f"User {user['id']} is interested in {', '.join(user['interests'])}."
        user_embedding = get_embedding(user_text)
        add_to_vector_store(f"user_{user['id']}", user_embedding)

def process_content_data(file_path='src/data/content_catalog.json'):
    with open(file_path, 'r') as f:
        content_data = json.load(f)
    
    for content in content_data['content']:
        content_text = f"{content['title']}. {content['description']}"
        content_embedding = get_embedding(content_text)
        add_to_vector_store(f"content_{content['id']}", content_embedding)

def process_ad_data(file_path='src/data/ad_inventory.json'):
    with open(file_path, 'r') as f:
        ad_data = json.load(f)
    
    for ad in ad_data['ads']:
        ad_text = f"{ad['title']}. {ad['description']}"
        ad_embedding = get_embedding(ad_text)
        add_to_vector_store(f"ad_{ad['id']}", ad_embedding)

def process_all_data():
    process_user_data()
    process_content_data()
    process_ad_data()