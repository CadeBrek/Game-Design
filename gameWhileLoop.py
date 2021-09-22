#Cade Brekken
#Learning how to use while loops

# Place instructions of your game
import os, random 
os.system('cls')

name=input("What is your name ")
print("Hi, ", name)
answer= input("Would you like to play a game ")
while ('y' in answer):
    randy=random.randrange(1,100)
    counter=0
    guess=input("please enter an integer ")
    while(guess != randy):
        try:
            guess=int(guess)
            check=True
        except ValueError:
  
            guess=int(guess)
        guess = randy
        print ("I was here ")
        #try and except so to convert the guess to integer
        #if Check
        #end loop
        answer=input("Do you want to play again")
print("Thank you for playing my game, ", name)