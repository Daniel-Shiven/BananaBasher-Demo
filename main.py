#Import Packets
from tkinter import *
from tkinter.tix import *
from tkinter import ttk
from PIL import Image, ImageTk
import time

#----Variables----#

#Clicking
bananas = 0 #Banana Count
bps = 0 #Bananas per Second
clickMultiplier = 1 #Click Multiplier

#Shop
monkeyAmount = 0 #Amount of Monkeys
monkeyPrice = 50 #Price of Monkey
monkeyIncome = 0 #Stores the bps for Monkeys
monkeyMultiplier = 1 #Income Multiplier

farmAmount = 0 #Amount of Farm
farmPrice = 550 #Price of Farm
farmIncome = 0 #Stores the bps for Farm
farmMultiplier = 1 #Income Multiplier

plantAmount = 0 #Amount of Plantation
plantPrice = 7200 #Price of Plantation 
plantIncome = 0 #Stores the bps for Plantation
plantMultiplier = 1 #Income Multiplier

complexAmount = 0 #Amount of Industrial Complexes
complexPrice = 82000 #Price of Industrial Complexes
complexIncome = 0 #Stores the bps for Industrial Complexes
complexMultiplier = 1 #Income Multiplier


#Upgrades
# '' - Not Unlocked
# False - Unlocked, but not purchased
# True - Purchased

availableUpgrades = 1 #Available upgrades (for formatting)

doubleTapPrice = 100 #Price of doubleTap
doubleTapStatus = False #Status of double Tap

tripleTapPrice = 1000 #Price of tripleTap
tripleTapStatus = '' #Status of tripleTap

butterFlyPrice = 5000 #Price of butterfly clicking
butterFlyStatus = '' #Status of butterfly clicking

chimpPrice = 500 #Price of Chimp
chimpStatus = '' #Status of Chimp

harambePrice = 2500 #Price of Harambe
harambeStatus = '' #Status of Harambe

betterHoePrice = 2300 #Price of BetterHoes
betterHoeStatus = '' #Status of betterHoes

#----Variables----#
root = Tk()
root.title("Banana Basher")
root.resizable(False,False)




#--------------------------------------------FUNCTIONS---------------------------------------------------#



#--------------------Updating the Banana Count--------------------#

def updateBanana():

    global bananas
    global bps

    global monkeyIncome
    global monkeyMultiplier

    global farmIncome
    global farmMultiplier

    global plantIncome
    global complexIncome

    
    bps = (monkeyIncome*monkeyMultiplier)+(farmIncome*farmMultiplier)+plantIncome+complexIncome
    bpsCounter.config(text=(f"BPS: {round(bps,1)}"),font=('Comic Sans MS',14,'bold'))

    bananas = bananas+(bps/10)
    
    bananaDisplay = round(bananas)
    bananaCount.config(text=(f"{bananaDisplay} Bananas"))
    root.after(100,updateBanana)


#Clicking the Banana
def clickBanana():
    global bananas
    bananas = bananas+(1*clickMultiplier)

    bananaDisplay = round(bananas)
    bananaCount.config(text=f"{bananaDisplay} Bananas")
    print("Banana (Post Click): "+str(bananaDisplay) )





#--------------------SHOP--------------------#

