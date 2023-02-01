#Import Packets
from tkinter import *
from tkinter.tix import *
from tkinter import ttk
from PIL import Image, ImageTk


#---------------------------------------------------------------------------------------------------#
#============================================ VARIABLES ============================================#
#---------------------------------------------------------------------------------------------------#

#============ SYSTEM/SETUP VARIABLES ============#

#--- Startup ---#
root = Tk() #Create the window
root.title("Banana Basher") #Giving the window a title
root.resizable(False,False) #You can't resize the window

#--- Startup ---#
bananas = 0 #Banana Count
bps = 0 #Bananas per Second
clickMultiplier = 1 #Click Multiplier


#============ SHOP MANAGEMENT VARIABLES ============#

#--- Monkeys ---#
monkeyAmount = 0 #Amount of Monkeys
monkeyPrice = 50 #Price of Monkey
monkeyIncome = 0 #Stores the bps for Monkeys
monkeyMultiplier = 1 #Income Multiplier

#--- Farms ---#
farmAmount = 0 #Amount of Farm
farmPrice = 550 #Price of Farm
farmIncome = 0 #Stores the bps for Farm
farmMultiplier = 1 #Income Multiplier

#--- Plantations ---#
plantAmount = 0 #Amount of Plantation
plantPrice = 7200 #Price of Plantation 
plantIncome = 0 #Stores the bps for Plantation
plantMultiplier = 1 #Income Multiplier

#--- Industrial Complexes ---#
complexAmount = 0 #Amount of Industrial Complexes
complexPrice = 82000 #Price of Industrial Complexes
complexIncome = 0 #Stores the bps for Industrial Complexes
complexMultiplier = 1 #Income Multiplier


#============ UPGRADE SYSTEM VARIABLES ============#
# 'locked' - Not Unlocked, can be changed through updateUpgrades()
# 'unlocked' - Unlocked, after a change through updateUpgrades()
# 'purchased' - Purchased, after a change through activation()


#------------------------------------------#
#---------------| CLICKING |---------------#
#------------------------------------------#

#------- DOUBLE TAP -------#
doubleTapPrice = 100 #Price of doubleTap
doubleTapStatus = 'locked' #Status of double Tap
doubleTap = Button(root) #Setup doubleTap Button
doubleTapBorder = Canvas(root) #Setup the button border
doubleTapHover = Balloon(root)
doubleTapImg = ''
doubleTapDark = ''
doubleTapLight = ''
doubleTapMsg = (f"DOUBLE TAP \nCost: 100 Bananas\nClicks are 2x Efficient")

#------ TRIPLE TAP -------#
tripleTapPrice = 1000 #Price of tripleTap
tripleTapStatus = 'locked' #Status of tripleTap
tripleTap = Button(root) #Setup tripleTap Button
tripleTapBorder = Canvas(root) #Setup the button border
tripleTapHover = Balloon(root) #Setup the hover button
tripleTapMsg = (f"TRIPLE TAP \nCost: 1000 Bananas\nClicks are 3x Efficient") #Setup hover button message
tripleTapImg = '' #Setup tripleTapImg
tripleTapDark = '' #Setup tripleTapDark Image
tripleTapLight = '' #Setup tripleTapLight Image

#------- BUTTERFLY -------#
butterFlyPrice = 5000 #Price of butterfly clicking
butterFlyStatus = 'locked' #Status of butterfly clicking
butterFly = Button(root) #Setup butterFly Button
butterFlyBorder = Canvas(root) #Setup the button border
butterFlyHover = Balloon(root)
butterFlyImg = ''
butterFlyDark = ''
butterFlyLight = ''
butterFlyMsg = (f"BUTTERFLY CLICKING \nCost: 5000 Bananas\nClicks are 2x Efficient")


#-----------------------------------------#
#---------------| MONKEYS |---------------#
#-----------------------------------------#

#------- CHIMPANZEE -------#
chimpPrice = 500 #Price of Chimp
chimpStatus = 'locked' #Status of Chimp
chimp = Button(root) #Setup chimp Button
chimpBorder = Canvas(root) #Setup the button border
chimpHover = Balloon(root)
chimpImg = ''
chimpDark = ''
chimpLight = ''
chimpMsg = (f"CHIMPANZEES \nCost: 500 Bananas\nMonkeys are 2x Efficient")

