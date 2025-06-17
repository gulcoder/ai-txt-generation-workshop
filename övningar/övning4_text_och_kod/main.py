import os
from openai import OpenAI

def main():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    concept = "for-loop i Python"

    prompt = (
        f"Förklara kort vad en {concept} är och visa ett litet fungerande exempel på kod.\n"
        "Format:\n"
        "- Kort förklaring\n"
        "- Kodblock i Python"
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Du är en hjälpsam assistent."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )

    text = response.choices[0].message.content

    # Dela upp svaret i förklaring och kod
    if "```" in text:
        explanation, code_block = text.split("```", 1)
        code = code_block.strip("python\n ").rstrip("```").strip()
    else:
        explanation = text
        code = ""

    print("\nKort förklaring:\n")
    print(explanation.strip())
    print("\nKodexempel:\n")
    print(code)

if __name__ == "__main__":
    main()
