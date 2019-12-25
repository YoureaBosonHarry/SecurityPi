import cv2
import numpy as np
import os
import requests


class MotionCamera():
    def __init__(self, threshold):
        self.last_frame = None
        self.threshold = threshold

    def capture(self):
        cap = cv2.VideoCapture(-1)
        while True:
            ret, frame = cap.read()
            gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    def check_motion(self, frame):
        pixel_sum = np.sum(frame)
        if pixel_sum  > self.threshold*self.last_frame:
            print("Oh god there is so much motion")