#------- HARAMBE -------#
harambePrice = 2500 #Price of Harambe
harambeStatus = 'locked' #Status of Harambe
harambe = Button(root) #Setup harambe Button
harambeBorder = Canvas(root) #Setup the button border
harambeHover = Balloon(root)
harambeImg = ''
harambeDark = ''
harambeLight = ''
harambeMsg = (f"HARAMBE \nCost: 2500 Bananas\nMonkeys are 2x Efficient")


#-----------------------------------------#
#---------------| FARMS |---------------#
#-----------------------------------------#

#---------- betterHoes ----------#
betterHoePrice = 2300 #Price of BetterHoes
betterHoeStatus = 'locked' #Status of betterHoes
betterHoe = Button(root) #Setup betterHoe Button
betterHoeBorder = Canvas(root) #Setup the button border
betterHoeHover = Balloon(root)
betterHoeImg = ''
betterHoeDark = ''
betterHoeLight = ''
betterHoeMsg = (f"BETTER HOES \nCost: 2300 Bananas\nFarms are 2x Efficient")




#---------------------------------------------------------------------------------------------------#
#============================================ FUNCTIONS ============================================#
#---------------------------------------------------------------------------------------------------#


#============ Updating the Banana Count ============#

def updateBanana():

    global bananas
    global bps
    
    bps = (monkeyIncome*monkeyMultiplier)+(farmIncome*farmMultiplier)+(plantIncome*plantMultiplier)+(complexIncome*complexMultiplier)
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
            print("Monkey Income:",monkeyIncome)

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
    global mainPosX
    global mainPosY
    global borderPosX
    global borderPosY
    borderPosX = (9-57)
    borderPosY = 74
    mainPosX = (11-57)
    mainPosY = 76

    def deleteMove(main,border,imageID,hover,hoverMsg):
        main.destroy()
        border.destroy()
        global mainPosX
        global mainPosY
        global borderPosX
        global borderPosY
        if borderPosX >= 233:
            mainPosX = 11
            borderPosX = 9
            mainPosY = mainPosY+57
            borderPosY = borderPosY+57
            print(borderPosX,borderPosY)
        else:
            mainPosX = mainPosX+57
            borderPosX = borderPosX+57
            print(borderPosX,borderPosY)

        border = Canvas(root,bg=upgradeBorderColor,highlightbackground=upgradeBorderColor,highlightthickness=2,bd=0,
        height=54,width=54)
        main = Button(root,bg='black',image=imageID,borderwidth=0,activebackground="black")
        hover.bind_widget(main,balloonmsg=hoverMsg)

        upgrades.create_window(mainPosX,mainPosY,anchor='nw',window=main)
        upgrades.create_window(borderPosX,borderPosY,anchor='nw',window=border)

        return (main,border)

    global doubleTapStatus
    if doubleTapStatus == 'unlocked':    #Cost: 100
        global doubleTap
        global doubleTapBorder
        buffer = deleteMove(doubleTap,doubleTapBorder,doubleTapImg,doubleTapHover,doubleTapMsg)
        doubleTap = buffer[0]
        doubleTap.config(command=lambda: activation(doubleTapPrice,doubleTapStatus,2,"doubleTap","click",doubleTap,doubleTapBorder))
        doubleTapBorder = buffer[1]

    global chimpStatus
    if chimpStatus == 'unlocked':    #Cost: 500
        global chimp
        global chimpBorder
        buffer = deleteMove(chimp,chimpBorder,chimpImg,chimpHover,chimpMsg)
        chimp = buffer[0]
        chimp.config(command=lambda: activation(chimpPrice,chimpStatus,2,"chimp","monkey",chimp,chimpBorder))
        chimpBorder = buffer[1]

    global tripleTapStatus
    if tripleTapStatus == 'unlocked':    #Cost: 1000
        global tripleTap
        global tripleTapBorder
        buffer = deleteMove(tripleTap,tripleTapBorder,tripleTapImg,tripleTapHover,tripleTapMsg)
        tripleTap = buffer[0]
        tripleTap.config(command=lambda: activation(tripleTapPrice,tripleTapStatus,3,"tripleTap","click",tripleTap,tripleTapBorder))
        tripleTapBorder = buffer[1]

    global betterHoeStatus
    if betterHoeStatus == 'unlocked':    #Cost: 2300
        global betterHoe
        global betterHoeBorder
        buffer = deleteMove(betterHoe,betterHoeBorder,betterHoeImg,betterHoeHover,betterHoeMsg)
        betterHoe = buffer[0]
        betterHoe.config(command=lambda: activation(betterHoePrice,betterHoeStatus,2,"betterHoe","farm",betterHoe,betterHoeBorder))
        betterHoeBorder = buffer[1]

    global harambeStatus
    if harambeStatus == 'unlocked':    #Cost: 2500
        global harambe
        global harambeBorder
        buffer = deleteMove(harambe,harambeBorder,harambeDark,harambeHover,harambeMsg)
        harambe = buffer[0]
        harambe.config(command=lambda: activation(harambePrice,harambeStatus,3,"harambe","monkey",harambe,harambeBorder))
        harambeBorder = buffer[1]

    global butterFlyStatus
    if butterFlyStatus == 'unlocked':    #Cost: 2500
        global butterFly
        global butterFlyBorder
        buffer = deleteMove(butterFly,butterFlyBorder,butterFlyDark,butterFlyHover,butterFlyMsg)       
        butterFly = buffer[0]
        butterFly.config(command=lambda: activation(butterFlyPrice,butterFlyStatus,2,"butterFly","click",butterFly,butterFlyBorder))
        butterFlyBorder = buffer[1]



