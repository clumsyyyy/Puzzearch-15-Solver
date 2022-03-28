import fparser as fp
import puzzle as pc

def main():
    # fname = input("Enter the testfile name | >> ")
    fname = "test1.txt" # hardcoded for now
    p = pc.Puzzle(fp.parseText(fname))
    p.show()
    
main()