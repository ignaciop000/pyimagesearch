# USAGE
# python analyze_covers.py --output visualizations

# import the necessary packages
from __future__ import print_function
import numpy as np
import argparse
import json
import cv2

def filter_by_decade(decade, data):
	# initialize the list of filtered rows
	filtered = []

	# loop over the rows in the data list
	for row in data:
		# grab the publication date of the magazine
		pub = int(row["pubDate"].split("-")[0])

		# if the publication date falls within the current decade,
		# then update the filtered list of data
		if pub >= decade and pub < decade + 10:
			filtered.append(row)

	# return the filtered list of data
	return filtered

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True,
	help="path to output visualizations directory")
args = vars(ap.parse_args())

# load the JSON data file
data = json.loads(open("output.json").read())

# loop over each individual decade Time magazine has been published
for decade in np.arange(1920, 2020, 10):
	# initialize the magazine covers list
	print("[INFO] processing years: {}-{}".format(decade, decade + 9))
	covers = []

	# loop over the magazine issues belonging to the current decade
	for row in filter_by_decade(decade, data):
		# load the image
		cover = cv2.imread("output/{}".format(row["files"][0]["path"]))

		# if the image is None, then there was an issue loading it
		# (this happens for ~3 images in the dataset, likely due to
		# a download problem during the scraping process)
		if cover is not None:
			# resize the magazine cover, flatten it into a single
			# list, and update the list of covers
			cover = cv2.resize(cover, (400, 527)).flatten()
			covers.append(cover)

	# compute the average image of the covers then write the average
	# image to disk
	avg = np.average(covers, axis=0).reshape((527, 400, 3)).astype("uint8")
	p = "{}/{}.png".format(args["output"], decade)
	cv2.imwrite(p, avg)