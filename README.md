# 🎥 Project Demo Video and ppt link👇👇

https://drive.google.com/drive/folders/1PpBtZLQ1SbRoEIDEQ07STcEI_dS4egvb

---

# 🤖 AI Data Analyst Assistant

A simple chat-based system that allows users to interact with data using natural language and visualize results instantly.

---

## ✨ Features

- Chat-based user interface  
- Instant data retrieval from database  
- Automatic chart generation  
- Simple and user-friendly design  
- Fast backend processing  
- Lightweight database integration  
- Real-time response  
- Easy to set up and run  
- Works without deep technical knowledge  
- Clean UI with chat bubbles  

---

## 🏗️ System Architecture
User (Chat UI)
↓
Frontend (HTML + JavaScript)
↓
API Request
↓
Backend (FastAPI)
↓
Database (SQLite)
↓
Processed Data
↓
Response + Chart (Chart.js)


---

## 🛠️ Agent Tools

This system uses backend tools to process user queries and fetch relevant data.

| Tool Name        | Description                              | Returns               |
|-----------------|------------------------------------------|----------------------|
| Query Processor | Converts user input into SQL query       | SQL Query            |
| DB Connector    | Connects to SQLite database              | Data rows            |
| Chart Generator | Generates bar chart from data            | Visual chart output  |

---

## ⚡ Quick Start


### 2. Create Virtual Environment

### 3. Activate Environment

### 4. Install Dependencies

### 5. Start Backend

### 6. Open Frontend

Open `chat_ui.html` in your browser.

---

## 💬 Example Conversations

User: show products  
Bot: Displays product details and sales  

User: sales data  
Bot: Shows data with bar chart  

---

## 🗄️ Sample Database Schema

### 6. Open Frontend

Open `chat_ui.html` in your browser.

---

## 💬 Example Conversations

User: show products  
Bot: Displays product details and sales  

User: sales data  
Bot: Shows data with bar chart  

---

## 🗄️ Sample Database Schema
Table: products

Columns:
id INTEGER PRIMARY KEY
name TEXT
category TEXT
sales INTEGER

---

## ⚙️ Configuration

- Backend runs on: http://127.0.0.1:8000  
- Database file: sales.db  
- Frontend file: chat_ui.html  

---

## 🔗 API Reference

### POST /chat

Request:
{
"question": "show products"
}

Response:
{
"bot_message": "...",
"result": [...]
}


---

## 📊 Evaluation Criteria Coverage

- Functionality ✅  
- UI/UX ✅  
- Data Visualization ✅  
- Backend Integration ✅  
- Working Demo ✅  

---

## ⭐ Bonus Features Implemented

- Chat-based interaction  
- Dynamic chart generation  
- Simple UI design  
- Fast response system  

---

## 💻 Tech Stack

- Frontend: HTML, JavaScript  
- Backend: FastAPI (Python)  
- Database: SQLite  
- Charts: Chart.js  

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository  
2. Create a new branch  
3. Make changes  
4. Submit a pull request  

---

## ⚙️ Manual Setup / How It Works

1. User enters a query in chat  
2. Frontend sends request to backend  
3. Backend processes request  
4. Data is fetched from SQLite database  
5. Response is sent back  
6. Chart is generated and displayed  

---

## 👨‍💻 Developed By

**Team Smart Coders**
