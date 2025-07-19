# 🤖 Smart Chatbot

A simple and fun general-purpose chatbot built using **Python Flask**, **HTML/CSS**, and **Vanilla JavaScript**. It can tell jokes, do basic math, report the current time and date, and much more — all with expressive emoji responses!

---

## 🛠️ Features

- 🕒 Tells current time and date
- 😄 Tells random tech jokes
- 🧠 Performs basic math calculations (e.g., `calculate 5 + 3`)
- 💬 Chat-style interaction with emojis
- 👋 Friendly greetings and sign-off
- 📦 Flask backend with POST request handling

---

## 📁 Project Structure

```
SMART_CHATBOT/
├── app.py                # Flask backend
├── chatbot_logic.py      # Logic for responses
├── static/
│   └── style.css         # Styling for UI
├── templates/
│   └── index.html        # Frontend layout
└── README.md             # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone or Download

Unzip or clone this repo into your machine:

```
git clone https://github.com/yourname/smart-chatbot.git
cd smart-chatbot
```

### 2. Install Dependencies

Make sure you have Python installed. Then install Flask:

```bash
pip install flask
```

### 3. Run the App

```bash
python app.py
```

Now open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 💡 Example Inputs

- `hello`
- `how are you`
- `time`
- `date`
- `calculate 5 + 6 * 3`
- `tell me a joke`
- `bye`

---

## 📌 Notes

- Do **not** open `index.html` directly from your browser (e.g., with Live Server)
- Always access the app through **Flask** at `http://127.0.0.1:5000`

---

## 📸 Screenshot

![Chatbot Preview](preview.png)

---

## 📄 License

This project is free to use for educational or personal purposes.