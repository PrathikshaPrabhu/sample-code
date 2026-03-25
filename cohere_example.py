import os
import cohere

co = cohere.ClientV2(api_key=os.getenv("COHERE_API_KEY"))

def query_cohere(prompt):
    try:
        response = co.chat(
            model="command-a-03-2025",   # latest as of 2025
            messages=[{"role": "user", "content": prompt}],
        )
        return response.message.content[0].text
    except Exception as e:
        print("Error type:", type(e).__name__)
        print("Full error:", repr(e))
        return "Failed."

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying Cohere...")
    print(query_cohere(user_prompt))