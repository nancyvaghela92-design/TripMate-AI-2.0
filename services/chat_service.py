import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def chat_with_ai(message, history):

    conversation = ""

    for chat in history:
        conversation += f"{chat['role']}: {chat['content']}\n"

    conversation += f"user: {message}"

    prompt = f"""
You are TripMate AI.

You are a professional travel assistant.

Conversation:

{conversation}

Reply naturally and helpfully.
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"❌ Error : {e}"