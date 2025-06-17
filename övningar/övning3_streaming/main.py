import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Sätt din OPENAI_API_KEY i .env-filen")

client = OpenAI(api_key=api_key)

def stream_programming_tips():
    prompt = "Ge mig 3 korta, konkreta tips för nybörjare som vill bli bättre på programmering."
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    
    print("Programmeringstips för nybörjare:\n")
    
    for chunk in response:
        # chunk.choices är en lista, ta första choice
        delta = chunk.choices[0].delta
        if hasattr(delta, "content") and delta.content:
            print(delta.content, end="", flush=True)
    print("\n\n-- Slut på tips --")

if __name__ == "__main__":
    stream_programming_tips()