#-----UPGRADE ACTIVATION-----#
def activation(price,status,increase,upgrade,type,main,border):
    global bananas

    if bananas >= price and status == "unlocked":
        print(upgrade,"purchase validated")
        bananas = bananas-price
        main.destroy()
        border.destroy()

        if type == 'click':
            print("Increase:",increase)
            global clickMultiplier
            print("Before cps:",clickMultiplier)
            clickMultiplier = clickMultiplier*increase
            print("After cps:",clickMultiplier)
            
            if upgrade == "doubleTap":
                global doubleTapStatus
                doubleTapStatus = 'purchased'
            
            if upgrade == "tripleTap":
                global tripleTapStatus
                tripleTapStatus = 'purchased'
            
            if upgrade == "butterFly":
                global butterFlyStatus
                butterFlyStatus = 'purchased'

        if type == 'monkey':
            global monkeyMultiplier
            print("Increase:",increase)
            global monkeyMultiplier
            print("Before cps:",monkeyMultiplier)
            monkeyMultiplier = monkeyMultiplier*increase
            print("After cps:",monkeyMultiplier)
            
            if upgrade == "chimp":
                global chimpStatus
                chimpStatus = 'purchased'
            
            if upgrade == "harambe":
                global harambeStatus
                harambeStatus = 'purchased'

        if type == 'farm':
            global farmMultiplier
            print("Increase:",increase)
            global farmMultiplier
            print("Before cps:",farmMultiplier)
            farmMultiplier = farmMultiplier*increase
            print("After cps:",farmMultiplier)
            
            if upgrade == "betterHoe":
                global betterHoeStatus
                betterHoeStatus = 'purchased'

        if type == 'plant':
            global plantMultiplier
            plantMultiplier = plantMultiplier*increase

        if type == 'complex':
            global complexMultiplier
            complexMultiplier = complexMultiplier*increase
        
        rearrangeUpgrades()
        print("upgrade rearrange order sent")
        


#--------------------UPGRADES (2)--------------------#
def upgradeStatus():
    global bananas
    global bps
    global monkeyAmount
    global farmAmount
    global option
    option = False

# 'locked' - Not Unlocked, can be changed through updateUpgrades()
# 'unlocked' - Unlocked, after a change through updateUpgrades()
# 'purchased' - Purchased, after a change through activation()

    def unlockUpgrade(requirement,current,status,darkFinal,lightFinal,lightImg,darkImg):
        if current >= requirement and status == 'locked':
            global option
            option = True

            image = Image.open(darkImg)
            resized_img = image.resize((52,52))
            darkFinal = ImageTk.PhotoImage(resized_img)

            status = 'unlocked'
            image = Image.open(lightImg)
            resized_img = image.resize((52,52))
            lightFinal = ImageTk.PhotoImage(resized_img)

        return(status,darkFinal,lightFinal)

    def availabileUpgrade(bananas,cost,status,dark,light,main):
        if bananas >= cost and status == 'unlocked': #If requirement is met
            img = light
            main.config(image=light)
        elif status == 'unlocked':
            img = dark
            main.config(image=dark)
        else:
            img = ''
        return(img)



