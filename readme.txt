Auto FM - Robot Radio
####################

Description:
--------------------
This script simulates a radio station, using your music and your rss feeds to play
a constant mix of music and news.

MP3s:
--------------------
Music needs to be placed in the '/Music' folder (duh). These tracks can't be in
sub-folders and must have at least the artist and track name details given in the
MP3.

RSS feeds:
--------------------
The urls for the rss feeds need placing in the rss list array in rss.py.

Requirements:
--------------------
All the above need to be installed using pip before the script will run. I might
write a script that installs them all if I get round to it:
  pygame
  gTTS
  tinytag
  feedparser
  mutagen

Known issues:
--------------------
  -Some mp3s run at a weird speed, this is something to do with the bitrate of those
  songs. Again I haven't got round to fixing it.
  -Since the voice MP3s are being constanly written to and deleted from the disk,
  this script could cripple your hard drive if you're not careful. I'm looking
  for a more elegant solution.
