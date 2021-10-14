#Cade Brekken
#10/13/21
#Easy word game
#Choose a difficulty
#Guess a letter to figure out the word and get your name on the scoreboard

import random, os
os.system('cls')
#Updates words and dashes
def updateWord(word, guesses, letCount):
    for letter in word:
        if letter in guesses:
            print(letter,end=" ")
            letCount+=1
        else:
            print('_', end=' ')
    return letCount
def scoreBoard():
    print("Scoreboard")
    myScore=open('score.txt','r')
    print(myScore.read())
    myScore.close()
    answer2=input("Do oyu want to return to the menu ")
    os.system('cls')
def Exitnow():
    myFile=open('score.txt','a')
    myFile.write(name +"\t Highest Score: \t"+str(maxScore))
    myFile.close()
    print("Thanks for playing")
    os._exit
    print()
def Menu():
    print("________________________________________")
    print("|                MENU                  |")
    print("|                                      |")
    print("|            1. Level 1                |")
    print("|            2. Level 2                |")
    print("|            3. Level 3                |")
    print("|            4. ScoreBoard             |")
    print("|            5. Exit                   |")
    print("|     To play the game select 1-4      |")
    print("|           To exit select 5           |")
    print("________________________________________")
    print()
    sel=input("What would you like to do? ")
    sel=int(sel)
    return sel
def selWord(sel):
    if sel == 1:
        word= random.choice(Level1)
    elif sel ==2:
        word= random.choice(Level2)
    elif sel ==3: 
        word= random.choice(Level3)
    elif sel ==4:
        scoreBoard()
    elif sel ==5:
        exit()
    return word

Level1=["tiger", "elephant","dog","cat","fish","lion"]
Level2=["banana", "strawberries","orange","apple","kiwi","pear"]
Level3=["earth", "moon", "venus", "jupiter", "mercury", "neptune"]

name= input("What is your name? ")
maxScore=0
sel = Menu()
if sel ==4:
    scoreBoard()
    sel =Menu()
if sel ==5:
    Exitnow()
    os._exit
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
    if sel ==4:
        scoreBoard()
        sel =Menu()
    if sel ==5:
        Exitnow()
        os._exit