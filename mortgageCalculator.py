from tkinter import Label, Frame, Entry, Button, END


class Mortgage(Frame):
    "computes the monthly mortgage payment given in loan amount"

    def __init__(self, parent=None):
        "Contructor"
        Frame.__init__(self, parent)
        Mortgage.make_widget(self)
        self.pack()
        self.grid()

    def make_widget(self):
        Label(self, text='Loan Amount: ').grid(row=0, column=0)
        Label(self, text='Intrest Rate: ').grid(row=1, column=0)
        Label(self, text='Loan Terms: ').grid(row=2, column=0)

        self.P = Entry(self)
        self.P.grid(row=0, column=1)

        self.iRate = Entry(self)
        self.iRate.grid(row=1, column=1)

        self.terms = Entry(self)
        self.terms.grid(row=2, column=1)

        self.mortgage = Entry(self)
        self.mortgage.grid(row=3, column=1)

        Button(self, text="Compute Morgage ", command=self.calculate).grid(row=3, column=0)

    def calculate(self):
        "calculates formulas"

        a = eval(self.P.get())
        r = eval(self.iRate.get())
        t = eval(self.terms.get())
        # m = eval(self.mortgage.get())

        c = r / 1200
        m = a * (c * (1 + c) ** t) / ((1 + c) ** t - 1)
        self.mortgage.delete(0, END)
        self.mortgage.insert(END, m)


Mortgage()
