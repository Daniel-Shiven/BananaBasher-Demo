#---------------------------------------------------------------------------------------------------------#
#============================================ SETUP/VARIABLES ============================================#
#---------------------------------------------------------------------------------------------------------#

#============ PACKETS ============#
from tkinter import *
from tkinter.tix import *
from tkinter import ttk
from PIL import Image, ImageTk


#============ WINDOW ============#
root = Tk() #Create the window
root.title("Banana Basher") #Giving the window a title
root.resizable(False,False) #You can't resize the window
photo = ImageTk.PhotoImage(Image.open('banana1.png'))
root.wm_iconphoto(False, photo)

#============ System Variables ============#
stats = (0,0) #bananas and bps
bananas = 0 #Banana Count
bps = 1 #Bananas per Second
clickMultiplier = 1 #Click Multiplier
tapMultiplier = 0 #Tap Multiplier


#============ Separator Variables ============#

separators = ['Separators/separator1.jpg','Separators/separator2.jpg','Separators/border1.jpg','Separators/border2.jpg']

for i in range(2):
    img = Image.open(separators[i])
    separators[i] = ImageTk.PhotoImage(img.resize((50,600)))

img = Image.open(separators[2])
separators[2] = ImageTk.PhotoImage(img.resize((400,25)))

#============ SHOP MANAGEMENT VARIABLES ============#
buildings = 0

generators = (
    # Monkey
[['Monkey',0,50,0,1,1],['Buildings/monkey.png'],
 ["Monkies","Buildings/monkeybg.png"]],
    # Farm
[['Farm',0,250,0,4,1],['Buildings/farm.png'],
 ["Farms","Buildings/farmbg.png"]],
    # Plantation
[['Banana Estate',0,2800,0,30,1],['Buildings/estate.png'],
 ["Banana\nEstates","Buildings/estatebg.png"]],
    # Complex
[['Industrial Complex',0,32000,0,165,1],['Buildings/complex.png'],
 ["Complexes","Buildings/complexbg.png"]])

# buildings = ([type,amount,price,income,base income, multiplier],
#               [Logo Address, Logo, Shop Price Button]
#               [Type, GenBg, Master, BgColor, Amount]


#============ UPGRADE MANAGEMENT VARIABLES ============#