#Purchase an Item
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
            global xMonkey
            global yMonkey
            if amount == 1:
                income = 1

            monkeyPrice = price #Sets Price
            monkeyAmount = amount #Sets amount
            monkeyIncome = income #Sets income
            print(monkeyIncome)

            monkeyLevel.config(text=(f"Monkey: Level {monkeyAmount}")) #For middleWidth
            monkeyPurchase.config(text=(f"Monkey: {monkeyAmount}\n{monkeyPrice} Bananas"))
            if monkeyAmount % 15 == 0: #new row
                xMonkey = 1
                if yMonkey !=3:
                    yMonkey = yMonkey + 1
            elif monkeyAmount == 1: #first time
                xMonkey = 1
                yMonkey = 1
            else:
                xMonkey = xMonkey + 1
            monkeyShop.create_image(-5+(35*xMonkey)+(yMonkey*3),35+(30*yMonkey),image=monkeyImg)
        
        #IF IT IS A FARM
        if type == "farm":
            #Calling in the variables as global
            global farmPrice
            global farmAmount
            global farmIncome
            global xFarm
            global yFarm
            if amount == 1:
                income = 4

            farmPrice = price #Sets Price
            farmAmount = amount #Sets amount
            farmIncome = income #Sets income
            print(farmIncome)

            farmLevel.config(text=(f"Farm: Level {farmAmount}")) #Display the displayed generator level
            farmPurchase.config(text=(f"Farm: {farmAmount}\n{farmPrice} Bananas")) #Set the displayed shop level
            if farmAmount % 15 == 0: #new row
                xFarm = 1
                if yFarm !=3:
                    yFarm = yFarm + 1
            elif farmAmount == 1: #first time
                xFarm = 1
                yFarm = 1
            else:
                xFarm = xFarm + 1
            farmShop.create_image(-5+(35*xFarm)+(yFarm*3),35+(30*yFarm),image=farmImg)
        
        #IF IT IS A PLANTATION
        if type == "plant":
            #Calling in the variables as global
            global plantPrice
            global plantAmount
            global plantIncome
            global xPlant
            global yPlant
            if amount == 1:
                income = 30

            plantPrice = price #Sets Price
            plantAmount = amount #Sets amount
            plantIncome = income #Sets income
            print(plantIncome)

            plantLevel.config(text=(f"Plantion: Level {plantAmount}")) #Display the displayed generator level
            plantPurchase.config(text=(f"Plantation: {plantAmount}\n{plantPrice} Bananas")) #Set the displayed shop level
            if plantAmount % 15 == 0: #new row
                xPlant = 1
                if yPlant !=3:
                    yPlant = yPlant + 1
            elif plantAmount == 1: #first time
                xPlant = 1
                yPlant = 1
            else:
                xPlant = xPlant + 1
            plantShop.create_image(-5+(35*xPlant)+(yPlant*3),35+(30*yPlant),image=plantImg)
        
        #IF IT IS AN INDUSTRIAL COMPLEX
        if type == "complex":
            #Calling in the variables as global
            global complexPrice
            global complexAmount
            global complexIncome
            global xComplex
            global yComplex
            if amount == 1:
                income = 165

            complexPrice = price #Sets Price
            complexAmount = amount #Sets amount
            complexIncome = income #Sets income
            print(complexIncome)

            complexLevel.config(text=(f"Industrial Complex: Level {complexAmount}")) #Display the displayed generator level
            complexPurchase.config(text=(f"Industrial Complex: {complexAmount}\n{complexPrice} Bananas")) #Set the displayed shop level
            if complexAmount % 15 == 0: #new row
                xComplex = 1
                if yComplex !=3:
                    yComplex = yPlant + 1
            elif complexAmount == 1: #first time
                xComplex = 1
                yComplex = 1
            else:
                xComplex = xComplex + 1
            complexShop.create_image(-5+(35*xComplex)+(yComplex*3),35+(30*yComplex),image=complexImg)
    


#--------------------UPGRADES--------------------#


