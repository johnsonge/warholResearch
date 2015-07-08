"""
Created on April 6 2015

@author: Eugene Johnson
"""

import csv
import io
import pandas as pd
from pandasql import sqldf

#def sqlSelect():
pysqldf = lambda q: sqldf(q, globals())

df = pd.read_csv('workbook.csv')

# Gets user input to use for selection
choiceArray = []
print("""Color Options:
    Blue    Green   Magenta Orange  Pink       
    Purple  Red     Teal    White   Yellow
    (Leave Blank for 'Any')""")
choice1 = raw_input("Enter choice 1: ")
if choice1 == '':
     choice1 = "%"
choice2 = raw_input("Enter choice 2: ")
if choice2 == '':
     choice2 = "%"
choice3 = raw_input("Enter choice 3: ")
if choice3 == '':
     choice3 = "%"
choice4 = raw_input("Enter choice 4: ")
if choice4 == '':
     choice4 = "%"


# Uses 24 OR statements to make order in user input not matter 
q = ("SELECT DISTINCT imageName, size FROM df WHERE /*1: 1 2 3 4*/ (color1 LIKE '%s' AND color2 LIKE '%s' AND color3 LIKE '%s' AND color4 LIKE '%s') /*2: 1 2 4 3 */ OR (color1 LIKE '%s' AND color2 LIKE '%s' AND color4 LIKE '%s' AND color3 LIKE '%s') /*3: 1 3 2 4 */ OR (color1 LIKE '%s' AND color3 LIKE '%s' AND color2 LIKE '%s' AND color4 LIKE '%s') /*4: 1 3 4 2 */ OR (color1 LIKE '%s' AND color3 LIKE '%s' AND color4 LIKE '%s' AND color2 LIKE '%s') /*5: 1 4 3 2 */ OR (color1 LIKE '%s' AND color4 LIKE '%s' AND color3 LIKE '%s' AND color2 LIKE '%s') /*6: 1 4 2 3 */ OR (color1 LIKE '%s' AND color4 LIKE '%s' AND color2 LIKE '%s' AND color3 LIKE '%s') /*7: 2 1 3 4 */ OR (color2 LIKE '%s' AND color1 LIKE '%s' AND color3 LIKE '%s' AND color4 LIKE '%s') /*8: 2 1 4 3 */ OR (color2 LIKE '%s' AND color1 LIKE '%s' AND color4 LIKE '%s' AND color3 LIKE '%s') /*9: 2 3 1 4 */ OR (color2 LIKE '%s' AND color3 LIKE '%s' AND color1 LIKE '%s' AND color4 LIKE '%s') /*10: 2 3 4 1*/ OR (color2 LIKE '%s' AND color3 LIKE '%s' AND color4 LIKE '%s' AND color1 LIKE '%s') /*11: 2 4 1 3*/ OR (color2 LIKE '%s' AND color4 LIKE '%s' AND color1 LIKE '%s' AND color3 LIKE '%s') /*12: 2 4 3 1*/ OR (color2 LIKE '%s' AND color4 LIKE '%s' AND color3 LIKE '%s' AND color1 LIKE '%s') /*13: 3 1 2 4*/ OR (color3 LIKE '%s' AND color1 LIKE '%s' AND color2 LIKE '%s' AND color4 LIKE '%s') /*14: 3 1 4 2*/ OR (color3 LIKE '%s' AND color1 LIKE '%s' AND color4 LIKE '%s' AND color2 LIKE '%s') /*15: 3 2 1 4*/ OR (color3 LIKE '%s' AND color2 LIKE '%s' AND color1 LIKE '%s' AND color4 LIKE '%s') /*16: 3 2 4 1*/ OR (color3 LIKE '%s' AND color2 LIKE '%s' AND color4 LIKE '%s' AND color1 LIKE '%s') /*17: 3 4 1 2*/ OR (color3 LIKE '%s' AND color4 LIKE '%s' AND color1 LIKE '%s' AND color2 LIKE '%s') /*18: 3 4 2 1*/ OR (color3 LIKE '%s' AND color4 LIKE '%s' AND color2 LIKE '%s' AND color1 LIKE '%s') /*19: 4 1 2 3*/ OR (color4 LIKE '%s' AND color1 LIKE '%s' AND color2 LIKE '%s' AND color3 LIKE '%s') /*20: 4 1 3 2*/ OR (color4 LIKE '%s' AND color1 LIKE '%s' AND color3 LIKE '%s' AND color2 LIKE '%s') /*21: 4 2 1 3*/ OR (color4 LIKE '%s' AND color2 LIKE '%s' AND color1 LIKE '%s' AND color3 LIKE '%s') /*22: 4 2 3 1*/ OR (color4 LIKE '%s' AND color2 LIKE '%s' AND color3 LIKE '%s' AND color1 LIKE '%s') /*23: 4 3 1 2*/ OR (color4 LIKE '%s' AND color3 LIKE '%s' AND color1 LIKE '%s' AND color2 LIKE '%s') /*23: 4 3 2 1*/ OR (color4 LIKE '%s' AND color3 LIKE '%s' AND color2 LIKE '%s' AND color1 LIKE '%s') "%(choice1,choice2,choice3,choice4,choice1,choice2,choice3,choice4,choice1,choice2,choice3,choice4,choice1,choice2,choice3,choice4,choice1,choice2,choice3,choice4,choice1,choice2,choice3,choice4,choice1,choice2,choice3,choice4,choice1,choice2,choice3,choice4,choice1,choice2,choice3,choice4,choice1,choice2,choice3,choice4,choice1,choice2,choice3,choice4,choice1,choice2,choice3,choice4,choice1,choice2,choice3,choice4,choice1,choice2,choice3,choice4,choice1,choice2,choice3,choice4,choice1,choice2,choice3,choice4,choice1,choice2,choice3,choice4,choice1,choice2,choice3,choice4,choice1,choice2,choice3,choice4,choice1,choice2,choice3,choice4,choice1,choice2,choice3,choice4,choice1,choice2,choice3,choice4,choice1,choice2,choice3,choice4,choice1,choice2,choice3,choice4))

print pysqldf(q)

#print sqlSelect()