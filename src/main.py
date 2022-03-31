import fparser as fp
import puzzle as pc
import algo 
def main():
    while (True):
        print("\n\nSelect your desired input method: ")
        print("[1] Text file")
        print("[2] Input by user")
        print("[0] Exit")
        try:
            option = int(input("| >> "))
            if (option == 1):
                print("\n[SELECTED] Text file")
                print("Input your filename (without .txt)|")
                print("[IMPORTANT] File must be included in the test folder!")
                fname = input("| >> ")
                try:
                    buffer = fp.parseText(fname)
                except Exception as e:
                    print(e)
                    continue
            elif (option == 2):
                buffer = fp.parseInput()
                
            elif (option == 0):
                print("Exiting program...")
                break
        except Exception as e:
            print(e)
            continue
        if (buffer == "err"):
            print("Filename doesn't exist!")
        else:
            p = pc.Puzzle(buffer)
            _, res, outputMessage = algo.solve(p)
            for i in range(len(res)):
                res[i][0].show()
                print("Step {} | Command: {} \n".format(i, res[i][1]))
            print(outputMessage)

main()