def rearrangeUpgrades():
    global upgradeBorderColor
    upgradesAmount = 0
    borderPosX = -46
    borderPosY = 74
    mainPosX = -44
    mainPosY = 76

        
    #Destroy All Upgrades
    global doubleTapStatus
    if doubleTapStatus == False:
        global doubleTap
        global doubleTapBorder
        global doubleTapHover
        doubleTap.destroy()
        doubleTapBorder.destroy()

    global chimpTapStatus
    if chimpStatus == False:
        global chimp
        global chimpBorder
        global chimpHover
        chimp.destroy()
        chimpBorder.destroy()

    global tripleTapStatus
    if tripleTapStatus == False:
        global tripleTap
        global tripleTapBorder
        global tripleTapHover
        tripleTap.destroy()
        tripleTapBorder.destroy()

    global betterHoeStatus
    if betterHoeStatus == False:
        global betterHoe
        global betterHoeBorder
        global betterHoeHover
        betterHoe.destroy()
        betterHoeBorder.destroy()
        
    global harambeStatus
    if harambeStatus == False:
        global harambe
        global harambeBorder
        global harambeHover
        harambe.destroy()
        harambeBorder.destroy()
        
    global butterFlyStatus
    if butterFlyStatus == False:
        global butterFly
        global butterFlyBorder
        global butterFlyHover
        butterFly.destroy()
        butterFlyBorder.destroy()
        

    if doubleTapStatus == False:    #Cost: 100
        upgradesAmount = upgradesAmount+1
        mainPosX = mainPosX+56
        borderPosX = borderPosX+56

        doubleTapBorder = Canvas(root, bg=upgradeBorderColor,highlightbackground = upgradeBorderColor, highlightthickness = 2, bd=0,height=58,width=58)
        doubleTap = Button(root,image=doubleTapImg,bg="black",borderwidth=0,activebackground="black",command=doubleTapActivate)
        doubleTapHover = Balloon(root)
        doubleTapHover.bind_widget(doubleTap,balloonmsg=(f"DOUBLE TAP \nCost: {doubleTapPrice} Bananas\nClicks are 2x Efficient"))

        upgrades.create_window(mainPosX,mainPosY,anchor='nw',window=doubleTap)
        upgrades.create_window(borderPosX,borderPosY,anchor='nw',window=doubleTapBorder)
    
    if chimpStatus == False: #Cost: 500
        upgradesAmount = upgradesAmount+1
        mainPosX = mainPosX+56
        borderPosX = borderPosX+56

        chimpBorder = Canvas(root, bg=upgradeBorderColor,highlightbackground = upgradeBorderColor, highlightthickness = 2, bd=0,height=58,width=58)
        chimp = Button(root,image=chimpImg,bg="black",borderwidth=0,activebackground="black",command=chimpActivate)
        chimpHover = Balloon(root)
        chimpHover.bind_widget(chimp,balloonmsg=(f"CHIMPANZEE \nCost: {chimpPrice} Bananas\nMonkeys are 2x efficient"))
        
        upgrades.create_window(mainPosX,mainPosY,anchor='nw',window=chimp)
        upgrades.create_window(borderPosX,borderPosY,anchor='nw',window=chimpBorder)
    
    if tripleTapStatus == False:    #Cost: 1000
        upgradesAmount = upgradesAmount+1
        mainPosX = mainPosX+56
        borderPosX = borderPosX+56

        tripleTapBorder = Canvas(root, bg=upgradeBorderColor,highlightbackground = upgradeBorderColor, highlightthickness = 2, bd=0,height=58,width=58)
        tripleTap = Button(root,image=tripleTapImg,bg="black",borderwidth=0,activebackground="black",command=tripleTapActivate)
        tripleTapHover = Balloon(root)
        tripleTapHover.bind_widget(tripleTap,balloonmsg=(f"TRIPLE TAP \nCost: {tripleTapPrice} Bananas\nClicks are 3x Efficient"))
        
        upgrades.create_window(mainPosX,mainPosY,anchor='nw',window=tripleTap)
        upgrades.create_window(borderPosX,borderPosY,anchor='nw',window=tripleTapBorder)
    
    if betterHoeStatus == False:    #Cost: 2300
        upgradesAmount = upgradesAmount+1
        mainPosX = mainPosX+56
        borderPosX = borderPosX+56

        betterHoeBorder = Canvas(root, bg=upgradeBorderColor,highlightbackground = upgradeBorderColor, highlightthickness = 2, bd=0,height=58,width=58)
        betterHoe = Button(root,image=betterHoeImg,bg="black",borderwidth=0,activebackground="black",command=betterHoeActivate)
        betterHoeHover = Balloon(root)
        betterHoeHover.bind_widget(betterHoe,balloonmsg=(f"BETTER HOES \nCost: {betterHoePrice} Bananas\nFarms are 2x efficient"))
        
        upgrades.create_window(mainPosX,mainPosY,anchor='nw',window=betterHoe)
        upgrades.create_window(borderPosX,borderPosY,anchor='nw',window=betterHoeBorder)
    
    if harambeStatus == False:    #Cost: 2500
        upgradesAmount = upgradesAmount+1
        mainPosX = mainPosX+56
        borderPosX = borderPosX+56

        harambeBorder = Canvas(root, bg=upgradeBorderColor,highlightbackground = upgradeBorderColor, highlightthickness = 2, bd=0,height=58,width=58)
        harambe = Button(root,image=harambeImg,bg="black",borderwidth=0,activebackground="black",command=harambeActivate)
        harambeHover = Balloon(root)
        harambeHover.bind_widget(harambe,balloonmsg=(f"HARAMBE \nCost: {harambePrice} Bananas\nMonkeys are 2x efficient"))
        
        upgrades.create_window(mainPosX,mainPosY,anchor='nw',window=harambe)
        upgrades.create_window(borderPosX,borderPosY,anchor='nw',window=harambeBorder)
    
    if butterFlyStatus == False:    #Cost: 5000
        upgradesAmount = upgradesAmount+1
        mainPosX = mainPosX+56
        borderPosX = borderPosX+56
        
        butterFly.destroy()
        butterFlyBorder.destroy()

        butterFlyBorder = Canvas(root, bg=upgradeBorderColor,highlightbackground = upgradeBorderColor, highlightthickness = 2, bd=0,height=58,width=58)
        butterFly = Button(root,image=butterFlyImg,bg="black",borderwidth=0,activebackground="black",command=butterFlyActivate)
        butterFlyHover = Balloon(root)
        butterFlyHover.bind_widget(butterFly,balloonmsg=(f"BUTTERFLY CLICKING \nCost: {butterFlyPrice} Bananas\nClicks are 2x Efficient"))
        
        upgrades.create_window(mainPosX,mainPosY,anchor='nw',window=butterFly)
        upgrades.create_window(borderPosX,borderPosY,anchor='nw',window=butterFlyBorder)
        

