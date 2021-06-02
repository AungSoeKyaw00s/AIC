#imports
from tkinter import *
from PIL import ImageTk, Image

#run tkinter
app = Tk()

# Code to add widgets 
#app.geometry("500x300")
app.title("Automatic Item Checkout")
app.configure(bg='white')

Label1 = Label(app, text = "Thank you for using Automatic Item Checkout!", font=("Times", "20"), background='white')
Label2 = Label(app, text = "Click the button below for the new checkout", font=("Times", "18"), background='white')


def newWindow():
    app.destroy()
    import page1

button1 = Button(app, padx= "10", text = "Start", command=newWindow)

Label1.grid(row=1, column=0, padx= 25, pady= 25)
Label2.grid(row=2, column=0, padx= 25)
button1.grid(row=3, column=0, padx= 25, pady= 25, columnspan=5)

app.mainloop()