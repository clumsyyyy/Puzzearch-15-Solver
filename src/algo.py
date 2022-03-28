import string
import copy
from queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)
    direction: string=field
    
    
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
            print("Solving puzzle ... ")

            depth = 0
            prioqueue = PriorityQueue()
            prioqueue.put(PrioritizedItem(0, p, "NONE"))
            
            # evaluate each possible direction
            while (prioqueue.qsize() != 0):
                puzzleObj = prioqueue.get()
                temp = puzzleObj.item
                pdir = puzzleObj.direction
                # p.show()
                depth += 1
                
                for i in range(0, len(dir_list)):
                    if (((depth == 1) or (depth > 1 and dir_list[i] != dir_dict[pdir]))
                        and temp.checkDir(dir_list[i])):
                        
                        tp = copy.deepcopy(temp)
                        tp.shift(dir_list[i])
                        tempcost = depth + tp.nonMatchingTile()
                        prioqueue.put(PrioritizedItem(tempcost, tp, dir_list[i]))
               
                        if temp.isSolved():
                            print("Puzzle solved!")
                            return
                        
                        # t.swap(dir_dict[dir_list[i]])
                    
    else:
        print("Puzzle is already solved!")