import cv2
import numpy as np
cap= cv2.VideoCapture(0)
back= cv2.imread('C:\invisible\image.jpg')

while cap.isOpened():
    #take each frame
    ret, frame= cap.read()

    if ret:
        #convert to hsv
        hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #cv2.imshow("hsv",hsv)
        #how to get hsv value?
        #lower: hue-10,100,100, higher: h+10,255,255
        green= np.uint8([[[0,0,255]]])#bgr value of green
        hsv_green= cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
        #get the hsv value of red form bgr
        #print(hsv_red)
        #threshold the hsv value to get only read colors
        l_green= np.array([0, 100,100])
        u_green= np.array([10,255,255])

        mask= cv2.inRange(hsv, l_green, u_green)
        #cv2.imshow("mask",mask)
        #part 1 is all things red
        part1= cv2.bitwise_and(back, back, mask=mask)

        mask= cv2.bitwise_not(mask)

        #part 2 is all things not red
        part2= cv2.bitwise_and(frame, frame, mask=mask)
        kernel = np.ones((5,5),np.uint8)
        dilation = cv2.dilate(part1,kernel, iterations=1)
        cv2.imshow("cloak", dilation+part2)

        if cv2.waitKey(5)==ord('q'):
           break

cap.release()
cv2.destroyAllWindows()
