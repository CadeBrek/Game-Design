#Cade Brekken
#10/13/21
#Easy word game

import random, os
os.system('cls')
def updateWord(word, guesses, letCount):
    for letter in word:
        if letter in guesses:
            print(letter,end=" ")
            letCount+=1
        else:
            print('_', end=' ')
    return letCount
def Menu():
    print("________________________________________")
    print("|                MENU                  |")
    print("|                                      |")
    print("|       1. Animals                     |")
    print("|       2. Planets                     |")
    print("|       3. Fruits                      |")
    print("|       4. ScoreBoard                  |")
    print("|       5. Exit                        |")
    print("|    To play the game select 1-4       |")
    print("|       To exit select 5               |")
    print("________________________________________")
    print()
    sel=input("What would you like to do? ")
    sel=int(sel)
    return sel
def selWord(sel):
    if sel == 1:
        word= random.choice(animals)
    elif sel ==2:
        word= random.choice(planets)
    elif sel ==3: 
        word= random.choice(fruits)
    elif sel ==4:
        scoreBoard()
    elif sel5==5:
        Exit()
    return word

animals=["tiger", "elephant","dog","cat","fish","lion"]
fruits=["banana", "strawberries","orange","apple","kiwi","pear"]
planets=["earth", "moon", "venus", "jupiter", "mercury", "neptune"]

name= input("What is your name? ")
maxScore=0
sel = Menu()
print(sel)
while sel==1 or sel==2 or sel==3:
    print(name, " Good Luck! you have 5 chances to guess")
    
    word= selWord(sel)
    word = word.lower()
    wordCount=len(word)
    turns= wordCount+2
    letCount=0
    guesses=''
    score=0
    letCount=updateWord(word, guesses, letCount)
    while turns > 0 and letCount<wordCount:
        print()
        newguess=input (name + " Give me a letter ")
        newguess= newguess.lower()
        if newguess in word:
            guesses += newguess
            
            print("you guessed one letter ")
        else:
            turns -=1
            print("Sorry, you have ", turns, "turns left")
        letCount=0
        letCount= updateWord(word, guesses, letCount)
    os.system('cls')
    score=3*wordCount+5*turns
    if score > maxScore:
        maxScore=score
    print(maxScore)
    sel=Menu()