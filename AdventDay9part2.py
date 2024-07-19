from collections import deque
with open(r"C:\\Users\\Woda\\Desktop\\adventDay9.txt", "r") as file:
    code=file.read()

def getSequences(string):
    sequences=[]
    string=string[:-1]
    for line in string.split("\n"):
        numbers = line.split(" ")
        print(numbers)
        numbers = [int(num) for num in numbers]
        sequences.append(numbers)
    return sequences   
def getNextLevelDown(numList):
    newList=[]
    for n in range(1,len(numList)):
        newList.append((numList[n]-numList[n-1]))
    return newList
def checkIfAllZeros(numList):
        maximum=0
        minimum=1
        for n in numList:
            maximum=max(maximum,n) 
            minimum=min(minimum,n)
        return maximum==0 and minimum==0
def getAllLevels(numList):
    allLevels=[]
    allLevels.append(numList)
    level=numList
    while not checkIfAllZeros(level):
        level=getNextLevelDown(level)
        allLevels.append(level)
    return allLevels
def makePredctions(allLevels):
    lastPrediction=0
    for level in reversed(allLevels):
        lastPrediction=lastPrediction+level[len(level)-1]
        level.append(lastPrediction)
    return allLevels
def makeBackwardsprediction(allLevels):
    predicted=deque()
    lastPrediction=0
    for level in reversed(allLevels):
        level = deque(level)
        lastPrediction=level[0]-lastPrediction
        level.appendleft(lastPrediction)
        level = list(level)
        predicted.appendleft(level)
    return list(predicted)
def getFinalSumOfBackwards(solvedAllLevels):
    total=0
    for sequence in solvedAllLevels:
        total+=sequence[0][0]
    return total


       
sequences=getSequences(code)
print(f"All sequences: \n{sequences}")
allLevels=[]
for sequence in sequences:
    allLevels.append(getAllLevels(sequence))
#print(allLevels)
solvedAllLevels=[]
for sequence in allLevels:
    solvedAllLevels.append(makeBackwardsprediction(sequence))
print(f"Solved predictions: \n{solvedAllLevels} \n end")
print(f"Solution: {getFinalSumOfBackwards(solvedAllLevels)}")
