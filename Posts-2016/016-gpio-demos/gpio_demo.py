# USAGE
# python gpio_demo.py

# import the necessary packages
import RPi.GPIO as GPIO
import time
import cv2

# load the input image and display it to our screen
print("click on the image and press any key to continue...")
image = cv2.imread("hoover_dam.jpg")
cv2.imshow("Image", image)
cv2.waitKey(0)
print("moving on...")

# set the GPIO mode
GPIO.setmode(GPIO.BCM)

# loop over the LEDs on the TrafficHat and light each one
# individually
for i in (22, 23, 24):
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, GPIO.HIGH)
	time.sleep(3.0)
	GPIO.output(i, GPIO.LOW)

# perform a bit of cleanup
GPIO.cleanup()