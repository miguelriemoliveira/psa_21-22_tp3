#!/usr/bin/env python3

import cv2

# -----------------------------------------
# Initialization
# -----------------------------------------
cv2.namedWindow("preview")
vc = cv2.VideoCapture(4)

# -----------------------------------------
# Execution (in cycle)
# -----------------------------------------
while True:
    rval, image = vc.read()  # get new image from camera

    cv2.imshow("preview", image)
    key = cv2.waitKey(20)
    if key == 113:  # exit on "q"
        break

# -----------------------------------------
# Termination
# -----------------------------------------
vc.release()
cv2.destroyWindow("preview")
