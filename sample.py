#imports
from tkinter import *


#run tkinter
app = Tk()

# Code to add widgets will go here...
app.geometry("500x300")
app.title("Automatic Item Checkout")

def newWindow():
    app.destroy()
    import sample2

button1 = Button(app, text = "sample2", command=newWindow)
button1.pack()

app.mainloop()