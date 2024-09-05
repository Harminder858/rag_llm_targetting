def generate_context_analysis_prompt(user_data, similar_contexts):
    prompt = f"Analyze the following user data: {user_data}\n\n"
    prompt += "Similar contexts:\n"
    for context in similar_contexts:
        prompt += f"- {context}\n"
    prompt += "\nProvide a brief analysis of the user's interests and behavior based on this information."
    return prompt

def generate_ad_ranking_prompt(user_context, ads):
    prompt = f"Given the following user context:\n{user_context}\n\n"
    prompt += "Rank the following ads from most to least relevant:\n"
    for ad in ads:
        prompt += f"- {ad}\n"
    prompt += "\nProvide the ranked list of ads, with brief explanations for each ranking."
    return prompt