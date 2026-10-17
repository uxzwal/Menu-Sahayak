# Menu Sahayak

Menu Sahayak is a local menu translator for Indian restaurants that takes dish names in Hindi or regional languages and converts them into an English-friendly menu with transliterated dish names plus short appetizing descriptions including key ingredients and spice level.

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
