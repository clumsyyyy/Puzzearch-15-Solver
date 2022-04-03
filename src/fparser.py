import os

def checkValid(arr):
    temp = [x for x in (arr)]
    temp.remove("ES")
    temp.append("16")
    temp = [int(x) for x in temp]
    temp.sort()
    for i in range(len(temp)):
        if (int(temp[i]) != i + 1):
            raise Exception("[INVALID] Input is not valid!")
    return True

def parseText(fname):
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, '../test/')
    if (os.path.exists(path + fname + ".txt")):
        file = open(path + fname + ".txt", "r")
        arr = file.read().replace("-", "ES").replace("\n", " ").split(" ")
        return arr if checkValid(arr) else None
    else:
        raise Exception("[INVALID] File doesn't exist! Make sure it is stored in the 'test' folder and the filename is correct! (without .txt)")
    
def parseInput():
    buffer = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        print("[ROW {}] | >> ".format(i + 1), end = " ")
        buffer[i] = list(map(str, input().split()))
        
    flattened_buffer = ' '.join([x for arr in buffer for x in arr])
    arr = flattened_buffer.replace("-", "ES").replace("\n", " ").split(" ")
    return arr if checkValid(arr) else None

def parseGUI(buffer):
    print(buffer)
    arr = buffer.rstrip().replace("-", "ES").replace("\n", " ").split(" ")
    return arr if checkValid(arr) else None

