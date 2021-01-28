from basicFunctions import *
from Letter import *
from Name import *
from Player import *

import pyautogui
import time
from PIL import Image
from numpy import asarray

time.sleep(3)
myScreenshot = pyautogui.screenshot()
#Will have to change directory
myScreenshot.save(r'C:\Users\Scot\R6-Test\screenshot.png')

im = Image.open(r'C:\Users\Scot\R6-Test\screenshot.png')

left = 467
top = 310
right = 750
bottom = 875
cropped = im.crop((left, top, right, bottom))
cropped.show()

#Converts the white pixels into a string with the white pixels being represented
#by a "-" and all the others with a space. Each name is also seperated with a ">"
firstString = ''
counter = 0
pixelData = asarray(cropped)
for i in range(len(pixelData)):
    line = ''
    for a in range(len(pixelData[0])):
        if pixelData[i][a][0] > 250 and pixelData[i][a][1] > 250 and pixelData[i][a][2] > 250:
            line+='-'
        else:
            line+=' '
    if('-' in line and ' ' in line):
        firstString += line + '\n'
        counter = 0
    elif(' ' in line):
        firstString += '\n'
        counter += 1
    if(counter == 4):
        firstString += '>\n'

#Converts the string into an array
chart = toChart(firstString)

#Cuts out all of the empty rows
chart = cut(chart)

#Breaks up the main chart into an array of names
namesChart = breakChart(chart)
playerList = []

#Creates a list of Name objects and finds the String
for i in range(len(namesChart)):
    name = Name(namesChart[i])
    name.letters()
    playerList.append(Player(name.getName()))
    try:
        playerList[i].getStats()
    except:
        print("Can't find account:", playerList[i].user, '\n\n')
    
#Calculates the average MMR from both teams and compares them
if(len(playerList) == 10):
    friendlyMMR = 0
    opponentMMR = 0
    Fcount = 0
    Ocount = 0
    for i in range(5):
        try:
            if(',' in playerList[i].currentMMR):
                friendlyMMR += int(playerList[i].currentMMR[:-4].replace(',', ''))
                Fcount += 1
        except:
            continue
    for i in range(4, 10):
        try:
            if(',' in playerList[i].currentMMR):
                opponentMMR += int(playerList[i].currentMMR[:-4].replace(',', ''))
                Ocount += 1
        except:
            continue
    friendlyMMR /= Fcount
    opponentMMR /= Ocount
    
    print('Your Teams Average MMR:', round(friendlyMMR), '\nOpponents Average MMR:',
    round(opponentMMR), '\nMMR Difference:', round(abs(opponentMMR - friendlyMMR)))



        
    

     















