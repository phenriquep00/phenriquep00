from __future__ import unicode_literals
import youtube_dl
import os
from moviepy.editor import *


def convert_to_mp3(link):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl: # Download .mp4 from youtube
        video = ydl.extract_info(str(link), download=True)

        name = str(ydl.prepare_filename(video))

    video = VideoFileClip(name)
    print(type(name))
    video.audio.write_audiofile(os.path.join('musics', f'{name[:-16]}.mp3'))  # Create a .mp3 file
    os.remove(name)  # Delete the .mp4 file


music = str(input('youtube link for the music: '))
convert_to_mp3(music)
