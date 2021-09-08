#CadeBrekken
#09/08/21

#We are going to learn how to ask the user for data
#We are going to learn how to loop
star= int(input("Please enter number of stars ")) #allow to get values from the user
#print ("* * * *")
# loop
#variable to count lines
line = star
for Lncounter in range(line):
    for counter in range(star) :
        print("* ", end=" ")
    print()
for Lncounter in range(line):
    for counter in range(star) :
        print("* ", end=" ")
    print()
    star = star-1
