from GaussianJordan import *
from GaussElimination import *


def methods_win(iter=50, errors=0.00001, initPoint=[0, 0, 0]):
    window = Tk()
    window.title("Solving Equations by Guass & Guass-Jordan")
    window.configure(bg="#cad9ea")
    window.geometry("700x600")

    m_label = Label(window, text="Gauss Elimination Method",
                    bg="#5a92bf", fg="#e4ebf2", font=(15))
    m_label.place(x=230, y=20)

    uknowns_label = Label(
        window, text="Enter number of equations.", bg="#cad9ea", fg="black")
    uknowns_label.place(x=85, y=100)

    unknownsEntry = Entry(window, width=15, bg="#e4ebf2", borderwidth=.5)
    unknownsEntry.place(x=245, y=100)

    equations_label = Label(
        window, text="Enter your equations separated by a comma.", bg="#cad9ea", fg="black")
    equations_label.place(x=85, y=150)

    equEntry = Entry(window, width=90, bg="#e4ebf2", borderwidth=.5)
    equEntry.place(x=80, y=175)

    line = Label(window,
                 text="--------------------------------------------------------------------------------------------------------------------------------------------",
                 bg="#cad9ea", fg="black")
    line.place(x=0, y=205)

    m_label2 = Label(window, text="Gauss Jordan Method",
                     bg="#5a92bf", fg="#e4ebf2", font=(15))
    m_label2.place(x=245, y=240)

    uknowns_label2 = Label(
        window, text="Enter number of equations.", bg="#cad9ea", fg="black")
    uknowns_label2.place(x=85, y=320)

    unknownsEntry2 = Entry(window, width=15, bg="#e4ebf2", borderwidth=.5)
    unknownsEntry2.place(x=245, y=320)

    equations_label2 = Label(
        window, text="Enter your equations separated by a comma.", bg="#cad9ea", fg="black")
    equations_label2.place(x=85, y=375)

    equEntry2 = Entry(window, width=90, bg="#e4ebf2", borderwidth=.5)
    equEntry2.place(x=80, y=400)
    line = Label(window,
                 text="--------------------------------------------------------------------------------------------------------------------------------------------",
                 bg="#cad9ea", fg="black")
    line.place(x=0, y=450)

    def solve_all():
        output_win = Tk()
        output_win.title("Equations Result")
        output_win.configure(bg="#cad9ea")
        output_win.geometry("850x450")

        results = Label(
            output_win, text="RESULTS", bg="green", fg="black")
        results.place(x=400, y=15)

        output = Text(output_win, width=80, height=8.5,
                      wrap=WORD, background="#e4ebf2")
        output.place(x=100, y=50)
        output2 = Text(output_win, width=80, height=8.5,
                       wrap=WORD, background="#e4ebf2")
        output2.place(x=100, y=205)

        unknownsNoField = unknownsEntry.get()
        equationField = equEntry.get()
        output.delete(0.0, END)
        output.insert(END, '**Gauss Elimination**\n\n')
        output.insert(END, GaussianElimination(
            int(unknownsNoField), equationField))

        unknownsNoField = unknownsEntry2.get()
        equationField = equEntry2.get()
        output2.delete(0.0, END)
        output2.insert(END, '**Gauss Jordan**\n\n')
        output2.insert(END, gauss_jordan(int(unknownsNoField), equationField))

    solve_btn = Button(window, text="Solve All", width=20, height=1,
                       bg="#ff9732", fg="black", command=solve_all)
    solve_btn.place(x=280, y=520)
