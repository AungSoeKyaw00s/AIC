#imports
from tkinter import *
from PIL import *

#run tkinter
app = Tk()

# Code to add widgets will go here...
app.geometry("500x300")
app.title("Automatic Item Checkout")

Label1 = Label(app, text = "Welcome to the smart checkout!", font=("Times", "20"))
Label2 = Label(app, text = "Card Only!", font=("Times", "18", "bold"))


def newWindow():
    app.destroy()
    import sample2

Label1.pack()
Label2.pack()
button1 = Button(app, padx= "10", text = "sample2", command=newWindow)
button1.pack()

app.mainloop()