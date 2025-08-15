# 🗨️ Task 8: Advanced Rule-Based Chatbot

## 📌 Objective
Create a **rule-based chatbot** in Python that responds to user inputs using `if-else` logic (dictionary-based here) and can handle multiple commands like greetings, jokes, date, and time.

---

## ✨ Features
- 100+ predefined responses for common phrases.
- Handles greetings, casual chat, and goodbyes.
- Dynamic features:
  - Shows current **time**.
  - Shows **today's date**.
  - Tells **random jokes**.
- Case-insensitive matching using `.lower()`.
- Clean **dictionary-based structure** instead of long if-else chains.
- Runs continuously until the user types `exit`.

---

## 📂 Project Structure
task8_chatbot/
│
├── chatbot.py # Main chatbot script
├── README.md # Project documentation
└── requirements.txt # Empty (no external dependenci

---

## ▶️ How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/task8_chatbot.git
   cd task8_chatbot
Example Interaction
🤖 Hello! I’m your advanced chatbot.
Type 'exit' to quit.

You: hi
🤖 Hello there! 👋

You: tell me a joke
😂 Why don’t skeletons fight? They don’t have the guts.

You: what time is it
🕒 Current time: 14:45:12

You: what date is it
📅 Today's date: 2025-08-15

You: exit
🤖 Goodbye! Have a nice day.
