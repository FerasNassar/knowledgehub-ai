# Step 6.2: Make our first LLM API request using LangChain.
# The program loads our API key, initializes a model,
# sends one question, and prints the response.

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()  # Load environment variables from .env file

llm = ChatGroq( # Create a LangChain chat model connected to Groq.
    model="openai/gpt-oss-20b",
    temperature=0.3,
)

print("AI is ready to answer your questions. Type 'exit' to quit.")

while True:
    user_input=input("\nYou: ").strip()

    if user_input.lower() == "exit":
        print("Exiting the chat. Goodbye!")
        break

    if not user_input:
        print("Please enter a question or type 'exit' to quit.")
        continue

    try:
        response = llm.invoke(user_input)
        print(f"\nAI: {response.content}")
    except Exception as e:
        print(f"\n Error: {e}")
    
