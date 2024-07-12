import re
code = open(r"C:\\Users\\Woda\\Desktop\\adventDay4.txt", "r")

def ingestCards(str):
    cards=[]
    for line in str:
        winningNumbers,guessedNumbers=line.split("|")
        cardNumber,winningNumbers=winningNumbers.split(":")
        winningNumbers=parseNumbers(winningNumbers)
        guessedNumbers=parseNumbers(guessedNumbers)
        cardNumber=int(parseNumbers(cardNumber)[0])
        cardValue=calculatePointValue([cardNumber,winningNumbers,guessedNumbers])
        cards.append([cardNumber,winningNumbers,guessedNumbers,cardValue])
    return cards

def parseNumbers(str):
    numbers=re.findall(r"\d+",str)
    numbers=list(numbers)
    return numbers

def calculatePointValue(card):
    guessed=set(card[1])
    wining=set(card[2])
    cardValue=len(wining.intersection(guessed))
    return cardValue

def calculateOldPointValue(card):
    guessed=set(card[1])
    wining=set(card[2])
    right=len(wining.intersection(guessed))
    cardValue=winFunction(right)
    return cardValue

def winFunction(num):
    if num==0:
        return 0
    return 2**(num-1)

def getTrueCardValue(card,cards):
    truevalue=1
    if len(card)>4:
        return card[4]
    elif card[3]==0:
        truevalue=1
    else: 
        for i in range(card[0],card[0]+card[3]):
            truevalue+=getTrueCardValue(cards[i],cards)
    card.append(truevalue)
    return truevalue
            



print("\nIngesting cards")
cards=ingestCards(code)
trueTotal=0
for card in cards:
    trueTotal+=getTrueCardValue(card,cards)
    print(f"Card number: {card[0]} TrueValue:{card[4]} Value:{card[3]} Winning: {card[1]} Guessed: {card[2]}")
print("Total true point value: ",trueTotal)


