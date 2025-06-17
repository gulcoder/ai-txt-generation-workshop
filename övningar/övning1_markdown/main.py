import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Sätt din OPENAI_API_KEY i .env-filen")

client = OpenAI(api_key=api_key)

prompt = """
Skapa en lista med 5 populära programmeringsspråk.

Varje objekt ska innehålla: namn, skapare och år.

Svara i **Markdown-format**.
"""

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.5,
    max_tokens=500,
)

print(response.choices[0].message.content)
