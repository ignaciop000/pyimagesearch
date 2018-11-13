# USAGE
# python show_image.py

# import the necessary pacakges
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

# display our image
image = mpimg.imread("chelsea-the-cat.png")
plt.imshow(image)
plt.show()

# turn axex off
plt.axis("off")
plt.imshow(image)
plt.show()

# load the image using OpenCV and display it -- but uh, oh!
# our image doesn't look right!
image = cv2.imread("chelsea-the-cat.png")
plt.axis("off")
plt.imshow(image)
plt.show()

# OpenCV stores images in BGR order, whereas matplotlib expects
# them in RGB order -- the simple fix is to use OpenCV to convert
# from BGR to RGB
plt.axis("off")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()