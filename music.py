from tinytag import TinyTag
from sound import *
import os
import random

################################################################################
## music.py
## Contains all the functions related to music.
################################################################################

# Gets the details of a song and introduces it, producing an mp3 which is added
# to the queue folder. The mp3's name is returned so it can be added to the queue.
def introArtist(song):
    a = []
    tag = TinyTag.get(song)
    x = "Coming up next, we have "+tag.title+" by "+tag.artist
    a.append(saveSpeak(x))
    return a

# Picks a song from the music folder. The name of the song is returned so that it
# can be added to the queue.
def pickSong():
    a = os.listdir("Music")
    b = random.choice(a)
    return b

# This function picks a song, makes an introduction for it. These things are returned
# as an array to be added to the queue.
def playSong():
    x = pickSong()
    y = "Music/"+x
    z = introArtist(y)
    return z+[y]