#============= UNLOCKING UPGRADES =============#

    #DoubleTap Upgrade
    global doubleTapStatus
    global doubleTapDark
    global doubleTapLight
    buffer = unlockUpgrade(0,bps,doubleTapStatus,doubleTapDark,doubleTapLight,'Upgrades/(1)Mouse/doubletap.png','Upgrades/(1)Mouse/darkdoubletap.png')
    doubleTapStatus = buffer[0]
    doubleTapDark = buffer[1]
    doubleTapLight = buffer[2]

    global doubleTap
    global doubleTapImg
    doubleTapImg = availabileUpgrade(bananas,doubleTapPrice,doubleTapStatus,doubleTapDark,doubleTapLight,doubleTap)


    #TripleTap Upgrade
    global tripleTapStatus
    global tripleTapDark
    global tripleTapLight
    buffer = unlockUpgrade(2,bps,tripleTapStatus,tripleTapDark,tripleTapLight,'Upgrades/(1)Mouse/tripletap.png','Upgrades/(1)Mouse/darktripletap.png')
    tripleTapStatus = buffer[0]
    tripleTapDark = buffer[1]
    tripleTapLight = buffer[2]

    global tripleTap
    global tripleTapImg
    tripleTapImg = availabileUpgrade(bananas,tripleTapPrice,tripleTapStatus,tripleTapDark,tripleTapLight,tripleTap)

    #butterFly Upgrade
    global butterFlyStatus
    global butterFlyDark
    global butterFlyLight
    buffer = unlockUpgrade(30,bps,butterFlyStatus,butterFlyDark,butterFlyLight,'Upgrades/(1)Mouse/butterfly.png','Upgrades/(1)Mouse/darkbutterfly.png')
    butterFlyStatus = buffer[0]
    butterFlyDark = buffer[1]
    butterFlyLight = buffer[2]

    global butterFly
    global butterFlyImg
    butterFlyImg = availabileUpgrade(bananas,butterFlyPrice,butterFlyStatus,butterFlyDark,butterFlyLight,butterFly)


#============= MONKEY UPGRADES =============#

    #Chimp Upgrade
    global chimpStatus
    global chimpDark
    global chimpLight
    buffer = unlockUpgrade(1,monkeyAmount,chimpStatus,chimpDark,chimpLight,'Upgrades/(2)Monkey/chimp.png','Upgrades/(2)Monkey/darkchimp.png')
    chimpStatus = buffer[0]
    chimpDark = buffer[1]
    chimpLight = buffer[2]

    global chimp
    global chimpImg
    chimpImg = availabileUpgrade(bananas,chimpPrice,chimpStatus,chimpDark,chimpLight,chimp)

    #Harambe Upgrade
    global harambeStatus
    global harambeDark
    global harambeLight
    buffer = unlockUpgrade(5,monkeyAmount,harambeStatus,harambeDark,harambeLight,'Upgrades/(2)Monkey/harambe.png','Upgrades/(2)Monkey/darkharambe.png')
    harambeStatus = buffer[0]
    harambeDark = buffer[1]
    harambeLight = buffer[2]

    global harambe
    global harambeImg
    harambeImg = availabileUpgrade(bananas,harambePrice,harambeStatus,harambeDark,harambeLight,harambe)


#============= FARM UPGRADES =============#

    #betterHoe Upgrade
    global betterHoeStatus
    global betterHoeDark
    global betterHoeLight
    buffer = unlockUpgrade(1,farmAmount,betterHoeStatus,betterHoeDark,betterHoeLight,'Upgrades/(3)Farm/betterhoe.png','Upgrades/(3)Farm/darkbetterhoe.png')
    betterHoeStatus = buffer[0]
    betterHoeDark = buffer[1]
    betterHoeLight = buffer[2]

    global betterHoe
    global betterHoeImg
    betterHoeImg = availabileUpgrade(bananas,betterHoePrice,betterHoeStatus,betterHoeDark,betterHoeLight,betterHoe)

    if option == True:
        rearrangeUpgrades()

    root.after(1000,upgradeStatus)
        




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

rightWidth = 299
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

#rightWidth = 300

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

upgrades.create_line(5, 0, 
5, upgradeHeight,
fill='#964B00', width=6) #Left Line

upgrades.create_line(
298, 0,
298, upgradeHeight,
fill='#964B00', width=5) #Right Line

upgrades.create_line(
0, upgradeHeight,
rightWidth+2, upgradeHeight,
fill='#964B00', width=7) #Bottom Line



#----------Update banana Count + Tkinter operation loop---------#

updateBanana()
upgradeStatus()
root.mainloop()
