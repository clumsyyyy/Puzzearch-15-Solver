# Parser script for testcases

import os

def parseText():
    print("\n[SELECTED] Text file")
    print("Input your filename (without .txt)|")
    print("[IMPORTANT] File must be included in the test folder!")
    fname = input("| >> ")
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, '../test/')
    file = open(path + fname, "r")
    return file.read().replace("-", "ES").replace("\n", " ").split(" ")


def parseInput():
    print("\n[SELECTED] Input by user")
    print("Input the desired matrix in a 4 x 4 grid style!")
    print("Fill the empty space character with '-'!")
    buffer = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        print("[ROW {}] | >> ".format(i + 1), end = " ")
        buffer[i] = list(map(str, input().split()))
    flattened_buffer = ' '.join([x for arr in buffer for x in arr])
    
    return flattened_buffer.replace("-", "ES").replace("\n", " ").split(" ")