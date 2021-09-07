import time

import cv2
import os
import mediapipe as mp

from dotenv import load_dotenv

load_dotenv()
rtsp_username = os.environ.get('rtspUsername')
rtsp_password = os.environ.get('rtspPassword')
rtsp_address = os.environ.get('rtspAddress')

# cap = cv2.VideoCapture("rtsp://{}:{}@{}".format(rtsp_username, rtsp_password, rtsp_address))
cap = cv2.VideoCapture(0)
pTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()

while cap.isOpened():
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    print(results)
    if results.detections:
        for id, detection in enumerate(results.detections):
            # mpDraw.draw_detection(img, detection)
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih),
            cv2.rectangle(img, bbox, (0, 255, 123), 2)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS:{int(fps)}', (20, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 255, 255), 2)
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
