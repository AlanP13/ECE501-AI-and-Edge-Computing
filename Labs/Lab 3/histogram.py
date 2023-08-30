import cv2, sys
import numpy as np
from matplotlib import pyplot as plt

for image in sys.argv[1:]:
	img = cv2.imread(image)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	equ = cv2.equalizeHist(img)
	plt.subplot(121), plt.imshow(img, cmap='gray')
	plt.title('Original Image'), plt.xticks([]), plt.yticks([])
	plt.subplot(122), plt.imshow(equ, cmap='gray')
	plt.title('Histogram Expansion'), plt.xticks([]), plt.yticks([])
	plt.show()
	
	out = image[:-4] + '_histogram.png'
	cv2.imwrite(out, equ)
