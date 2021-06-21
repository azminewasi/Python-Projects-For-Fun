import youtube_dl
import os

url="https://youtu.be/xLYiIBCN9ec"
save_path=os.path.join(os.path.expanduser('~'),'Downloads')
opts={
		'verbose':True,
		'fixup':'detect_or_warn',
		'format':'bestaudio/best',
		'postprocessors':[{
		'key':'FFmpegExtractAudio',
		'preferredcodec':'mp3',
		'preferredquality':'1411',
		}],
		'extractaudio':True,
		'outtmpl':save_path+'/%(title)s.%(ext)s',
		'noplaylist':True
		}
ydl=youtube_dl.YoutubeDL(opts)
ydl.download(url)