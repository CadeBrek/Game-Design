#Cade Brekken
#09/30/21
#Guessing Game (letter by letter)

import random,os
os.system('cls')

animals=["elephant", "seal", "wolf", "monkey", "whale", "bear"]
fruits=["apple", "pear", "banana", "grapes" , "orange", "blueberry"]
planets=["earth", "moon", "venus", "jupiter", "mercury", "neptune"]
name= input("what is your name ")
answer=input(name + " ,Do you want to play ")
while 'y' in answer:       
    print("____________________")
    print("|                  |")
    print("|   Choose Game    |")
    print("|   1 - Animals    |")
    print("|   2 - Fruits     |")
    print("|   3 - Planets    |")
    print("|   4 - ScoreBoard |")
    print("|   5 - Exit       |")
    print("|__________________|")
Dif= input("Enter Dificulty ")
if Dif == 1:
        word= random.choice(animals)
elif Dif ==2:
        word= random.choice(fruits)
else:
        word= random.choice(planets)
        while sel==1 or sel==2 or sel==3:       
            while sel==1 or sel==2 or sel==3:
         print(name, " Good Luck! you have 5 chances to guess")
word= Dif(sel)
word = word.lower()
turns=len(word)+2
check = True
guesses=''
while (turns>0 and check):
        for letter in word:
            if letter in guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        if len(guesses)==len(word):
            check= False
        if check:
            newGuess=input ("\n please enter a letter ")
            if newGuess in word:
                guesses += newGuess
                print(" Good Guess ")
            else:
                turns -=1
                print("Sorry guess again")
answer=input(name + " Do you want to play agian ")
print("Thank you for playing ", name)
print("You guessed right! The word was", word)
letCount=0
letCount=(word, guesses, letCount)
os.system('cls')
score=3+len+5*turns
if score > score:
        maxScore=score
print(maxScore)
sel=Menu()
