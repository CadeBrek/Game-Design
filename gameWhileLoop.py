#Cade Brekken
#Learning how to use while loops

# Place instructions of your game
import os, random 
os.system('cls')

name=input("What is your name ")
print("Hi, ", name)
answer= input("Would you like to play a game ")
while ('Yes' in answer):
    randy=random.randrange(1,100)
    print(randy)
    counter=0
    guess=input("please enter an integer ")
    while(guess != randy):
        try:
            guess=int(guess)
            check=True
        except ValueError:
            check=False
        if(check):
            if guess==randy:
                print("You win, # of tries", counter+1)
                break
        else: 
            print("Sorry, Try again")
            counter +=1
            if guess >randy:
                print("you guessed to high")
            else:
                print("you guessed to low")
        guess=input("please guess again ")

    
print("Thank you for playing my game, ", name)