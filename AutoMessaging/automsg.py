import pyautogui
from time import sleep
from random import randint

x=500

def message():
	messagelist=["#PUBGMOBILE  #PMCC IGN: 1HP丨表丨EAGLE ID: 5506983947"]
	msg=messagelist[randint(0,len(messagelist)-1)]
	return msg

while True:
	printmsg="FARI"
	pyautogui.typewrite(printmsg)
	sleep(2)
	pyautogui.typewrite("\n")
	sleep(2)
	x=x-1
	if x==0:
		break
		