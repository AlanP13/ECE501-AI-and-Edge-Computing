import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

kernel = np.ones((5, 5), np.uint8)

for image in sys.argv[1:]:
    print('Processing image ' + image)
    img = cv2.imread(image)

    # Histogram Expansion
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equ = cv2.equalizeHist(gray)
    plt.subplot(121), plt.imshow(gray, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(equ, cmap='gray')
    plt.title('Histogram Expansion'), plt.xticks([]), plt.yticks([])
    plt.show()

    out_histogram = image[:-4] + '_histogram.png'
    cv2.imwrite(out_histogram, equ)

    # Morphological Operations
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

