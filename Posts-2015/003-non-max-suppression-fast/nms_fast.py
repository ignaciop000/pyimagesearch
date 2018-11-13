# import the necessary packages
from pyimagesearch.nms import non_max_suppression_fast
import numpy as np
import cv2

# construct a list containing the images that will be examined
# along with their respective bounding boxes
images = [
	("images/zombies_01.jpg", np.array([
	(180, 72, 244, 136),
	(186, 72, 250, 136),
	(186, 78, 250, 142)])),
	("images/zombies_02.jpg", np.array([
	(504, 306, 568, 370),
	(217, 150, 395, 328)])),
	("images/sarah4.jpg", np.array([
	(66, 100, 244, 278),
	(83, 100, 261, 278),
	(66, 117, 244, 295),
	(83, 117, 261, 295),
	(66, 133, 244, 311),
	(83, 133, 261, 311)]))]

# loop over the images
for (imagePath, boundingBoxes) in images:
	# load the image and clone it
	print "[x] %d initial bounding boxes" % (len(boundingBoxes))
	image = cv2.imread(imagePath)
	orig = image.copy()

	# loop over the bounding boxes for each image and draw them
	for (startX, startY, endX, endY) in boundingBoxes:
		cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 0, 255), 2)

	# perform non-maximum suppression on the bounding boxes
	pick = non_max_suppression_fast(boundingBoxes, 0.3)
	print "[x] after applying non-maximum, %d bounding boxes" % (len(pick))

	# loop over the picked bounding boxes and draw them
	for (startX, startY, endX, endY) in pick:
		cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)

	# display the images
	cv2.imshow("Original", orig)
	cv2.imshow("After NMS", image)
	cv2.waitKey(0)