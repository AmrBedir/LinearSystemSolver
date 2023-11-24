from tkinter import *
import tkinter.font as font
from GaussianJordan import *
from GaussElimination import *
from BothOfThemGUI import *

root = Tk()
root.configure(bg="#cad9ea")
root.geometry("400x350")
root.title("Linear Equations Solver")

label = Label(text="Choose a method for solution",
              bg="#cad9ea", fg="black", font=(1))
label.place(x=70, y=50)

gauss_elimination = Button(root, text="Gauss Elimination", width=20, height=2, bg="#5a92bf", fg="white",
                           command=gauss_elimination_win)
gauss_elimination.place(x=30, y=100)

gauss_jordan = Button(root, text="Gauss-Jordan", width=20, height=2, bg="#5a92bf", fg="white",
                      command=gauss_jordan_win)
gauss_jordan.place(x=220, y=100)

both_of_them = Button(root, text="Both of them", width=25, height=2, bg="#5a92bf", fg="white",
                      command=methods_win)
both_of_them.place(x=100, y=190)

root.mainloop()
