
audio='speech.mp3'
from gtts import gTTS
from playsound import playsound
lang='en'
playsound(audio)
sp.save(audio)
sp=gTTS(text=text,lang=lang,slow=False)
text="a mi ek ta  baaalmarka computer. baal dao thik moto kortey parina"