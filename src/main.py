import fparser as fp
import puzzle as pc
import algo 
def main():
    print("Selected your desired input method: ")
    print("[1] Text file")
    print("[2] Input by user")
    print("[0] Exit")
    option = int(input("| >> "))
    if (option == 1):
        buffer = fp.parseText()
    elif (option == 2):
        buffer = fp.parseInput()
    elif (option == 0):
        print("Exiting program...")
        return
    p = pc.Puzzle(buffer)
    algo.solve(p)

main()