import cv2
import numpy as np

# https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html?highlight=imread#imread
# cv2.imread(filename[, flags]) → retval
image = cv2.imread("./images/Computer-Vision.jpg")

# https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#void%20imshow(const%20string&%20winname,%20InputArray%20mat)
# cv2.imshow(winname, mat) → None
# winname – Name of the window.
# image – Image to be shown.
cv2.imshow("Computer Visions", image)