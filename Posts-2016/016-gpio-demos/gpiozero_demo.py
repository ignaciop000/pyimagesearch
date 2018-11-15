# USAGE
# python gpiozero_demo.py

# import the necessary packages
from gpiozero import TrafficHat
import time
import cv2

# load the input image and display it to our screen
print("click on the image and press any key to continue...")
image = cv2.imread("hoover_dam.jpg")
cv2.imshow("Image", image)
cv2.waitKey(0)
print("moving on...")

# initialize the TrafficHAT, then create the list of lights
th = TrafficHat()
lights = (th.lights.green, th.lights.amber, th.lights.red)

# loop over the lights and turn them on one-by-one
for light in lights:
	light.on()
	time.sleep(3.0)
	light.off()