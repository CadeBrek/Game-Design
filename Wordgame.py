import os, random
os.system('cls')

name=input("What is your name? ")
print( "Hi, ",name)
answer=input("Would you like to play my game ")
while ('y' in answer):
    randy=random.randrange(1,100)
    print(randy)
    counter=0
    guess=input("please enter an integer ")
while(guess != randy and counter < 5):
    try:
        guess=int(guess)
        check=True
    except ValueError:
        check=False
if(check):
    if (guess == randy):
            print("you win! # of tries: ", counter+1)
    else:
        print("sorry! You lost, try again")
counter +=1
if guess > randy:
    print("you guessed too high")
else:
    print("you guessed too low")
guess=input("please guess again ")
answer=input("Do you want to play again?")
print("Thank you for playing the game")