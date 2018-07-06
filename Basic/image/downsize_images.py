import os
import cv2
import numpy



"""
	Downsize images to 64 x 60 using opencv and also convert to gray scale
"""


def downsize(url):
	print(url)
	image = cv2.imread(url,0)
	#cv2.imshow("orginal",image)
	#plt.imshow(image)


	down_sized = cv2.resize(image,(64,60))

	#down_sized = cv2.cvtColor(down_sized,cv2.COLOR_BGR2GRAY)

	return down_sized

for f in os.listdir("."):
	if '.jpg' in f or '.png' in f:	
		down_sized = downsize(f)
	
		cv2.imwrite(f[:-4] + "_64x60.png",down_sized)	

	#plt.imshow(down_sized)
