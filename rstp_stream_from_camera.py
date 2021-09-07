import time

import cv2
import os

from dotenv import load_dotenv

load_dotenv()
rtsp_username = os.environ.get('rtspUsername')
rtsp_password = os.environ.get('rtspPassword')
rtsp_address = os.environ.get('rtspAddress')

cap = cv2.VideoCapture("rtsp://{}:{}@{}".format(rtsp_username, rtsp_password, rtsp_address))
# cap = cv2.VideoCapture(0)
pTime = 0
while cap.isOpened():
    ret, frame = cap.read()
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(frame, f'FPS:{int(fps)}', (20, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 255, 255), 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
