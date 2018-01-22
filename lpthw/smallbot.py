"""
Small Program to evaluate chatbot concept
"""
import random
GREETING_KEYWORDS = ("Hi", "Hello", "Buddy", "Whats up", "what's up")
GREETING_RESPONSES = ("'sup bro", "hey", "*nods*", "hey you get my snap?")

def check_for_greeting(sentence):
    """If any of the words in the user's input was a greeting, return a greeting response"""
    for word in sentence.words:
        if word.lower() in GREETING_KEYWORDS:
            return random.choice(GREETING_RESPONSES)

print repr(check_for_greeting("Hi welcome"))
