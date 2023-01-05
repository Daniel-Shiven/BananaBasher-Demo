import threading
import time
        #Import Packets
from tkinter import *
from tkinter.tix import *
from tkinter import ttk
from PIL import Image, ImageTk

#----Variables----#
global bananas
bananas = 0

global bps
bps = 0


#Shop
global monkeyAmount
monkeyAmount = 0
global monkeyPrice
monkeyPrice = 50
global monkeyIncome
monkeyIncome = 0

global farmAmount
farmAmount = 0
global farmPrice
farmPrice = 550
global farmIncome
farmIncome = 0

global plantAmount
plantAmount = 0
global plantPrice
plantPrice = 7200
global plantIncome
plantIncome = 0

global complexAmount
complexAmount = 0
global complexPrice
complexPrice = 82000
global complexIncome
complexIncome = 0


#Upgrades
global clickMultiplier
clickMultiplier = 1

global doubleTapPrice
doubleTapPrice = 100
global doubleTapStatus
doubleTapStatus = False

global tripleTapPrice
tripleTapPrice = 1000
global tripleTapStatus
tripleTapStatus = False

        

def main():

    #Set up screen
    root = Tk()
    root.title("Banana Basher")


    def updateBanana():
        global bananas
        bananaCount.config(text=(str(bananas)+" Bananas"))
        root.after(1000,updateBanana)


    #----Functions!----#
    def clickBanana():
        global bananas
        bananas = bananas+(1*clickMultiplier)
        bananaCount.config(text=(str(bananas)+" Bananas"))
        print("Banana (Post Click): "+str(bananas) )


#--------------------SHOP--------------------#

    def purchaseAnShop(amount,price,income,type):
        global bananas
        
        if bananas >= price:
            bananas = bananas-price

            price = round(price*1.15) #Increase the price
            amount = amount+1 #Increaes the amount
            if amount != 1: #1 4 30 165
                income = income*1.15 #Increase the income
            
            #IF IT IS A MONKEY
            if type == "monkey":
                global monkeyPrice
                global monkeyAmount
                global monkeyIncome
                if amount == 1:
                    income = 1

                monkeyPrice = price #Sets Price
                monkeyAmount = amount #Sets amount
                monkeyIncome = income #Sets income
                print(monkeyIncome)

                monkeyLevel.config(text=(f"Monkey: Level {monkeyAmount}")) #For Generators

                monkeyPurchase.config(text=(f"Monkey: {monkeyAmount}\n{monkeyPrice} Bananas"))
            
            #IF IT IS A FARM
            if type == "farm":
                #Calling in the variables as global
                global farmPrice
                global farmAmount
                global farmIncome
                if amount == 1:
                    income = 4

                farmPrice = price #Sets Price
                farmAmount = amount #Sets amount
                farmIncome = income #Sets income

                farmLevel.config(text=(f"Farm: Level {monkeyAmount}")) #Display the displayed generator level

                farmPurchase.config(text=(f"Farm: {farmAmount}\n{farmPrice} Bananas")) #Set the displayed shop level
            
            #IF IT IS A PLANTATION
            if type == "plant":
                #Calling in the variables as global
                global plantPrice
                global plantAmount
                global plantIncome
                if amount == 1:
                    income = 30

                plantPrice = price #Sets Price
                plantAmount = amount #Sets amount
                plantIncome = income #Sets income

                plantLevel.config(text=(f"Farm: Level {monkeyAmount}")) #Display the displayed generator level

                plantPurchase.config(text=(f"Farm: {farmAmount}\n{farmPrice} Bananas")) #Set the displayed shop level
            
            #IF IT IS AN INDUSTRIAL COMPLEX
            if type == "complex":
                #Calling in the variables as global
                global complexPrice
                global complexAmount
                global complexIncome
                if amount == 1:
                    income = 165

                complexPrice = price #Sets Price
                complexAmount = amount #Sets amount
                complexIncome = income #Sets income

                complexLevel.config(text=(f"Farm: Level {complexAmount}")) #Display the displayed generator level

                complexPurchase.config(text=(f"Farm: {complexAmount}\n{complexPrice} Bananas")) #Set the displayed shop level
        


