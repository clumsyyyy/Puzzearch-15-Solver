from queue import PriorityQueue
from puzzle import PuzzleItem, InvItem, Puzzle
import timeit as time

def solve(p):  
    # displays initial puzzle
    print()  
    print("Initial Puzzle:")
    p.show()
    print()
    
    outputMessage = ""
    res = []
    kurangMessage = ""
    # displays initial invalid values (kurang[i])
    if (not p.isSolved()):
        invalid_pq = PriorityQueue()
        for i in range(16):
            if (p.buffer[int(i/4)][int(i%4)] == "ES"):
                invalid_pq.put(InvItem(16, p.invalidPos(i)))
            else:
                currentValue = int(p.buffer[int(i/4)][int(i%4)])
                invalid_pq.put(InvItem(currentValue, p.invalidPos(i)))
                
        kurangMessage += "List of Invalid Values: \n"
        
        while (not invalid_pq.empty()):
            temp = invalid_pq.get()
            if (temp.priority == 16):
                kurangMessage += "Kurang[ES] = {}\n".format(temp.value)
            else:
                kurangMessage += "Kurang[{}] = {}\n".format(temp.priority, temp.value)
                
        kurangMessage+= "Sum of invalid values: {}\n".format(p.sumOfInvalidPos())
        kurangMessage += "Sum of invalid values and whether empty space in determined position: {}\n".format(
            p.sumOfInvalidPos() + p.nullPos())
        
        print(kurangMessage)
        
        if ((p.sumOfInvalidPos() + p.nullPos()) % 2 != 0):
            raise Exception("This puzzle cannot be solved!\n")
        
        else:
            print("\nSolving puzzle ... ")
            prioqueue = PriorityQueue()
            p.curr_depth = 0
            p.id = 0
            
            # initializes initial puzzle as first item in queue
            prioqueue.put(PuzzleItem(0, [p, "NONE"]))
            state_dict = {}
            puzzle_arr = []
            curr_id = 0
            deq_count = 0
            
            # starts searching process
            start_time = time.default_timer()
            
            while (prioqueue.qsize() != 0):
                
                # dequeues item with lowest priority
                puzzleItem = prioqueue.get()
                temp = puzzleItem.item[0]
                prev_direction = puzzleItem.item[1]
                # adds that item to the list of solved puzzles
                puzzle_arr.append([temp, prev_direction])
                deq_count += 1
                curr_id += 1
                
                if temp.isSolved():
                    stop_time = time.default_timer()
                    break
                
                if (temp.checkDir("UP") and prev_direction != "DOWN"):
                    puzzle_up = Puzzle([x for arr in temp.buffer for x in arr])
                    puzzle_up.shift("UP")
                    has_existed, state = puzzle_up.checkState(state_dict)
                    if (not has_existed):
                        puzzle_up.curr_depth = temp.curr_depth + 1
                        puzzle_up.id = curr_id
                        currCost = puzzle_up.curr_depth + puzzle_up.nonMatchingTile()
                        prioqueue.put(PuzzleItem(currCost, [puzzle_up, "UP"]))
                        state_dict[state] = True
                            
                if (temp.checkDir("RIGHT") and prev_direction != "LEFT"):
                    puzzle_right = Puzzle([x for arr in temp.buffer for x in arr])
                    puzzle_right.shift("RIGHT")
                    has_existed, state = puzzle_right.checkState(state_dict)
                    if (not has_existed):
                        puzzle_right.curr_depth = temp.curr_depth + 1
                        puzzle_right.id = curr_id
                        currCost = puzzle_right.curr_depth + puzzle_right.nonMatchingTile()
                        prioqueue.put(PuzzleItem(currCost, [puzzle_right, "RIGHT"]))
                        state_dict[state] = True
            
                if (temp.checkDir("DOWN") and prev_direction != "UP"):
                    puzzle_down = Puzzle([x for arr in temp.buffer for x in arr])
                    puzzle_down.shift("DOWN")
                    has_existed, state = puzzle_down.checkState(state_dict)
                    if (not has_existed):
                        puzzle_down.curr_depth = temp.curr_depth + 1
                        puzzle_down.id = curr_id
                        currCost = puzzle_down.curr_depth + puzzle_down.nonMatchingTile()
                        prioqueue.put(PuzzleItem(currCost, [puzzle_down, "DOWN"]))
                        state_dict[state] = True             
                    
                if (temp.checkDir("LEFT") and prev_direction != "RIGHT"):
                    puzzle_left = Puzzle([x for arr in temp.buffer for x in arr])
                    puzzle_left.shift("LEFT")
                    has_existed, state = puzzle_left.checkState(state_dict)
                    if (not has_existed):
                        puzzle_left.curr_depth = temp.curr_depth + 1
                        puzzle_left.id = curr_id
                        currCost = puzzle_left.curr_depth + puzzle_left.nonMatchingTile()
                        prioqueue.put(PuzzleItem(currCost, [puzzle_left, "LEFT"]))
                        state_dict[state] = True


            # backtracks parent id to get the path
            # of solutions
            res = []
            puzzle_elmt = puzzle_arr[-1]
            while (puzzle_elmt[0].id != 0):
                res = [puzzle_elmt] + res
                puzzle_elmt = puzzle_arr[puzzle_elmt[0].id - 1]
            res = [[p, "NONE"]] + res

            # outputs process information
            outputMessage += "\nPuzzle solved successfully!"
            outputMessage += "\nElapsed time: " + str("%.11f" % (stop_time - start_time)) + " seconds"
            outputMessage += "\nRaised nodes: " + str(deq_count+ len(res))
            outputMessage += "\nCurrent ID: " + str(curr_id)
            outputMessage += "\nSteps taken : " + str(len(res))
            return kurangMessage, res, outputMessage
    else:
        raise Exception("This puzzle is already solved! >:(\n")