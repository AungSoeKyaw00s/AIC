#imports
from tkinter import *
from PIL import ImageTk, Image

#run tkinter
app = Tk()

# Code to add widgets will go here...
app.geometry("500x300")
app.title("Automatic Item Checkout")

Label1 = Label(app, text = "Welcome to the smart checkout!", font=("Times", "20"))
Label2 = Label(app, text = "Card Only!", font=("Times", "18", "bold"))
image = Image.open("guiimg\_Barcode_32896.jpg")

# Reszie the image using resize() method
resize_image = image.resize((100, 50))
  
img = ImageTk.PhotoImage(resize_image)
  
# create label and add resize image
label3 = Label(image=img)
label3.image = img
  
def newWindow():
    app.destroy()
    import sample2

Label1.pack()
label3.pack()
Label2.pack()
button1 = Button(app, padx= "10", text = "Enter", command=newWindow)
button1.pack()

app.mainloop()