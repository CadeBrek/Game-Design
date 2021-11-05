#Cade Brekke
#10/28/21

import pygame, os,random,time

os.system('cls')

pygame.init()
settingMessages=["Screen Size", "Background Colors", "Object Colors", "Sound On/Off"]
#Global Variables
colors = {'red':(200,0,0), 'green':(0,200,0), 'blue':(0,0,200), 'purple':(200,0,200), 'white':(255,255,255), 'black':(0,0,0), 'neongreen':(0,200,50), 'brown':(150,100,75), 'orange':(175,75,50)}
White=colors.get('white')
Black=colors.get('black')
Orange=colors.get('orange')

Width=800
Height=800
wbox=30
hbox=30
x=70
y=150
win=pygame.display.set_mode((Width,Height))
pygame.display.set_caption(" Settings")
square=pygame.Rect(x,y, wbox, hbox)
#Declare Fonts
Title_Font=pygame.font.SysFont('comicsans', 80)
Menu_Font=pygame.font.SysFont('comicsans', 40)
text= Title_Font.render('message', 1,Black)

def create_NewWindow(winTitle):
    pygame.display.set_caption(winTitle)
    win.fill(White)
    pygame.display.update

def display_Title(message):
    win.fill(White)
    pygame.time.delay(100)
    text= Title_Font.render(message, 1,Black)
    xm=Width/2-text.get_width()/2
    ym=40
    win.blit(text, (xm,ym))
    pygame.display.update()
    pygame.time.delay(100)
def Menu_function():
    pygame.time.delay(100)
    ym=y
    xm=x+wbox+10
    square.y=ym
    for i in range(0,len(settingMessages)):
        word=settingMessages[i]
        pygame.draw.rect(win, Orange, square)
        text=Menu_Font.render(word,1,Black)
        win.blit(text, (xm,ym))
        pygame.display.update()
        pygame.time.delay(100)
        ym +=100
        square.y=ym

display_Title('MAIN MENU')
Menu_function()

run=True

while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run=False
        if eve.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                mouse_pos =pygame.mouse.get_pos()
                print(mouse_pos)
                xp=mouse_pos[0]
                yp=mouse_pos[1]
                print(x,y)
                if xp>=x <x+wbox and yp>150 and yp<175:
                    create_NewWindow("Instruction")
                    display_Title('Instructions')
                if xp>=70 <x+wbox and yp>250 and yp<275:
                    create_NewWindow("Level 1")
                    display_Title('LEVEL 1')
                if xp>=x <x+wbox and yp>350 and yp<375:
                    create_NewWindow("Level 2")
                    display_Title('LEVEL 2')
                if xp>=x <x+wbox and yp>450 and yp<475:
                    create_NewWindow("Settings")
                    display_Title('SETTINGS')


display_Title("Settings")
Menu_function()

run=True

while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run=False
        if eve.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                mouse_pos =pygame.mouse.get_pos()
                print(mouse_pos)
                xp=mouse_pos[0]
                yp=mouse_pos[1]
                print(x,y)
                if xp>=x <x+wbox and yp>450 and yp>475:
                    Menu_function(settingMessages)
                    display_Title("Settings")
                if xp>=x <x+wbox and yp>150 and yp<175:
                    create_NewWindow("Screen Size")
                    display_Title('SCREEN SIZE')
                if xp>=70 <x+wbox and yp>250 and yp<275:
                    create_NewWindow("Background Colors")
                    display_Title('BACKGROUND COLORS')
                if xp>=x <x+wbox and yp>350 and yp<375:
                    create_NewWindow("Object Colors")
                    display_Title('OBJECT COLORS')
                if xp>=x <x+wbox and yp>450 and yp<475:
                    create_NewWindow("Sound On/Off")
                    display_Title('SOUND CONTROL')



                    print("("+str(mouse_pos[0])+","+ str(mouse_pos[1])+")")
        pygame.display.update()



        