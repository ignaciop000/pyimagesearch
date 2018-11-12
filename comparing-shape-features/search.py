# USAGE
# python search.py --index index.cpickle --query cropped.png

# import the necessary packages
from pyimagesearch.searcher import Searcher
from pyimagesearch.zernikemoments import ZernikeMoments
from pyimagesearch import imutils
import numpy as np
import argparse
import cPickle
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-", "--index", required = True,
	help = "Path to where the index file will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
args = vars(ap.parse_args())

# load the index
index = open(args["index"]).read()
index = cPickle.loads(index)

# load the query image, convert it to grayscale, and
# resize it
image = cv2.imread(args["query"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = imutils.resize(image, width = 64)

# threshold the image
thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
	cv2.THRESH_BINARY_INV, 11, 7)

# initialize the outline image, find the outermost
# contours (the outline) of the pokemon, then draw
# it
outline = np.zeros(image.shape, dtype = "uint8")
(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
cv2.drawContours(outline, [cnts], -1, 255, -1)

# compute Zernike moments to characterize the shape of
# pokemon outline
desc = ZernikeMoments(21)
queryFeatures = desc.describe(outline)

# perform the search to identify the pokemon
searcher = Searcher(index)
results = searcher.search(queryFeatures)
print "That pokemon is: %s" % results[0][1].upper()

# show our images
cv2.imshow("image", image)
cv2.imshow("outline", outline)
cv2.waitKey(0)