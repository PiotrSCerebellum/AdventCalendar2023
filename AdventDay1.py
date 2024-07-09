import re
code = open(r"C:\\Users\\Woda\\Desktop\\code.txt", "r")
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
            first=findFirstNum(line)
            last=findLastNum(line)
            result+=int(first+last)
        except:
            print("failed at iteration: {0} and line: {1}".format(i,line))
        finally:
            i+=1
    print(result)
print("\nStart decoding")
decode(code)