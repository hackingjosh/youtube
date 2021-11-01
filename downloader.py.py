from __future__ import unicode_literals
import youtube_dl
import PySimpleGUI as sg 
import subprocess 
from subprocess import Popen, PIPE
import os 
import tempfile 
import yt_dlp

sg.theme('BlueMono')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Close Window')],
            [sg.Multiline(size=(80, 5), key='textbox')]]  # identify the multiline via key option

# Create the Window
window = sg.Window('Test', layout)
#window.Maximize()
ydl_opts = {
    'format': 'mp4+bestaudio[ext=mp3]/best',
    'updatetime': False,
    'writethumbnail': True,
    'verbose': True,
    'output': '%(title)s.%(ext)s',
    'postprocessors': [{
    'key': 'EmbedThumbnail',
    'already_have_thumbnail': False,
    }],
}
     



while True:
    event, values = window.read()
    if event in (None, 'Close Window'): # if user closes window or clicks cancel
        break
    if event == 'Ok':
         vocab = list(values.values()) 
         ydl_opts = {}
         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([vocab[0]])
            sys.stdout = sys.__stdout__
            window['textbox'].update(f"{sys.stdout}")
            ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
         # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
         #    result = ydl.extract_info(
         #    vocab[0],
         #    download=True
         #    window['textbox'].print(f"{str(result.read())}") # We just want to extract the info
    #      #    )

    # if 'entries' in result:
    # # Can be a playlist or a list of videos
    #     video = result['entries'][0]
    #     out = video.decode('utf-8')
    #     print(out)
    #     window['textbox'].print(f"{video}")
    # else:
    # # Just a video
    #     video = result
    #     out = video.decode('utf-8')
    #     print(out)
    #     window['textbox'].print(f"{video}")

    # # print(video)
    # # video_url = video['url']
    # # print(video_url)








        


