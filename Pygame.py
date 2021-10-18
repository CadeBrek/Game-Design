#Cade Brekken
#10/18/21
#Create a pygame to play

import pygame, os, time
os.system('cls')

pygame.init()
#Declare the object to display game
#red = (255,0,0)
#purple = (200,0,200)
colors = {'red':(200,0,0), 'green':(0,200,0), 'blue':(0,0,200), 'purple':(200,0,200), 'white':(255,255,255), 'black':(0,0,0), 'neongreen':(0,200,50), 'brown':(150,100,75), 'orange':(175,75,50)}
color= input("What color do you perfer: red,blue,green,purple,white, and brown ")
height= input("Enter the height of the window ")
width= input("Enter the width of your screen ")

height= int(height)
width= int(width)

screen=pygame.display.set_mode((width,height))
myColor= colors.get('color')
purple= colors.get('purple')
neongreen= colors.get('green')
brown= colors.get('brown')
orange= colors.get('orange')
screen.fill(color)
pygame.display.update() #Use to update your screen

pygame.display.set_caption("My Game")
run=True #Variable to control main loop
while run:
    pygame.time.delay(1000) #Milliseconds
    for anyThing in pygame.event.get():
        if anyThing.type ==pygame.QUIT:
            run=False
pygame.quit()
