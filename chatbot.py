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

response = llm.invoke( # send a message to the model and receive its response
    "Explain what a neural network is in two sentences."
)

print(response.content)