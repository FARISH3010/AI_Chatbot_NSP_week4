import random
from datetime import datetime

def get_response(user_input):
    user_input = user_input.lower().strip()

    # Greetings
    if any(word in user_input for word in ["hello", "hi", "hey", "good morning", "good evening"]):
        return "👋 Hey there! How can I help you today?"

    # Bot's name
    elif "your name" in user_input:
        return "🤖 I'm ChatBot, your helpful assistant!"

    # Emotion check
    elif "how are you" in user_input:
        return "😊 I'm doing great! Thanks for asking. How are you?"

    # Time and date
    elif "time" in user_input:
        return f"🕒 The current time is {datetime.now().strftime('%I:%M %p')}."
    elif "date" in user_input:
        return f"📅 Today is {datetime.now().strftime('%A, %B %d, %Y')}."

    # Help
    elif "help" in user_input:
        return (
            "🛠️ I can help you with:\n"
            "- 🕒 Time\n"
            "- 📅 Date\n"
            "- 😄 Jokes\n"
            "- 🧠 Calculations (e.g., 'calculate 5 * 6')\n"
            "- 💬 General chat\n"
            "Just ask me!"
        )

    # Joke
    elif "joke" in user_input:
        jokes = [
            "😄 Why don't scientists trust atoms? Because they make up everything!",
            "😂 Why was the math book sad? Because it had too many problems.",
            "🤣 Why do programmers hate nature? It has too many bugs!"
        ]
        return random.choice(jokes)

    # Math calculation
    elif "calculate" in user_input:
        try:
            expression = user_input.replace("calculate", "").strip()
            result = eval(expression)
            return f"🧠 The result is: {result}"
        except:
            return "❌ Oops! That didn’t work. Try something like 'calculate 8 + 2'."

    # Reset / clear
    elif "clear" in user_input or "reset" in user_input:
        return "🔄 Okay! Let’s start fresh!"

    # Goodbye
    elif "bye" in user_input or "exit" in user_input:
        return "👋 Bye! Take care and have a wonderful day!"

    # Fallback
    else:
        return "🤔 I’m not sure how to respond to that. Try asking me the time, a joke, or for help!"
