from queue import PriorityQueue
from puzzle import PuzzleItem

def solve(p):  
    print()  
    if (not p.isSolved()):
        if ((p.sumOfInvalidPos() + p.nullPos()) % 2 != 0):
            print("Puzzle couldn't be solved!")
        else:
            print("Solving puzzle ... ")

            prioqueue = PriorityQueue()
            prioqueue.put(PuzzleItem(0, p, "NONE"))
            puzzle_arr = []
            res = []
            curr_id = 0

            while (prioqueue.qsize() != 0):
                puzzleItem = prioqueue.get()
                puzzle_arr.append([puzzleItem.item, puzzleItem.direction])
                curr_id += 1
                if (not puzzleItem.item.insertingIntoQueue(prioqueue, curr_id, puzzleItem.direction)):
                    break
        
            puzzle_elmt = puzzle_arr[-1]
            while (puzzle_elmt[0].id != 0):
                res.append(puzzle_elmt)
                puzzle_elmt = puzzle_arr[puzzle_elmt[0].id - 1]
            res.append([p, "NONE"])
            res.reverse()
            
            for i in range(len(res)):
                res[i][0].show()
                print("Command | " + res[i][1])
                print()
                
            print("Solved!")        
    else:
        print("Puzzle is already solved!")