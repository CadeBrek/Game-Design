#Cade Brekken
# 10/26/21
# Fonts, Blit and creating functions

from typing import Text
import pygame as py, os, time, random

from Pygamea2 import display_subtitle

py.init()

colors = {'red':(200,0,0), 'green':(0,200,0), 'blue':(0,0,200), 'purple':(200,0,200), 'white':(255,255,255), 'black':(0,0,0), 'neongreen':(0,200,50), 'brown':(150,100,75), 'orange':(175,75,50)}
width=800
height=800
black=colors.get('black')
white=colors.get('white')
win=py.display.set_mode((width,height))
win.fill(colors.get('white'))
#title_font=py.font.SysFont('comicsana',80, bold=False, italic=False)
title_font=py.font.SysFont('comicsana',80)
words_font=py.font.SysFont('comicsana',40)
text=title_font.render("message", 1, black)
def display_Title(message, x,y):
    py.time.delay(100)
    text=title_font.render(message,1, colors.get('neongreen'))
    #x= half the screen - half of the text length
    #the y is going to be half of the height -40
    win.blit(text, (x,y))
    py.display.update()
    py.time.delay(100)
def display_Subtitle

run = True
count = 0
while run:
    for eve in py.event.get():
        if eve.type == py.QUIT:
            run = False
    if count==0:
        win.fill(white)
        display_Title(" Settings",width/2-text.get_width()/2,40)
        py.time.delay(200)
        display_subtitle(" Screen Size", 75, 200)
        py.time.delay(200)
        display_subtitle("background color", 80, 350)
        py.time.delay(300)
        display_subtitle("object colors", 80, 450)
        py.time.delay(300)
        display_subtitle("sound (on/off)", 80, 550)
        py.time.delay(300)
    count += 1



x=width/2-text.get_width()
y=height/2-text.get_height()
square=py.Rect(x,y)
py.draw
py.display.update()
