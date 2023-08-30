import cv2, sys
import numpy as np

kernel = np.ones((5,5), np.uint8)

for image in sys.argv[1:]:
	print('Processing image ' + image)
	img = cv2.imread(image)

	opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
	closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
	erosion = cv2.erode(img, kernel, iterations=1)
	dilation = cv2.dilate(img, kernel, iterations=1)
	
	image = image[:-4]
	cv2.imwrite(image + '_opening.png', opening)
	cv2.imwrite(image + '_closing.png', closing)
	cv2.imwrite(image + '_erosion.png', erosion)
	cv2.imwrite(image + '_dilation.png', dilation)
	print('Image processed')
