#conditinal statment
this_true = False
if this_true ==True:
    pass
elif this_true == True:
    pass
else:
    pass


#nested if statement
name = "anya"
dad = "loid"
mom = "yor"
pepole = ""
if name == "anya":
    pepole = pepole + " my name is anya"
    if dad == "loid":
        pepole = pepole + " my dad is loid"
    elif dad == "tim":
        pepole = pepole + " my dad is tim"
    else:
        pepole = pepole + " i dont know who my dad is"
    
    if mom == "yor":
        pepole = pepole + " My mom is Yor"
    elif mom == "Kiera":
        pepole = pepole + " my mom is Kieria"
    else:
        pepole = pepole + " I dont know who my mom is"
elif name == "loid":
    pepole = pepole + " my name is loid"
    if dad == "anya":
        pepole = pepole + " my dad is loid"
    elif dad == "tim":
        pepole = pepole + " my dad is tim"
    else:
        pepole = pepole + " i dont know who my dad is"
    
    if mom == "yor":
        pepole = pepole + " My mom is Yor"
    elif mom == "Kiera":
        pepole = pepole + " my mom is Kieria"
    else:
        pepole = pepole + " I dont know who my mom is"
elif name == "yor":
    pepole = pepole  + " my name is yor"
    if dad == "loid":
        pepole = pepole + " my dad is loid"
    elif dad == "tim":
        pepole = pepole + " my dad is tim"
    else:
        pepole = pepole + " i dont know who my dad is"
    
    if mom == "anya":
        pepole = pepole + "My mom is Yor"
    elif mom == "Kiera":
        pepole = pepole + "my mom is Kieria"
    else:
        pepole = pepole + "I dont know who my mom is"
print (pepole)
#for loop
for x in range (1,100):
    print (x)

#while loop
count = 0
while count <= 3:
    count = count + 1
    print (count)

# # Nested loop
count2 = 5
for y in range(1,104):
    while count2 <= 104:
        count2 = count2 + 1
        print(count2)

# #break
import random
while True:
    x = random.randit(1,4)
    print(x)
    if x ==3:
        break

# #met condition
if 10>5:
    print("True")

# #faild condition
if 10<5:
    print ("I lie")

#itrate
x = ["cats","dogs","bird"]
y = random.randint(0,2)
print (x[y])

# #infinate loop
# #whale true:
# #   print (Anya Forger)