import os
import cv2
import sys
import numpy as np

path = r'D:\data\mask ml\images\val2017'
print(path)
for filename in os.listdir(path):
    if os.path.splitext(filename)[1] == '.png':
        print(filename)
        print(path+'\\'+filename)
        img = cv2.imread(path+'\\'+filename)
        print(type(img))
        #print(filename.replace(".png", ".jpg"))
        newfilename = filename.replace(".png", ".jpg")
        cv2.imwrite(path + newfilename, img)