#DoubleTap
def doubleTapActivate():
    print("Begun")
    global doubleTapPrice
    global clickMultiplier
    global availableUpgrades
    global doubleTapStatus
    global bananas

    if bananas >= doubleTapPrice and doubleTapStatus == False:
        print("DoubleTap Purchased")
        bananas = bananas-doubleTapPrice
        clickMultiplier = clickMultiplier*2
        doubleTapStatus = True
        
        availableUpgrades = availableUpgrades-1

        doubleTap.destroy()
        doubleTapBorder.destroy()
        rearrangeUpgrades()

#TripleTap
def tripleTapActivate():
    global tripleTapPrice
    global clickMultiplier
    global availableUpgrades
    global tripleTapStatus
    global bananas

    if bananas >= tripleTapPrice and tripleTapStatus == False:
        print("TripleTap Purchased")
        bananas = bananas-tripleTapPrice
        clickMultiplier = clickMultiplier*3
        tripleTapStatus = True
        
        availableUpgrades = availableUpgrades-1

        #Deleting the button and its border
        tripleTap.destroy()
        tripleTapBorder.destroy()
        rearrangeUpgrades()

#ButterFly Clickings
def butterFlyActivate():
    global butterFlyPrice
    global clickMultiplier
    global availableUpgrades
    global butterFlyStatus
    global bananas

    if bananas >= butterFlyPrice and butterFlyStatus == False:
        print("butterFly Purchased")
        bananas = bananas-butterFlyPrice
        clickMultiplier = clickMultiplier*2
        butterFlyStatus = True
        
        availableUpgrades = availableUpgrades-1

        #Deleting the button and its border
        butterFly.destroy()
        butterFlyBorder.destroy()
        rearrangeUpgrades()

