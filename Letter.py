from basicFunctions import *

class Letter:
    def __init__(self, letterChart):
      self.letterChart = letterChart  
    
    def search(self):
        trim = cut(self.letterChart)
        letterList = []
        #print(toString(trim))
        letterBankFile = open('letterBankFile.txt', 'r')
        letterBank = letterBankFile.readlines()
        
        '''Removes the "\n" from the end of each string and converts them into
         an array, creating a 2D array instead of a 1D array of strings'''
        for i in range(len(letterBank)-1):
            letterBank[i] = letterBank[i][:-1]
            letterBank[i] = list(letterBank[i])
             
        '''Creates a list of letters from the file and closes it'''
        letterList = breakChart(letterBank)
        letterBankFile.close()
         
        '''Creates a bank for the indexes of the letters and an empty
        probability list which will be populated later. A new file is also
        opened to be appended to if there is a letter it doesnt recognize'''
        letterBankFile = open('newLetterBankFile.txt', 'a')
        letterKey = ['A', 'B', 'C', 'D', 'D', 'E', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'U', 'V', 'W', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'd', 'e', 'f', 'f', 'g', 'g', 'h', 'h', 'i', 'j', 'k', 'l', 'l', 'm', 'n', 'n', 'o', 'p', 'p', 'q', 'q', 'r', 'r', 's', 't', 't', 'u', 'u', 'u', 'v', 'w', 'w', 'x', 'x', 'y', 'y', 'z', 'z', '0', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '-', '-', '_', '_']
        probabilities = []
        
        '''Loops through the letters in the letterList and, if the letter at the
        index has the same height and width of the letter its given, loops through
        the entire 2D list of pixels and finds the probability that it is that
        letter (sometimes the same letter may vary by a few pixels). The highest
        index of the probability is then used to find the letter from the bank.'''
        for i in range(len(letterList)):
            percent = 0
            if(len(letterList[i]) == len(trim) and len(letterList[i][0]) == len(trim[0])):    
                for a in range(len(trim)):
                    for j in range(len(trim[0])):
                        if(letterList[i][a][j] == trim[a][j]):
                            percent += 1
                percent /= len(trim) * len(trim[0])
            probabilities.append(percent)
        if(max(probabilities) > 0):
            letter = letterKey[probabilities.index(max(probabilities))]
        else:
            letterBankFile.write(toString(trim) + '\n>')
            letter = '[?]'
        return letter