import requests
from bs4 import BeautifulSoup

class Player:
    def __init__(self, user):
        self.user = user
        self.currentMMR = 0
    
    def getStats(self):
        #Sets up Beautiful Soup with html from the link
        url = 'http://r6.tracker.network/profile/pc/' + self.user
        page = requests.get(url)
        s = BeautifulSoup(page.content, 'html.parser')
        
        #Gets the current MMR
        baseClass = s.find(class_='trn-site__container')
        elms = baseClass.find_all(class_='trn-text--dimmed')
        self.currentMMR = elms[5].text
        currentRank = elms[1].text
        if('Skill' in currentRank):
            currentRank = 'Not ranked yet.'
            
        #Sets up the seasons information with the html location and declares variables
        contents = baseClass.find_all(class_="trn-card__content pt8 pb8")
        seasonCard = contents[1].find_all(class_="r6-quickseason")
        seasons = []
        seasonMMR = []
        seasonNames = []
        seasonRanks = []
        
        #Loops through each seasons html to find the season name, rank, and MMR
        for i in range(len(seasonCard)):
            seasons.append(seasonCard[i].find(title="Highest MMR").text)
            seasonData = seasons[i].split('\n')
            for a in range(len(seasonData)):
                if(',' in seasonData[a] or '0' in seasonData[a]):
                    seasonMMR.append(int(seasonData[a][:-4].replace(',', '')))
                    seasonNames.append(seasonData[a-2])
                    seasonRanks.append(seasonData[a+1])
                elif('Unranked' in seasonData[a]):
                    seasonMMR.append(0)
                    seasonNames.append(seasonData[a-1])
                    seasonRanks.append(seasonData[a+1])
              
        #Sets highest rank overall, highest rank of the season, and first season
        maxRank = seasonRanks[seasonMMR.index(max(seasonMMR))]
        highestRankThisSeason = seasonRanks[0]
        firstSeason = ''
        for i in range(len(seasonMMR)):
            if(seasonMMR[i] != 0):
                firstSeason = seasonNames[i]
        if(firstSeason == ''):
            firstSeason = 'Never been ranked.'
              
        #Sets the ranked KD
        cards = baseClass.find_all(class_="trn-card__content")
        rankedCard = cards[7]
        rankedStats = rankedCard.find_all(class_="trn-defstat__value")
        KD = rankedStats[7].text
        KD = KD.replace('\n', '')
        
        #Sets up Beautiful Soup with html from the new link
        url += '/operators'
        page = requests.get(url)
        s = BeautifulSoup(page.content, 'html.parser')
        
        #Sets topAttacker and topDefender
        baseAttackClass = s.find(class_="trn-card trn-card--ftr-purple")
        attackers = baseAttackClass.find_all(class_="trn-table__row")
        topAttacker = attackers[1].find('span').text
        baseDefendClass = s.find(class_="trn-card trn-card--ftr-blue")
        defenders = baseDefendClass.find_all(class_="trn-table__row")
        topDefender = defenders[1].find('span').text
        
        #Prints out user information
        print(self.user, '\nKD:', KD, '\nCurrent Rank:', currentRank,
        '\nHighest Rank of Season:', highestRankThisSeason,
        '\nHighest Overall Rank:', maxRank, '\nPlaying Since:', firstSeason,
        '\nTop Operators:', topAttacker, ',', topDefender, '\n\n')
        
        
        
        
        