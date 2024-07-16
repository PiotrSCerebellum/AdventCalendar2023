import re
code = open(r"C:\\Users\\Woda\\Desktop\\adventDay5.txt", "r")
mapsDictionary={
    "seeds": r"(?<=seeds:)(.*?)(?=seed)",
    "seed-to-soil":r"(?<=seed-to-soil map:)(.*?)(?=soil)",
    "soil-to-fertilizer":r"(?<=soil-to-fertilizer map:)(.*?)(?=fertilizer)",
    "fertilizer-to-water":r"(?<=fertilizer-to-water map:)(.*?)(?=water)",
    "water-to-light":r"(?<=water-to-light map:)(.*?)(?=light)",
    "light-to-temperature":r"(?<=light-to-temperature map:)(.*?)(?=temperature)",
    "temperature-to-humidity":r"(?<=temperature-to-humidity map:)(.*?)(?=humidity)",
    "humidity-to-location":r"(?<=humidity-to-location map:)(.*?)(?=$)",
 
}
def getString(io):
    decoded=""
    for line in io:
        decoded+=line
    return decoded
def getMaps(str):
    solutionDictionary=mapsDictionary.copy()
    for key in mapsDictionary:
        pattern = mapsDictionary[key]
        match = re.search(pattern, str, flags=re.DOTALL) 
        numbers=[x for x in match.group(1).split("\n") if len(x)>0]
        solutionDictionary[key]=numbers
    return solutionDictionary

def reverseTransformFromMap(listOfMaps,input):
    transform=input
    for map in listOfMaps:
        map=map.split()
        target=int(map[1])
        source=int(map[0])
        spread=int(map[2])
        spread=(source,source+spread)
        if input>=spread[0] and input<=spread[1]:
            transform=transform-source+target
            return transform
    return transform

def getSeedRanges(dict):
    seedRanges=[]
    seedRanges=re.findall(r"\d+",dict["seeds"][0])
    result=[]
    for seedRange in range(0,len(seedRanges),2):
        x1, dx = map(int, (seedRanges[seedRange],seedRanges[seedRange+1]))
        x2 = x1 + dx
        result.append((x1, x2, "seed-to-soil"))
    return result

def transfromSeeds(dictionary):
    levelProgression=[x for x in dictionary]
    levelProgression.append("finish")
    toCheck=getSeedRanges(dictionary)
    min_location=2147483647
    while toCheck:
        x1,x2,level=toCheck.pop()
        if level == "finish":
            min_location = min(x1, min_location)
            continue
        for mapping in dictionary[level]:
            mapping=mapping.split()
            z=int(mapping[0])
            y1=int(mapping[1])
            dy=int(mapping[2])
            y2 = y1 + dy
            diff = z - y1
            if x2 <= y1 or y2 <= x1:    # no overlap
                continue
            if x1 < y1:                 # split original interval at y1
                toCheck.append((x1, y1, level))
                x1 = y1
            if y2 < x2:                 # split original interval at y2
                toCheck.append((y2, x2, level))
                x2 = y2
            toCheck.append((x1 + diff, x2 + diff, levelProgression[levelProgression.index(level)+1])) # perfect overlap 
            break
        else:
            toCheck.append((x1, x2, levelProgression[levelProgression.index(level)+1]))
    return min_location



    

fullString=getString(code)
solutionDict=getMaps(fullString)
result=transfromSeeds(solutionDict)

print("\n\n Ingesting Almanch")
print(f"Final answer \n {result}")


