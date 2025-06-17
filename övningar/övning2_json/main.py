import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Sätt din OPENAI_API_KEY i .env-filen")

client = OpenAI(api_key=api_key)

prompt = """
Skapa en JSON-lista med 5 populära programmeringsspråk.
Varje objekt ska innehålla: "namn", "skapare" och "år".
Svara endast med giltig JSON.
"""

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.3,
    max_tokens=500,
)

text_response = response.choices[0].message.content

print("Raw response från API:")
print(text_response)

# Försök tolka svaret som JSON
try:
    json_data = json.loads(text_response)
    print("\nStrukturerad JSON-utskrift:")
    print(json.dumps(json_data, indent=4, ensure_ascii=False))
except json.JSONDecodeError as e:
    print("\nMisslyckades att tolka JSON:")
    print(e)
