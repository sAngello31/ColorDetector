import cv2 as cv
import numpy as np

def dibujarContornos(mask, color, colorText):
    contornos, jera = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cont = 0
    for c in contornos:
        area = cv.contourArea(c)
        if area > 3000:
            x,y,w,h = cv.boundingRect(c)
            cv.rectangle(frame, (x,y), (x+w, h+y), color, 4)
            cv.putText(frame, colorText, (x+10, y+20), 0, 0.75, color, 2,cv.LINE_AA)
            cont = cont + 1
    
    return cont
    

lowRed1 = np.array([0, 100, 20], dtype= np.uint8)
highRed1 = np.array([5, 255, 255], dtype= np.uint8)

lowRed2 = np.array([175, 100, 20], dtype= np.uint8)
highRed2 = np.array([179, 255, 255], dtype= np.uint8)

lowYellow = np.array([15, 200, 200], dtype=np.uint8)
highYellow = np.array([45,255,255], dtype=np.uint8)

lowBlue = np.array([100, 100, 20], dtype=np.uint8)
highBlue = np.array([110, 255, 255], dtype=np.uint8)

contRed = 0
contYellow = 0

capture = cv.VideoCapture(0)

while True:
    ret, frame = capture.read()
    #print(frame.shape)
    frameHSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    maskRed1 = cv.inRange(frameHSV,lowRed1, highRed1)
    maskRed2 = cv.inRange(frameHSV, lowRed2, highRed2)
    maskRed = cv.add(maskRed1, maskRed2)

    maskYellow = cv.inRange(frameHSV, lowYellow, highYellow)
    maskBlue = cv.inRange(frameHSV, lowBlue, highBlue)

    contRed = dibujarContornos(maskRed, (0,0,255), "Rojo")
    contYellow = dibujarContornos(maskYellow, (0, 255, 255), "Amarillo")
    #dibujarContornos(maskBlue, (255, 0, 0), "Azul")

    cv.rectangle(frame, (0, 380), (200, 480), (255,255,255), -1)
    cv.putText(frame, "Rojo: {}".format(contRed),(0,420), 0, 0.75,(0,0,0), 2, cv.LINE_AA)
    cv.putText(frame, "Amarillo: {}".format(contYellow), (0, 450), 0, 0.75, (0,0,0), 2, cv.LINE_AA)

    cv.imshow("maskRed", maskYellow)
    cv.imshow("frame", frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

capture.release()
cv.destroyAllWindows()

