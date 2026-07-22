import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_trip(destination, budget, travelers, travel_type):

    prompt = f"""
You are an expert travel planner.

Create a beautiful 3-day travel itinerary.

Destination: {destination}

Budget: {budget}

Travelers: {travelers}

Travel Type: {travel_type}

Include:

Day 1
Day 2
Day 3

Best attractions

Food recommendations

Transportation

Estimated budget

Travel tips

Return the answer in proper headings and bullet points.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"❌ AI service is temporarily unavailable.\n\nDetails:\n{e}"
    