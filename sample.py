# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:15:39 2020

@author: Admin
"""

import cv2

img=cv2.imread('flower.jpg',1)#0 for black and white and 1 for color image
resized=cv2.resize(img,(600,500))
#print(type(img))
#print(img.shape)
cv2.imshow("Flower",resized)
cv2.waitKey(2000)
cv2.destroyAllWindows()