import fparser as fp
import puzzle as pc
import algo 
def main():
    # fname = input("Enter the testfile name | >> ")
    fname = "test3.txt" # hardcoded for now
    p = pc.Puzzle(fp.parseText(fname))
    algo.solve(p)

main()