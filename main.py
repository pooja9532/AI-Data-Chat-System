# main.py

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- DATABASE ----------
def get_data():
    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()
    cursor.execute("SELECT product, amount FROM sales")
    data = cursor.fetchall()
    conn.close()
    return data

# ---------- HOME ----------
@app.get("/", response_class=HTMLResponse)
def home():
    with open("chat_ui.html", "r", encoding="utf-8") as f:
        return f.read()

# ---------- CHAT ----------
@app.get("/chat")
def chat(user_input: str):
    text = user_input.lower()
    data = get_data()

    try:
        # greetings
        if "hello" in text or "hi" in text:
            return {"bot": "Hello! Ask me anything about sales data 😊"}

        # show all
        elif "show" in text or "display" in text:
            return JSONResponse({
                "bot": "Here is complete sales data 📊",
                "data": data
            })

        # total
        elif "total" in text:
            total = sum([x[1] for x in data])
            return {"bot": f"Total sales is {total}"}

        # highest
        elif "highest" in text or "max" in text:
            highest = max(data, key=lambda x: x[1])
            return {"bot": f"{highest[0]} has highest sales = {highest[1]}"}

        # lowest
        elif "lowest" in text or "min" in text:
            lowest = min(data, key=lambda x: x[1])
            return {"bot": f"{lowest[0]} has lowest sales = {lowest[1]}"}

        # count
        elif "count" in text or "how many" in text:
            return {"bot": f"There are {len(data)} products in database"}

        # product specific
        else:
            for product, amount in data:
                if product.lower() in text:
                    return {"bot": f"{product} sales is {amount}"}

        # fallback
        return {"bot": "I can answer sales-related questions. Try: show, total, highest, lowest"}

    except Exception as e:
        return {"bot": f"Error: {str(e)}"}