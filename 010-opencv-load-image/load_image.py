# USAGE
# python load_image.py --image grant-and-trex.jpg 

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

# load the image off disk
image = cv2.imread(args["image"])

# display the image on screen and wait for a key press
cv2.imshow("image", image)
cv2.waitKey(0)