# List of all Upgrade Info
# upgrades = ([genIdentity,status,price,reqStatus,req],[button,background,hover,msg],[currentimg,dark,light])
upgrades = (
[['double','locked,',100,bps,0],[],['','Upgrades/(1)Mouse/double.png','Upgrades/(1)Mouse/darkdouble.png']],
[['triple','locked,',1000],[],['','Upgrades/(1)Mouse/triple.png','Upgrades/(1)Mouse/darktriple.png']],
[['butterfly','locked',5000],[],['','Upgrades/(1)Mouse/butterfly.png','Upgrades/(1)Mouse/darkbutterfly.png']],
[['jitter','locked',10000],[],['','Upgrades/(1)Mouse/jitter.png','Upgrades/(1)Mouse/darkjitter.png']],
[['bawl','locked',100000],[],['','Upgrades/(1)Mouse/bawl.png','Upgrades/(1)Mouse/darkbawl.png']],
[['drag','locked',1000000],[],['','Upgrades/(1)Mouse/drag.png','Upgrades/(1)Mouse/darkdrag.png']],
[['macro','locked',10000000],[],['','Upgrades/(1)Mouse/macro.png','Upgrades/(1)Mouse/darkmacro.png']],
[['auto','locked',100000000],[],['','Upgrades/(1)Mouse/auto.png','Upgrades/(1)Mouse/darkauto.png']],
[['chimp','locked',500],[],['','Upgrades/(2)Monkey/chimp.png','Upgrades/(2)Monkey/darkchimp.png']],
[['harambe','locked',2500],[],['','Upgrades/(2)Monkey/harambe.png','Upgrades/(2)Monkey/darkharambe.png']],
[['ape','locked',7800],[],['','Upgrades/(2)Monkey/ape.png','Upgrades/(2)Monkey/darkape.png']],
[['gorilla','locked',45000],[],['','Upgrades/(2)Monkey/gorilla.png','Upgrades/(2)Monkey/darkgorilla.png']],
[['donkey','locked',550000],[],['','Upgrades/(2)Monkey/donkey.png','Upgrades/(2)Monkey/darkdonkey.png']],
[['king','locked',3800000],[],['','Upgrades/(2)Monkey/king.png','Upgrades/(2)Monkey/darkking.png']],
[['hanuman','locked',40000000],[],['','Upgrades/(2)Monkey/hanuman.png','Upgrades/(2)Monkey/darkhanuman.png']],
[['mania','locked',4000000000],[],['','Upgrades/(2)Monkey/mania.png','Upgrades/(2)Monkey/darkmania.png']],
[['betterhoe','locked',2300],[],['','Upgrades/(3)Farm/betterhoe.png','Upgrades/(3)Farm/darkbetterhoe.png']],
[['irrigation','locked',12000],[],['','Upgrades/(3)Farm/irrigation.png','Upgrades/(3)Farm/darkirrigation.png']],
[['gmo','locked',60000],[],['','Upgrades/(3)Farm/gmo.png','Upgrades/(3)Farm/darkgmo.png']],
[['vines','locked',600000],[],['','Upgrades/(3)Farm/vines.png','Upgrades/(3)Farm/darkvines.png']],
[['qasar','locked',6000000],[],['','Upgrades/(3)Farm/qasar.png','Upgrades/(3)Farm/darkqasar.png']],
[['pest','locked',6000000],[],['','Upgrades/(3)Farm/pest.png','Upgrades/(3)Farm/darkpest.png']],
[['seeds','locked',60000000],[],['','Upgrades/(3)Farm/seeds.png','Upgrades/(3)Farm/darkseeds.png']],
[['precision','locked',600000000],[],['','Upgrades/(3)Farm/precision.png','Upgrades/(3)Farm/darkprecision.png']],
)

# Accessing the directories and making images out of them
for i in range(len(upgrades)):

    for j in range(1,3):
        img = Image.open(upgrades[i][2][j])
        upgrades[i][2][j] = ImageTk.PhotoImage(img.resize((52,52)))


#---------------------------------------------------------------------------------------------------#
#============================================ FUNCTIONS ============================================#
#---------------------------------------------------------------------------------------------------#

#---------------------------------#
#============ BANANAS ============#
#---------------------------------#

#============ Update Banana Count ============#
def updateBanana():

    global bananas
    global bps
    
    bps = 0
    for i in range(len(generators)):
        bps += generators[i][0][3]

    bpsCounter.config(text=(f"BPS: {round(bps,1)}"),font=('Comic Sans MS',14,'bold'))

    bananas = bananas+(bps/10)
    
    bananaDisplay = round(bananas)
    bananaCount.config(text=(f"{bananaDisplay} Bananas"))
    root.after(50,updateBanana)


#Clicking the Banana
def clickBanana():
    global bananas
    global buildings

    bananas = bananas+1

    bananaDisplay = round(bananas)
    bananaCount.config(text=f"{bananaDisplay} Bananas")



#------------------------------#
#============ SHOP ============#
#------------------------------#

def purchase(x):    
    if bananas >= generators[x][0][2]:
        generators[x][0][1] += 1 #Increase Amount
        generators[x][0][2] = round(generators[x][0][2]*1.15) #Increase Price

        #Increase Income
        if generators[x][0][1] == 1:
            generators[x][0][3] = generators[x][0][4]
        else:
            generators[x][0][3] *= 1.15

        generators[x][1][1].config(text=(f" {generators[x][0][0]}\n {generators[x][0][2]} 🍌"))
        generators[x][2][4].config(text=(f"{generators[x][0][1]}"))
        



#----------------------------------#
#============ UPGRADES ============#
#----------------------------------#
        
def upgradeStatus():
    
# 'locked' - Not Unlocked, can be changed through updateUpgrades()
# 'unlocked' - Unlocked, after a change through updateUpgrades()
# 'purchased' - Purchased, after a change through activation()

    for i in range(upgrades):
        if upgrades[i][0][1] == 'locked' and upgrades[i][0][3] >= upgrades[i][0][4]:
            upgrades[i][0][1] = 'unlocked'
            
            img = Image.open(upgrades[i][1][2])





