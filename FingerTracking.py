import cv2
import os
import mediapipe as mp
from HandTracking import HandDetector

class FingerTracking:

    def __init__(self, wCam=1080, hCam=720):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, wCam)
        self.cap.set(4, hCam)
        self.detector = HandDetector()
        self.tipIds = [4, 8, 12, 16, 20]

    def run(self):
        while True:
            success, img = self.cap.read()
            img = self.detector.findHands(img)
            lmList = self.detector.findPosition(img, draw=False)

            if len(lmList) != 0:
                fingers = []

                # Thumb
                if lmList[self.tipIds[0]][1] > lmList[self.tipIds[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

                # 4 Fingers
                for id in range(1, 5):
                    if lmList[self.tipIds[id]][2] < lmList[self.tipIds[id] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                # print(fingers)
                totalFingers = fingers.count(0)
                print(totalFingers)

            cv2.imshow("Image", img)
            cv2.waitKey(1)
