import cv2
import mediapipe as mp

width=1280
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

findFace=mp.solutions.face_detection.FaceDetection()
drawFace=mp.solutions.drawing_utils

while True:
    ignore, frame = cam.read()
    frame=cv2.resize(frame,(width,height))
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=findFace.process(frameRGB)
    print(results.detections)
    if results.detections !=None:
        for face in results.detection:

            bBox=face.location_data.relative_bounding_box
            topLeft=(int(bBox.xmin*width),int(bBox.ymin*height))
            bottomRight=(int(bBox.xmin+ bBox.width)*width,int((bBox.ymin+bBox.height)*height))
            cv2.rectangle(frame,(topLeft,bottomRight),(0,255,0),3)

    cv2.imshow('Mircosoft webcam', frame)
    cv2.moveWindow('Mircosoft webcam',0,0)
    if cv2.waitKey(0) & 0xff ==ord('q'):
        break
cam.release()