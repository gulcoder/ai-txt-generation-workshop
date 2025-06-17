import os
from openai import OpenAI

def main():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = (
        "Fyll i följande karaktärsmall baserat på din fantasi:\n\n"
        "- Namn:\n"
        "- Ålder:\n"
        "- Yrke:\n"
        "- Egenskaper (3 egenskaper):\n"
        "- Kort bakgrundshistoria:\n"
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Du är en kreativ och detaljerad författare."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=400,
    )

    character = response.choices[0].message.content.strip()
    print("Genererad karaktär:")
    print(character)

if __name__ == "__main__":
    main()
