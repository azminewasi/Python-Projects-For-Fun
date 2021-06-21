import youtube_dl
import os

class Download(object):
	def _init_(self, url):
		self.url=url
		self.save_path=os.path.join(os.path.expanduser('~'),'Downloads')
		self.song()

	def song(self):
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
		'outtmpl':self.save_path+'/%(title)s.%(ext)s',
		'noplaylist':True
		}
		ydl=youtube_dl.YoutubeDL(opts)
		yd1.download(self.url)

if __name__=='__main__':
	url="https://www.youtube.com/watch?v=DOLxpAA5Hkw"
	Download(url)