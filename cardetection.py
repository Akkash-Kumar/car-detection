import cv2   #opencv

import imutils  #resize

cascade = 'cars.xml'   #initialise algorithm filename

alg = cv2.CascadeClassifier(cascade)   #loading algorithm


camera= cv2.VideoCapture(0)   #initialise primary camera

while True :   #to run infinitely

    _, img = camera.read()   #read frame from camera

    img = imutils.resize(img,width= 600)  #resize frame

    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #convert to b&w pic

    car = alg.detectMultiScale(grayImg,1.1,1)  #detect car coordinates

    for (x,y,w,h) in car:

        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)   #draw rectangle


    cv2.imshow('frame',img)  #display frame

    b = str(len(car))  #get length of cars

    a = int(b)  #convert to int

    print("North : %d" %(a))

    if a>=8:

        print("more traffic")

    else:

        print("no traffic")

    key = cv2.waitKey(10)  #wait for 10 frames

    if key == 27:  #when esc key is pressed,ends camera
        break

camera.release()  #release camera

cv2.destroyAllWindows()  #close window

    

