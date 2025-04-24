from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

# Load your .env file
load_dotenv()

def chat_local(prompt: str) -> str:
    try:
        # Set up the Groq model
        chat = ChatGroq(
            model_name="llama3-70b-8192",  # ✅ Use currently supported model
            temperature=0.7,
        )

        # Send the message
        response = chat.invoke([
            HumanMessage(content=prompt)
        ])

        return response.content

    except Exception as e:
        return f"⚠️ Local AI Error: {e}"
