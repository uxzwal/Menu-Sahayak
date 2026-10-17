import os

import gradio as gr
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

if os.getenv("GROQ_API_KEY"):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
else:
    client = None
MODEL_NAME = "llama-3.3-70b-versatile"
SYSTEM_PROMPT = (
    "Keep dish names transliterated, NOT literally translated. "
    "Add a short appetizing English description with key ingredients and spice level. "
    "Output as a clean numbered list."
)


def translate_menu(menu_text: str):
    if not menu_text or not menu_text.strip():
        yield "Please paste a menu first.", ""
        return

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key or client is None:
        yield "Set GROQ_API_KEY in .env file", "<span style='color:red'>Set GROQ_API_KEY in .env file</span>"
        return

    try:
        stream = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": menu_text.strip()},
            ],
            stream=True,
            temperature=0.4,
        )

        output = ""
        for chunk in stream:
            delta = chunk.choices[0].delta.content if chunk.choices else None
            if delta:
                output += delta
                yield output, ""

    except Exception as exc:
        error_text = f"API error: {exc}"
        yield error_text, f"<span style='color:red'>{error_text}</span>"


with gr.Blocks(
    title="Menu Sahayak — Open-Weight Menu Translator"
) as demo:
    gr.Markdown("# Menu Sahayak — Open-Weight Menu Translator")
    gr.Markdown("Powered by Llama 3.3 70B (open-weight) via Groq. No data stored.")

    menu_input = gr.Textbox(
        label="Paste menu (one dish per line)",
        lines=12,
        placeholder="e.g.\nPaneer Tikka\nAloo Chaat\nMasala Dosa",
    )
    output_box = gr.Textbox(label="English Menu", lines=14)
    error_box = gr.Markdown()

    translate_btn = gr.Button("Translate Menu")
    translate_btn.click(
        fn=translate_menu,
        inputs=menu_input,
        outputs=[output_box, error_box],
    )


if __name__ == "__main__":
    demo.launch()
