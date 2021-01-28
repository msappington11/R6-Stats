'''Returns the array of white pixels as a string'''
def toString(chart):
    chartToString = ''
    for i in range(len(chart)):
        chartToString += '\n'
        for a in range(len(chart[i])):
            chartToString += chart[i][a] 
    return chartToString

'''Returns the string of white pixels as an array'''
def toChart(string):
    chart = []
    lines = string.split('\n')
    for i in range(len(lines)):
        chart.append([])
        for a in range(len(lines[i])):
            chart[i].append(lines[i][a])
    return chart

'''Breaks up a chart into an array of smaller charts at a ">" seperator'''
def breakChart(chart):
    #Finds the index values of the breaks between names so they can be seperated
    #in a different list
    breaks = []
    for i in range(len(chart)):
        for a in range(len(chart[i])):
            if(chart[i][a] == '>'):
                breaks.append(i)
    
    #Breaks up the whole chart into an array of individual names
    brokenList = []
    for i in range(len(breaks)-1):
        brokenList.append(chart[breaks[i]: breaks[i+1]])
    
    #Removes the breaks so they are not included in the names
    for i in range(len(brokenList)):
        brokenList[i] = brokenList[i][1:]
    return brokenList

'''Cuts out any empty space above and below the letters'''
def cut(trimmed):     
    i=0
    while(i < len(trimmed)):
        if('-' in trimmed[i] or '>' in trimmed[i]):
            i+=1
        else:
            trimmed.remove(trimmed[i])
    return trimmed