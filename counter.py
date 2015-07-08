"""
Created on Feb 10 2015

@author: Eugene Johnson

Run this program to read in the values of Workbook.csv from running readColor.py and 
count up occurrences for quicker data manipulation
"""

import csv
import io
import pandas as pd

df = pd.read_csv('Workbook.csv')

#Writes counted data to new csv
colorCounts = df.stack().value_counts()
colorCounts.columns=['color','count']
colorCounts.to_csv('colorCounts.csv')
countsdf = pd.read_csv('colorCounts.csv')
#df2 = df[['color', 'count']]  

## Getting data from relevent columns
col1Data = df['color1'].value_counts()
col2Data = df['color2'].value_counts()
col3Data = df['color3'].value_counts()
col4Data = df['color4'].value_counts()

# since no pink in some columns, gives NaN
# total = col1Data + col2Data + col3Data + col4Data

melted = pd.melt(df, id_vars=["imageName", "size", "relation"], value_name="color")

sizeList = melted.groupby(["size","color"]).size()
relationList = melted.groupby(["size", "relation"]).size()

colorTotal = sizeList.groupby(level="color").sum()
relationTotal = relationList.groupby(level="relation").sum()

colorPercent = (sizeList/colorTotal)*100
relationPercent = (relationList/relationTotal)*100

i = 0
allBlue = []
allGreen = []
allMagenta = []
allOrange = []
allPink = []
allPurple = []
allRed = []
allTeal = []
allWhite = []
allYellow = []

hasBlue = []
hasGreen = []
hasMagenta = []
hasOrange = []
hasPink = []
hasPurple = []
hasRed = []
hasTeal = []
hasWhite = []
hasYellow = []

for index, row in df.iterrows():
    if (row['color1'] == 'Blue' and row['color2'] == 'Blue' and row['color3'] == 'Blue' and row['color4'] == 'Blue'):
        allBlue.append(row['imageName'])
        i = i+1
    
    elif (row['color1'] == 'Green' and row['color2'] == 'Green' and row['color3'] == 'Green' and row['color4'] == 'Green'):
        allGreen.append(row['imageName'])


    elif (row['color1'] == 'Magenta' and row['color2'] == 'Magenta' and row['color3'] == 'Magenta' and row['color4'] == 'Magenta'):
        allMagenta.append(row['imageName'])

    elif (row['color1'] == 'Orange' and row['color2'] == 'Orange' and row['color3'] == 'Orange' and row['color4'] == 'Orange'):
        allOrange.append(row['imageName'])

    elif (row['color1'] == 'Pink' and row['color2'] == 'Pink' and row['color3'] == 'Pink' and row['color4'] == 'Pink'):
        allPink.append(row['imageName'])

    elif (row['color1'] == 'Purple' and row['color2'] == 'Purple' and row['color3'] == 'Purple' and row['color4'] == 'Purple'):
        allPurple.append(row['imageName'])

    elif (row['color1'] == 'Red' and row['color2'] == 'Red' and row['color3'] == 'Red' and row['color4'] == 'Red'):
        allRed.append(row['imageName'])

    elif (row['color1'] == 'Teal' and row['color2'] == 'Teal' and row['color3'] == 'Teal' and row['color4'] == 'Teal'):
        allTeal.append(row['imageName'])

    elif (row['color1'] == 'White' and row['color2'] == 'White' and row['color3'] == 'White' and row['color4'] == 'White'):
        allWhite.append(row['imageName'])

    elif (row['color1'] == 'Yellow' and row['color2'] == 'Yellow' and row['color3'] == 'Yellow' and row['color4'] == 'Yellow'):
        allYellow.append(row['imageName'])

# print '\n'.join(map(str, allPurple))

# print (sizeList/total)*100
# print total
# print melted
# print sizeList


        # elif (row['color1'] == 'Blue' or row['color2'] == 'Blue' or row['color3'] == 'Blue' or row['color4'] == 'Blue'):
 #            # allBlue.extend(row['imageName'])
 #                # print hasBlue