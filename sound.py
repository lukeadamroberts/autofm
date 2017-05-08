from gtts import gTTS
from pygame import mixer
import os
import time
import re

################################################################################
## sound.py
## Contains all the functions related to speech playback.
################################################################################

#Immediately plays the given string. Needs an int value for the mp3 name.
def speak(x,num):
        tts = gTTS(text=x, lang='en')
        tts.save("voice"+str(num)+".mp3")
        mixer.music.load("voice"+str(num)+".mp3")
        mixer.music.play()

#Saves an mp3 for the given string. Returns the mp3 location.
def saveSpeak(x):
        tts = gTTS(text=x, lang='en')
        number = genName()
        tts.save("/run/shm/queue/"+number+".mp3")
        return "/run/shm/queue/"+number+".mp3"

#Plays a given mp3
def play(x):
        mixer.music.load(str(x)+'.mp3')
        mixer.music.play()

#Pauses the program for a short time
def pause():
    time.sleep(5)

#Gets a uniqe id for an mp3 and returns the value
def genName():
    a = os.listdir("/run/shm/queue")
    num = 1
    done = False
    while(done == False):
        match = False
        for i in a:
            b = re.sub('\.mp3$', '', i)
            if( str(num) == b ):
                match = True
        if(match == False):
            done = True
        else:
            num += 1
    return str(num)
