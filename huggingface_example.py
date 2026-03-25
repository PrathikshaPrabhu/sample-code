import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    token=os.getenv("HUGGINGFACE_API_KEY")
)

def query_huggingface(prompt):
    try:
        response = client.chat_completion(
            model="Qwen/Qwen2.5-7B-Instruct",  
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )
        return response.choices[0].message.content

    except Exception as e:
        print("Full Error:", repr(e))
        return "Something went wrong."


if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying Hugging Face...")
    print(query_huggingface(user_prompt))