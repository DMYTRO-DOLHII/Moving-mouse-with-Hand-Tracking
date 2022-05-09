import cv2
import mediapipe as mp
import time
import HandTracking as ht

detector = ht.HandDetector()

wCam, hCam = 1080, 720

cap = cv2.VideoCapture(0)
cap.set(4, wCam)
cap.set(3, hCam)

while True:
    success, img = cap.read()

    cv2.imshow("Image", img)
    cv2.waitKey(1)