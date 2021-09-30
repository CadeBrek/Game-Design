#Cade Brekken
#09/30/21
#Guessing Game (letter by letter)

import os, random
os.system('cls')

animals=["elephant", "seal", "wolf", "monkey", "whale", "bear"]
name= input("what is your name ")
answer=input(name + " ,Do you want to play ")
while 'y' in answer:
    word= random.choice(animals)
    word = word.lower()
    print(word)
    turns=len(word)+2
    check = True
    guesses=''
    while (turns>0 or check):
        for letter in word:
            if letter in guesses:
                print(letter, end=" " )
                if len(guesses)==len(word):
                    check = False
            else:
                print ("_", end= " ")
            newGuess=input ("\n please enter a letter ")
            if newGuess in word:
                guesses += newGuess
                print(" Good Guess ")
        else:
            turns -=1
            print("Sorry guess again")
    answer=input(name + "Do you want to play agian ")
print("Thank you for playing ", name)
