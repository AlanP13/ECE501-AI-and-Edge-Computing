import cv2, sys
import numpy as np
from matplotlib import pyplot as plt

for image in sys.argv[1:]:
	img = cv2.imread(image)
	edges = cv2.Canny(img, 100, 200)
	plt.subplot(121), plt.imshow(img)
	plt.title('Original Image'), plt.xticks([]), plt.yticks([])
	plt.subplot(122), plt.imshow(edges, cmap='gray')
	plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
	plt.show()
	
	out = image[:-4] + '_edges.png'
	cv2.imwrite(out, edges)
