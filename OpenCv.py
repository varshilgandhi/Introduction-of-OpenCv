# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 03:40:13 2021

@author: abc
"""

# OpenCv

import cv2

img = cv2.imread("C:\\Users\\abc\\Desktop\\image\\aeroplane\\test_image.jpg")
print(img.shape)


img = cv2.imread("C:\\Users\\abc\\Desktop\\image\\aeroplane\\test_image.jpg",0)
print(img.shape)

img = cv2.imread("C:\\Users\\abc\\Desktop\\image\\aeroplane\\test_image.jpg",2)
print(img.shape)

img = cv2.imread("C:\\Users\\abc\\Desktop\\image\\aeroplane\\test_image.jpg",0)
print("Tope left",img[0,0])
