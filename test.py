
import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "Hello! Introduce yourself."
        }
    ]
)

print(response.message.content)
