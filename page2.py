#imports
from tkinter import *
import cv2
#from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import pandas as pd
import torch
import requests
import tqdm
import torchvision
import yaml
import seaborn
import os

#run tkinter
app = Tk()

app.geometry("500x300")
app.title("Automatic Item Checkout")

LabelOpenImg = Label(text = "Click to start scanning.", font=("Times", 10))
Labelspace = Label(text="Please scan your items below", font=("Times", 15))
ResultLabel = Label(text = "Items:", font=("Arial Bold", 10))
imagebar = Image.open("guiimg/barcode.jpg")
  
foto = ImageTk.PhotoImage(imagebar.resize((150, 100)))
  
# create label and add resize image


labelbar = Label(image=foto)
labelbar.image = foto

#Deep learning section

#PyTorch
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')
model.eval()

# Open Image Function using OpenCV
def openImg(filename):
    # Open the image using OPENCV
    img = cv2.imread(filename)
    return img

def BttnScan_func():
    # Use the File Dialog component to Open the Dialog box to select files
    file = filedialog.askopenfilename(filetypes = (("Images files","*.jpg"),("Video Files","*.mp4"),("all files","*.*")))
    # Passing the file to openImg method to show is using opencv (imread, imshow)
    results = model(openImg(file))  # inference
    ResultLabel.config(text = results.print())
    results.show()
    


def newWindow():
    app.destroy()
    import page3

ScanBttn = Button(text="Scan", command=BttnScan_func)
ScanBttn.config(width=15)
nextBtn = Button(text="Checkout", command=newWindow)

#openProcess = Button(text="Process Image", command=BttnProcess_Clicked)
#openProcess.config(width=15)

#Grid system
Labelspace.grid(row=0, column=0)
labelbar.grid(row=0, column=1,padx = 25, pady= 10)
LabelOpenImg.grid(row=1, column=0, padx= 25, pady= 10)

ScanBttn.grid(row=1, column=1, padx= 25)

ResultLabel.grid(row=2,column=0, padx= 25,pady= 20)

nextBtn.grid(row=3,column=1, padx= 25,pady= 20)


app.mainloop()