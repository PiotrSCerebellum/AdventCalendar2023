import re

with open(r"C:\\Users\\Woda\\Desktop\\adventDay8.txt", "r") as file:
    code=file.read()



def getRoute(string):
    return re.search(r"[LR]{5,}",string).group(0)
def mapAsDictionary(string:str):
    mapDict=dict()
    for line in string.splitlines():
        if re.match(r"[A-Z]{3} ",line):
            node=re.match(r"[A-Z]{3} ",line).group().strip()
            left=re.search(r"[A-Z]{3}(?=,)",line).group()
            right=re.search(r"[A-Z]{3}(?=\))",line).group()
            mapDict.update({node:(left,right)})
    return mapDict
def findStartingPoints(mapDictionary):
    starts=[]
    for node in mapDictionary:
       if node[2:3]!="A":
           continue
       starts.append(node)
    return starts
def findLoopLength(startingPoints,mapDictionary,route):
    loops=[]
    for start in startingPoints:
        currentRoute=route
        currentNode=start
        loopEndings=[]
        segmentLengths=[]
        stepsTo=0
        while currentNode[2:3]!="Z":
            turn = 0 if currentRoute[0:1] == "L" else 1
            currentRoute= currentRoute[1:]+currentRoute[0:1]
            currentNode=mapDictionary[currentNode][turn]
            stepsTo+=1
        while currentNode not in loopEndings:
            if currentNode[2:3]=="Z":
                loopEndings.append(currentNode)
                segmentLengths.append(stepsTo)
                stepsTo=0
            turn = 0 if currentRoute[0:1] == "L" else 1
            currentRoute= currentRoute[1:]+currentRoute[0:1]
            stepsTo+=1
            currentNode=mapDictionary[currentNode][turn]

        # if currentNode[2:3]=="Z":
        #     loopEndings.append(currentNode)
        #     segmentLengths.append(stepsTo)
        #     stepsTo=0
        completeLoop=[]
        for i in range(len(loopEndings)):
            completeLoop.append((start,loopEndings[i],segmentLengths[i]))
        loops.append(completeLoop)


    return loops
def getDivisors(n) : 
    #non one and itself
    listOfDivisors=[]
    i = 2
    while i < n : 
        if (n % i==0) : 
            listOfDivisors.append(i)
        i = i + 1  
    return listOfDivisors       
def result(loops):
    allDivisors=[]
    usedDivisors=[]
    result=1
    for loop in loops:
        allDivisors.append(getDivisors(loop[0][2]))
        continue
    for num in allDivisors:
        for n in num:
            if n in usedDivisors:
                continue
            result=result*n
            usedDivisors.append(n)
    return result,allDivisors
            



route=getRoute(code)
print(route)
mapDictionary=mapAsDictionary(code)
print(mapDictionary)
startingPoints=findStartingPoints(mapDictionary)
print(startingPoints)
loops=findLoopLength(startingPoints,mapDictionary,route)
print(loops)
print(result(loops))
