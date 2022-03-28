class Puzzle:
    
    # data members
    ROW_SIZE = 4
    COL_SIZE = 4
    NULL_I = 0
    NULL_J = 0
    
    '''
    Constructor for the puzzle matrix
    ''';
    def __init__(self, puzzle_string):
        print(puzzle_string)
        self.buffer = [[0 for _ in range(self.COL_SIZE)] for _ in range(self.ROW_SIZE)]
        for i in range(self.ROW_SIZE):
            for j in range(self.COL_SIZE):
                elmt = puzzle_string[i * self.COL_SIZE + j]
                self.buffer[i][j] = elmt
                if (elmt == "NULL"):
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
        print()
    
    '''
    Checks possible movement directions for the current position
    '''
    def checkDir(self, i, j, direction):
        if (direction == "LEFT"):
            return self.buffer[i][j - 1] != "NULL" and j != 0
        elif (direction == "RIGHT"):
            return self.buffer[i][j + 1] != "NULL" and j != self.COL_SIZE - 1
        elif (direction == "UP"):
            return self.buffer[i - 1][j] != "NULL" and i != 0
        elif (direction == "DOWN"):
            return self.buffer[i + 1][j] != "NULL" and i != self.ROW_SIZE - 1
        
    '''
    Swaps element of the puzzle matrix
    '''
    def swap(self, direction):
        i = self.NULL_I
        j = self.NULL_J
        if (self.checkDir(i, j, direction)):
            if (direction == "LEFT"): # NULL goes left
                self.buffer[i][j] = self.buffer[i][j - 1]
                self.buffer[i][j - 1] = "NULL"
                self.NULL_J -= 1
            elif (direction == "RIGHT"): # NULL goes right
                self.buffer[i][j] = self.buffer[i][j + 1]
                self.buffer[i][j + 1] = "NULL"
                self.NULL_J += 1
            elif (direction == "UP"): # NULL goes up
                self.buffer[i][j] = self.buffer[i - 1][j]
                self.buffer[i - 1][j] = "NULL"
                self.NULL_I -= 1
            elif (direction == "DOWN"): # NULL goes down
                self.buffer[i][j] = self.buffer[i + 1][j]
                self.buffer[i + 1][j] = "NULL"
                self.NULL_I += 1
                
    '''
    Checks if the puzzle is solved
    '''
    def isSolved(self):
        # return False if last element is not NULL
        if (self.buffer[self.NULL_I][self.NULL_J] != "NULL"):
            return False
        
        # else, check if all elements are in correct order, except for last element
        flattened_buffer = [x for arr in self.buffer for x in arr]
        for i in range(1, len(flattened_buffer) - 1):
            # return False if any element is not in correct order
            if (int(flattened_buffer[i]) != int(flattened_buffer[i - 1]) + 1):
                return False
        
        # return solved if all is sorted
        return True
    
    
        
    