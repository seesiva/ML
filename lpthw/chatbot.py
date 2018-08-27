import time
import random
import datetime

def intro():
    print "Welcome to Chatbot!"
    print "-------------------"
    print "Use Q or q to quit!"
    print "-------------------"

begin_context=False
GREETING_KEYWORDS=("Hello","Hi","Greetings", "Good Morning", "Welcome", "Hey")
GREETING_RESPONSES=("Hi", "Welcome", "Hey","Good to meet.")

RESPONSES={'What is your name?':["I'm Altran Chatbot","My name is altran Chatbot! How about you ?"],"How are you ?":["Great. You?","Good. How about you ?"]}


def check_for_otherResponse(message):
    if message.strip() in RESPONSES:
        return random.choice(RESPONSES[message.strip()])

def getCurrentTimeGreeting():
    currentTime = datetime.datetime.now()
    if currentTime.hour < 12:
        return 'Good morning'
    elif 12 <= currentTime.hour < 18:
        return 'Good afternoon'
    else:
        return 'Good evening'

def check_for_greeting(sentence, context):
    """If any of the words in the user's input was a greeting, return a greeting response"""
    if (sentence.strip() in GREETING_KEYWORDS) and (context==True):
        return getCurrentTimeGreeting()+", "+random.choice(GREETING_RESPONSES)
    else:
        return random.choice(GREETING_RESPONSES)

def respond(message,context):
    if check_for_greeting(message,context):
        return check_for_otherResponse(message)
        
if __name__=='__main__':
    intro()
    begin_context=True
    inp="Hai"
    while(True):
            inp = raw_input("You: ")
            if(inp.strip()=="Q" or inp.strip()=="q"):
                print "Thanks for using the chatbot!!"
                break
            else:
                #time.sleep(0.5)
                #print inp
                print "Bot:", respond(inp,begin_context)
                begin_context=False
    