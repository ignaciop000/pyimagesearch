# USAGE
# python humoments.py

# import the necessary packages
import cv2

# load the image, convert it to grayscale, and display it
image = cv2.imread("diamond.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("image", image)

# extract Hu Moments from the image -- this list of numbers
# is our 'feature vector' used to quantify the shape of the
# object in our image
features = cv2.HuMoments(cv2.moments(image)).flatten()
print features

# wait for a keypress
cv2.waitKey(0)