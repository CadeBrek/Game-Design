#AmanJaleel

#10/20/21

# Mouse position drawing rectangle moving object

 

import os

import pygame as py

 

py.init() #Here we are initiating

#Now we have to create the window

height= 600

width= 800

colors = {'red':(150,0,0),'green':(0,200,0), 'blue':(0,0,255), 'purple':(150, 0, 150), 'white': (255,255,255), 'black': (0,0,0)}

screen=py.display.set_mode((width,height))

myColor= colors.get('purple')

screen.fill(myColor)

py.display.flip

py.display.set_caption("Moving Square")

py.display.flip()

 

#here we're defining the parameters that will define our square

x=width/2

y=height/2

hbox=50

wbox=50

#here we're creating out object square

square=py.Rect(x,y,wbox,hbox)

 

#now we have to draw our object with the draw command

objColor=colors.get('red')

py.draw.rect(screen, objColor, square)

py.display.update #update and flip are the same thing


speed= 5
run=True #variable to control loop
while run:
    py.time.delay(100) #This is milliseconds
    for anyThing in py.event.get():
        if anyThing.type ==py.QUIT:
            run =False
    keyPressed= py.key.get_pressed()
    if keyPressed[py.K_LEFT]:
        square.x -= speed
        screen.fill(myColor)
        py.display.update 
py.quit()