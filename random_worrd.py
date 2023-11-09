import random
words_list=[]
f =open("words.txt","r")
for x in f:
    words_list.append(x)
print (random.choice(words_list))