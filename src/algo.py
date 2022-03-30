from queue import PriorityQueue
from puzzle import PuzzleItem, InvItem
import timeit as time

def solve(p):  
    # displays initial puzzle
    print()  
    print("Initial Puzzle:")
    p.show()
    print()
    
    # displays initial invalid values (kurang[i])
    if (not p.isSolved()):
        invalid_pq = PriorityQueue()
        for i in range(16):
            if (p.buffer[int(i/4)][int(i%4)] == "ES"):
                invalid_pq.put(InvItem(16, p.invalidPos(i)))
            else:
                currentValue = int(p.buffer[int(i/4)][int(i%4)])
                invalid_pq.put(InvItem(currentValue, p.invalidPos(i)))
                
        print("List of Invalid Values: ")
        while (not invalid_pq.empty()):
            temp = invalid_pq.get()
            if (temp.priority == 16):
                print("Kurang[ES] = {}".format(temp.value))
            else:
                print("Kurang[{}] = {}".format(temp.priority, temp.value))
                
        print("Sum of invalid values:", p.sumOfInvalidPos())
        print("Sum of invalid values and whether empty space in determined position:",
              p.sumOfInvalidPos() + p.nullPos())
        
        if ((p.sumOfInvalidPos() + p.nullPos()) % 2 != 0):
            print("This puzzle cannot be solved!\n")
        else:
            prioqueue = PriorityQueue()
            # initializes initial puzzle as first item in queue
            prioqueue.put(PuzzleItem(0, p, "NONE"))
            puzzle_arr = []
            res = []
            curr_id = 0

            # starts searching process
            print("\nSolving puzzle ... ")
            start_time = time.default_timer()
            deq_count = 0
            while (prioqueue.qsize() != 0):
                # dequeues item with lowest priority
                puzzleItem = prioqueue.get()
                deq_count += 1
                # adds that item to the list of solved puzzles
                puzzle_arr.append([puzzleItem.item, puzzleItem.direction])
                # puzzleItem.item.show()
                curr_id += 1
                
                #stop loop if current puzzle is already solved
                #else, keep inserting
                if puzzleItem.item.isSolved():
                    res.append([puzzleItem.item, puzzleItem.direction])
                    break
                else:
                    if (not puzzleItem.item.insertingIntoQueue(prioqueue, curr_id, puzzleItem.direction)):
                        break
                    
            stop_time = time.default_timer()
            
            # backtracks parent id to get the path
            # of solutions
            answer = prioqueue.get()
            res = [[answer.item, answer.direction]]
            puzzle_elmt = puzzle_arr[-1]
            while (puzzle_elmt[0].id != 0):
                res = [puzzle_elmt] + res
                puzzle_elmt = puzzle_arr[puzzle_elmt[0].id - 1]
            res = [[p, "NONE"]] + res
            
            # outputs solution
            for i in range(len(res)):
                res[i][0].show()
                print("Step {} | Command: {} \n".format(i, res[i][1]))

            # outputs process information
            print("Puzzle solved successfully!") 
            print("Elapsed time:", "%.11f" % (stop_time - start_time), "seconds")
            print("Raised nodes:", curr_id)
            print("Queue length: ", prioqueue.qsize())
            print("Dequeue count: ", deq_count)
            print("Steps taken :", len(res))
            print()
    else:
        print("This puzzle is already solved! >:(\n")