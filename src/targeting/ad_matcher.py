from src.models.llm import generate_text

def match_ads(context):
    # In a real scenario, you'd have a database of ads to choose from
    ads = [
        "New smartphone with advanced AI features!",
        "Subscribe to our sports streaming service",
        "Learn coding with our online courses",
        "Get fit with our new smart fitness tracker",
        "Exclusive tech news subscription"
    ]
    
    # Use the LLM to rank ads based on the context
    prompt = f"Given the user context: {context}, rank the following ads from most to least relevant:\n"
    prompt += "\n".join(ads)
    
    ranked_ads = generate_text(prompt).split("\n")
    
    return ranked_ads[:3]  # Return top 3 ads