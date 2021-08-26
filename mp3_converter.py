from __future__ import unicode_literals
import youtube_dl
import os
from moviepy.editor import *


ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    video = ydl.extract_info('https://www.youtube.com/watch?v=I4pQbo5MQOs', download=True)

    name = str(ydl.prepare_filename(video))


name = os.rename(str(name), 'video.mp4')
video = VideoFileClip(os.path.join('video.mp4'))
video.audio.write_audiofile(os.path.join('musics', 'audio.mp3'))
os.remove('video.mp4')
