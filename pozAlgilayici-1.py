import cv2
from cvzone.PoseModule import PoseDetector
 
cap = cv2.VideoCapture('kosu.mp4')
 
detector = PoseDetector()
posList = []
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img)
   
    cv2.imshow("Image", img)
    cv2.waitKey(1)
