import numpy as np
import eq_mat as matrix
from tkinter import *

# "2x+5y-7,x+3y-4"
# "2x+5y=-7,x+3y=-4"


def gauss_jordan(n, equations):
    output = list()
    Matrix = matrix.inputToMatrix(n, equations)

    result = np.zeros(n)

    for i in range(n):
        if Matrix[i][i] == 0.0:
            output.append('ERROR! Dividing by zero')
            return output

        for j in range(n):
            if i != j:
                ratio = Matrix[j][i] / Matrix[i][i]

                for k in range(n + 1):
                    Matrix[j][k] = Matrix[j][k] - ratio * Matrix[i][k]

    for i in range(n):
        result[i] = Matrix[i][n] / Matrix[i][i]

    for i in range(n):
        output.append('Root%d = %0.3f' % (i + 1, result[i]))
    f = open("JordanOutput.txt", "w")
    f.write(str(output))
    f.close()
    return output


############# GUI #############
def gauss_jordan_win(noOfV=0, eqs=""):
    def clickGaussJordan():
        unknownsNoField = unknownsEntry.get()
        equationField = equEntry.get()
        output.delete(0.0, END)
        output.insert(END, gauss_jordan(int(unknownsNoField), equationField))

    window = Tk()
    window.title("Gauss Jordan Method")
    window.configure(bg="#cad9ea")
    window.geometry("600x400")

    m_label = Label(window, text="Gauss Jordan Method",
                    bg="#5a92bf", fg="#e4ebf2", font=(15))
    m_label.place(x=220, y=20)

    uknowns_label = Label(
        window, text="Enter number of equations.", bg="#cad9ea", fg="black")
    uknowns_label.place(x=30, y=95)

    unknownsEntry = Entry(window, width=15, bg="#e4ebf2", borderwidth=.5)
    unknownsEntry.insert(0, noOfV)
    unknownsEntry.place(x=205, y=95)

    equations_label = Label(
        window, text="Enter your equations separated by a comma.", bg="#cad9ea", fg="black")
    equations_label.place(x=30, y=150)

    equEntry = Entry(window, width=90, bg="#e4ebf2", borderwidth=.5)
    equEntry.insert(0, eqs)
    equEntry.place(x=25, y=175)

    solve_btn = Button(window, text="Solve", width=15, height=1,
                       bg="#ff9732", fg="black", command=clickGaussJordan)
    solve_btn.place(x=240, y=230)

    output = Text(window, width=90, height=8.5,
                  wrap=WORD, background="#e4ebf2")
    output.place(x=0, y=265)