#--------------------UPGRADES--------------------#
    def doubleTapActivate():
        global doubleTapPrice
        global clickMultiplier
        global doubleTapStatus
        global bananas

        if bananas >= doubleTapPrice and doubleTapStatus == False:
            print("DoubleTap Purchased")
            bananas = bananas-doubleTapPrice
            clickMultiplier = clickMultiplier*2
            doubleTapStatus = True
            doubleTap.destroy()
            doubleTapBorder.destroy()


    def tripleTapActivate():
        global tripleTapPrice
        global clickMultiplier
        global tripleTapStatus
        global bananas

        if bananas >= tripleTapPrice and tripleTapStatus == False:
            print("TripleTap Purchased")
            bananas = bananas-tripleTapPrice
            clickMultiplier = clickMultiplier*3
            tripleTapStatus = True
            tripleTap.destroy()
            tripleTapBorder.destroy()
            






    #--------------------------------------------LEFT---------------------------------------------------#


    #-----Create Canvas-----#
    cc = Canvas(root,height=600,width=300)
    cc.grid(column=0,row=0)
    root.grid_rowconfigure(0, weight=1)

    #---Create banana Image + Button---#

    #Image  
    img = Image.open("banana1.png")
    resized_img = img.resize((250, 250))
    banana1 = ImageTk.PhotoImage(resized_img)

    #Creating button, and adding it to the window
    click_banana = Button(root,image=banana1,command=clickBanana,borderwidth=0)
    cc.create_window(150, 300, window=click_banana)


    #---Create bananas Count---#
    bananaCount = Label(root, text=(str(bananas)+" Bananas"),font=('Comic Sans MS',20,'bold'))

    cc.create_window(150,150,window=bananaCount)

    #---Create Separator---#
    sep1 = ttk.Separator(root, orient='vertical')
    sep1.grid(row=0,column=1, sticky='ns')
    root.grid_columnconfigure(1, weight=1)




    #--------------------------------------------MIDDLE---------------------------------------------------#




    #-----Create Generator Canvas-----#
    generators = Canvas(root,width=500,height=600)
    generators.grid(row=0,column=2)



    #----------CREATE MONKEY----------#
    img = Image.open('Buildings/monkey.png')
    resized_img = img.resize((50,50))
    monkeyImg = ImageTk.PhotoImage(resized_img)


    #---Create monkey canvas---#
    monkeyShopColor = '#785f5f'
    monkeyShop = Canvas(root,width=500,height=150,bg=monkeyShopColor) #Create monkey Canvas
    generators.create_window(0,75,window=monkeyShop,anchor='w') #Add monkey Canvas to Generators Canvas

    #Create monkey level counter
    monkeyLevel = Label(root, text="Monkey: Level 0",anchor='w',font=('Comic Sans MS',14,'bold'),bg=monkeyShopColor)
    monkeyShop.create_window(2,2,window=monkeyLevel,anchor='nw') #Add counter to the canvas



    #----------CREATE FARM----------#
    img = Image.open('Buildings/farm.png')
    resized_img = img.resize((50,50))
    farmImg = ImageTk.PhotoImage(resized_img)


    #---Create Farm canvas---#
    farmShopColor = '#785f5f' #Establish the shop and levels buttons
    farmShop = Canvas(root,width=500,height=150,bg=farmShopColor) #Create Farm Canvas
    generators.create_window(0,225,window=farmShop,anchor='w') #Add Farm Canvas to Generators Canvas

    #Create Farm level counter
    farmLevel = Label(root, text="Farm: Level 0",anchor='w',font=('Comic Sans MS',14,'bold'),bg=farmShopColor)
    farmShop.create_window(2,2,window=farmLevel,anchor='nw') #Add counter to the canvas



    #----------CREATE PLANTATION----------#
    img = Image.open('Buildings/plant.png')
    resized_img = img.resize((50,50))
    plantImg = ImageTk.PhotoImage(resized_img)


    #---Create Plantation  canvas---#
    plantShopColor = '#785f5f' #Establish the shop and levels buttons
    plantShop = Canvas(root,width=500,height=150,bg=plantShopColor) #Create plantation Canvas
    generators.create_window(0,375,window=plantShop,anchor='w') #Add plantation Canvas to Generators Canvas

    #Create Plantation level counter
    plantLevel = Label(root, text="Plantation: Level 0",anchor='w',font=('Comic Sans MS',14,'bold'),bg=plantShopColor)
    plantShop.create_window(2,2,window=plantLevel,anchor='nw') #Add counter to the canvas


    #---Create Separator---#
    sep2 = ttk.Separator(root, orient='vertical')
    sep2.grid(row=0,column=3, sticky='ns')
    root.grid_columnconfigure(3, weight=1)



    #----------CREATE INDUSTRIAL COMPLEX----------#
    img = Image.open('Buildings/complex.png')
    resized_img = img.resize((50,50))
    complexImg = ImageTk.PhotoImage(resized_img)


    #---Create Industrial Complex canvas---#
    complexShopColor = '#785f5f' #Establish the industrial complex and levels buttons
    complexShop = Canvas(root,width=500,height=150,bg=complexShopColor) #Create Industrial Complex Canvas
    generators.create_window(0,525,window=complexShop,anchor='w') #Add Industrial Complex Canvas to Generators Canvas

    #Create Industrial Complex level counter
    complexLevel = Label(root, text="Industrial Complex: Level 0",anchor='w',font=('Comic Sans MS',14,'bold'),bg=complexShopColor)
    complexShop.create_window(2,2,window=complexLevel,anchor='nw') #Add counter to the canvas


    #---Create Separator---#
    sep2 = ttk.Separator(root, orient='vertical')
    sep2.grid(row=0,column=3, sticky='ns',rowspan=2)
    root.grid_columnconfigure(3, weight=1)




    #---------------------------------------------RIGHT (SHOP)--------------------------------------------------#




    #-----Create Shop Canvas-----#

    shopWidth = 300
    shop = Canvas(root,width=shopWidth,height=600)
    shop.grid(row=0,column=4)




    #----------CREATE SHOP MONKEY----------#
    monkeyShopColor = '#9eb3b5'

    #Add monkey Button
    image = Image.open('Buildings/monkey.png')
    img = image.resize((50,50))
    monkeyImg = ImageTk.PhotoImage(img)

    monkeyPurchase = Button(root,
    text=(f"Monkey: {monkeyAmount}\n{monkeyPrice} Bananas"),font=('Comic Sans MS',14,'bold'),
    justify=LEFT,
    anchor='w',
    image=monkeyImg,
    compound=LEFT,
    bg=monkeyShopColor,
    width=shopWidth,
    height=60,
    command=lambda: purchaseAnShop(monkeyAmount,monkeyPrice,monkeyIncome,"monkey")) #Create monkey level counter
    
    shop.create_window(0,35,window=monkeyPurchase,anchor='w') #Add monkey Shop Canvas to overall Shop Canvas



    #----------CREATE SHOP FARM----------#
    farmShopColor = '#9eb3b5'

    #Add Farm Button
    image = Image.open('Buildings/farm.png')
    resized_img = image.resize((50,50))
    farmImg = ImageTk.PhotoImage(resized_img)

    farmPurchase = Button(root, 
    text=(f"Farm: {farmAmount}\n{farmPrice} Bananas"),font=('Comic Sans MS',14,'bold'),
    justify=LEFT,
    image=farmImg,
    compound=LEFT,
    anchor="w",
    bg=monkeyShopColor,
    width=shopWidth,
    height=60,
    command=lambda: purchaseAnShop(monkeyAmount,monkeyPrice,monkeyIncome,"monkey")) #Create monkey level counter) #Create monkey level counter    shop.create_window(0,100,window=farmPurchase,anchor='w') #Add farm Shop Canvas to overall Shop Canvas

    shop.create_window(0,105,window=farmPurchase,anchor='w') #Add monkey Shop Canvas to overall Shop Canvas



    #----------CREATE SHOP PLANTATION----------#
    plantShopColor = '#9eb3b5'

    #Add Farm Button
    image = Image.open('Buildings/plant.png')
    resized_img = image.resize((50,50))
    plantImg = ImageTk.PhotoImage(resized_img)

    plantPurchase = Button(root,
    text=(f"Plantation: {plantAmount}\n{plantPrice} Bananas"),font=('Comic Sans MS',14,'bold'),
    justify=LEFT,
    image=plantImg,
    compound=LEFT,
    anchor='w',
    bg=plantShopColor,
    width=shopWidth,
    height=60,
    command=lambda: purchaseAnShop(monkeyAmount,monkeyPrice,monkeyIncome,"monkey")) #Create monkey level counter) #Create Plantation level counter

    shop.create_window(0,175,window=plantPurchase,anchor='w') #Add plantation Shop Canvas to overall Shop Canvas



    #----------CREATE SHOP INDUSTRIAL COMPLEX----------#
    complexShopColor = '#9eb3b5'

    #Add Farm Button
    image = Image.open('Buildings/complex.png')
    resized_img = image.resize((50,50))
    complexImg = ImageTk.PhotoImage(resized_img)

    complexPurchase = Button(root,
    text=(f"Industrial Complex: {complexAmount}\n{complexPrice} Bananas"),font=('Comic Sans MS',14,'bold'),
    justify=LEFT,
    image=complexImg,
    compound=LEFT,
    anchor='w',
    bg=complexShopColor,
    width=shopWidth,
    height=60,
    command=lambda: purchaseAnShop(monkeyAmount,monkeyPrice,monkeyIncome,"monkey")) #Create monkey level counter) #Create Industrial Complex level counter
    shop.create_window(0,245,window=complexPurchase,anchor='w') #Add Industrial Complex Shop Canvas to overall Shop Canvas


    #---------------------------------------------RIGHT (UPGRADES)--------------------------------------------------#
    

    #-----CREATE UPGRADE CANVAS-----#
    upgradesColor = "#4e4f87" #Sets the background color for the upgrades Canvas

    upgradeHeight = 275

    upgrades = Canvas(root,width=shopWidth,height=upgradeHeight,bg=upgradesColor) #Creates the upgrades Canvas 
    shop.create_window(0,275,window=upgrades,anchor='nw') #Places the canvas on the shop

    upgradesLabel = Label(root,text="Hover over an upgrade to\nview its benefits",
    justify = CENTER,
    font=('Comic Sans MS',14,'bold'),
    anchor='c',
    bg=upgradesColor) #Top Part
    upgrades.create_window(shopWidth/2,10,window=upgradesLabel,anchor='n')

    #Establishes a background color for all the upgrades
    upgradeBorderColor = "#a14c3f"


    #-----HORIZONTAL LINE-----#
    upgrades.create_line(0, 4, shopWidth+2, 4, fill='#964B00', width=4) #Top Line
    upgrades.create_line(0, 72, shopWidth+2, 72, fill='#964B00', width=2)# Middle Line

    upgrades.create_line(
    4, 0,
    4, upgradeHeight,
    fill='#964B00', width=4) #Left Line

    upgrades.create_line(
    shopWidth, 0,
    shopWidth, upgradeHeight,
    fill='#964B00', width=4) #Right Line

    upgrades.create_line(
    0, upgradeHeight,
    shopWidth+2, upgradeHeight,
    fill='#964B00', width=4) #Bottom Line



    #-----CREATE DOUBLE TAP-----#
    
    #Uploads the image
    image = Image.open('Upgrades/doubletap.png')
    resized_img = image.resize((48,48))
    doubletapImg = ImageTk.PhotoImage(resized_img)

    #Creates the button and the hover button
    doubleTapBorder = Canvas(root, bg=upgradeBorderColor,highlightbackground = upgradeBorderColor, highlightthickness = 2, bd=0,height=50,width=50)
    doubleTap = Button(root,image=doubletapImg,bg="black",borderwidth=0,activebackground="black",command=doubleTapActivate)

    doubleTapHover = Balloon(root)
    doubleTapHover.bind_widget(doubleTap,balloonmsg="DOUBLE TAP\nCost: 100 Bananas\nMouse is 2x Efficient")

    upgrades.create_window(7,74,anchor='nw',window=doubleTapBorder)
    upgrades.create_window(9,76,anchor='nw',window=doubleTap)



    #-----CREATE TRIPLE TAP-----#
    
    #Uploads the image
    image = Image.open('Upgrades/tripletap.png')
    resized_img = image.resize((48,48))
    tripleTapImg = ImageTk.PhotoImage(resized_img)

    #Creates the button and the hover button
    tripleTapBorder = Canvas(root, bg=upgradeBorderColor,highlightbackground = upgradeBorderColor, highlightthickness = 2, bd=0,height=50,width=50)
    tripleTap = Button(root,image=tripleTapImg,bg="black",borderwidth=0,activebackground="black",command=tripleTapActivate)

    tripleTapHover = Balloon(root)
    tripleTapHover.bind_widget(tripleTap,balloonmsg="TRIPLE TAP\nCost: 1000 Bananas\nMouse is 3x Efficient")

    upgrades.create_window(61,74,anchor='nw',window=tripleTapBorder)
    upgrades.create_window(63,76,anchor='nw',window=tripleTap)



    #----------Update banana Count + Tkinter operation loop---------#

    updateBanana()
    root.mainloop()


    


#--------------------------------------------------BananaUp--------------------------------------------------#
def bananaUp():
    global bananas
    global bps
    global monkeyIncome
    global farmIncome
    global plantIncome
    global complexIncome

    

    while 0 == 0:
        time.sleep(1)
        bps = monkeyIncome+farmIncome+plantIncome+complexIncome
        bananas = round(bananas+bps)
 
 
if __name__ =="__main__":
    # creating thread
    mainThread = threading.Thread(target=main)
    bananaThread = threading.Thread(target=bananaUp)
 
    # starting thread 1
    mainThread.start()
    bananaThread.start()


#-------------TESTING----------------#

#import time #POWER

##global startTime
#startTime = time.time()
#print(startTime)

#while 0 == 0:
    #time.sleep(1)
    #print(round((time.time()-startTime),2))