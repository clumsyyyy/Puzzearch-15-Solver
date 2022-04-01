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
        kurangMsg, res, outputMsg = solve(p)
        ans_text.configure(text = outputMsg)
        kurang_label.configure(text = kurangMsg)
        
        delay_time = 0.5
        if (time_entry.get()) != "":
            delay_time = float(time_entry.get())
        layout.renderAll(res, delay_time)

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
                frame.grid_slaves(row = i, column = j)[0].delete(0, END)
                
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

    def renderAll(self, puzzle_arr, delay_time):
        global frame
        for i in range(len(puzzle_arr)):
            self.render(puzzle_arr[i][0])
            steps_label.configure(text = "Step " + str(i + 1) + ": " + puzzle_arr[i][1])
            time.sleep(delay_time)
            window.update()
            
            

begin_coord = 150

window = Tk()
window.geometry("500x400")
window.minsize(500, 400)
window.maxsize(500, 400)
window.title("15-Puzzle Solver")

frame = Frame(window)
frame.pack(fill= BOTH, expand= True, padx= 20, pady=20)

fname_entry = Entry(frame, text = "Input file name (without *.txt)", font = ('Arial', 10), width = 20)
fname_entry.place(x = 0, y = begin_coord + 40)

time_entry = Entry(frame, text = "Time limit (in seconds)", font = ('Arial', 10), width = 6)
time_entry.place(x = 200, y = begin_coord + 40 )

time_label = Label(frame, text = "Delay\ntime", font = ('Arial', 8))
time_label.place(x = 170, y = begin_coord + 30)

layout = GUIPuzzle()

steps_label = Label(frame, font = ("Arial", 8))
steps_label.place(x = 0, y = begin_coord)

fname_label = Label(frame, font = ("Arial, 8"), text = "Input file name (without *.txt)")
fname_label.place(x = 0, y = begin_coord + 20)

kurang_label = Label(frame, font = ("Arial, 8"), wraplength = 150)
kurang_label.place(x = 300, y = 0)

solve_button = Button(frame, text = "Solve", width = 16, command = solveClick)
solve_button.place(x = 0, y = begin_coord + 70)

clear_button = Button(frame, text = "Clear", width = 16, command = layout.clear)
clear_button.place(x = 128, y = begin_coord + 70)

ans_text = Label(frame, font = ("Arial", 8), text = "Waiting for search to begin...")
ans_text.place(x = 25, y = begin_coord + 100)

window.mainloop()

