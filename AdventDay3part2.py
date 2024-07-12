import re
code = open(r"C:\\Users\\Woda\\Desktop\\adventDay3.txt", "r")


def makeAdjecencyGrid(str):
    grid = [["."]]
    specialChars=set()
    gears=set()
    numbers=[]
    x=1
    for line in str:
        row=["."]
        y=1
        consequtive=False
        for char in line:
            if(char=="\n"):
                continue
            row.append(char)
            if(re.match(r"[^1234567890\.\n]",char)!=None):
                specialChars.add((x,y))
                if(char=="*"):
                    gears.add((x,y))
            if(re.match(r"\d",char)!=None):
                if(not consequtive):
                    numbers.append([(x,y)])
                else:
                    numbers[len(numbers)-1].append((x,y))
                consequtive=True
            else:
                consequtive=False
            y+=1
        row.append(".")
        grid.append(row)
        x+=1
    grid[0]=grid[1].copy()
    for i in range(len(grid[0])):
        grid[0][i]="."
    grid.append(grid[0])
    return grid,specialChars,numbers,gears

def confirmNumbers(numbers,specials):
    confirmedNumbers=[]
    for number in numbers:
        numberSurroudings=set()
        for digit in number:
            for x in range(3):
                for y in range(3):
                    coordinates = (digit[0]+x-1,digit[1]+y-1)
                    numberSurroudings.add(coordinates)
        if len(numberSurroudings.intersection(specials))==0:
            continue
        confirmedNumbers.append(number)
    return confirmedNumbers

def readNumbers(numbers,grid):
    results=[]
    for num in numbers:
        numberString=""
        for digit in num:
            numberString+=grid[digit[0]][digit[1]]
        results.append(numberString)
    return results

def addNumbers(numbers):
    result=0
    for number in numbers:
        result+=int(number)
    return result
def multiplyNumbers(numbers):
    result=1
    for number in numbers:
        result*=int(number)
    return result
def getGearRatios(gears,numbers,grid):
    results=[]
    for gear in gears:
        surroundings=set()
        ratios=[]
        for x in range(3):
             for y in range(3):
                coordinates = (gear[0]+x-1,gear[1]+y-1)
                surroundings.add(coordinates)
        for number in numbers:
            setOfNumber=set(number)
            if len(surroundings.intersection(setOfNumber))==0:
                continue
            ratios.append(number)
        if len(ratios)<2:
            continue
        gearRatio=readNumbers(ratios,grid)
        results.append(multiplyNumbers(gearRatio))
    return results
        

        
        

            

        


    

print("\n Starting blueprint ingestion")
grid,index,numbers,gears=makeAdjecencyGrid(code)
print("The grid")
print(grid)
print("Special chars coordinates")
print(index)
print("Numbers")
print(numbers)
confirmedNumbers=confirmNumbers(numbers,index)
print("Confirmed numbers")
print(confirmedNumbers)
parsedNumbers=readNumbers(confirmedNumbers,grid)
print("Parsed numbers")
print(parsedNumbers)
result=addNumbers(parsedNumbers)
print("Resulting sum")
print(result)
gearRatios=getGearRatios(gears,numbers,grid)
print("Gear Ratios")
print(gearRatios)
gearSum=addNumbers(gearRatios)
print("Resulting gear sum")
print(gearSum)




