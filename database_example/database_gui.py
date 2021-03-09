from database import *
from tkinter import *


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.grid(padx=20, pady=20)
        Label(master, text="Database for persons").grid(row=0, column=0)
        Label(master, text="").grid(row=0, column=1)

        Label(master, text="Name").grid(row=1)
        Label(master, text="Forename").grid(row=2)

        self.sname = Entry(master)
        self.fname = Entry(master)

        Button(master, text='Entry DB', width=20, command=self.action).grid(row=3, column=0, sticky=W, pady=4)
        Button(master, text='Cancel', width=20, command=root.destroy).grid(row=3, column=1, sticky=W, pady=4)

        self.sname.grid(row=1, column=1)
        self.fname.grid(row=2, column=1)
        self.display = Text(master, height=4, width=40)
        self.status = Label(master, text="")
        self.status.grid(row=6, columnspan=2)

        db = DB()

        self.status['text'] = db.initDB()
        result = db.readDB()
        self.display.insert(END, result[0])
        self.display.grid(row=4, columnspan=2)
        self.display.configure(state='disabled')
        self.dataset = Label(master, text="")
        self.dataset.grid(row=5, columnspan=2)
        self.dataset['text'] = "Count of datasets: " + result[1]

    def action(self):
        db = DB()
        self.status['text'] = ""
        db.writeDB(self.sname.get(), self.fname.get())
        self.display.configure(state='normal')
        result = db.readDB()
        self.display.delete(1.0, END)
        self.display.insert(END, result[0])
        self.display.configure(state='disabled')
        self.dataset['text'] = "Count of datasets: " + result[1]

root = Tk()
app = Application(master=root)
app.mainloop()
