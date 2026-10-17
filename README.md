# 🍛 Menu Sahayak — Open-Weight Menu Translator for Indian Restaurants

A lightweight Gradio app that translates Hindi/regional restaurant menus into polished English menus. Each dish gets a **transliterated name** (not a literal translation) plus a **1-line appetizing description** mentioning key ingredients and spice level.

Powered by **Llama 3.3 70B — an open-weight model** — served via [Groq](https://groq.com). Built for the [Hacktoberfest Open-Source AI Challenge Week 2: Side Hustle](https://dev.to/challenges/hacktoberfest-week2-2026-10-12).

---

## 🎯 The Problem

Generic translation tools fail at Indian menus. Google Translate turns **"Paneer Tikka"** into **"Cheese Piece"** — it literally translates dish names instead of transliterating them. Restaurant owners who want tourist-facing English menus (or cloud kitchens listing on Zomato/Swiggy) end up with awkward, wrong descriptions.

Menu Sahayak solves this with a **carefully designed system prompt on an open-weight model**:
- Dish names stay transliterated (`Paneer Tikka` → `Paneer Tikka`, not `Cheese Piece`)
- Each dish gets a short appetizing description with ingredients + spice level
- Output is a clean numbered list, ready to paste into a menu or listing

---

## ✨ Why an Open-Weight Model?

I deliberately chose **Llama 3.3 70B (open-weight)** over a closed API:

1. **Model swap freedom** — I can switch to Qwen, Gemma, or Mistral by changing one line. No vendor lock-in, no re-integration.
2. **Cost** — Groq's free tier makes this **₹0 to run**. A closed model of similar quality would charge per token, which matters for a small restaurant doing 10+ menus a month.
3. **Transparency & portability** — Open weights mean I know exactly what model I'm running, and I could **self-host the same model later** on my own hardware without changing a single line of app logic.

The open pieces aren't decorative — the entire product is built around an open-weight model I can swap, prompt, and self-host. Remove the open model and the project stops working.

---

## 🚀 Setup

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/menu-sahayak.git
cd menu-sahayak
