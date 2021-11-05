#Aman Jaleel

#10/28/31

#We are creating the setting window as a class

 

import pygame, os, random, time

 

os.system('cls')

pygame.init() #here we're initiating

 

#Lists for menu messages

settingMessages=["screen size", "background colors", "object colors", "sounds on/off"]

#These are global variables

colors= {'black':(0,0,0),

          'red':(255,0,0),

          'green':(0,255,0),

          'blue':(0,0,255),

          'white':(255,255,255),

          'purple':(150,0,150)}

WHITE=colors.get('white')

BLACK=colors.get('black')

GREEN=colors.get('green')

RED=colors.get('red')

BLUE=colors.get('blue')

PURPLE=colors.get('purple')

 

WIDTH=800

HEIGHT=800

wbox=30

hbox=30

x=70

y=150

square=pygame.Rect(x,y, wbox, hbox)

win=pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Setting Window")

#Last but not least, we have to declare the fonts

TITLE_FONT=pygame.font.SysFont('comicsans', 80)

MENU_FONT=pygame.font.SysFont('comicsans', 40)

text= TITLE_FONT.render('message',1,BLACK)

 

def create_NewWindow(messages):

    win.fill(WHITE)

    pygame.time.delay(100)

    text = TITLE_FONT.render(messages,1, BLACK)

    win.fill(WHITE)

    pygame.display.update

 

def display_title(message):

    win.fill(WHITE)

    pygame.time.delay(100)

    text= TITLE_FONT.render(message,1,BLACK)

    xm=WIDTH/2-text.get_width()/2

    ym=40

    win.blit(text, (x,y))

    pygame.display.update

    pygame.time.delay(100)

 

def Menu_function():
    pygame.time.delay(100)
    ym=y
    xm=x+wbox+10
    square.y=ym
    for i in range(0,len(settingMessages)):
        word=settingMessages[i]
        pygame.draw.rect(win, RED, square)
        text=MENU_FONT.render(word,1,BLACK)
        win.blit(text, (xm,ym))
        pygame.display.update()
        pygame.time.delay(100)
        ym +=100
        square.y=ym


display_title("settings")

run=True

while run: #Main loop

    for eve in pygame.event.get():

        if eve.type == pygame.QUIT:

            run=False

        if eve.type ==pygame.MOUSEBUTTONDOWN:
            mouse_presses=pygame.mouse.get_pressed()
            if mouse_presses[0]:

                mouse_pos =pygame.mouse.get_pos()

                print(mouse_pos)

                xp=mouse_pos[0]

                yp=mouse_pos[1]

                print(x,y)

            if xp <x+wbox and yp>y and yp<245:

                create_NewWindow("Screen Size")

                display_title("Screen Size", 40)

        pygame.display.update
