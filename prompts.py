SYSTEM_PROMPT = """
You are a helpful AI assistant.
Always give:
1. Simple explanation
2. Example
3. Use bullet points
"""

def zero_shot(user_input):
    return f"""
Explain the following in simple terms with an example:

{user_input}
"""

def few_shot(user_input):
    return f"""
Answer strictly in this format:
- Definition:
- Example:

Q: What is AI?
A:
- Definition: AI is the simulation of human intelligence
- Example: chatbots, recommendation systems

Q: What is ML?
A:
- Definition: ML is a subset of AI
- Example: spam detection

Q: {user_input}
A:
"""