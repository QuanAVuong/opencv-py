import cv2
import numpy as np

# https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html?highlight=imread#imread
# cv2.imread(filename[, flags]) -> retval
input = cv2.imread("./images/Gods Eye Graphics by Cantina.jpg")

# https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#void%20imshow(const%20string&%20winname,%20InputArray%20mat)
# cv2.imshow(winname, mat) -> None
# winname: Name of the window.
# image: Image to be shown.
cv2.imshow("Computer Visions", input)

# https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html?highlight=waitkey#waitkey
# Waits for a pressed key, allows us to input information when a image window is open
# cv2.waitKey([delay]) -> retval
# delay: Delay in milliseconds. 0 is the special value that means "forever".
cv2.waitKey(0)

# https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#void%20destroyAllWindows()
# cv2.destroyAllWindows() -> None
# The function destroyAllWindows destroys all of the opened HighGUI windows.
# Close all window, else program hangs
cv2.destroyAllWindows()


print(input.shape)		# => (417L, 1000L, 3L)
print 'Height of Image:', int(input.shape[0]), 'pixels'		# => Height of Image: 417 pixels
print 'Width of Image: ', int(input.shape[1]), 'pixels'		# => Width of Image:  1000 pixels
