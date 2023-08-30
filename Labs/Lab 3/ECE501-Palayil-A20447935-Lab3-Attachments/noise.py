import numpy as np
import cv2
import sys
import os

mean = 0
variance1 = 0.005
variance2 = 0.01

for image in sys.argv[1:]:
    img = cv2.imread(image)
    row, col, ch = img.shape

    noise1 = np.random.randn(row, col, ch) * np.sqrt(variance1)
    noisy1 = img + noise1.astype(np.uint8)

    noise2 = np.random.randn(row, col, ch) * np.sqrt(variance2)
    noisy2 = img + noise2.astype(np.uint8)

    base_name = os.path.splitext(image)[0]
    out1 = base_name + '_noise_005.png'
    out2 = base_name + '_noise_01.png'

    cv2.imwrite(out1, noisy1)
    cv2.imwrite(out2, noisy2)

