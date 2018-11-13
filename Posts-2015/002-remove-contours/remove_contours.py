# USAGE
# python remove_contours.py

# import the necessary packages
import numpy as np
import cv2

def is_contour_bad(c):
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)

	# the contour is 'bad' if it is not a rectangle
	return not len(approx) == 4

# load the shapes image, convert it to grayscale, and edge edges in
# the image
image = cv2.imread("shapes.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 50, 100)
cv2.imshow("Original", image)

# find contours in the image and initialize the mask that will be
# used to remove the bad contours
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
mask = np.ones(image.shape[:2], dtype="uint8") * 255

# loop over the contours
for c in cnts:
	# if the contour is bad, draw it on the mask
	if is_contour_bad(c):
		cv2.drawContours(mask, [c], -1, 0, -1)

# remove the contours from the image and show the resulting images
image = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask", mask)
cv2.imshow("After", image)
cv2.waitKey(0)