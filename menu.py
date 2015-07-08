"""
Created on Jan 10 2015

@author: Eugene Johnson
"""

import csv
import io
import counter
import pandas as pd
from pandasql import sqldf

# from counter import allColors

#df = pd.read_csv('colorCounts.csv')
df = pd.read_csv('workbook.csv')
pd.set_option('display.max_rows', 1000)

#Pull in data from counter.py
#print (counter.fourOfKind)


#totalCount = df["sum"] = df.sum(axis=1)
#print (df(axis=0))
#(totalCount)

#def menu():
## main menu         
ans=True
menuNum = True

while ans:
    print ("\nMain Menu\n" """
1.Flower Colors
2.Color Relationships
3.Search Picture by Flower Color
4.Exit/Quit
        """)
#### menu  1.1 - - - - - - - - - - - - - - - - 
    menuNum = 1
    while menuNum == 1:
        ans=raw_input("Please enter choice: ") 
  
        if ans=="1": 
            print("\nFlower Colors Menu\n" """
1.List All
2.Blue
3.Green 
4.Magenta
5.Orange
6.Pink
7.Purple
8.Red
9.Teal
10.White
11.Yellow
12.Exit/Quit
            """)
            menu1Ans = raw_input("Please enter choice: ")                 
            if menu1Ans == "1":
                print("Total occurrences of each color\n")
                print(counter.colorTotal)
                try:
                    input("\nPress Enter to Return to the Main Menu")
                except SyntaxError:
                    pass
                    break;
                    
            elif menu1Ans == "2":
                print ("\nThe Following Images contain all Blue")
                print '\n'.join(map(str, counter.allBlue))
                try:
                    input("\nPress Enter to Return to the Main Menu")
                except SyntaxError:
                    pass
                    break;

            elif menu1Ans == "3":
                print ("\nThe Following Images contain all Green")
                print '\n'.join(map(str, counter.allGreen))
                try:
                    input("\nPress Enter to Return to the Main Menu")
                except SyntaxError:
                    pass
                    break;

            elif menu1Ans == "4":
                print ("\nThe Following Images contain all Magenta")
                print '\n'.join(map(str, counter.allMagenta))
                try:
                    input("\nPress Enter to Return to the Main Menu")
                except SyntaxError:
                    pass
                    break;

            elif menu1Ans == "5":
                print ("\nThe Following Images contain all Orange")
                print '\n'.join(map(str, counter.allOrange))
                try:
                    input("\nPress Enter to Return to the Main Menu")
                except SyntaxError:
                    pass
                    break;

            elif menu1Ans == "6":
                print ("\nThe Following Images contain all Pink")
                print '\n'.join(map(str, counter.allPink))
                try:
                    input("\nPress Enter to Return to the Main Menu")
                except SyntaxError:
                    pass
                    break;

            elif menu1Ans == "7":
                print ("\nThe Following Images contain all Purple")
                print '\n'.join(map(str, counter.allPurple))
                try:
                    input("\nPress Enter to Return to the Main Menu")
                except SyntaxError:
                    pass
                    break;

            elif menu1Ans == "8":
                print ("\nThe Following Images contain all Red")
                print '\n'.join(map(str, counter.allRed))
                try:
                    input("\nPress Enter to Return to the Main Menu")
                except SyntaxError:
                    pass
                    break;
            elif menu1Ans == "9":
                print ("\nThe Following Images contain all Teal")
                print '\n'.join(map(str, counter.allTeal))
                try:
                    input("\nPress Enter to Return to the Main Menu")
                except SyntaxError:
                    pass
                    break;
            elif menu1Ans == "10":
                print ("\nThe Following Images contain all White")
                print '\n'.join(map(str, counter.allWhite))
                try:
                    input("\nPress Enter to Return to the Main Menu")
                except SyntaxError:
                    pass
                    break;    
    
            elif menu1Ans == "11":
                print ("\nThe Following Images contain all Yellow")
                print '\n'.join(map(str, counter.allYellow))
                try:
                    input("\nPress Enter to Return to the Main Menu")
                except SyntaxError:
                    pass
                    break;
    
            elif menu1Ans == "12":
                ans = False
                print("\nThank You!") 
                break;
                    
            else:
                print("Please enter a valid choice")
          
          
          
            ## menu 2.1 (Number of occurences by color )                
        elif ans=="2":
            print("\nStatistics Menu\n" """
1.Colors by Size: Count
2.Colors by Size: Percent
3.Relations by Size: Count
4.Relations by Size: Percent
5.Color Count Totals
6.Relations Count Totals
7.Exit/Quit
            """)
    
            menu2Ans = raw_input("Please enter choice: ")                 
            if menu2Ans == "1":
                print(counter.sizeList)
                try:
                    input("\nPress Enter to Return to the Main Menu")
                except SyntaxError:
                    pass
                    break;
            elif menu2Ans == "2":
                print(counter.colorPercent)
                try:
                    input("\nPress Enter to Return to the Main Menu")
                except SyntaxError:
                    pass
                    break;
            elif menu2Ans == "3":
                print(counter.relationList)
                try:
                    input("\nPress Enter to Return to the Main Menu")
                except SyntaxError:
                    pass
                    break;
            elif menu2Ans == "4":
                print(counter.relationPercent)
                try:
                    input("\nPress Enter to Return to the Main Menu")
                except SyntaxError:
                    pass
                    break;
            elif menu2Ans == "5":
                print(counter.colorTotal)
                try:
                    input("\nPress Enter to Return to the Main Menu")
                except SyntaxError:
                    pass
                    break;
            elif menu2Ans == "6":
                print(counter.relationTotal)
                try:
                    input("\nPress Enter to Return to the Main Menu")
                except SyntaxError:
                    pass
                    break;
            elif menu2Ans == "7":
                ans = False
                print("\nThank You!") 
                break;
            else:
                print("Please enter a valid choice")
                    
        elif ans=="3":
            print("\nColor Search\n") 
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
            break;
            
        elif ans=="4":
            ans = False
            print("\nThank You!") 
            break;
        elif ans !="":
            print("\n" + "'" + ans + "'" + " is not a Valid Number") 