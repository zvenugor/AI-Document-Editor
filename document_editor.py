import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def edit_document(text):
    prompt = f"Edit the following document for clarity, grammar, and style improvement:\n\n{text}\n\nEdited Document:"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a skilled document editor."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=250
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    document = input("Enter your document text: ")
    edited = edit_document(document)
    print("Edited Document:\n", edited)
