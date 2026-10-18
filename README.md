# Allergen Lens — Menu Allergen Checker for Indian Restaurants

A lightweight Gradio app that analyzes Indian restaurant menu items and flags **likely allergens** per dish.

Powered by **Llama 3.3 70B (open-weight)** via [Groq](https://groq.com).

## What it does

Paste menu items (one dish per line), and the app returns a numbered list with:
- dish name
- likely allergens from: dairy, nuts, gluten, eggs, soy
- one concise safety note

The model is instructed to avoid unsupported certainty: allergens are marked as likely/possible based on common preparation, and users should verify with restaurant staff for severe allergies.

## Why this is useful

Tourists with allergies may struggle to read Hindi or regional-language menus. This tool provides quick, practical allergen guidance dish-by-dish.

## Setup

1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r menu-sahayak/requirements.txt
   ```
3. Create env file:
   ```bash
   cp menu-sahayak/.env.example menu-sahayak/.env
   ```
4. Add your Groq API key in `menu-sahayak/.env`:
   ```bash
   GROQ_API_KEY=your_key_here
   ```
5. Run:
   ```bash
   cd menu-sahayak
   python app.py
   ```

Get a free Groq API key at: https://console.groq.com/keys
