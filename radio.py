from sound import *
from rss import *


playing = True
speechSave = 1

while(playing == True):
    choice = input("Enter 1 to type, 2 to quit or type 3 to play music\n")
    if(choice == '1'):
        sen = input("What should I say?\n")
        speak(sen,speechSave)
        if(speechSave == 1):
            speechSave = 0
        else:
            speechSave = 1
    elif(choice == '2'):
        print("Goodbye\n")
        playing = False
    elif(choice == '3'):
        play("Lunacy")
    else:
        print("Please try again\n")