#--------------------------------------------------------------------------------------------------#
#========================================== SCREEN SETUP ==========================================#
#--------------------------------------------------------------------------------------------------#


#Setup the three frames

canvas = (
Canvas(root,width=350,height=600,bd=-2),
Canvas(root,width=450,height=600,bd=-2),
Canvas(root,width=50,height=600,bd=-2),
Frame(root,width=300,height=600))

#-------------------------------------------------------#
#====================== LEFT SIDE ======================#
#-------------------------------------------------------#

#----- Create Canvas -----#
canvas[0].grid(column=0,row=0)

#----- Create Background and Banana Images -----#
img_bg = Image.open("background.jpg")
background = ImageTk.PhotoImage(img_bg.resize((300, 600)))

img_banana = Image.open("banana1.png")
banana1 = ImageTk.PhotoImage(img_banana.resize((250, 250)))

#----- Add images to the leftSide (canvas[0]) canvas -----#
bg_item = canvas[0].create_image(150, 300, image=background)
banana_item = canvas[0].create_image(150, 300, image=banana1)
canvas[0].tag_bind(banana_item, "<Button-1>", lambda event: clickBanana())


#----- Counters -----#

# Banana Display
bananaBg = Canvas(canvas[0],bg='white',highlightbackground='white',highlightthickness=2,bd=0,height=40,width=296)
canvas[0].create_window(150,150, window=bananaBg)
bananaCount = Label(canvas[0], text=(str(bananas)+" Bananas"), font=('Comic Sans MS', 20, 'bold'), bg='white')
canvas[0].create_window(150, 150, window=bananaCount)

# BPS Counter
bpsBg = Canvas(canvas[0],bg='white',highlightbackground='white',highlightthickness=2,bd=0,height=30,width=296)
canvas[0].create_window(150,95, window=bpsBg)
bpsCounter = Label(canvas[0], text=(f"BPS: {bps}"), font=('Comic Sans MS', 14, 'bold'), bg='white')
canvas[0].create_window(150, 95, window=bpsCounter)

#----- Create Separator -----#
canvas[0].create_image(300,0,image=separators[0],anchor='nw')



#---------------------------------------------------------#
#====================== MIDDLE SIDE ======================#
#---------------------------------------------------------#

#----- Create Frame -----#
midContainer = Frame(root,width=400,height=600)
midCanvas = Canvas(midContainer,width=400,height=600,bd=-2)
midBar = Scrollbar(midContainer, orient="vertical", command=midCanvas.yview)
midScrollable = Frame(midCanvas)

midScrollable.bind(
    "<Configure>",
    lambda e: midCanvas.configure(
        scrollregion=midCanvas.bbox("all")
    )
)

midCanvas.create_window((0, 0), window=midScrollable, anchor="nw")

midCanvas.configure(yscrollcommand=midBar.set)

#----------CREATE GENERATORS----------#

genColor = '#527AA5'

#generators = ([GenText, GenBg Image, GenMaster, Bg Color, Type, Amount])

for i in range(len(generators)):

    # The Master Canvas
    generators[i][2].append(Canvas(midScrollable,width=400,height=175,bd=-2))
    generators[i][2][2].pack(side=TOP,fill=X)

    # Separator Canvas
    generators[i][2][2].create_image(0,150,image=separators[2],anchor='nw')

    # Background Image
    img = Image.open(generators[i][2][1])
    generators[i][2][1] = (ImageTk.PhotoImage(img.resize((300,150))))
    generators[i][2][2].create_image(100,0,image=generators[i][2][1],anchor='nw')

    # Background Color
    generators[i][2].append(Canvas(generators[i][2][2],bg=genColor,width=100,height=150,bd=-2))
    generators[i][2][2].create_window(0,0,window=generators[i][2][3],anchor='nw')
    
    # Type and Amount (Monkey Level 0)
    generators[i][2][0] = (Label(generators[i][2][3],text=generators[i][2][0],anchor='c',font=('Comic Sans MS',14,'bold'),bg=genColor))
    generators[i][2].append(Label(generators[i][2][3],text='0',anchor='c',font=('Comic Sans MS',34,'bold'),bg=genColor))
    generators[i][2][3].create_window(50,40,window=generators[i][2][4],anchor='c')
    generators[i][2][3].create_window(50,100,window=generators[i][2][0],anchor='c')

