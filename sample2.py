# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:01:05 2020


@author: Admin
"""
import cv2
Face_Cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("vvk.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=Face_Cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,500,500),2)
cv2.imshow("NTR",img)
cv2.waitKey()
cv2.destroyAllWindows()