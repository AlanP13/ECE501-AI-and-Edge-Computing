import cv2
import sys

for image in sys.argv[1:]:
    print('Processing image:', image)
    
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    out = image.rsplit('.', 1)[0] + '_thresh.png'
    cv2.imwrite(out, thresh)
    
    print('Finished processing')
    print('Output saved to:', out)

