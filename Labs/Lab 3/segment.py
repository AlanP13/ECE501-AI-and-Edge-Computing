import numpy as np
import cv2, sys
from matplotlib import pyplot as plt

for image in sys.argv[1:]:
	print('Processing image ' + image)
	
	img = cv2.imread(image)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	out = image[:-4] + '_thresh.png'
	cv2.imwrite(out, thresh)
	
	print('Finished processing')
	print('Output saved to ' + out)
