import os, random
os.system('cls')

#Guessing Game

compParts=["keyboard", "printer", "motherboard", "CPU", "fans", "storage"]

word= random.choice(compParts)
word = word.lower()
print(word)
for letter in word:
    print("_ ", end = " ")
    print(letter)
guess=input("guess the word I am thinking ")
while (guess not in word):
    guess= guess.lower
    if guess in word:
        print ("Good Job")
        break
    else:
        print(" Wrong ")
        guess=input("try again ")
print("thank you for playing")
