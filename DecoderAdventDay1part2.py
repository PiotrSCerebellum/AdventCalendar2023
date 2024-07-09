import re
code = open(r"C:\\Users\\Woda\\Desktop\\code.txt", "r")
digit_dict = {
  "zero": "0",
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9",
   "0": "0",
  "1": "1",
  "2": "2",
  "3": "3",
  "4": "4",
  "5": "5",
  "6": "6",
  "7": "7",
  "8": "8",
  "9": "9"
}


def decodeStringToNumbers(str):
    decodedString=" " * len(str)
    for digit in digit_dict:
        index = findIndexesOfStrings(str,digit)
        if(index==[]):
            continue
        newstring=digit_dict[digit]
        decodedString=replaceCharsAtIndexes(decodedString,index,newstring)
    decodedString=decodedString.replace(" ","")
    return decodedString
def replaceCharsAtIndexes(string,indexes,newstring):
    for index in indexes:
        string = string[:index] + newstring + string[index + 1:]
    return string
def findIndexesOfStrings(string,substring):
    return [i for i in range(len(string)) if string.startswith(substring, i)] 
def findFirstNum(str):
    return re.search(r"\d", str).group(0)
def findLastNum(str):
    revStr=str[::-1]
    return re.search(r"\d", revStr).group(0)
def decode(str):
    result=0
    i=0
    for line in str:
        try:
            decodedLine=decodeStringToNumbers(line)
            first=findFirstNum(decodedLine)
            last=findLastNum(decodedLine)
            result+=int(first+last)
            print(f"{first+last} {result} {decodedLine} {line}")
        except Exception as error:
            print("failed at iteration: {0} and line: {1}".format(i,line))
            print("An exception occurred:", error)
        finally:
            i+=1
    print("Final result is: ",result)
print("\nStart decoding")
decode(code)