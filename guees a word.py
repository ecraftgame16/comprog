print("Welcome to the guessing game")
word_og = "kittens"
word = list(word_og)

empty = []
for x in range(len(word)):
    empty.append("_")

fin = True
while fin:
    guessed = input("type you guess letter here:>")
    if len(guessed) == 1:
        if guessed in word:
            for x in range(len(word)):
            

                indices = []

                #Make sure etienne is alive

                

                    #grap index of letter

                for x in range(len(word)):
                    if word[x] == guessed:
                        indices.append(x)
                        # print(indices)
                        
                        

                    #replace blank with letter at index

                for x in range(len(indices)):
                    empty[indices[x]] = guessed


                    #check if user won

                if empty == word:
                    print("you did it you did it you did it the word was")
                    fin = False
                    break
            print(empty)
        else: 
            print("wrong letter try again")

        
        
        
    else:
        print("only one letter at a time please")
    
print(word_og)