import fparser as fp
import puzzle as pc
import algo 

def title():
    print(" ____  _     ____  ____  _____ ____  ____  ____  _           _  ____ ")
    print("/  __\\/ \\ /\\/_   \\/_   \\/  __//  _ \\/  __\\/   _\\/ \\ /|      / \\/ ___\\")
    print("|  \\/|| | || /   / /   /|  \\  | / \\||  \\/||  /  | |_||_____ | ||    \\")
    print("|  __/| \_/|/   /_/   /_|  /_ | |-|||    /|  \_ | | ||\____\| |\___ |")
    print("\_/   \____/\____/\____/\_____\\_/ \|\_/\_/\\____/\_/ \|      \_/\____/")
    print()
    print(pc.GREEN_COLOR + "A(nother) 15-Puzzle Solver" + pc.RESET_COLOR)
    
def main():
    
    while (True):
        print("\nSelect your desired input method: ")
        print("[1] Text file")
        print("[2] Input by user")
        print("[0] Exit")
        
        try:
            
            option = int(input("| >> "))
            
            if (option == 1):
                print(pc.CYAN_COLOR + "\n[SELECTED] Text file" + pc.RESET_COLOR)
                print("Input your filename (without .txt)|")
                print("[IMPORTANT] File must be included in the test folder!")
                fname = input("| >> ")
                buffer = fp.parseText(fname)
            elif (option == 2):
                print(pc.CYAN_COLOR + "\n[SELECTED] Input by user" + pc.RESET_COLOR)
                print("Input the desired matrix in a 4 x 4 grid style!")
                print("Fill the empty space character with '-'!")
                buffer = fp.parseInput()
            elif (option == 0):
                print("Exiting program...\n")
                break
            
            p = pc.Puzzle(buffer)
            _, res, outputMessage = algo.solve(p)
            for i in range(len(res)):
                res[i][0].show()
                print("Step {} | Command: {} \n".format(i, pc.GREEN_COLOR + res[i][1] + pc.RESET_COLOR))
            print(outputMessage)
            
        except Exception as e:
            print(e)
            continue
title()
main()