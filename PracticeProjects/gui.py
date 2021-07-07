from tkinter import *
from tkinter import filedialog as fd

def selectFile1():
    folder1 = fd.askdirectory()
    browseBox1.insert(0,folder1)

def selectFile2():
    folder2 = fd.askdirectory()
    browseBox2.insert(0,folder2)


win = Tk()
win.title("Check files")
win.minsize(480, 170)
win.maxsize(480, 170)

browse1 = Button(win, text="Browse...", command=selectFile1, width=13)
browse2 = Button(win, text="Browse...", command=selectFile2, width=13)
check = Button(win, text="Check for files...", width=13)
close = Button(win, text="Close Program")
browseBox1 = Entry(win, width=52)
browseBox2 = Entry(win, width=52)


browse1.grid(row=0, column=0, padx=10, pady=(40,0))
browseBox1.grid(row=0, column=1, padx=(20,15), pady=(40,0), sticky=E)
browse2.grid(row=1, column=0, padx=10, pady=(10,0))
browseBox2.grid(row=1, column=1, padx=(20,15), pady=(10,0), sticky=E)
check.grid(row=2, column=0, ipady=8, pady=(10,0))
close.grid(row=2, column=1, ipady=8, pady=(10,0), padx=(0,15), sticky=E)
