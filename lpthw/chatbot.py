import time
import random
import datetime

def intro():
    print "Welcome to Chatbot!"
    print "-------------------"
    print "Use Q or q to quit!"
    print "-------------------"

GREETING_KEYWORDS=("Hello","Hi","Greetings", "Good Morning", "Welcome", "Hey")
GREETING_RESPONSES=("Hi", "Welcome", "Hey","Good to meet.")
RESPONSES={"What is your name ?":"My name is altran Chatbot! How about you ?","How are you ?":"Good. How about you ?"}

def respond(message):
    return check_for_greeting(message)

def getCurrentGreeting():
    currentTime = datetime.datetime.now()
    if currentTime.hour < 12:
        return 'Good morning'
    elif 12 <= currentTime.hour < 18:
        return 'Good afternoon'
    else:
        return 'Good evening'

def check_for_greeting(sentence):
    """If any of the words in the user's input was a greeting, return a greeting response"""
    if sentence.strip() in GREETING_KEYWORDS:
        return getCurrentGreeting()+", "+random.choice(GREETING_RESPONSES)
    else:
        return "I can hear you said > {}".format(sentence)

if __name__=='__main__':
    intro()
    inp="Hai"
    while(True):
            inp = raw_input("You: ")
            if(inp.strip()=="Q" or inp.strip()=="q"):
                print "Thanks for using the chatbot!!"
                break
            else:
                time.sleep(0.5)
                print "Bot: ",respond(inp)
    