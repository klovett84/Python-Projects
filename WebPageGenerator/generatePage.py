from tkinter import *
import webbrowser

# this function first generates an HTML page,
# then takes the text input from enterText and inserts it into
# the <h1> wildcard.
# after that, it opens the file in the web browser

def createPage():
    bodyText = enterText.get()
    
    page = open("page.html", "w")
    page.write("""<html>
                    <head>
                        <title>Web Page Generator</title>
                    </head>
                    <body>
                        <h1>{}</h1>
                    </body>
                  </html>""".format(bodyText))
    page.close()
    webbrowser.open("page.html")

# GUI configuration
win = Tk()
win.title("Web Page Generator")

textLabel = Label(win, text="Enter web page body text:")
enterText = Entry(win, width=50)
# this button calls createPage() when clicked
setText = Button(win, text="Set body text", command=createPage)

textLabel.grid(row=0, column=0, padx=10, pady=(10,0), sticky=W)
enterText.grid(row=1, column=0, padx=10, pady=(0,10))
setText.grid(row=1, column=2, padx=10, pady=(0,10))
