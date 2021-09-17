# Cade Brekken
# 09/16/21
# Strings

txt = "BE HAPPY"
if ("happy" not in txt):
    print("happy is Not present.")

b = "Play, Sports"
print(b[5,2])

# Cade Brekken
# 09/16/21
# Slice

b = "Play, Sports"
print(b[-7:-2])

# Cade Brekken
# 09/16/21
# Modify

a = "Be Creative"
print(a.split(",")) # returns [Be,Creative]

# Cade Brekken
# 09/16/21
#Concaternate

a = "Don't"
b = "Die"
c = a + " " + b
print(c)

# Cade Brekken
# 09/16/21
# Format

quantity = 5.99
itemno = 2
price =  10
myorder = "I want to buy {2} ice cream cones with scoops of vanilla for {0}."
print(myorder.format(quantity, itemno, price))

# Cade Brekken
# 09/16/21
# Escape Character

txt = "I am a boy from \"Texas\" from the south."
print(txt)