#Chimp Upgrade
def chimpActivate():
    global chimpPrice
    global monkeyMultiplier
    global availableUpgrades
    global chimpStatus
    global bananas

    if bananas >= chimpPrice and chimpStatus == False:
        print("chimp Purchased")
        bananas = bananas-chimpPrice
        monkeyMultiplier = monkeyMultiplier*2
        chimpStatus = True
        
        availableUpgrades = availableUpgrades-1

        #Deleting the button and its border
        chimp.destroy()
        chimpBorder.destroy()
        rearrangeUpgrades()

#Harambe Upgrade
def harambeActivate():
    global harambePrice
    global monkeyMultiplier
    global availableUpgrades
    global harambeStatus
    global bananas

    if bananas >= harambePrice and harambeStatus == False:
        print("harambe Purchased")
        bananas = bananas-harambePrice
        monkeyMultiplier = monkeyMultiplier*2
        harambeStatus = True
        
        availableUpgrades = availableUpgrades-1

        #Deleting the button and its border
        harambe.destroy()
        harambeBorder.destroy()
        rearrangeUpgrades()

#Harambe Upgrade
def betterHoeActivate():
    global betterHoePrice
    global farmMultiplier
    global availableUpgrades
    global betterHoeStatus
    global bananas

    if bananas >= betterHoePrice and betterHoeStatus == False:
        print("betterHoe Purchased")
        bananas = bananas-betterHoePrice
        farmMultiplier = farmMultiplier*2
        betterHoeStatus = True
        
        availableUpgrades = availableUpgrades-1

        #Deleting the button and its border
        betterHoe.destroy()
        betterHoeBorder.destroy()
        rearrangeUpgrades()


