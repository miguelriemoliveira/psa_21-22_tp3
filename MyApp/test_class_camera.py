#!/usr/bin/env python3

import cv2
from ClassCamera import ClassCamera

# -----------------------------------------
# Initialization
# -----------------------------------------
cv2.namedWindow("preview")

camera = ClassCamera() # Create an instance of the ClassCamera
camera.connect(4)

# -----------------------------------------
# Execution (in cycle)
# -----------------------------------------
while True:
    success = camera.getData()
    if success:
        cv2.imshow("preview", camera.image)

    key = cv2.waitKey(20)
    if key == 113:  # exit on "q"
        break

# -----------------------------------------
# Termination
# -----------------------------------------
cv2.destroyWindow("preview")
camera.disconnect()
