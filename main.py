import cv2
import mediapipe as mp
import time
import HandTracking as ht
import FingerTracking as ft

if __name__ == "__main__":
    # detector = ht.HandDetector()
    # detector.run()
    tracker = ft.FingerTracking()
    tracker.run()