#--------------------UPGRADES (2)--------------------#
def updateUpgrades():
    global availableUpgrades
    global upgradeBorderColor
    global bps
    global monkeyAmount
    global farmAmount
    borderPosX = 7
    borderPosY = 74
    mainPosX = 9
    mainPosY = 76


    #MAKING CHIMPANZEE BUTTON
    global chimpStatus
    if monkeyAmount >= 1 and chimpStatus == '':
        
        global chimpImg
        global chimpBorder
        global chimp
        global chimpHover
        chimpStatus = False

        #Uploads the image
        image = Image.open('Upgrades/(2)Monkey/chimp.png')
        resized_img = image.resize((56,56))
        chimpImg = ImageTk.PhotoImage(resized_img)

        #Creates the button and the hover button
        chimpBorder = Canvas(root, bg=upgradeBorderColor,highlightbackground = upgradeBorderColor, highlightthickness = 2, bd=0,height=58,width=58)
        chimp = Button(root,image=chimpImg,bg="black",borderwidth=0,activebackground="black",command=chimpActivate)

        chimpHover = Balloon(root)
        chimpHover.bind_widget(chimp,balloonmsg=(f"CHIMPANZEE \nCost: {chimpPrice} Bananas\nMonkeys are 2x efficient"))

        upgrades.create_window(borderPosX+(56*availableUpgrades),74,anchor='nw',window=chimpBorder)
        upgrades.create_window(mainPosX+(56*availableUpgrades),76,anchor='nw',window=chimp)

        availableUpgrades = availableUpgrades+1


    #MAKING TRIPLE TAP BUTTON
    global tripleTapStatus
    if bps >= 2 and tripleTapStatus == '':
        
        global tripleTapImg
        global tripleTapBorder
        global tripleTap
        global tripleTapHover
        tripleTapStatus = False

        #Uploads the image
        image = Image.open('Upgrades/(1)Mouse/tripletap.png')
        resized_img = image.resize((56,56))
        tripleTapImg = ImageTk.PhotoImage(resized_img)

        #Creates the button and the hover button
        tripleTapBorder = Canvas(root, bg=upgradeBorderColor,highlightbackground = upgradeBorderColor, highlightthickness = 2, bd=0,height=58,width=58)
        tripleTap = Button(root,image=tripleTapImg,bg="black",borderwidth=0,activebackground="black",command=tripleTapActivate)

        tripleTapHover = Balloon(root)
        tripleTapHover.bind_widget(tripleTap,balloonmsg=(f"TRIPLE TAP \nCost: {tripleTapPrice} Bananas\n Clicks are 3x efficient"))

        upgrades.create_window(borderPosX+(56*availableUpgrades),74,anchor='nw',window=tripleTapBorder)
        upgrades.create_window(mainPosX+(56*availableUpgrades),76,anchor='nw',window=tripleTap)
        
        availableUpgrades = availableUpgrades+1


    #MAKING HARAMBE BUTTON
    global harambeStatus
    if monkeyAmount >= 5 and harambeStatus == '':
        
        global harambeImg
        global harambeBorder
        global harambe
        global harambeHover
        harambeStatus = False

        #Uploads the image
        image = Image.open('Upgrades/(2)Monkey/harambe.png')
        resized_img = image.resize((56,56))
        harambeImg = ImageTk.PhotoImage(resized_img)

        #Creates the button and the hover button
        harambeBorder = Canvas(root, bg=upgradeBorderColor,highlightbackground = upgradeBorderColor, highlightthickness = 2, bd=0,height=58,width=58)
        harambe = Button(root,image=harambeImg,bg="black",borderwidth=0,activebackground="black",command=harambeActivate)

        harambeHover = Balloon(root)
        harambeHover.bind_widget(harambe,balloonmsg=(f"HARAMBE \nCost: {harambePrice} Bananas\nMonkeys are 2x efficient"))

        upgrades.create_window(borderPosX+(56*availableUpgrades),74,anchor='nw',window=harambeBorder)
        upgrades.create_window(mainPosX+(56*availableUpgrades),76,anchor='nw',window=harambe)
        
        availableUpgrades = availableUpgrades+1


    #MAKING HARAMBE BUTTON
    global betterHoeStatus
    if farmAmount >= 1 and betterHoeStatus == '':
        
        global betterHoeImg
        global betterHoeBorder
        global betterHoe
        global betterHoeHover
        betterHoeStatus = False

        #Uploads the image
        image = Image.open('Upgrades/(3)Farm/betterhoe.png')
        resized_img = image.resize((56,56))
        betterHoeImg = ImageTk.PhotoImage(resized_img)

        #Creates the button and the hover button
        betterHoeBorder = Canvas(root, bg=upgradeBorderColor,highlightbackground = upgradeBorderColor, highlightthickness = 2, bd=0,height=58,width=58)
        betterHoe = Button(root,image=betterHoeImg,bg="black",borderwidth=0,activebackground="black",command=betterHoeActivate)

        betterHoeHover = Balloon(root)
        betterHoeHover.bind_widget(betterHoe,balloonmsg=(f"BETTER HOES \nCost: {betterHoePrice} Bananas\nFarms are 2x efficient"))

        upgrades.create_window(borderPosX+(56*availableUpgrades),74,anchor='nw',window=betterHoeBorder)
        upgrades.create_window(mainPosX+(56*availableUpgrades),76,anchor='nw',window=betterHoe)
        
        availableUpgrades = availableUpgrades+1


    #MAKING BUTTERFLY BUTTON
    global butterFlyStatus
    if bps >= 30 and butterFlyStatus == '':
        global butterFlyImg
        global butterFlyBorder
        global butterFly
        global butterFlyHover
        butterFlyStatus = False

        print(bps)
        print(butterFlyStatus)
        print("begun")

        #Uploads the image
        image = Image.open('Upgrades/(1)Mouse/butterfly.png')
        resized_img = image.resize((56,56))
        butterFlyImg = ImageTk.PhotoImage(resized_img)

        #Creates the button and the hover button
        butterFlyBorder = Canvas(root, bg=upgradeBorderColor,highlightbackground = upgradeBorderColor, highlightthickness = 2, bd=0,height=58,width=58)
        butterFly = Button(root,image=butterFlyImg,bg="black",borderwidth=0,activebackground="black",command=butterFlyActivate)

        butterFlyHover = Balloon(root)
        butterFlyHover.bind_widget(butterFly,balloonmsg=(f"BUTTERFLY CLICKING \nCost: {butterFlyPrice} Bananas\nClicks are 2x Efficient"))

        upgrades.create_window(borderPosX+(56*availableUpgrades),74,anchor='nw',window=butterFlyBorder)
        upgrades.create_window(mainPosX+(56*availableUpgrades),76,anchor='nw',window=butterFly)

        availableUpgrades=availableUpgrades+1

    root.after(1000,updateUpgrades)
        




