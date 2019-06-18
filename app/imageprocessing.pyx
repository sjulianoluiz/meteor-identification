import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
import cython
# from cython.parallel import prange

# class ImageProcessing(object):
@cython.boundscheck(False)
@cython.wraparound(False)
def countBrightnessPixels(pixels, image):
	imgOriginal = cv.imread(image)
	imgCurt = imgOriginal[:(imgOriginal.shape[0]-round(imgOriginal.shape[0]*0.035)), :]
	imgGray = cv.cvtColor(imgCurt, cv.COLOR_BGR2GRAY)

	imgMask = np.zeros(imgGray.shape[:2], dtype = "uint8")
	cdef int x, y, i, shapeX, shapeY, shapeX1, shapeY1

	#with nogil, parallel():
	for pixel in pixels:
		y = round(float(pixel[1]))
		x = round(float(pixel[0]))
		shapeX = imgGray.shape[0]
		shapeY = imgGray.shape[1]
		shapeX1 = imgMask.shape[0]
		shapeY1 = imgMask.shape[1]
		i=15
		if x+i < shapeX and y+i < shapeY or x-i > shapeX and y-i > shapeY:
			for xMask in range(shapeX1):
				for yMask in range(shapeY1):
					if x == xMask and y == yMask:
						imgMask[x-i:x+i, y-i:y+i] = imgGray[x-i:x+i, y-i:y+i]

	#cv.imshow(image, imgMask)
	#cv.waitKey(0)
	#cv.destroyAllWindows()

	#histograma = plt.hist(imgMask.ravel(), 256, [70, 256])	
	hist_mask = cv.calcHist ([imgGray.ravel()], [0], imgMask.ravel(), [256], [70,256])
	
	#plt.show()
	cdef int count = 0
	#for i in histograma[0]:
	#	count = count + i
	#print(count)
	#count = 0
	for i in hist_mask:
		count = count + i
	#print(count)

	return str(count)
#	print(count)
