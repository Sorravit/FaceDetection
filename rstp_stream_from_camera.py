import cv2
import os

from dotenv import load_dotenv

load_dotenv()
rtsp_username = os.environ.get('rtspUsername')
rtsp_password = os.environ.get('rtspPassword')
rtsp_address = os.environ.get('rtspAddress')

# cap = cv2.VideoCapture("rtsp://{}:{}@{}".format(rtsp_username, rtsp_password, rtsp_address))
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    cv2.putText(frame, "HEllooo", (20, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
