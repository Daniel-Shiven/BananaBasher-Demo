#---------------------------------------------------------------------------------------------------------#
#============================================ SETUP/VARIABLES ============================================#
#---------------------------------------------------------------------------------------------------------#

#============ PACKETS ============#
import pygame

from pygame.locals import ( # Import pygame.locals for easier access to key coordinates (flake8 and black standards)
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#============ SHOP MANAGEMENT VARIABLES ============#

#base price, base income
gen = (
    # Monkey
['Monkey',50,1,'Buildings/monkey.png',"Buildings/monkeybg.png","Monkies"],
    # Farm
['Farm',250,4,'Buildings/farm.png',"Buildings/farmbg.png","Farms"],
    # Plantation
['Banana Estate',2800,30,'Buildings/estate.png',"Buildings/estatebg.png","Estates"],
    # Complex
['Industrial Complex',32000,165,'Buildings/complex.png',"Buildings/complexbg.png","Complexes"])


#============ COLORS ============#
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (200, 200, 200)
GENCOLOR = (82, 122, 165)

#============ SYSTEM VARIABLES ============#
bananas = 0
bps = 1

#============ CLASSES AND OBJECTS ============#

#Generator Class

class generator:

    #[amount, price, income, starting income, multiplier]
    amount = 0
    price = 0
    income = 0
    base_income = 0
    multiplier = 0

    def __init__ (self,address,i,typeDisplay):

        self.colorBg = pygame.Surface((100,150)) #Load color

        self.imageBg = pygame.image.load(address) #Load Image
        self.imageBg = pygame.transform.scale(self.imageBg,(300,150))
        middle.blit(self.imageBg,(100,i*175))

        self.comic3 = pygame.font.SysFont("comicsansms", 45, True)
        self.quantity = self.comic3.render((f"{self.amount}"), True, BLACK)

        self.comic4 = pygame.font.SysFont("comicsansms", 18, True)
        self.type = self.comic4.render((f"{typeDisplay}"), True, (0,0,0))
        

        middle.blit(sep2,(0,150+(i*175))) #Blit Separator
    
    def update(self,i):
        self.colorBg.fill(GENCOLOR)
        self.colorBg.blit(self.type,(50-(self.type.get_width()/2),(110-(self.type.get_height()/2))))
        
        self.quantity = self.comic3.render((f"{self.amount}"), True, BLACK)
        self.colorBg.blit(self.quantity,(50-(self.quantity.get_width()/2),(50-(self.quantity.get_height()/2))))
        middle.blit(self.colorBg,(0,i*175))

class scrollbox():
    
    box_width = 20
    bar_y = 0
    def __init__ (self,height,scrn_y):

        # Set up scrollBox
        self.box_surface = pygame.Surface((self.box_width, height))

        # Height of scrollbar function of height of scrollbox
        self.bar_height = (600/height)*600

        #Set up scrollbar
        self.bar_surface = pygame.Surface((self.box_width, self.bar_height))

        self.multi = (height-600)/(scrn_y-self.bar_height)


#---------------------------------------------------------------------------------------------------------#
#============================================ SCREEN CREATION ============================================#
#---------------------------------------------------------------------------------------------------------#
#Left is 0 to 300x
#Middle is 350x to 770x


#============ WINDOW ============#
pygame.init() #initialize pygame

#scrn Dimensions
scrn_x = 1120 #Left(300): 300, Separator(50): 350, Middle(400): 750, Scrollbar(20): 770, Separator(50): 820, Right(300): 1120 
scrn_y = 600

scrn = pygame.display.set_mode([scrn_x,scrn_y]) #create screen
pygame.display.set_caption('Banana Basher') #setting screen name
bigBanana = pygame.image.load('banana2.png')
pygame.display.set_icon(bigBanana)


#============ LEFT SECTION ============#
left_width = 300
left_height = 600

background = pygame.image.load('background.jpg') #Background
background = pygame.transform.scale(background, (left_width,left_height))

banana = pygame.image.load('banana1.png') #Banana
button_mask = pygame.mask.from_surface(banana)

button_sprite = pygame.sprite.Sprite()
button_sprite.image = banana
button_sprite.rect = banana.get_rect()







sep1 = pygame.image.load('Separators/separator1.jpg') #Separator1
sep1 = pygame.transform.scale(sep1, (50,left_height))

countBg = pygame.Surface((left_width, 50))
countBg.fill(WHITE)

bpsBg = pygame.Surface((left_width, 35))
bpsBg.fill(WHITE)

# Set up the font
comic1 = pygame.font.SysFont("comicsansms", 30, True)
comic2 = pygame.font.SysFont("comicsansms", 18, True)



#============ MIDDLE SECTION ============#
mid_height = (len(gen)*175)
mid_width = 400

middle = pygame.Surface((mid_width,mid_height))
middle.fill(BLUE)

sep2 = pygame.image.load('Separators/border1.jpg') #Separator1

middleBox = scrollbox(mid_height,scrn_y)

for i in range(len(gen)):
    gen[i][0] = generator(gen[i][4],i,gen[i][5]) #Set up class

    gen[i][0].price = gen[i][1] #Set up base price
    gen[i][0].base_income = gen[i][2] #Set up base income

    gen[i][0].update(i)




running = True

#Movement Speed
vel = 3
difference = 0
dragging = False
mouseDown = False

while running:
    pygame.time.delay(10)

    scrolling = False
    scroll_direction = 0
    mouse_x, mouse_y = pygame.mouse.get_pos() # Set mouse x and y positions
    mouse_rel = pygame.mouse.get_rel() #mouse_rel[0] horizontal, [1] for vertical



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEWHEEL:
            scrolling = True
            scroll_direction = event.y  # y will be positive for scrolling down, negative for scrolling up
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True

        elif event.type == pygame.MOUSEMOTION:
            #If mouse is over bar
            if mouse_x > 750 and mouse_x < 770 and mouse_y > middleBox.bar_y and mouse_y < middleBox.bar_y+middleBox.bar_height:
                if dragging == False:
                    difference = mouse_y - middleBox.bar_y
                dragging = True


        elif event.type == pygame.MOUSEBUTTONUP:
            scrolling = False
            mouseDown = False

    #If currently scrolling
    if scrolling:
        
        #Check to see if mouse is in the middle
        if mouse_x > 350 and mouse_x < 770:
                middleBox.bar_y += scroll_direction * vel

    #If currently dragging
    if dragging and mouseDown:
            middleBox.bar_y = mouse_y - difference

    else:
        difference = 0
        dragging = False
    
    if middleBox.bar_y < 0: #If too high
        middleBox.bar_y = 0

    # print(middleBox.bar_y,"is greater than",(scrn_y-middleBox.bar_height))
    if middleBox.bar_y >= scrn_y-middleBox.bar_height: #If too low
        middleBox.bar_y = scrn_y-middleBox.bar_height


    #Change middle canvas based on scrollbar
    bar_y = round(middleBox.bar_y)
    middle_y = -1*(bar_y*middleBox.multi)

    if middleBox.bar_y == scrn_y-middleBox.bar_height:
        middleBox.bar_y += 1 #Adjust for rounding

    
    scrn.fill(WHITE)
#----------------------------------------------------------------#
#====================== ON SCREEN MATERIAL ======================#
#----------------------------------------------------------------#


    #============ LEFT SECTION ============#

    # Update quantites in the left section
    bananaCount = comic1.render((f"{bananas} Bananas"), True, (0,0,0))
    bpsCount = comic2.render((f"BPS: {bps}"), True, (0,0,0))

    scrn.blit(background,(0,0)) #background
    scrn.blit(banana,(150-(banana.get_width()/2),300-(banana.get_height()/2))) #banana

    scrn.blit(countBg,(0,150-(countBg.get_height()/2)))
    countBg.fill(WHITE)
    countBg.blit(bananaCount, (150-(bananaCount.get_width()/2), 0))
    
    scrn.blit(bpsBg,(0,95-(bpsBg.get_height()/2)))
    scrn.blit(bpsCount, ([150-(bpsCount.get_width()/2), 95-(bpsCount.get_height()/2)]))


    scrn.blit(sep1,(300,0)) #Separator1


    #============ MIDDLE SECTION ============#

    # Update quantities in the generator section
    for i in range(len(gen)): 
        gen[i][0].update(i)

    middleBox.box_surface.fill(GREY)
    scrn.blit(middleBox.box_surface,(750,0)) #middleBox
    scrn.blit(middleBox.bar_surface,(750,middleBox.bar_y)) #middleBar
    
    scrn.blit(middle,(350,middle_y))

      
    # it refreshes the window
    pygame.display.update() 


pygame.quit()
