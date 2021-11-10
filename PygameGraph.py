#Cade Brekken
#11/9/21
import os
import pygame as py, time, sys

py.init()
py.time.delay(100)


height= 700
width= 800

colors= {'red':(150,0,0), 'green': (0,200,0), 'blue':(0,0,255), 'purple':(150, 0, 150), 'white':(255,255,255), 'black':(0,0,0)}
screen=py.display.set_mode((width,height))
py.display.flip()
green=colors.get('green')
red=colors.get('red')
blue=colors.get('blue')

screen = py.display.set_mode((width, height))
x=200
y=200
wbox=50
hbox=50
boldX=width-300
boldY=height-200

screen.fill(green)
py.display.set_caption("Boulder game")

boulder=py.Rect(boldX,boldY,100,200)
rect = py.Rect(x, y, hbox, wbox)
COUNT = 10
jumpCount = COUNT
Jump = False 
run=True
while run:
    for ev in py.event.get():
        if ev.type == py.QUIT:
            run=False

        speed = 2 
        keyBoardkey = py.key.get_pressed()
    if keyBoardkey [py.K_LEFT]:
        if rect.colliderect(boulder):
            print("collide")
            rect.x +=5
        else:
            rect.x -= speed 
    if keyBoardkey [py.K_RIGHT]:
        if rect.colliderect(boulder):
            rect.x -=5
        else:
            rect.x += speed 
    if not Jump:
        if keyBoardkey[py.K_UP]:
            rect.y -= speed
        if keyBoardkey[py.K_DOWN]:
            if rect.colliderect(boulder):
                rect.y -=5
            else:
                rect.y += speed
        if keyBoardkey[py.K_SPACE]:
            Jump = True
    else:
        if jumpCount>=-COUNT:
            if rect.colliderect(boulder):
                rect.y= rect.y-5
                Jump=False
                jumpCount=COUNT
            else:
                rect.y-= jumpCount*abs(jumpCount)/2
                jumpCount -=1
        else:
            jumpCount=COUNT
            Jump=False

    rad= wbox/2
    if rect.y > height - hbox : rect.y = height - hbox
    if rad < y : rad = y 
    if rad < 0 : rad = 0
    if rad > width-x : rad = width -x 
    screen.fill(green)
    py.draw.rect(screen,(red),rect)
    py.draw.rect(screen,blue,boulder)
    py.display.update()
    py.time.delay(30)