#CAde Brekken
#10/06/21
#We are going to learn how to to
#write ('w')
#read ('r')
#append('a')
#close()
import os,time

#To create a file you must declare a variable name so we can open the file
# this is the way to open and create a file
myFile=open('score.txt', 'w')
myFile.write("Hello there, \nMy name is Cade \t 1234")
myFile.close() #ALWAYS CLOSE A FILE as soon as yiu don't need it
# this is the way to open and read a file
myFile=open('score.txt', 'r')
print(myFile.read())
myFile.close()
#Write things on the file, 'w' will delete what is on the file and write over it
anotherFile=open('score.txt', 'w')
anotherFile.write("Sorry I changed my mind")
anotherFile.close()
#reprint
myFile=open('score.txt', 'r')
print(myFile.read())
myFile.close()
#append
anotherFile=open('score.txt', 'a')
anotherFile.write("\n Let's try again \n The score is: \t 23")
anotherFile.close()
myFile=open('score.txt', 'r')
print(myFile.readline())
print(myFile.readline())
myFile.close()