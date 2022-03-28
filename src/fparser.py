# Parser script for testcases

import os

def parseText(fname):
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, '../test/')
    file = open(path + fname, "r")
    return file.read().replace("\n", " ").split(" ")
