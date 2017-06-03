import numpy as np
import cv2

cap = cv2.VideoCapture(1)
count = 0
while(True):    
    _, frame = cap.read()
    frame = cv2.resize(frame,(28,28))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("frame%d.png" % count, frame)
    count = count
    
    cv2.imshow('pred',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
