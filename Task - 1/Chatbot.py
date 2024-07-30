import datetime

Time = datetime.datetime.now()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("Good Morning!")

    elif hour>=12 and hour<15:
        return("Good afternoon!")

    else:
        return("Good Evening!")

while True:
    print("USER : ",end="")
    query = input()
    print("BOT : ",end="")
    if "hello" in query or "hi" in query:
        print("Hi, how can i help you")
    elif "your name" in query or "who are you" in query:
        print("Hi, I am Jarvis, a ChatBot")
        print("       can I help you")
    elif "time now" in query:
        print("Sir the time is : ",Time)
    elif "bye" in query:
        print("Ok, Sir see you soon")
        break
    else:
        print("I couldn't understand")
