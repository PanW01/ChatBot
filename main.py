from openai import OpenAI
from context_loader import Context
import os

API_KEY = os.environ.get("API_KEY")

messages_history = []

topics, responses = Context.load()
instructions = "\n".join(
    f'- If the user says "{topic}" or something similar, respond with: "{response}"'
    for topic, response in zip(topics, responses)
)

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=API_KEY,    
)

def continue_chat(prompt: str):
    messages_history.append("User:" + prompt)
    response = client.chat.completions.create(
        model="gemini-2.5-flash-preview-05-20",
        messages=[
            {
                "role": "system", 
                "content": f"""You are a helpful AI assistant. Always respond in Spanish, and keep your replies under 100 words.
                Follow these strict rules: {instructions}, Don't answer literally, but naturally \n if user ask for something that is not in the rules, answer freely,\n this is the chat: {"\n".join(messages_history)}. \n
                You have to be kind, nice and polite with people. """,
            },
            {
                "role": "user", 
                "content": f"{prompt}"
            }
        ]
    )
    message = response.choices[0].message.content
    messages_history.append("AI: " + message)
    return message