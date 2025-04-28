from flask import Flask, render_template, request
import random
import nltk
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Pairs for the chatbot
pairs = [
    [
        r"(hi|hello|hey|hii|hiii)",
        ["Hello there! 👋", "Hi! How can I assist you today?", "Hey! Hope you're doing great!"]
    ],
    [
        r"how are you?",
        ["I'm doing great, thanks for asking! How about you?", "Feeling awesome! 😊 What about you?"]
    ],
    [
        r"what is your name?",
        ["I'm your friendly Chatbot 🤖", "They call me CodeAlpha Bot!"]
    ],
    [
        r"who created you?",
        ["I was built by a talented intern during their journey at CodeAlpha! 🚀"]
    ],
    [
        r"what can you do?",
        ["I can chat, answer simple questions, tell jokes, and make your day better! 🎉"]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything! 😂", "Why was the math book sad? Because it had too many problems. 😅"]
    ],
    [
        r"thank you|thanks",
        ["You're welcome! 😊", "Anytime! 👍", "Glad to help! 🙌"]
    ],
    [
        r"bye|goodbye|see you",
        ["Goodbye! Take care! 👋", "See you later! 👋 Have a great day!"]
    ],
    [
        r"what is weather today?",
        ["I'm not connected to a live weather API yet, but I hope it's sunny wherever you are! ☀️"]
    ],
    [
        r"i'm feeling (.*)",
        ["Oh no, I'm sorry to hear that! Is there anything I can do to help?", "I hope you feel better soon! Want to talk about it?"]
    ],
    [
        r"(.*)",
        ["I’m still learning... Could you ask something else? 🤔", "Interesting! Tell me more! ✨"]
    ]
]

# Initialize chatbot
chatbot = Chat(pairs, reflections)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_text = request.args.get('msg')
    response = chatbot.respond(user_text)
    if response is None:
        return "I'm not sure about that. Can you ask something else?"
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
