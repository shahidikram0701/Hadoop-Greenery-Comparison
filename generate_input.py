import cv2
import numpy as np
img_file = 'myplace.png'
img = cv2.imread(img_file, cv2.IMREAD_COLOR) 
rows,cols=img.shape[0],img.shape[1]
count=0
target=open('myplace_input.txt','w')
for i in range(0,rows):
	for j in range(0,cols):
		target.write(str(img[i][j][0]))
		target.write("\t")
		target.write(str(img[i][j][1]))
		target.write("\t")
		target.write(str(img[i][j][2]))
		target.write("\n")
		

		

