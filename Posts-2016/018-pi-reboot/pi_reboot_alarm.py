# USAGE
# python pi_alarm.py
# python pi_alarm.py --picamera 1

# import the necessary packages
from __future__ import print_function
from imutils.video import VideoStream
from gpiozero import TrafficHat
import argparse
import datetime
import logging
import imutils
import time
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--picamera", type=int, default=-1,
	help="whether or not the Raspberry Pi camera should be used")
ap.add_argument("-l", "--log", type=str, default="log.txt",
	help="path to output log file")
args = vars(ap.parse_args())

# open the logging file
logging.basicConfig(filename=args["log"], level=logging.DEBUG)

# initialize the video stream and allow the cammera sensor to
# warmup
logging.info("[{}] waiting for camera to warmup".format(
	datetime.datetime.now()))
vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)

# define the lower and upper boundaries of the "green"
# ball in the HSV color space
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)

# initialize the TrafficHat and whether or not the LED is on
th = TrafficHat()
ledOn = False

# loop over the frames from the video stream
while True:
	# grab the next frame from the video stream, resize the
	# frame, and convert it to the HSV color space
	frame = vs.read()
	frame = imutils.resize(frame, width=500)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

	# find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]
	center = None

	# only proceed if at least one contour was found
	if len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		# only proceed if the radius meets a minimum size
		if radius > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(frame, (int(x), int(y)), int(radius),
				(0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)

			# if the led is not already on, raise an alarm and
			# turn the LED on
			if not ledOn:
				logging.info("[{}] alarm ON".format(
					datetime.datetime.now()))
				th.buzzer.blink(0.1, 0.1, 10, background=True)
				th.lights.green.on()
				ledOn = True

	# if the ball is not detected, turn off the LED
	elif ledOn:
		logging.info("[{}] alarm OFF".format(
			datetime.datetime.now()))
		th.lights.green.off()
		ledOn = False

# do a bit of cleanup
logging.info("[{}] cleaning up".format(
	datetime.datetime.now()))
cv2.destroyAllWindows()
vs.stop()