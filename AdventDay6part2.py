import re
import math
code = open(r"C:\\Users\\Woda\\Desktop\\adventDay6.txt", "r")

def getRace(string):
    timeOrNot=False
    for line in string:
        timeOrNot= not timeOrNot
        numbers=re.findall(r"\d+",line)
        if(timeOrNot):
            raceTime=int("".join(numbers))
        else:
            raceDistance=int("".join(numbers))
    return (raceTime,raceDistance)

def getRangeFromEquation(race):
    #solve record=(time-x)(0+x)
    a = -1
    b = race[0]
    c = -race[1]
    d = (b**2) - (4*a*c)
    sol1 = (-b+math.sqrt(d))/(2*a)
    sol2 = (-b-math.sqrt(d))/(2*a)
    print(f'The solution are {sol1} and {sol2}')
    print("And the range is: ")
    print(math.floor(sol2)-math.ceil(sol1)+1)
print("\nScript Beggining")
race=getRace(code)
print(f"Race is:{race}")
getRangeFromEquation(race)



