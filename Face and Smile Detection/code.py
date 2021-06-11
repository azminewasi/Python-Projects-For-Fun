import cv2

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')

def detect(gray, frame):
	faces=face_cascade.detectMultiScale(gray,1.3,5)
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),((x+w),(y+h)),(255,0,0),2)
		roi_gray=gray[y:y + h,x:x+w]
		roi_color=frame[y:y + h,x:x+w]
		facesy=eye_cascade.detectMultiScale(roi_gray,1.3,5)
		for (x,y,w,h) in facesy:
			cv2.rectangle(roi_color,(x,y),((x+w),(y+h)),(255,90,180),2)
		facesyT=smile_cascade.detectMultiScale(roi_gray,1.3,5)
		for (x,y,w,h) in facesyT:
			cv2.rectangle(roi_color,(x,y),((x+w),(y+h)),(25,190,190),2)
	return frame

video_capture=cv2.VideoCapture(0)
while True:
	ret,frame=video_capture.read()
	gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	canvas=detect(gray,frame)
	cv2.imshow('Video',canvas)
	k = cv2.waitKey(30) & 0xff  
	if k==27:
		break  
video_capture.release()
cv2.destroyAllWindows()