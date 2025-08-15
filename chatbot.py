# chatbot.py
# Advanced Rule-based Chatbot with 100 responses

import datetime
import random

# Dictionary for fixed responses
RESPONSES = {
    # Greetings
    "hi": "Hello there! 👋",
    "hello": "Hey! How are you doing?",
    "hey": "Hi! What's up?",
    "good morning": "Good morning! 🌞",
    "good afternoon": "Good afternoon! ☀️",
    "good evening": "Good evening! 🌇",
    "yo": "Yo! How’s it going?",
    "hiya": "Hiya! Nice to meet you.",
    "howdy": "Howdy partner! 🤠",
    "sup": "Not much! What about you?",

    # Politeness
    "thank you": "You're welcome! 😊",
    "thanks": "Anytime! 🙌",
    "thanks a lot": "No problem at all.",
    "appreciate it": "Happy to help!",
    "you are great": "Aww, thanks! You’re great too.",

    # Name & Identity
    "what is your name": "I'm a Python chatbot.",
    "who are you": "I'm your friendly chatbot assistant.",
    "do you have a name": "Not really, but you can call me PyBot.",
    "are you human": "Nope, I’m 100% code!",
    "what are you": "I’m a chatbot built using Python.",

    # How Are You
    "how are you": "I’m doing great! How about you?",
    "how’s it going": "Pretty good! You?",
    "how do you feel": "I feel as good as code can feel.",
    "are you okay": "Absolutely!",
    "how have you been": "I’ve been chatting all day.",

    # Help Requests
    "help": "I can chat, tell jokes, give the date and time.",
    "what can you do": "I can chat, tell time/date, and tell jokes.",
    "show commands": "Commands: greetings, jokes, time, date.",
    "features": "I’m simple: greet, tell jokes, date/time.",
    "capabilities": "I’m here to talk and have fun.",

    # Weather
    "how’s the weather": "I can’t check now, but I hope it’s sunny!",
    "weather": "I’m not connected to live weather data.",
    "is it raining": "No idea, but carry an umbrella just in case!",
    "is it sunny": "Hopefully!",
    "forecast": "I wish I could tell you the forecast.",

    # Feelings
    "i am happy": "That’s great! 😊",
    "i am sad": "I’m here if you want to talk.",
    "i am bored": "Want to hear a joke?",
    "i feel lonely": "You’re not alone — I’m here!",
    "i am angry": "Deep breaths help.",

    # Yes/No
    "yes": "Alright!",
    "no": "Okay.",
    "maybe": "Take your time.",
    "sure": "Cool!",
    "of course": "Great!",

    # Casual Conversation
    "what’s up": "Not much, just chatting.",
    "nothing much": "Alright.",
    "how’s life": "Life’s good in the digital world.",
    "do you eat": "Nope, no food for me.",
    "do you sleep": "Never! Always online.",
    "are you real": "In a way, yes — in your computer!",
    "do you like me": "Of course!",
    "do you work": "Yes, chatting with you.",
    "are you busy": "Never too busy for you.",
    "do you think": "Not like humans do.",
    "do you feel": "Not really.",
    "are you smart": "I try my best!",
    "are you alive": "In a sense, yes.",
    "are you bored": "Never!",
    "do you love me": "I care for you as much as code can.",

    # Goodbyes
    "bye": "Bye! 👋",
    "goodbye": "Goodbye!",
    "see you": "See you later!",
    "take care": "You too!",
    "later": "Later!",
    "catch you later": "Sure!",
    "see you soon": "Definitely.",
    "farewell": "Farewell!",
    "peace out": "Peace!",
    "have a nice day": "Thanks! You too.",

    # Miscellaneous
    "sing a song": "I can’t sing, but I can hum in binary!",
    "dance": "I can’t dance, but I can code!",
    "story": "Once upon a time, there was a chatbot...",
    "who made you": "I was made by a Python developer.",
    "where are you from": "From the land of code!",
    "can you help me": "Sure, what do you need?",
    "do you know python": "Of course! I’m written in Python.",
    "are you funny": "Sometimes!",
    "do you like jokes": "Yes! I love them."
}

# Special categories for dynamic responses
JOKES = [
    "Why did the math book look sad? Too many problems.",
    "I told my computer I needed a break, and it froze!",
    "Parallel lines have so much in common… it’s a shame they’ll never meet.",
    "Why don’t skeletons fight? They don’t have the guts.",
    "Why do programmers prefer dark mode? Less bugs.",
    "I would tell you a UDP joke… but you might not get it.",
    "Why did the scarecrow get promoted? He was outstanding in his field.",
    "Why don’t eggs tell jokes? They might crack up.",
    "I asked my dog what’s two minus two. He said nothing.",
    "What do you call fake spaghetti? An impasta."
]

def chatbot():
    print("🤖 Hello! I’m your advanced chatbot.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("🤖 Goodbye! Have a nice day.")
            break

        response_given = False

        # Handle date and time
        if "time" in user_input:
            print(f"🕒 Current time: {datetime.datetime.now().strftime('%H:%M:%S')}")
            response_given = True
        if "date" in user_input:
            print(f"📅 Today's date: {datetime.datetime.now().strftime('%Y-%m-%d')}")
            response_given = True

        # Handle jokes
        if "joke" in user_input or "funny" in user_input or "laugh" in user_input:
            print("😂 " + random.choice(JOKES))
            response_given = True

        # Check fixed responses
        if not response_given:
            reply = RESPONSES.get(user_input)
            if reply:
                print(f"🤖 {reply}")
                response_given = True

        # Fallback
        if not response_given:
            print("🤖 Sorry, I don't understand that yet.")

if __name__ == "__main__":
    chatbot()
