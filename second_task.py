import cv2 
import pytesseract
import numpy as np
import cv2 as cv
import docx
import pandas as pd

import opencv.write as write
import detection

#This task has Three parts: 
# reading from docx file and writing on the image
write.writeOnImage(r'C:\Users\nobarial\Desktop\ali\ComputerVision Assignment.docx')


#second part detects the text from the image
for i in range(1,400):
    
    image_name = "images/savedImage" + str(i) + ".jpg"
    detection.textDecector(image_name)
    
    
#third part- loading text file fo dataframe
df = pd.DataFrame()
path = r'C:\mine10\opencv\file_name.txt'
list_data = []
with open(path, "r") as f:
    print(f.read()) 
    list_data.append(f)
    
