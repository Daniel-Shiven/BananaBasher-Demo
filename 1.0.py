#Import Packets
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


root = Tk()

farmAmount = 0
farmPrice = 500

#"Farm: "+str(farmAmount)+"\n"+str(farmPrice)+" Cookies")

#Add monkey Button
image = Image.open('farm.png')
resized_img = image.resize((50,50))
farmImg = ImageTk.PhotoImage(resized_img)

purchaseFarm = Button(root,
text=(" Farm: "+str(farmAmount)+"     \n"+str(farmPrice)+" Cookies"),
font=('Comic Sans MS',14,'bold'),
image=farmImg,
compound=LEFT,
anchor="c",
width=275,
height=60)
purchaseFarm.pack()

root.mainloop()