import cv2
import numpy as np
from PIL import Image

bgr = cv2.imread('puzzle.png')
gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
_, roi = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
cv2.imwrite('/hroi.png', roi)
cont = cv2.findContours(roi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
output = np.zeros(gray.shape, dtype=np.uint8)
cv2.drawContours(output, cont[0], -1, (255, 255, 255))

# removing boundary
boundary = 255*np.ones(gray.shape, dtype=np.uint8)
boundary[1:boundary.shape[0]-1, 1:boundary.shape[1]-1] = 0

toremove = output & boundary
output = output ^ toremove
np.savetxt("foo.txt", output, delimiter=",")
print (output.size())
output[0:256, 0:256] = [255, 0, 0]
img = Image.fromarray(output, 'RGB')
img.save('my.png')
img.show()