# Add the frame to the screen
midContainer.grid(column=1,row=0)
midCanvas.pack(side="left", fill="both", expand=True)
midBar.pack(side="right", fill="y")



#--------------------------------------------------------#
#====================== RIGHT SIDE ======================#
#--------------------------------------------------------#

rightWidth = 300

canvas[2].grid(column=2,row=0)
canvas[2].create_image(0,0,image=separators[1],anchor='nw')

#----- Create Frame -----#
shopContainer = Frame(root,width=300,height=600)
shopCanvas = Canvas(shopContainer,width=300,height=600,bd=-2)
shopBar = Scrollbar(shopContainer, orient="vertical", command=shopCanvas.yview)
shopScrollable = Frame(shopCanvas)

shopScrollable.bind(
    "<Configure>",
    lambda e: midCanvas.configure(
        scrollregion=midCanvas.bbox("all")
    )
)

shopCanvas.create_window((0, 0), window=shopScrollable, anchor="nw")

shopCanvas.configure(yscrollcommand=shopBar.set)


# Add the frame to the screen
shopContainer.grid(column=3,row=0)
shopCanvas.pack(side="left", fill="both", expand=True)
shopBar.pack(side="right", fill="y")

#-----Create Shop Canvas-----#

shopColor = '#9eb3b5'

for i in range(len(generators)):
    img = Image.open(generators[i][1][0])
    generators[i][1][0] = (ImageTk.PhotoImage(img.resize((50,50))))


    generators[i][1].append(Button(shopScrollable,
    text=(f" {generators[i][0][0]}\n {generators[i][0][2]} 🍌"),font=('Comic Sans MS',14,'bold'),
    justify=LEFT,
    anchor='w',
    image=generators[i][1][0],
    compound=LEFT,
    bg=shopColor,
    width=rightWidth-7,
    height=60))

    generators[i][1][1].pack(side=TOP)

generators[0][1][1].config(command=lambda: purchase(0))
generators[1][1][1].config(command=lambda: purchase(1))
generators[2][1][1].config(command=lambda: purchase(2))
generators[3][1][1].config(command=lambda: purchase(3))



#-----CREATE UPGRADE CANVAS-----#
upgradeSep = Canvas(shopScrollable,width=300,height=25,bd=-2)
upgradeSep.pack(side=TOP)

upgradeSep.create_image(0,0,image=separators[2],anchor='nw')

upgradesColor = "#4e4f87" #Sets the background color for the upgrades Canvas

#rightWidth = 300

upgradeCanvas = Canvas(shopScrollable,width=rightWidth,height=250,bg=upgradesColor,bd=-2) #Creates the upgrades Canvas 
upgradeCanvas.pack(side=BOTTOM)

upgradesLabel = Label(root,text="Hover over an upgrade to\nview its benefits",
justify = CENTER,
font=('Comic Sans MS',14,'bold'),
anchor='c',
bg=upgradesColor) #Top Part
upgradeCanvas.create_window(rightWidth/2,35,window=upgradesLabel,anchor='c')

#Establishes a background color for all the upgrades
upgradeBorderColor = "#a14c3f"


#-----HORIZONTAL LINE-----#
upgradeCanvas.create_line(0, 70, rightWidth+2, 70, fill='#964B00', width=2)# Middle Line

# upgradeCanvas.create_line(5, 0, 
# 5, 200,
# fill='#964B00', width=6) #Left Line

# upgradeCanvas.create_line(
# 298, 0,
# 298, 200,
# fill='#964B00', width=5) #Right Line

# upgradeCanvas.create_line(
# 0, 200,
# rightWidth+2, 200,
# fill='#964B00', width=7) #Bottom Line


#----------Update banana Count + Tkinter operation loop---------#

updateBanana()

root.mainloop()
