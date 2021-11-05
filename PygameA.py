#Aman Jaleel
#We're making a game where the circle eats the square
import pygame, os, random, math
from pygame.draw import circle
import pygame as py
os.system ('cls') 
pygame.init()
check=True
height=500
width=500
colors = {'purple':(150,0,150), 'red':(255,0,0), 'white': (255,255,255)}
keyList = list(colors.keys())
#we just initiated
while check:
    color = 'purple'
    try:
        height= int(height)
        width=int(width)
        check = False
    except ValueError:
        check = True
color= colors.get(color)
window= pygame.display.set_mode((height,width))
window.fill(color)
pygame.display.flip()
rect=pygame.Rect
x=height/2
y=width/2
hbox=50
wbox=50
speed=5
radius = hbox/2
xc = random.randint(25, 500)
yc = random.randint(25, 500)
square=py.Rect(x,y,wbox,hbox)
#draw rectangle
objColor=colors.get('red')
othColor=colors.get('white')
pygame.draw.rect(window, objColor, square)
py.draw.circle(window, othColor, (xc,yc), radius)
py.display.flip()
run= True
while run:
    pygame.time.delay(50)
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            run= False
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
    window.fill(color)
    py.draw.rect(window, objColor, square)
    py.draw.circle(window, othColor, (xc,yc), radius)   
pygame.display.update()
pygame.quit()
