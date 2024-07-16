import re
code = open(r"C:\\Users\\Woda\\Desktop\\adventDay5Test.txt", "r")
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
def transformFromMap(listOfMaps,input):
    transform=input
    for map in listOfMaps:
        map=map.split()
        target=int(map[0])
        source=int(map[1])
        spread=int(map[2])
        spread=range(source,source+spread)
        if(input in spread):
            transform=transform-source+target
            return transform
    return transform
def transfromSeeds(dictionary):
    seeds=[int(x) for x in dictionary["seeds"][0].split()]
    allTransformations=[]
    for seed in seeds:
        transformations=[seed]
        for map in dictionary:
            if map=="seeds":
                continue
            transformations.append(transformFromMap(dictionary[map],transformations[len(transformations)-1]))
        allTransformations.append(transformations)
    return allTransformations
def getLowestLocation(listOfAllTransformations):
    lowest=listOfAllTransformations[0][len(listOfAllTransformations[0])-1]
    for list in listOfAllTransformations:
        lowest=min(lowest,list[len(list)-1])
    return lowest

fullString=getString(code)
solutionDict=getMaps(fullString)
listOfAllTransformations=transfromSeeds(solutionDict)
lowestField=getLowestLocation(listOfAllTransformations)
print("\n\n Ingesting Almanch")
print(f"List of all transformations \n {listOfAllTransformations}")
print("Lowest field is: ")
print(lowestField)
