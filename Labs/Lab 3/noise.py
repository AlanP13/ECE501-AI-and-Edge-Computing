import numpy as np
import cv2, sys
from matplotlib import pyplot as plt

mean = 0
sigma1 = 255*0.0707	# variance of 0.005
sigma2 = 2*sigma1	# variance of 0.01

for image in sys.argv[1:]:
	img = cv2.imread(image)
	row,col,ch = img.shape
	
	gauss = np.random.normal(mean, sigma1, (row,col,ch))
	gauss = gauss.reshape(row, col, ch)
	noisy = img + gauss
	
	out = image[:-4] + '_noise_005.png'
	cv2.imwrite(out, noisy)
	
	gauss = np.random.normal(mean, sigma2, (row,col,ch))
	gauss = gauss.reshape(row, col, ch)
	noisy = img + gauss
	
	out = image[:-4] + '_noise_01.png'
	cv2.imwrite(out, noisy)
