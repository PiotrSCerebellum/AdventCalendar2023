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
def traverse(route,mapDictionary):
    currentNode="AAA"
    steps=0
    while currentNode!="ZZZ":
        turn = 0 if route[0:1] == "L" else 1
        route= route[1:]+route[0:1]
        currentNode=mapDictionary[currentNode][turn]
        steps+=1
    return steps

route=getRoute(code)
print(route)
mapDictionary=mapAsDictionary(code)
print(mapDictionary)
stepsTaken=traverse(route,mapDictionary)
print(stepsTaken)