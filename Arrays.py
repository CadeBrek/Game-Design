#Learning Python Collections

# Cade Brekken
#09/28/21
import os
os.system('cls')
import os,random
#Lists
names = ["Alex", "Jack", "Mary", "Ellen", "Peter", "Ray"]
print(names[1])
for nam in names:
    print(nam, end=" ")
print("\n These are all the names! \n")
#Going in reverse
print(names[-1])
# range of indexes
print(names[2:5])
#change value of an element
names[3]="Betty"
if "Ellen" in names:
    print("You win!")
else:
    print("sorry, you were wrong")
#leinght if a list
print(len(names))
#add elements using append()
names.append("Owen")
print(names)
#add elements using insert()
names.insert(4,"Joan")
print(names)
#copy a list to another list
otherNames= names[2:6].copy()
print(otherNames)
#Guessing Game

compParts=["keyboard", "printer", "motherboard", "CPU", "fans", "storage"]

word= random.choice(compParts)
word = word.lower()
print(word)
for letter in word:
    print("_ ", end = " ")
guess=input("guess the word I am thinking ")
while (guess not in word):
    guess= guess.lower
    if guess in word:
        print ("Good Job")
        break
    else:
        print(" Wrong ")
        guess=input("try again ")
print("thank you for playng")