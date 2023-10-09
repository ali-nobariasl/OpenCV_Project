import numpy as np
import cv2 as cv
import docx


def writeOnImage(file_path):
    # extracting data from docx file to string
    documents =  docx.Document(file_path)
    all_params = documents.paragraphs

    data = all_params[0].text

    #adding text on the blank image
    x = 25
    y = 25
    number =1
    for i in data.split("'"):
        blank = np.zeros((50,10000,3), dtype='uint8')
        cv.putText(blank, str(i)  , (x,y),cv.FONT_HERSHEY_TRIPLEX,1.0, color= (0,255,0),thickness=1)

        filename = 'portagal/savedImage' + str(number) + '.jpg'
        cv.imwrite(filename, blank) 
        number += 1

        



    #cv.imshow('blank', blank)
    #cv.waitKey(0)
    
    
    
