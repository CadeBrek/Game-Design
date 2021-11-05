#Cade Brekken
#10/18/21
#Create a pygame to play
#Mouse position, drawing rectangle, moving rectangle
import pygame as py
import os, time
import os, random
os.system('cls')

#First thing
py.init()

#create window
height = 600
width = 800
colors = {'red':(200,0,0), 'green':(0,200,0), 'blue':(0,0,200), 'purple':(200,0,200), 'white':(255,255,255), 'black':(0,0,0), 'neongreen':(0,200,50), 'brown':(150,100,75), 'orange':(175,75,50)}
screen=py.display.set_mode((width,height))
myColor= colors.get('purple')
screen.fill(myColor)
py.display.set_caption("Moving Square ")
py.display.flip()
#parameters to define our square
x=width/2
y=height/2
wbox=50
hbox=50
Nums={10,11,12,13,14,15,16,17,18,19,20}
xc= random.randint(10,width)
yc= random.randint(10, height)
rad= wbox/2
colorVar= colors.get('white')
#creating object square
#square=py.rect(x,y,wbox,hbox)
square=py.Rect(x,y,wbox,hbox)
#draw rectangle
objColor=colors.get('red')
py.draw.rect(screen, objColor, square)
py.draw.circle(screen, colorVar, (xc,yc), rad)
py.display.flip()
#createspeed to move the object
speed = 5

run=True #Variable to control main loop
while run:
    py.time.delay(100) #Milliseconds
    for anyThing in py.event.get():
        if anyThing.type ==py.QUIT:
            run=False
    keyPressed= py.key.get_pressed()
    if keyPressed[py.K_RIGHT]:
        square.x += speed
    if keyPressed[py.K_LEFT]: 
        square.x -= speed
    if keyPressed[py.K_UP]:
        square.y -= speed
    if keyPressed[py.K_DOWN]: 
        square.y += speed   
    if keyPressed[py.K_d]:
        xc+= speed 
    if keyPressed[py.K_a]: 
        xc-= speed
    if keyPressed[py.K_w]:
        yc -= speed
    if keyPressed[py.K_s]: 
        yc += speed    
    screen.fill(myColor)
    py.draw.rect(screen, objColor, square)
    py.draw.circle(screen, colorVar, (xc,yc), rad)
        while:
            square.y>height
    py.display.update()
py.quit()