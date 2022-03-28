import puzzle as pc

def solve(p):
    dir_dict = {
        "LEFT": "RIGHT",
        "RIGHT": "LEFT",
        "UP": "DOWN",
        "DOWN": "UP"
    }
    dir_list = ["UP", "RIGHT", "DOWN", "LEFT"]
    if (not p.isSolved()):
        if ((p.sumOfInvalidPos() + p.nullPos()) % 2 != 0):
            print("Puzzle couldn't be solved!")
        else:
            print("Puzzle can be solved!")

            depth = 0
            ans_queue = []
            # evaluate each possible direction
            while (not p.isSolved()):
                depth += 1
                minCost = 16
                minDir = ""
                for i in range(0, len(dir_list)):
                    if ((depth == 1) or (depth > 1 and dir_list[i] != dir_dict[ans_queue[0]])
                        and p.checkDir(dir_list[i])):
                        p.swap(dir_list[i])
                        if (depth + p.nonMatchingTile() <= minCost):
                            minCost = depth + p.nonMatchingTile()
                            minDir = dir_list[i]
                        p.swap(dir_dict[dir_list[i]])
                print(minDir)
                p.swap(minDir)
                p.show()
                ans_queue = [minDir] + ans_queue
                    
    else:
        print("Puzzle is already solved!")