#Setup the three frames

leftWidth = 300
leftSide = Canvas(root,width=leftWidth,height=600)

middleWidth = 500
middleSide = Canvas(root,width=middleWidth,height=600)

rightWidth = 300
rightSide = Canvas(root,width=rightWidth,height=600)

#--------------------------------------------LEFT---------------------------------------------------#

#-----Create Canvas-----#
leftSide.grid(column=0,row=0)

#---Create banana Image + Button---#

#Image  
img = Image.open("banana1.png")
resized_img = img.resize((250, 250))
banana1 = ImageTk.PhotoImage(resized_img)

#Creating banana button, and adding it to the window
click_banana = Button(root,image=banana1,command=clickBanana,borderwidth=0)
leftSide.create_window(150, 300, window=click_banana)

#---Create bananas Count---#
bananaCount = Label(root, text=(str(bananas)+" Bananas"),font=('Comic Sans MS',20,'bold'))
leftSide.create_window(150,150,window=bananaCount)

#Creating BPS counter
bpsCounter = Label(root,text=(f"BPS: {bps}"))
leftSide.create_window(150,100, window=bpsCounter)

#---Create Separator---#
sep1 = ttk.Separator(root, orient='vertical')
sep1.grid(row=0,column=1, sticky='ns')




#--------------------------------------------MIDDLE---------------------------------------------------#




#-----Create Generator Canvas-----#
middleSide.grid(row=0,column=2)



#----------CREATE MONKEY----------#
img = Image.open('Buildings/monkey.png')
resized_img = img.resize((50,50))
monkeyImg = ImageTk.PhotoImage(resized_img)


#---Create monkey canvas---#
monkeyShopColor = '#785f5f'
monkeyShop = Canvas(root,width=500,height=150,bg=monkeyShopColor) #Create monkey Canvas
middleSide.create_window(0,75,window=monkeyShop,anchor='w') #Add monkey Canvas to middleWidth Canvas

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
middleSide.create_window(0,225,window=farmShop,anchor='w') #Add Farm Canvas to middleWidth Canvas

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
middleSide.create_window(0,375,window=plantShop,anchor='w') #Add plantation Canvas to middleWidth Canvas

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
middleSide.create_window(0,525,window=complexShop,anchor='w') #Add Industrial Complex Canvas to middleWidth Canvas

#Create Industrial Complex level counter
complexLevel = Label(root, text="Industrial Complex: Level 0",anchor='w',font=('Comic Sans MS',14,'bold'),bg=complexShopColor)
complexShop.create_window(2,2,window=complexLevel,anchor='nw') #Add counter to the canvas


#---Create Separator---#
sep2 = ttk.Separator(root, orient='vertical')
sep2.grid(row=0,column=3, sticky='ns',rowspan=2)
root.grid_columnconfigure(3, weight=1)





#---------------------------------------------RIGHT (SHOP)--------------------------------------------------#


#-----Create Shop Canvas-----#

rightWidth = 300
rightSide.grid(row=0,column=4)




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
width=rightWidth,
height=60,
command=lambda: purchaseAnShop(monkeyAmount,monkeyPrice,monkeyIncome,"monkey")) #Create monkey level counter

