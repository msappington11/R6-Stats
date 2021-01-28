from basicFunctions import *
from Letter import *

class Name:
    def __init__(self, nameChart):
        self.nameChart = nameChart
        self.stringName = ''
        
    '''Finds all of the letters found within a name, assigns them to a Letter
    object, and searches them'''
    def letters(self):
        #Finds all of the empty spaces in a name
        height = len(self.nameChart)
        blanks = []
        spaces = []
        count = 0
        for i in range(len(self.nameChart)):
            for a in range(len(self.nameChart[i])):
                if(self.nameChart[i][a] == ' '):
                    count += 1
                    blanks.append(a)
        
        #Finds the spaces between letters by seeing when there is a solid line
        #of spaces from top to bottom
        for i in range(len(self.nameChart[1])):
            count = 0
            for a in range(len(blanks)):
                if(blanks[a] == i):
                    count +=1
            if(count == height):
                spaces.append(i)
                
        #If there is only a 1 pixel space between letters, it gets duplicated
        #to make getting the individual letters easier
        i=0
        while i < (len(spaces)-1):
            if(spaces[i] != spaces[i-1]+1 and spaces[i] != spaces[i+1]-1):
                spaces.insert(i, spaces[i])
                i+=2
            else:
                i+=1
        
        #Cleans up the spaces list to only include the spaces right next to a letter
        newSpaces = []
        for i in range(len(spaces)-1):
            if(spaces[i] != spaces[i+1]-1 or spaces[i] != spaces[i-1]+1):
                newSpaces.append(spaces[i])
        spaces = newSpaces[1:]
            
        #Converts the name into a list of Letter objects called "letters"
        letters = []
        while(len(spaces) > 1):
            letter = []
            for i in range(len(self.nameChart)):
                letter.append([])
                for a in range(spaces[0], spaces[1], 1):
                    letter[i].append(self.nameChart[i][a])
            letters.append(Letter(letter))
            spaces = spaces[2:]
                    
        #Searches each letter in the name
        for i in range(len(letters)):
            self.stringName += letters[i].search()
            
    def getName(self):
        return self.stringName