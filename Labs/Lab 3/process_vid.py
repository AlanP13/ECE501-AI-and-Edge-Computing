import numpy as np
import cv2, sys, os, glob

if len(sys.argv) != 2:
	print('Usage: python3 process_vid.py <video file>')

cap = cv2.VideoCapture(sys.argv[1])
fourcc = cap.get(cv2.CAP_PROP_FOURCC)
frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)
print('Number of frames: ' + str(frames))
print('Frames per second: ' + str(fps))
name = sys.argv[1][:-4]

save = input('Save video frames? [Y/N]')
save = save.lower() == 'y'

if save:
	try:
		os.mkdir(name)
	except OSError:
		print('Failed to make directory ' + name)
		exit()
	else:
		print('Created directory ' + name)

counter = 0
while(cap.isOpened()):
	ret, frame = cap.read()
	if ret == False:
		break
	
	if save:
		out = name + '/' + str(counter) + '.png'
		cv2.imwrite(out, frame)
	'''
	cv2.imshow('frame', frame)
	if cv2.waitKey(10) & 0xFF == ord('q'):
		break
	'''
	
	counter += 1

cap.release()
cv2.destroyAllWindows()

annotate = input('Perform shape extraction on frames? [Y/N]')
annotate = annotate.lower() == 'y'

def shapes(image):
	font = cv2.FONT_HERSHEY_COMPLEX
	img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
	_, threshold = cv2.threshold(img, 192, 255, cv2.THRESH_BINARY_INV)
	contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	
	for cnt in contours:
		approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
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
	return img

if save and annotate:
	for image in glob.glob(name + '/*.png'):
		print('Annotating frame ' + image)
		annotated = shapes(image)
		cv2.imwrite(image, annotated)
	print('All frames annotated')
elif annotate:
	print('Cannot annotate when no frames were saved')

new = input('Save new video from frames? [Y/N]')
if new.lower() != 'y':
	exit()

video = input('Video name: ')

frame = cv2.imread(name + '/0.png')
height, width, _ = frame.shape
size = (width, height)

def save_video(vid_name, framerate):
	vid = cv2.VideoWriter(vid_name, int(fourcc), framerate, size)

	for i in range(counter):
		print('Adding frame ' + str(i+1))
		img = cv2.imread(name + '/' + str(i) + '.png')
		vid.write(img)
	print('All frames added')

	cv2.destroyAllWindows()
	vid.release()

save_video(video + '.avi', fps)
save_video(video + '_slower.avi', fps/4)
