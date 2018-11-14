# USAGE
# python find_book.py

# import the necessary packages
import numpy as np
import cv2

# load the image containing the book
image = cv2.imread("ppao_hardcopy.png")
orig = image.copy()

# convert the image to grayscale, threshold it, and then perform a
# series of erosions and dilations to remove small blobs from the
# image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=2)

# find contours in the thresholded image, keeping only the largest
# one
(_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
c = max(cnts, key=cv2.contourArea)
cv2.drawContours(image, [c], -1, (0, 255, 255), 3)

# show the output image
thresh = np.dstack([thresh] * 3)
cv2.imshow("Output", np.hstack([orig, thresh, image]))
cv2.waitKey(0)