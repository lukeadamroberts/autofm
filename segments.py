from sound import *

################################################################################
## segments.py
## Contains all the functions related to frequently used bits of dialouge, things
## like openers or segways into songs/news.
################################################################################

#Returns the opening lines
def opening():
    a = []
    #a.append(saveSpeak("Welcome to auto FM"))
    #a.append(saveSpeak("robot. radio"))
    #a.append(saveSpeak("radio"))
    a.append("jingles/intro.mp3")
    return a

#Removes the 10 mp3s from a given number
def cleanUp(i,x):
    j = i + x
    no = True
    while( i < j):
        try:
            os.remove("queue/"+str(i)+".mp3")
        except:
            no = True
        i += 1

#Removes all mp3s
def garbageCollect():
    a = os.listdir("queue")
    for i in a:
        os.remove("queue/"+i)
