# USAGE
# python overlay.py

# import the necessary packages
from __future__ import print_function
import numpy as np
import cv2

# load the image
image = cv2.imread("mexico.jpg")

# loop over the alpha transparency values
for alpha in np.arange(0, 1.1, 0.1)[::-1]:
	# create two copies of the original image -- one for
	# the overlay and one for the final output image
	overlay = image.copy()
	output = image.copy()

	# draw a red rectangle surrounding Adrian in the image
	# along with the text "PyImageSearch" at the top-left
	# corner
	cv2.rectangle(overlay, (420, 205), (595, 385),
		(0, 0, 255), -1)
	cv2.putText(overlay, "PyImageSearch: alpha={}".format(alpha),
		(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)

	# apply the overlay
	cv2.addWeighted(overlay, alpha, output, 1 - alpha,
		0, output)

	# show the output image
	print("alpha={}, beta={}".format(alpha, 1 - alpha))
	cv2.imshow("Output", output)
	cv2.waitKey(0)