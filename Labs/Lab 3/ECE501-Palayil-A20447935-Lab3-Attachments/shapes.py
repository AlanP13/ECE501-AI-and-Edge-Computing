import cv2
import sys

if len(sys.argv) != 2:
    print('Usage: python3 shapes.py <image>')
    exit()

print('Image:', sys.argv[1])
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
_, threshold = cv2.threshold(img, 192, 255, cv2.THRESH_BINARY_INV)
_, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [approx], 0, (0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), font, 1, (0))
    elif len(approx) == 4:
        cv2.putText(img, "Rectangle", (x, y), font, 1, (0))
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), font, 1, (0))
    elif 6 < len(approx) < 15:
        cv2.putText(img, "Ellipse", (x, y), font, 1, (0))
    else:
        cv2.putText(img, "Circle", (x, y), font, 1, (0))

cv2.imshow("shapes", img)
cv2.imshow("Threshold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

out = sys.argv[1][:-4] + '_annotated.png'
cv2.imwrite(out, img)

