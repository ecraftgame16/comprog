import random
words_list=[]
f =open("sowpods.txt","r")
for x in f:
    words_list.append(x)
print (random.choice(words_list))