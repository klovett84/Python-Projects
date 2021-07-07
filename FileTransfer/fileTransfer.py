import shutil
import os
import datetime
from datetime import timedelta
from tkinter import *
from tkinter import filedialog as fd

# set the source folder to user's selection
def selectSource():
    source = fd.askdirectory()
    sourceBox.insert(0,source)

#set the destination folder to user's selection
def selectDestination():
    destination = fd.askdirectory()
    destinationBox.insert(0,destination)

# transfer files from source to destination if modified within last 24 hours
def transferFiles():
    # set current time and the time 24 hours ago
    now = datetime.datetime.now()
    last24hours = now - timedelta(hours = 24)

    sourceFolder = sourceBox.get() + "/"
    destinationFolder = destinationBox.get()
    # create a tuple of filepaths from source
    files = os.listdir(sourceFolder)

    for i in files:
        modificationTime = datetime.datetime.utcfromtimestamp(os.path.getmtime(sourceFolder+i))
        if modificationTime > last24hours:
            shutil.move(sourceFolder+i, destinationFolder)


win = Tk()
win.title("File Transfer")
win.minsize(500, 260)
win.resizable(False, False)

desc = Message(win, width=450, justify=LEFT, text="Move all files from the source folder that have been modified within the last 24 hours to the destination folder.")

sourceLabel = Label(win, text="Source folder:")
sourceBrowse = Button(win, text="Browse...", command=selectSource, width=13)
sourceBox = Entry(win, width=52)

destinationLabel = Label(win, text="Destination folder:")
destinationBrowse = Button(win, text="Browse...", command=selectDestination, width=13)
destinationBox = Entry(win, width=52)

transfer = Button(win, text="Transfer files", command=transferFiles, width=13)

#### GUI GRID ####
desc.grid(row=0, column=0, columnspan=2, padx=10, pady=(20,0), sticky=W)

sourceLabel.grid(row=1, column=0, padx=10, pady=(10,0), sticky=W)
sourceBrowse.grid(row=2, column=0, padx=10, pady=(0,10))
sourceBox.grid(row=2, column=1, padx=10, pady=(0,10))

destinationLabel.grid(row=3, column=0, padx=10, pady=(10,0), sticky=W)
destinationBrowse.grid(row=4, column=0, padx=10, pady=(0,20))
destinationBox.grid(row=4, column=1, padx=10, pady=(0,20))

transfer.grid(row=5,column=1, padx=10, pady=(0,20), ipady=8, sticky=E)


