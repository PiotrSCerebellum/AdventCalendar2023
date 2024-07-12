import re
code = open(r"C:\\Users\\Woda\\Desktop\\adventDay4.txt", "r")
def ingestCards(str):
    cards=[]
    for line in str:
        winningNumbers,guessedNumbers=line.split("|")
        cardNumber,winningNumbers=winningNumbers.split(":")
        winningNumbers=parseNumbers(winningNumbers)
        guessedNumbers=parseNumbers(guessedNumbers)
        cardNumber=parseNumbers(cardNumber)
        cards.append((cardNumber,winningNumbers,guessedNumbers))

    return cards
def parseNumbers(str):
    numbers=re.findall(r"\d+",str)
    numbers=list(numbers)
    return numbers
def calculatePointValue(cards):
    total=0
    for card in cards:
        guessed=set(card[1])
        wining=set(card[2])
        right=len(wining.intersection(guessed))
        total+=winFunction(right)
    return total
def winFunction(num):
    if num==0:
        return 0
    return 2**(num-1)  


print("\nIngesting cards")
cards=ingestCards(code)
total=calculatePointValue(cards)
for card in cards:
    print(f"Card number: {card[0]} Winning: {card[1]} Guessed: {card[2]}")
print("Total point value: ",total)

