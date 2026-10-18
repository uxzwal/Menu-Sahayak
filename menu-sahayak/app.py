"""
Allergen Lens — Menu Allergen Checker for Indian Restaurants
Powered by Llama 3.3 70B (open-weight) via Groq.
"""

import os
import gradio as gr
from groq import Groq
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
MODEL = "llama-3.3-70b-versatile"

SYSTEM_PROMPT = """You are an allergen analyst for Indian restaurants.

For each dish the user provides:
1. Output as a clean numbered list, one dish per entry.
2. For each entry, include exactly:
   - name: dish name
   - likely allergens: choose only from dairy, nuts, gluten, eggs, soy
   - safety note: exactly one concise line
3. Describe allergens as likely/possible based on common preparation. Do not claim certainty.
4. Include in each safety note that users should verify details with restaurant staff, especially for severe allergies.
5. Do not add any preamble, notes, or extra text — only the numbered list.

If the input is not a menu, respond: "Please paste a menu (one dish per line)."
"""


def translate_menu(menu_text: str):
    """Stream allergen analysis from Groq's Llama 3.3 70B."""
    # Guard: empty input
    if not menu_text or not menu_text.strip():
        yield "⚠️ Please paste a menu first (one dish per line)."
        return

    # Guard: missing API key
    if not API_KEY:
        yield "❌ GROQ_API_KEY not found. Add it to your .env file and restart the app."
        return

    try:
        client = Groq(api_key=API_KEY)
        stream = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Analyze likely allergens for this menu:\n\n{menu_text.strip()}"},
            ],
            temperature=0.4,
            max_tokens=1024,
            stream=True,
        )

        output = ""
        for chunk in stream:
            delta = chunk.choices[0].delta.content or ""
            if delta:
                output += delta
                yield output

        if not output.strip():
            yield "⚠️ Empty response from model. Try again."

    except Exception as e:
        error_msg = str(e)
        if "401" in error_msg or "invalid_api_key" in error_msg.lower():
            yield "❌ Invalid API key. Check GROQ_API_KEY in your .env file."
        elif "429" in error_msg or "rate_limit" in error_msg.lower():
            yield "⚠️ Rate limit hit. Wait a minute and try again."
        else:
            yield f"❌ Error: {error_msg}"


# ----------------------------
# Gradio UI
# ----------------------------
demo = gr.Interface(
    fn=translate_menu,
    inputs=gr.Textbox(
        lines=10,
        label="Paste menu dishes to check allergens (one dish per line)",
        placeholder="Paneer Tikka\nDal Makhani\nChicken Biryani\nMasala Dosa\nGulab Jamun",
    ),
    outputs=gr.Textbox(
        lines=15,
        label="Allergen analysis",
    ),
    title="Allergen Lens — Menu Allergen Checker for Indian Restaurants",
    description=(
        "Powered by **Llama 3.3 70B (open-weight)** via Groq. "
        "Tourists with allergies may struggle to read Hindi or regional-language menus. "
        "This tool flags likely allergens per dish using an open-weight Llama model."
    ),
    examples=[
        ["Paneer Tikka\nDal Makhani\nChicken Biryani\nMasala Dosa\nGulab Jamun"],
        ["Chole Bhature\nPalak Paneer\nRogan Josh\nRasmalai\nVeg Manchurian"],
    ],
    theme=gr.themes.Soft(),
    allow_flagging="never",
)

if __name__ == "__main__":
    demo.launch()
