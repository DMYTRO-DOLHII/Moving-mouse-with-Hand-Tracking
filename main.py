import cv2
import mediapipe as mp
import time
import HandTracking as ht

detector = ht.HandDetector()

detector.run()