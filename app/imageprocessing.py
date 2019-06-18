import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

class ImageProcessing(object):
	def countBrightnessPixels(self, pixels, image):
		imgOriginal = cv.imread(image)
		imgCurt = imgOriginal[:(imgOriginal.shape[0]-round(imgOriginal.shape[0]*0.035)), :]
		imgGray = cv.cvtColor(imgCurt, cv.COLOR_BGR2GRAY)

		imgMask = np.zeros(imgGray.shape[:2], dtype = "uint8")
		for pixel in pixels:
			y = round(float(pixel[1]))
			x = round(float(pixel[0]))
			i=15
			if x+i < imgGray.shape[0] and y+i < imgGray.shape[1] or x-i > imgGray.shape[0] and y-i > imgGray.shape[1]:
				for xMask in range(imgMask.shape[0]):
					for yMask in range(imgMask.shape[1]):
						if x == xMask and y == yMask:
							imgMask = imgGray[x-i:x+i, y-i:y+i]

		# cv.imshow(image, imgMask)
		# cv.waitKey(0)
		# cv.destroyAllWindows()

		histograma = plt.hist(imgMask.ravel(), 256, [70, 256])	
		count = 0
		for i in histograma[0]:
			count = count + i

		return str(count)
