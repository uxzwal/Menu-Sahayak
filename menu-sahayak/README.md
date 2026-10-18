# Allergen Lens — Menu Allergen Checker for Indian Restaurants

Allergen Lens is a local allergen-checking app for Indian restaurant menus. Tourists with allergies may struggle to read Hindi or regional-language menus, so this app flags likely allergens per dish using an open-weight Llama model via Groq.

For each dish, the app returns:
- dish name
- likely allergens selected from: dairy, nuts, gluten, eggs, soy
- one concise safety note

Allergen output is intentionally cautious: it marks likely/possible allergens based on common preparation and asks users to verify with restaurant staff for severe allergies.

## Why open-weight model?
- **Model swap freedom:** open-weight ecosystems make it easier to switch models without locking into one closed provider.
- **Cost control:** open-weight options help teams optimize quality/performance vs pricing over time.
- **Transparency:** model behavior and tradeoffs are easier to evaluate compared with fully closed systems.

## Setup
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy the env template:
   ```bash
   cp .env.example .env
   ```
4. Add your Groq API key in `.env` as `GROQ_API_KEY=...`.
5. Run the app:
   ```bash
   python app.py
   ```

Get a free Groq API key at: https://console.groq.com/keys

## Screenshot
![Screenshot placeholder](https://via.placeholder.com/1200x700?text=Menu+Sahayak+UI)

## License
MIT
