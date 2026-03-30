import requests
import os
from dotenv import load_dotenv
from prompts import zero_shot, few_shot, SYSTEM_PROMPT

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

def get_response(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": prompt}
]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']

if __name__ == "__main__":
    print("Chatbot started (type exit to stop)")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        mode = input("Mode (zero/few/compare): ")

        if mode == "compare":
            zero_prompt = zero_shot(user_input)
            few_prompt = few_shot(user_input)

            zero_reply = get_response(zero_prompt)
            few_reply = get_response(few_prompt)

            print("\n--- ZERO SHOT ---")
            print(zero_reply)

            print("\n--- FEW SHOT ---")
            print(few_reply)

        else:
            if mode == "few":
                prompt = few_shot(user_input)
            else:
                prompt = zero_shot(user_input)

            reply = get_response(prompt)

            print("\n--- Prompt Used ---")
            print(prompt)

            print("\n--- AI Response ---")
            print(reply)