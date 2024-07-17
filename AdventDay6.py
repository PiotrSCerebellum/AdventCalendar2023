import re
import math
import functools
code = open(r"C:\\Users\\Woda\\Desktop\\adventDay6.txt", "r")

def getRaces(string):
    timeOrNot=False
    raceTimes=[]
    raceDistances=[]
    races=[]
    for line in string:
        timeOrNot= not timeOrNot
        numbers=re.findall(r"\d+",line)
        if(timeOrNot):
            raceTimes=[int(x) for x in numbers]
        else:
            raceDistances=[int(x) for x in numbers]
    for race in range(len(raceTimes)):
        time=raceTimes[race]
        distance=raceDistances[race]
        races.append((time,distance))
    return races
def getNewRecords(race):
    time,distance=race
    speed=math.floor(time/2)
    timeLeft=math.ceil(time/2)
    newDistance=speed*timeLeft
    solutions=getMarginRaces(newDistance,distance,speed,timeLeft,-1)
    solutions.append((speed,newDistance))
    solutions+=getMarginRaces(newDistance,distance,speed,timeLeft,1)
    return solutions
def getMarginRaces(recordDistance,distance,speed,timeLeft,order):
        solutions=[]
        viable=recordDistance>distance
        while viable:
            speed=speed+order
            timeLeft=timeLeft-order
            recordDistance=speed*timeLeft
            viable=recordDistance>distance
            if viable:
                solutions.append((speed,recordDistance))
        if order==-1:
            solutions.reverse()
        return solutions
def getAnswer(marginRaces):
    answer=1
    for raceSeries in marginRaces:
        answer*=len(raceSeries)
    return answer

print("\nScript Beggining")
races=getRaces(code)
marginRaces=[]
for race in races:
    marginRaces.append(getNewRecords(race))
answer=getAnswer(marginRaces)
print(races)
print(marginRaces)
print(answer)

