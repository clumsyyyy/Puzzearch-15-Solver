from tkinter import *
from tkinter import messagebox
from algo import solve
from puzzle import *
from fparser import *
import time
puzzle_arr = []

def solveClick():
    global puzzle_arr
    filepath = fname_entry.get()
    try:
        if (len(filepath) != 0):
            p = Puzzle(parseText(filepath))
        else:
            p = Puzzle(parseGUI(layout.getBuf()))
        res, outputMsg = solve(p)
        ans_text.configure(text = outputMsg)
        layout.renderAll(res)
    except Exception as e:
        messagebox.showerror("[ERROR]", e)



class GUIPuzzle:
    def __init__(self):
        for i in range(4):
            for j in range(4):
                self.e = Entry(frame, width = 4, font = ('Arial', 20))
                self.e.grid(row = i, column = j)
                self.e.insert(END, "")
                
    def getBuf(self):
        buffer = ""
        for i in range(4):
            for j in range(4):
                buffer += frame.grid_slaves(row = i, column = j)[0].get() + " "

        return buffer
                
    def clear(self):
        for i in range(4):
            for j in range(4):
                frame.grid_slaves(row = i, column = j)[0].config({"background": "white"})
                frame.grid_slaves(row = i, column = j)[0].delete
    def render(self, puzzle):
        for i in range(4):
            for j in range(4):
                self.e = Entry(frame, width = 4, font = ('Arial', 20))
                self.e.grid(row = i, column = j)
                if (puzzle.buffer[i][j] == "ES"):
                    self.e.insert(END, "")
                    self.e.config({"background": "gray"})
                else:
                    self.e.insert(END, puzzle.buffer[i][j])

    def renderAll(self, puzzle_arr):
        global frame
        for i in range(len(puzzle_arr)):
            self.render(puzzle_arr[i][0])
            time.sleep(1)
            window.update()
            
    

        
begin_coord = 150
window = Tk()
window.geometry("500x400")
window.title("15-Puzzle Solver")
frame = Frame(window)
frame.pack(fill= BOTH, expand= True, padx= 20, pady=20)
fname_entry = Entry(frame, text = "Input file name (without *.txt)", font = ('Arial', 12), width = 28)
layout = GUIPuzzle()
fname_entry.place(x = 0, y = begin_coord)
solve_button = Button(frame, text = "Solve", width = 16, command = solveClick)
solve_button.place(x = 0, y = begin_coord + 40)
clear_button = Button(frame, text = "Clear", width = 16, command = layout.clear)
clear_button.place(x = 128, y = begin_coord + 40)
ans_text = Label(frame, font = ("Arial", 8), text = "Waiting for search to begin...")
ans_text.place(x = 25, y = begin_coord + 80)

window.mainloop()

