import cv2 

webCam=cv2.VideoCapture(0)
while True: 
    ignore, frame = webCam.read()
    grayframe=cv2.cvtcolor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Webcam',grayframe)
    cv2.moveWindow('Webcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()


