#imports
from tkinter import *
from PIL import ImageTk, Image

#run tkinter
app = Tk()

# Code to add widgets will go here...
#app.geometry("500x300")
app.title("Automatic Item Checkout")
app.configure(bg='white')


Label1 = Label(app, text = "Welcome to the Automatic Item Checkout!", font=("Times", "20"), background='white')
Label2 = Label(app, text = "Card Only!", font=("Times", "18", "bold"), background='white')
image = Image.open("guiimg/trolley.png")

# Reszie the image using resize() method
resize_image = image.resize((100, 100))
  
img = ImageTk.PhotoImage(resize_image)
  
# create label and add resize image
label3 = Label(image=img)
label3.image = img
   
def newWindow():
    app.destroy()
    import page2

label3.grid(row=0, column=0, padx= 25)
Label1.grid(row=1, column=0)
Label2.grid(row=2, column=0)
button1 = Button(app, padx= "10", text = "Enter", command=newWindow)
button1.grid(row=3, column=0, padx= 25, pady= 25, columnspan=5)

app.mainloop()