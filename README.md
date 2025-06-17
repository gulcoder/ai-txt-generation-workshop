# 🤖 OpenAI Textgenerering – Workshop

Ett pedagogiskt Python-projekt för att lära sig textgenerering med OpenAI:s API (GPT-4 och GPT-3.5).  
Här hittar du flera övningar som visar olika sätt att interagera med AI:n – från enkla frågor till streaming och formaterade svar.

---

## 🚀 Funktioner

- ✅ **Lär dig moderna tekniker för AI-textgenerering med OpenAI:s senaste Python-klient**
- ✅ **Jobba med olika outputformat** – Markdown, JSON, kodblock och mallbaserad text
- ✅ **Förstå hur streaming fungerar** för att visa svar i realtid
- ✅ **Använd `venv` och `.env`** för en säker och isolerad utvecklingsmiljö
- ✅ **Strukturerad kod per övning** – lätt att läsa, återanvända och utöka

---

## 🧰 Teknisk stack

| Delområde           | Teknik / Verktyg                                            |
|---------------------|-------------------------------------------------------------|
| AI/Textgenerering   | [OpenAI Python SDK](https://github.com/openai/openai-python) |
| Miljövariabler      | `python-dotenv`                                             |
| Virtuell miljö      | `venv` (inbyggt i Python)                                   |
| Terminalinteraktivitet | `print()`, `input()`, streaming                           |
| Versionskontroll    | Git + GitHub                                                |
| OS-kompabilitet     | Linux, macOS, Windows                                       |

---

## 🧪 Övningar

| Övning | Titel                  | Mål                                                       | Tekniker / Fokus                   |
| ------ | ---------------------- | --------------------------------------------------------- | ---------------------------------- |
| 1      | **Svar i Markdown**    | Styra API-svar till formaterad Markdown                   | 📄 Markdown-utdata                 |
| 2      | **Svar i JSON**        | Begära strukturerad JSON och hantera resultatet           | 🧱 JSON-format, strukturkontroll   |
| 3      | **Streama svar**       | Få realtidssvar i terminalen                              | 🔁 `stream=True`, realtidsutskrift |
| 4      | **Text + Kodexempel**  | Kombinera teori och praktik (t.ex. kodblock + förklaring) | 🧠 + 💻 Kodblock i svaret          |
| 5      | **Template Prompting** | Styra AI att fylla i en mallstruktur                      | 📝 Mallar (t.ex. karaktärsmallar)  |


Varje övning finns som en separat Python-fil: `övning1.py`, `övning2.py` osv.

---

## ⚙️ Installation & användning

```bash
1. Klona repot
git clone https://github.com/gulcoder/ai-txt-generation-workshop.git

2. Skapa och aktivera virtuellt Python-miljö
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3. Installera beroenden
pip install -r requirements.txt

4. Lägg till din API-nyckel
cp .env.example .env
# Redigera .env och fyll i din OPENAI_API_KEY

5. Kör en övning
python övning1.py
```



