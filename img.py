# importing the tkinter module and PIL that
# is pillow module
from tkinter import *
from PIL import ImageTk, Image



# Calling the Tk (The intial constructor of tkinter)
root = Tk()

# We will make the title of our app as Image Viewer
root.title("Image Viewer")

# The geometry of the box which will be displayed
# on the screen
root.geometry("700x700")

# Adding the images using the pillow module which
# has a class ImageTk We can directly add the
# photos in the tkinter folder or we have to
# give a proper path for the images
image_no_1 = ImageTk.PhotoImage(Image.open("guiimg/image_1122.jpg"))

label = Label(image=image_no_1)

# We have to show the the box so this below line is needed
label.grid(row=1, column=0, columnspan=3)


# root.quit for closing the app
button_exit = Button(root, text="Exit",
					command=root.quit)


# grid function is for placing the buttons in the frame
#button_back.grid(row=5, column=0)
button_exit.grid(row=5, column=1)
#button_forward.grid(row=5, column=2)

root.mainloop()
