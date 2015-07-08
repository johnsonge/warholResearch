# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 12:50:39 2013

@author: Thomas Brady
@author: Eugene Johnson
"""

from PIL import Image
import os,sys
from os import walk
import csv

##(Folder must contain only image files to be viewed)
mypath = ("./flowers/")

# reads files into list
def inFile():
    f = next(os.walk(mypath))[2]
    del f[0]  
    return f

def analyze():
    files = inFile()

    print ("Saving csv as 'Workbook'...")
    inExcel = ("Workbook.csv")
    excelFile = open(inExcel, 'rb')
    reader = csv.reader(excelFile)    
    rows = []
    for row in reader:
        rows.append(row)
    excelFile.close


    ## w = write, a = append
    ## rewrite to replace current sheet. wont give errors of adding to full space
    directory = mypath
    excelFile = open(inExcel, 'w')
    writer = csv.writer(excelFile, dialect = 'excel')
#Column names
    # With displayed colors
    # writer.writerow(['imageName', 'flower1', 'color1', 'flower2', 'color2', 'flower3', 'color3', 'flower4', 'color4', 'background', 'color'])
    writer.writerow(['imageName', 'color1', 'color2', 'color3', 'color4', 'size', 'relation'])
    
    for f in files:
        imageIn = f
        pic = Image.open(directory + imageIn)
        
        scale = pic.size
        
        # flower coordinates 
        xF1 = scale[0]*.20
        yF1 = scale[1]*.33
        xF2 = scale[0]*.80
        yF2 = scale[1]*.20
        xF3 = scale[0]*.33
        yF3 = scale[1]*.75
        xF4 = scale[0]*.75
        yF4 = scale[1]*.85
        xBack = scale[0]*.5
        yBack = scale[1]*.45
        val = pic.load()
        
        # Set Variables for determining color of flowers using above given coordinates

        rgbFlower1 = ''
        rgbFlower2 = ''
        rgbFlower3 = ''
        rgbFlower4 = ''
        background = val[xBack,yBack]


        flower1 = val[xF1,yF1]
        flower2 = val[xF2,yF2]
        flower3 = val[xF3,yF3]
        flower4 = val[xF4,yF4]

        rgbFlower1 = val[xF1,yF1]
        rgbFlower2 = val[xF2,yF2]
        rgbFlower3 = val[xF3,yF3]
        rgbFlower4 = val[xF4,yF4]
    
        
        # Gives the Red, Green, or Blue equivalent from the previously attained decimal rgb value

## Color analysis of Flowers
    ##Flower 1 (Upper Left)
        flowerColor1 = 0
        #White
        if rgbFlower1[0] > 190 and rgbFlower1[1] > 190 and rgbFlower1[2] > 190:
            flowerColor1 = 4
          
        #Red
        elif (rgbFlower1[0] > rgbFlower1[1] and rgbFlower1[0] > rgbFlower1[2]):
            flowerColor1 = 1 
            #Orange
            if (flowerColor1 == 1 and rgbFlower1[0] > 200 and rgbFlower1[0] < 215 and rgbFlower1[1] > 65 and rgbFlower1[1] < 110 and rgbFlower1[2] > 11 and rgbFlower1[2] < 65): 
                flowerColor1 = 5
            #Pink
            if (flowerColor1 == 1 and rgbFlower1[0] > 185 and rgbFlower1[0] < 250 and rgbFlower1[1] > 50 and rgbFlower1[1] < 125 and rgbFlower1[2] > 85 and rgbFlower1[2] < 185): 
                flowerColor1 = 8
            #Yellow
            elif (flowerColor1 == 1 and rgbFlower1[1] > 135 and rgbFlower1[1] < 225 and rgbFlower1[2] < 125): 
                flowerColor1 = 6
            #Magenta
            elif (flowerColor1 == 1 and rgbFlower1[0] > 165 and rgbFlower1[0] < 200 and rgbFlower1[1] > 30 and rgbFlower1[1] < 70 and rgbFlower1[2] > 60 and rgbFlower1[2] < 120): 
                flowerColor1 = 10
                      
        #Green
        elif (rgbFlower1[1] > rgbFlower1[0] and rgbFlower1[1] > rgbFlower1[2]):
            flowerColor1 = 2
            #Teal
            if (flowerColor1 == 2 and rgbFlower1[0] > 100): 
                flowerColor1 = 7
            
        #Blue
        elif (rgbFlower1[2] > rgbFlower1[0] and rgbFlower1[2] > rgbFlower1[1]):
            flowerColor1 = 3
            #Purple
            if (flowerColor1 == 3 and rgbFlower1[0] > 60 and rgbFlower1[0] < 100 and rgbFlower1[1] > 50 and rgbFlower1[1] < 90 and rgbFlower1[2] > 120 and rgbFlower1[2] < 160): 
                flowerColor1 = 9               

            #UNKNOWN
        else:
            flowerColor1 = 11


    ##Flower 2 (Upper Right)
        flowerColor2 = 0


            #White
        if rgbFlower2[0] > 190 and rgbFlower2[1] > 190 and rgbFlower2[2] > 190:
            flowerColor2 = 4
            
        #Red
        elif (rgbFlower2[0] > rgbFlower2[1] and rgbFlower2[0] > rgbFlower2[2]):
            flowerColor2 = 1 
            #Orange
            if (flowerColor2 == 1 and rgbFlower2[0] > 200 and rgbFlower2[0] < 215 and rgbFlower2[1] > 65 and rgbFlower2[1] < 110 and rgbFlower2[2] > 11 and rgbFlower2[2] < 65): 
                flowerColor2 = 5
            #Pink
            if (flowerColor2 == 1 and rgbFlower2[0] > 185 and rgbFlower2[0] < 250 and rgbFlower2[1] > 50 and rgbFlower2[1] < 125 and rgbFlower2[2] > 85 and rgbFlower2[2] < 185): 
                flowerColor2 = 8
            #Yellow
            elif (flowerColor2 == 1 and rgbFlower2[1] > 135 and rgbFlower2[1] < 225 and rgbFlower2[2] < 125): 
                flowerColor2 = 6
            #Magenta
            elif (flowerColor2 == 1 and rgbFlower2[0] > 165 and rgbFlower2[0] < 200 and rgbFlower2[1] > 30 and rgbFlower2[1] < 70 and rgbFlower2[2] > 60 and rgbFlower2[2] < 120): 
                flowerColor2 = 10
                      
        #Green
        elif (rgbFlower2[1] > rgbFlower2[0] and rgbFlower2[1] > rgbFlower2[2]):
            flowerColor2 = 2
            #Teal
            if (flowerColor2 == 2 and rgbFlower2[0] > 100): 
                flowerColor2 = 7
            
        #Blue
        elif (rgbFlower2[2] > rgbFlower2[0] and rgbFlower2[2] > rgbFlower2[1]):
            flowerColor2 = 3
            #Purple
            if (flowerColor2 == 3 and rgbFlower2[0] > 60 and rgbFlower2[0] < 100 and rgbFlower2[1] > 50 and rgbFlower2[1] < 90 and rgbFlower2[2] > 120 and rgbFlower2[2] < 160): 
                flowerColor2 = 9               
        

        #UNKNOWN
        else:
            flowerColor2 = 11


    ##Flower 3 (Lower Left)
        flowerColor3 = 0


        #White
        if rgbFlower3[0] > 190 and rgbFlower3[1] > 190 and rgbFlower3[2] > 190:
            flowerColor3 = 4
            
        #Red
        elif (rgbFlower3[0] > rgbFlower3[1] and rgbFlower3[0] > rgbFlower3[2]):
            flowerColor3 = 1 
            #Orange
            if (flowerColor3 == 1 and rgbFlower3[0] > 200 and rgbFlower3[0] < 215 and rgbFlower3[1] > 65 and rgbFlower3[1] < 110 and rgbFlower3[2] > 11 and rgbFlower3[2] < 65): 
                flowerColor3 = 5
            #Pink
            if (flowerColor3 == 1 and rgbFlower3[0] > 185 and rgbFlower3[0] < 250 and rgbFlower3[1] > 50 and rgbFlower3[1] < 125 and rgbFlower3[2] > 85 and rgbFlower3[2] < 185): 
                flowerColor3 = 8
            #Yellow
            elif (flowerColor3 == 1 and rgbFlower3[1] > 135 and rgbFlower3[1] < 225 and rgbFlower3[2] < 125): 
                flowerColor3 = 6
            #Magenta
            elif (flowerColor3 == 1 and rgbFlower3[0] > 165 and rgbFlower3[0] < 200 and rgbFlower3[1] > 30 and rgbFlower3[1] < 70 and rgbFlower3[2] > 60 and rgbFlower3[2] < 120): 
                flowerColor3 = 10
                      
        #Green
        elif (rgbFlower3[1] > rgbFlower3[0] and rgbFlower3[1] > rgbFlower3[2]):
            flowerColor3 = 2
            #Teal
            if (flowerColor3 == 2 and rgbFlower3[0] > 100): 
                flowerColor3 = 7
            
        #Blue
        elif (rgbFlower3[2] > rgbFlower3[0] and rgbFlower3[2] > rgbFlower3[1]):
            flowerColor3 = 3
            #Purple
            if (flowerColor3 == 3 and rgbFlower3[0] > 60 and rgbFlower3[0] < 100 and rgbFlower3[1] > 50 and rgbFlower3[1] < 90 and rgbFlower3[2] > 120 and rgbFlower3[2] < 160): 
                flowerColor3 = 9               
         
        #UNKNOWN
        else:
            flowerColor3 = 11


    ##Flower 4 (Lower Left)
        flowerColor4 = 0


        #White
        if rgbFlower4[0] > 190 and rgbFlower4[1] > 190 and rgbFlower4[2] > 190:
            flowerColor4 = 4
            
        #Red
        elif (rgbFlower4[0] > rgbFlower4[1] and rgbFlower4[0] > rgbFlower4[2]):
            flowerColor4 = 1 
            #Orange
            if (flowerColor4 == 1 and rgbFlower4[0] > 200 and rgbFlower4[0] < 215 and rgbFlower4[1] > 65 and rgbFlower4[1] < 110 and rgbFlower4[2] > 11 and rgbFlower4[2] < 65): 
                flowerColor4 = 5
            #Pink
            if (flowerColor4 == 1 and rgbFlower4[0] > 185 and rgbFlower4[0] < 250 and rgbFlower4[1] > 50 and rgbFlower4[1] < 125 and rgbFlower4[2] > 85 and rgbFlower4[2] < 185): 
                flowerColor4 = 8
            #Yellow
            elif (flowerColor4 == 1 and rgbFlower4[1] > 135 and rgbFlower4[1] < 225 and rgbFlower4[2] < 125): 
                flowerColor4 = 6
            #Magenta
            elif (flowerColor4 == 1 and rgbFlower4[0] > 165 and rgbFlower4[0] < 200 and rgbFlower4[1] > 30 and rgbFlower4[1] < 70 and rgbFlower4[2] > 60 and rgbFlower4[2] < 120): 
                flowerColor4 = 10
                      
        #Green
        elif (rgbFlower4[1] > rgbFlower4[0] and rgbFlower4[1] > rgbFlower4[2]):
            flowerColor4 = 2
            #Teal
            if (flowerColor4 == 2 and rgbFlower4[0] > 100): 
                flowerColor4 = 7
            
        #Blue
        elif (rgbFlower4[2] > rgbFlower4[0] and rgbFlower4[2] > rgbFlower4[1]):
            flowerColor4 = 3
            #Purple
            if (flowerColor4 == 3 and rgbFlower4[0] > 60 and rgbFlower4[0] < 100 and rgbFlower4[1] > 50 and rgbFlower4[1] < 90 and rgbFlower4[2] > 120 and rgbFlower4[2] < 160): 
                flowerColor4 = 9               
        
        #UNKNOWN
        else:
            flowerColor4 = 11

##  Background color
        # if (background[0] > 100 and background[1] > 100 and background[2] >100):
        #     BGColor = 1
        #
        # elif (background[0] < 100 and background[1] < 100 and background[2] < 100):
        #     BGColor = 1
        # else:
        #     BGColor = 2

## Set RGB category to flowers
        #Flower 1
        if flowerColor1 == 1:
            flowerColor1 = 'Red'
        elif flowerColor1 == 2:
            flowerColor1 = 'Green'
        elif flowerColor1 == 3:
            flowerColor1 = 'Blue'
        elif flowerColor1 == 4:
            flowerColor1 = 'White'           
        elif flowerColor1 == 5:
            flowerColor1 = 'Orange'
        elif flowerColor1 == 6:
            flowerColor1 = 'Yellow'
        elif flowerColor1 == 7:
            flowerColor1 = 'Teal'
        elif flowerColor1 == 8:
            flowerColor1 = 'Pink'
        elif flowerColor1 == 9:
            flowerColor1 = 'Purple'
        elif flowerColor1 == 10:
            flowerColor1 = 'Magenta'
        elif flowerColor1 == 11:
            flowerColor1 = 'ERROR'
            
        #Flower 2
        if flowerColor2 == 1:
            flowerColor2 = 'Red'
        elif flowerColor2 == 2:
            flowerColor2 = 'Green'
        elif flowerColor2 == 3:
            flowerColor2 = 'Blue'
        elif flowerColor2 == 4:
            flowerColor2 = 'White'
        elif flowerColor2 == 5:
            flowerColor2 = 'Orange'
        elif flowerColor2 == 6:
            flowerColor2 = 'Yellow'
        elif flowerColor2 == 7:
            flowerColor2 = 'Teal'
        elif flowerColor2 == 8:
            flowerColor2 = 'Pink'
        elif flowerColor2 == 9:
            flowerColor2 = 'Purple'
        elif flowerColor2 == 10:
            flowerColor2 = 'Magenta'            
        elif flowerColor2 == 11:
            flowerColor2 = 'ERROR'
            
        #Flower 3
        if flowerColor3 == 1:
            flowerColor3 = 'Red'
        elif flowerColor3 == 2:
            flowerColor3 = 'Green'
        elif flowerColor3 == 3:
            flowerColor3 = 'Blue'
        elif flowerColor3 == 4:
            flowerColor3 = 'White'
        elif flowerColor3 == 5:
            flowerColor3 = 'Orange'
        elif flowerColor3 == 6:
            flowerColor3 = 'Yellow'
        elif flowerColor3 == 7:
            flowerColor3 = 'Teal'
        elif flowerColor3 == 8:
            flowerColor3 = 'Pink'
        elif flowerColor3 == 9:
            flowerColor3 = 'Purple'
        elif flowerColor3 == 10:
            flowerColor3 = 'Magenta'           
        elif flowerColor3 == 11:
            flowerColor3 = 'ERROR'
            
        #Flower 4
        if flowerColor4 == 1:
            flowerColor4 = 'Red'
        elif flowerColor4 == 2:
            flowerColor4 = 'Green'
        elif flowerColor4 == 3:
            flowerColor4 = 'Blue'
        elif flowerColor4 == 4:
            flowerColor4 = 'White'
        elif flowerColor4 == 5:
            flowerColor4 = 'Orange'
        elif flowerColor4 == 6:
            flowerColor4 = 'Yellow'
        elif flowerColor4 == 7:
            flowerColor4 = 'Teal'
        elif flowerColor4 == 8:
            flowerColor4 = 'Pink'
        elif flowerColor4 == 9:
            flowerColor4 = 'Purple'
        elif flowerColor4 == 10:
            flowerColor4 = 'Magenta'            
        elif flowerColor4 == 11:
            flowerColor4 = 'ERROR'
        #Background
        # if BGColor == 1:
        #     BGColor = 'White'
        # if BGColor == 2:
        #     BGColor = 'UNIQUE'
        #Grass Color
            
        # outputs File name and RGB values of each flower to excel file
        # Includes RGB values as columns
        # row = [imageIn, str(flower1), str(flowerColor1) , str(flower2), str(flowerColor2), str(flower3), str(flowerColor3), str(flower4), str(flowerColor4), str(background), str(BGColor)]

        # Labels image sizes onto images  
        imageName = int(imageIn[:-4])
        imageSize = 0
        # print imageName
        if (imageName > 1464 and imageName < 1468):
            imageSize = '48in.on white'
        elif (imageName > 1467 and imageName < 1471):
            imageSize = '4 foot'        
        elif (imageName == 1471):
            imageSize = '100 x 84'  
        elif (imageName > 1471 and imageName < 1474):
            imageSize = '82 inch'    
        elif (imageName > 1473 and imageName < 1486):
            imageSize = '24 inch'
        elif (imageName == 1486):
            imageSize = 'large (81 x 160)' 
        elif (imageName > 1486 and imageName < 1513):
            imageSize = '22 inch'  
        elif (imageName > 1512 and imageName < 1573):
            imageSize = '14 inch'  
        elif (imageName > 1572 and imageName < 1720):
            imageSize = '8 inch'                 
        elif (imageName > 1719 and imageName < 1816):
            imageSize = '5 inch'  
    # Not included in sample pictures
        # elif (imageName == 1816):
        #     imageSize = '79 x 160'
        # elif (imageName == 1817):
        #     imageSize = '81 x 82'
        # elif (imageName == 1818):
        #     imageSize = '70 x 140'
        # elif (imageName == 1819):
        #     imageSize = '83 x 145'
        # elif (imageName == 1820):
        #     imageSize = '81 x 140'
        # elif (imageName == 1821):
        #     imageSize = '81 x 130'
        # elif (imageName == 1822):
        #     imageSize = '71 x 71'
        
        # # of kind
        numOfKind = 0
        if (flowerColor1 == flowerColor2 == flowerColor3 == flowerColor4):
            numOfKind = "Four of a Kind"
        elif (flowerColor1 == flowerColor2 == flowerColor3 != flowerColor4 or flowerColor1 == flowerColor2 == flowerColor4 != flowerColor3 or flowerColor1 == flowerColor4 == flowerColor3 != flowerColor2 or flowerColor4 == flowerColor2 == flowerColor3 != flowerColor1):            
            numOfKind = "Three of Kind"
        elif (flowerColor1 != flowerColor2 != flowerColor3 == flowerColor4 or flowerColor1 != flowerColor3 != flowerColor2 == flowerColor4 or flowerColor3 != flowerColor2 != flowerColor1 == flowerColor4 or flowerColor1 != flowerColor4 != flowerColor2 == flowerColor3 or flowerColor4 != flowerColor2 != flowerColor1 == flowerColor3 or flowerColor3 != flowerColor4 != flowerColor1 == flowerColor2 or flowerColor1 == flowerColor2 != flowerColor3 == flowerColor4 or flowerColor1 == flowerColor3 != flowerColor2 == flowerColor4 or flowerColor1 == flowerColor4 != flowerColor3 == flowerColor2):        
            numOfKind = "Two of a Kind"     
        elif (flowerColor1 != flowerColor2 != flowerColor3 != flowerColor4):
            numOfKind = "Unique"

   
        row = [imageIn[:-4], str(flowerColor1), str(flowerColor2), str(flowerColor3), str(flowerColor4), str(imageSize), str(numOfKind)]


##        # checks if row already exists in file, if it does then the row is not added
##        if row in rows:
##            None
##        # writes row to excel file
##        else:
        writer.writerow(row)
        
    excelFile.close
    
analyze()

    
    
