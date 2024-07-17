import re

code = open(r"C:\\Users\\Woda\\Desktop\\adventDay7.txt", "r")
dict={
   "A":14,
   "K":13,
   "Q":12,
   "J":1,
   "T":10
   
}
def getHands(string):
    hands=[]
    for line in string:
        hand,bid=line.strip().split(' ')
        value=0
        for card in hand:
            currentValue=0
            for i in re.finditer(f"[{card}J]", hand):
                currentValue+=1
            value=max(value,currentValue)
        if value>3:
            value+=2
        elif value==3:
            handSet=set(hand)
            handSet.discard("J")
            if len(handSet)==2: value=5
            else: value=4
        elif value==2:
            handSet=set(hand)
            handSet.discard("J")
            if len(handSet)==3: value=3
            else: value=2
        hands.append((hand,bid,value))
    return hands,len(hands)
def sortByLevel(hands):
    sorted=[[],[],[],[],[],[],[]]
    for hand in hands:
        sorted[hand[2]-1].append(hand)
    return sorted
def sortByCard(a,b,cardDict):
    #true if b is greater
    for card in range(len(a)):
        if a[card]==b[card]:
            continue
        valA=0
        valB=0
        if a[card] in cardDict.keys():
           valA=cardDict[a[card]]
        else:
           valA=int(a[card])
        if b[card] in cardDict.keys():
           valB=cardDict[b[card]]
        else:
           valB=int(b[card])
        return valA<valB
#sorts to descending
def bubbleSort(arr):
  for n in range(len(arr) - 1, 0, -1):
    swapped = False
    for i in range(n):  
        if sortByCard(arr[i][0],arr[i + 1][0],dict):
            swapped = True
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    if not swapped:
        return
def getFinalValue(sortedByCardAndLevel,totalHands):
    finalVal=0
    for level in reversed(sortedByCardAndLevel):
        for hand in level:
            handBid=int(hand[1])*totalHands
            totalHands-=1
            finalVal+=handBid
    return finalVal
        
print("\n Beggining script")
hands,handCount=getHands(code)
print(f"Hands: {hands}")
sortedByLevel=sortByLevel(hands)
print(f"Sorted by level: {sortedByLevel}")
for level in sortedByLevel:
    bubbleSort(level)
print(f"Sorted by card and level: {sortedByLevel}")
finalValue=getFinalValue(sortedByLevel,handCount)
print(f"Final bid: {finalValue}")