#garrett
import pygame, os, time
import pygame as py
pygame.init()
os.system('cls')
colors={'red':(150,0,0),'green':(0,200,0),'blue':(0,0,225),'purple':(150,0,150),'white':(225,225,225),'black':(0,0,0),'royal blue':(0,0,128),'orange':(225,165,0)}
color=input("what color do you prefer: red, green, blue , purple, white, black, royal blue, orange?")
height=input("enter the height of the window.")
width=input("enter the width of the window.")
check=True
while check:
    try:
        height=int(height)
        width=int(width)
        if height>100 and width>100 and height<1200 and width<1200:
            check=False
        else:
            print("sorry the variable is not between 100-1200")
    except ValueError:
        print("sorry enter a valid number")
    
screen=pygame.display.set_mode((width,height))
mycolor=colors.get(color)
screen.fill(mycolor)
pygame.display.update()
pygame.display.set_caption("My Game")
run=True
while run:
    pygame.time.delay(1000)
    for anything in pygame.event.get():
        if anything.type==pygame.QUIT:
            run=False
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
#creating object square
square=py.rect(x,y,wbox,hbox)
#draw rectangle
objColor=colors.get('red')
py.draw.rect(screen, objColor, square)
py.display.flip()
#createspedd to move the object
speed = 5

run=True #Variable to control main loop
while run:
    pygame.time.delay(100) #Milliseconds
    for anyThing in pygame.event.get():
        if anyThing.type ==pygame.QUIT:
            run=False
    keyPressed= py.key.get_pressed()
    if keyPressed[py.K_RIGHT]:
        square.x += speed
    if keyPressed[py.K_LEFT]: 
        square.x -= speed
    if keyPressed[py.K_UP]:
        square.y += speed
    if keyPressed[py.K_DOWN]: 
        square.y -= speed     
        screen.fill(myColor)
    py.draw.rect(screen, objColor, square)
    py.display.update()
pygame.quit()
