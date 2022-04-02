from dataclasses import dataclass, field
import string
from typing import Any

@dataclass(order=True)
class PuzzleItem:
    priority: int
    item: Any=field(compare=False)
    
@dataclass(order=True)
class InvItem:
    priority: int
    value: Any=field(compare=False)
    
class Puzzle:

    # data members
    ROW_SIZE = 4
    COL_SIZE = 4
    NULL_I = 0
    NULL_J = 0
    curr_depth = 0
    id = 0
    buffer = []
    
    '''
    Constructor for the puzzle matrix
    '''
    def __init__(self, puzzle_string):
        self.buffer = [[0 for _ in range(self.COL_SIZE)] for _ in range(self.ROW_SIZE)]
        for i in range(self.ROW_SIZE):
            for j in range(self.COL_SIZE):
                elmt = puzzle_string[i * self.COL_SIZE + j]
                self.buffer[i][j] = elmt
                if (elmt == "ES"):
                    self.NULL_I = i
                    self.NULL_J = j
                
    '''
    Prints the puzzle matrix in a readable format
    '''
    def show(self):
        for i in range(self.ROW_SIZE):
            for j in range(self.COL_SIZE):
                print(self.buffer[i][j], end = " ")
            print()
        
    '''
    Checks possible movement directions for the current position
    '''
    def checkDir(self, direction):
        i = self.NULL_I
        j = self.NULL_J
        if (direction == "LEFT"):
            return j != 0 and self.buffer[i][j - 1] != "ES"
        elif (direction == "RIGHT"):
            return (j != self.COL_SIZE - 1) and self.buffer[i][j + 1] != "ES"
        elif (direction == "UP"):
            return i != 0 and self.buffer[i - 1][j] != "ES"
        elif (direction == "DOWN"):
            return (i != self.ROW_SIZE - 1) and self.buffer[i + 1][j] != "ES" 
        
    '''
    Shifts element of the puzzle matrix
    '''
    def shift(self, direction):
        i = self.NULL_I
        j = self.NULL_J
        if (self.checkDir(direction)):
            if (direction == "LEFT"): # NULL goes left
                self.buffer[i][j] = self.buffer[i][j - 1]
                self.buffer[i][j - 1] = "ES"
                self.NULL_J -= 1
            elif (direction == "RIGHT"): # NULL goes right
                self.buffer[i][j] = self.buffer[i][j + 1]
                self.buffer[i][j + 1] = "ES"
                self.NULL_J += 1
            elif (direction == "UP"): # NULL goes up
                self.buffer[i][j] = self.buffer[i - 1][j]
                self.buffer[i - 1][j] = "ES"
                self.NULL_I -= 1
            elif (direction == "DOWN"): # NULL goes down
                self.buffer[i][j] = self.buffer[i + 1][j]
                self.buffer[i + 1][j] = "ES"
                self.NULL_I += 1
                
    '''
    Checks if the puzzle is solved
    '''
    def isSolved(self):
        # return False if last element is not NULL
        if (self.buffer[self.ROW_SIZE - 1][self.COL_SIZE - 1] != "ES"):
            return False
        
        # else, check if all elements are in correct order, except for last element
        flattened_buffer = [x for arr in self.buffer for x in arr]
        for i in range(1, len(flattened_buffer) - 1):
            # return False if any element is not in correct order
            if (int(flattened_buffer[i]) != int(flattened_buffer[i - 1]) + 1):
                return False
        
        # return solved if all is sorted
        return True
    
    '''
    Returns 1 if:
    - odd row and even column
    - even row and odd column
    '''
    def nullPos(self):
        return 1 if (self.NULL_I % 2 != self.NULL_J % 2) else 0
    
    '''
    Counts the appearance of invalid position where
    element with less value than current element appears on a higher position
    '''
    def invalidPos(self, idx):
        count = 0
        flattened_buffer = [x for arr in self.buffer for x in arr]
        if (flattened_buffer[idx] == "ES"):
            count = self.COL_SIZE * self.ROW_SIZE - idx - 1
        for i in range(idx, len(flattened_buffer)):
            if (flattened_buffer[i] != "ES" and flattened_buffer[idx] != "ES"):
                if (int(flattened_buffer[i]) < int(flattened_buffer[idx]) and i > idx):
                    count += 1
        return count
    
    '''
    Returns the sum of invalid position
    '''
    def sumOfInvalidPos(self):
        sum = 0
        for i in range(0, self.ROW_SIZE * self.COL_SIZE):
            sum += self.invalidPos(i)
        return sum
    
    '''
    Counts the appearance of invalid position where
    tile position doesn't match the value of the tile
    '''
    def nonMatchingTile(self):
        count = 0
        flattened_buffer = [x for arr in self.buffer for x in arr]
        for i in range(0, len(flattened_buffer)):
            if (flattened_buffer[i] != "ES" and (int(flattened_buffer[i]) != (i + 1))):
                count += 1
        return count;

    '''
    Checks whether current state of the puzzle has existed before
    '''
    def checkState(self, state_dict):
        state = "|".join([x for arr in self.buffer for x in arr])
        if (state in state_dict):
            return True, "|"
        else:
            return False, state

