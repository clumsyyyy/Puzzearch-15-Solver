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
            if ((p.sumOfInvalidPos() + p.nullPos()) % 2 != 0):
                outputMessage = "This puzzle cannot be solved!\n"
            else:
                print("\nSolving puzzle ... ")
                prioqueue = PriorityQueue()
                # initializes initial puzzle as first item in queue
                prioqueue.put(PuzzleItem(0, p, "NONE"))
                state_dict = {}
                puzzle_arr = []
                curr_id = 0

                # starts searching process

                start_time = time.default_timer()
                deq_count = 0
                while (prioqueue.qsize() != 0):
                    # dequeues item with lowest priority
                    puzzleItem = prioqueue.get()
                    temp = puzzleItem.item
                    prev_direction = puzzleItem.direction
                    deq_count += 1
                    # adds that item to the list of solved puzzles
                    state_dict["|".join([x for arr in puzzleItem.item.buffer for x in arr])] = True
                    puzzle_arr.append([puzzleItem.item, puzzleItem.direction])
                    # puzzleItem.item.show()
                    curr_id += 1
                    
                    #stop loop if current puzzle is already solved
                    #else, keep inserting
                    if puzzleItem.item.isSolved():
                        res.append([puzzleItem.item, puzzleItem.direction])
                        break
                    else:

                        if (p.isSolved()):
                            break
                        if (temp.checkDir("UP") and prev_direction != "DOWN"):
                            puzzle = Puzzle([x for arr in temp.buffer for x in arr])
                            puzzle.shift("UP")
                            puzzle.curr_depth = temp.curr_depth + 1
                            puzzle.id = curr_id
                            currCost = puzzle.curr_depth + puzzle.nonMatchingTile()
                            if (puzzle.isSolved()):
                                prioqueue.put(PuzzleItem(0, puzzle, "UP"))
                                stop_time = time.default_timer()
                                break
                            elif (not puzzle.stateExisted(state_dict)):
                                prioqueue.put(PuzzleItem(currCost, puzzle, "UP"))
                            
                        if (temp.checkDir("RIGHT") and prev_direction != "LEFT"):
                            puzzle = Puzzle([x for arr in temp.buffer for x in arr])
                            puzzle.shift("RIGHT")
                            puzzle.curr_depth = temp.curr_depth + 1
                            puzzle.id = curr_id
                            currCost = puzzle.curr_depth + puzzle.nonMatchingTile()
                            if (puzzle.isSolved()):
                                prioqueue.put(PuzzleItem(0, puzzle, "RIGHT"))
                                stop_time = time.default_timer()
                                break
                            elif (not puzzle.stateExisted(state_dict)):
                                prioqueue.put(PuzzleItem(currCost, puzzle, "RIGHT"))
                            
                        if (temp.checkDir("DOWN") and prev_direction != "UP"):
                            puzzle = Puzzle([x for arr in temp.buffer for x in arr])
                            puzzle.shift("DOWN")
                            puzzle.curr_depth = temp.curr_depth + 1
                            puzzle.id = curr_id
                            currCost = puzzle.curr_depth + puzzle.nonMatchingTile()
                            if (puzzle.isSolved()):
                                prioqueue.put(PuzzleItem(0, puzzle, "DOWN"))
                                stop_time = time.default_timer()
                                break
                            elif (not puzzle.stateExisted(state_dict)):
                                prioqueue.put(PuzzleItem(currCost, puzzle, "DOWN"))
                            
                        if (temp.checkDir("LEFT") and prev_direction != "RIGHT"):
                            puzzle = Puzzle([x for arr in temp.buffer for x in arr])
                            puzzle.shift("LEFT")
                            puzzle.curr_depth = temp.curr_depth + 1
                            puzzle.id = curr_id
                            currCost = puzzle.curr_depth + puzzle.nonMatchingTile()
                            if (puzzle.isSolved()):
                                prioqueue.put(PuzzleItem(0, puzzle, "LEFT"))
                                stop_time = time.default_timer()
                                break
                            elif (not puzzle.stateExisted(state_dict)):
                                prioqueue.put(PuzzleItem(currCost, puzzle, "LEFT"))
                        

                
                # backtracks parent id to get the path
                # of solutions
                answer = prioqueue.get()
                res = [[answer.item, answer.direction]]
                puzzle_elmt = puzzle_arr[-1]
                while (puzzle_elmt[0].id != 0):
                    res = [puzzle_elmt] + res
                    puzzle_elmt = puzzle_arr[puzzle_elmt[0].id - 1]
                res = [[p, "NONE"]] + res

                # outputs process information
                outputMessage += "\nPuzzle solved successfully!"
                outputMessage += "\nElapsed time: " + str("%.11f" % (stop_time - start_time)) + " seconds"
                outputMessage += "\nRaised nodes: " + str(deq_count+ len(res))
                outputMessage += "\nSteps taken : " + str(len(res))
                return kurangMessage, res, outputMessage
    else:
        raise Exception("This puzzle is already solved! >:(\n")