rightSide.create_window(0,35,window=monkeyPurchase,anchor='w') #Add monkey rightSide Canvas to overall Shop Canvas



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
width=rightWidth,
height=60,
command=lambda: purchaseAnShop(farmAmount,farmPrice,farmIncome,"farm")) #Create monkey level counter) #Create monkey level counter    shop.create_window(0,100,window=farmPurchase,anchor='w') #Add farm Shop Canvas to overall Shop Canvas

rightSide.create_window(0,105,window=farmPurchase,anchor='w') #Add monkey Shop Canvas to overall Shop Canvas



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
width=rightWidth,
height=60,
command=lambda: purchaseAnShop(plantAmount,plantPrice,plantIncome,"plant")) #Create monkey level counter) #Create Plantation level counter

rightSide.create_window(0,175,window=plantPurchase,anchor='w') #Add plantation Shop Canvas to overall Shop Canvas



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
width=rightWidth,
height=60,
command=lambda: purchaseAnShop(complexAmount,complexPrice,complexIncome,"complex")) #Create monkey level counter) #Create Industrial Complex level counter

rightSide.create_window(0,245,window=complexPurchase,anchor='w') #Add Industrial Complex Shop Canvas to overall Shop Canvas


#---------------------------------------------RIGHT (UPGRADES)--------------------------------------------------#


#-----CREATE UPGRADE CANVAS-----#
upgradesColor = "#4e4f87" #Sets the background color for the upgrades Canvas

upgradeHeight = 275

upgrades = Canvas(root,width=rightWidth,height=upgradeHeight,bg=upgradesColor) #Creates the upgrades Canvas 
rightSide.create_window(0,275,window=upgrades,anchor='nw') #Places the canvas on the shop

upgradesLabel = Label(root,text="Hover over an upgrade to\nview its benefits",
justify = CENTER,
font=('Comic Sans MS',14,'bold'),
anchor='c',
bg=upgradesColor) #Top Part
upgrades.create_window(rightWidth/2,10,window=upgradesLabel,anchor='n')

#Establishes a background color for all the upgrades
upgradeBorderColor = "#a14c3f"


#-----HORIZONTAL LINE-----#
upgrades.create_line(0, 4, rightWidth+2, 4, fill='#964B00', width=7) #Top Line
upgrades.create_line(0, 72, rightWidth+2, 72, fill='#964B00', width=2)# Middle Line

upgrades.create_line(
5, 0,
5, upgradeHeight,
fill='#964B00', width=7) #Left Line

upgrades.create_line(
rightWidth-2, 0,
rightWidth-2, upgradeHeight,
fill='#964B00', width=7) #Right Line

upgrades.create_line(
0, upgradeHeight,
rightWidth+2, upgradeHeight,
fill='#964B00', width=7) #Bottom Line



#-----CREATE DOUBLE TAP-----#

#Uploads the image
image = Image.open('Upgrades/(1)Mouse/doubletap.png')
resized_img = image.resize((56,56))
doubleTapImg = ImageTk.PhotoImage(resized_img)

#Creates the button and the hover button
doubleTapBorder = Canvas(root, bg=upgradeBorderColor,highlightbackground = upgradeBorderColor, highlightthickness = 2, bd=0,height=58,width=58)
doubleTap = Button(root,image=doubleTapImg,bg="black",borderwidth=0,activebackground="black",command=doubleTapActivate)

doubleTapHover = Balloon(root)
doubleTapHover.bind_widget(doubleTap,balloonmsg=(f"DOUBLE TAP \nCost: {doubleTapPrice} Bananas\nClicks are 2x Efficient"))

upgrades.create_window(10,74,anchor='nw',window=doubleTapBorder)
upgrades.create_window(12,76,anchor='nw',window=doubleTap)



#----------Update banana Count + Tkinter operation loop---------#

updateBanana()
updateUpgrades()
root.mainloop()