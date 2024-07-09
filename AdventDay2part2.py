import re
list = open(r"C:\\Users\\Woda\\Desktop\\adventDay2.txt", "r")
cubeDictionary={
  "blue": "-2",
    "red": "-2",
  "green": "-2"
  }
cubeAllowances={ 
  "blue": 14,
  "red": 12,
  "green": 13
}
def readGames(str:str):
    gameIndex=0
    blues=[0]
    reds=[0]
    greens=[0]
    game=str.split(":")
    gameIndex=getNum(game[0])
    draws=game[1].split(";")
    for draw in draws:
        for color in draw.split(","):
            for cube in cubeDictionary:
                index=color.find(cube)
                if(index==-1):
                    continue
                match cube:
                    case "blue":
                        blues.append(getNum(color))
                    case "red":
                        reds.append(getNum(color))
                    case "green":
                        greens.append(getNum(color))                   
    return [gameIndex,blues,reds,greens]
def getNum(str):
    return int(re.search(r"\d+", str).group(0) )
def getMaxCubes(table):
    for i in range(len(table)):
        if(i==0):
            continue
        table[i]=max((table[i]))
    return table
def checkIfPossible(table):
    maxTable=getMaxCubes(table)
    print(maxTable)
    if(maxTable[1]>cubeAllowances["blue"]):
        return 0
    if(maxTable[2]>cubeAllowances["red"]):
        return 0
    if(maxTable[3]>cubeAllowances["green"]):
        return 0
    return maxTable[0]
def getMinimalPowers(table):
    maxTable=getMaxCubes(table)
    print(maxTable)
    power=maxTable[1]*maxTable[2]*maxTable[3]
    return power

print(" \n\nStart games ingestion \n Index blue red green")
result=0
# for line in list:
#     result+=checkIfPossible(readGames(line))
for line in list:
     result+=getMinimalPowers(readGames(line))
print(f"Resulting code is: {result}")