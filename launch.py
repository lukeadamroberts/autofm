from sound import *
from rss import *
from segments import *
from music import *
import os
import pygame
import time
import random

# This function adds 5 news items to the queue with a breif introduction.
def newsSeg():
    i = 1
    a = []
    a.append(saveSpeak("Here is some news"))
    while(i<6):
        a.append(saveSpeak(newsList[0]))
        newsList.remove(newsList[0])
        if(len(newsList) == 0):
            return a
        i += 1
    return a

#Create radio variables
queue = []
newsList = []
mixer.init()
newsToggle = True

#Add the opening to the queue
queue += opening()
#Update the news list
newsList = newsList + collectRss()

#Start with either the news or a song
choice = random.randint(0,1)
if(choice == 0):
    queue.append(saveSpeak("Let's start with the news."))
    queue += newsSeg()
    queue.append(saveSpeak("Now let's move on with some music"))
    queue += playSong()
else:
    queue.append(saveSpeak("Let's start with a tune."))
    queue += playSong()
    queue.append(saveSpeak("Here's the news."))
    queue += newsSeg()

#Start the radio
while(len(queue) > 0):
    # Check what number mp3 is being played, this is then used to delete certain
    # mp3s to control the maximum number of mp3s in the queue file.
    if(queue[0] == "queue/13.mp3"):
        cleanUp(1,10)
    if(queue[0] == "queue/3.mp3"):
        cleanUp(11,10)
    ############################################################################
    # Load and play the first item in the queue
    mixer.music.load(queue[0])
    mixer.music.play()

    # The program remains in this next loop while the queue item above is playing
    # this is required otherwise the mp3s will constanly replace each other.
    playing = True
    while(playing == True):
        # Leave this loop once the queue item is finished playing.
        if(mixer.music.get_busy() == 0):
            playing = False
    # Remove the item from the queue.
    queue.remove(queue[0])

    # If the queue has less than 5 items load some new ones in.
    if(len(queue) < 5):
        # Choose to add either music or news, if the randint below chooses news
        # then music will still be added if the newslist is empty or news has just
        # been added. This is to avoid news read every 5 min.
        choice = random.randint(0,1)
        if(choice == 0):
            if(len(newsList) == 0 or newsToggle == True):
                queue.append(saveSpeak("It's time for some more music"))
                queue += playSong()
                newsToggle = False
            else:
                queue.append(saveSpeak("Let's have some more news."))
                queue += newsSeg()
                newsToggle = True
        else:
            queue += playSong()
    #If the news list is empty, refil it
    newsList = newsList + collectRss()

#There is currently no way to end the program so this stuff is kind of redundant.
#Show is over, play the outro
play("Outro")
pause()
#Remove all the queue files
garbageCollect()
