game_vrs = int(input("how many players 1 or 2:>"))

#sigle player
if game_vrs == 1:
    import random
    game_mode = int(input("give me a number between 1 and 100"))
    if game_mode %2 == 0:
        game = "random"
    else:
        gamemode = "rage"
    
    if game_mode == "random":
        player = int(input("""player make a pick
                        1 rock
                        2 papper
                        3 scissors:>"""))
        pc = random.randint(1,3)
        if player == 1 and pc == 1:
            print("its a tie")
        elif player == 2 and pc == 2:
            print("its a tie")
        elif player == 3 and pc == 3:
            print("its a tie")
        #player 1 wins
        elif player == 1 and pc == 3:
            print("player 1 wins")
        elif player == 2 and pc == 1:
            print("player 1 wins")
        elif player == 3 and pc == 2:
            print("player 1 wins")
        #player 2 wins
        elif player == 3 and pc == 1:
            print("player 2 wins")
        elif player == 1 and pc == 2:
            print("player 2 wins")
        elif player == 1 and pc == 3:
            print("player 2 wins")
    elif game_mode == "rage":
        print("you lost")


#2 player
elif game_vrs == 2:
    player1 = int(input("""player 1 make a pick
                        1 rock
                        2 papper
                        3 scissors:>"""))
    player2 = int(input("""player 2 make a pick
                        1 rock
                        2 papper
                        3 scissors:>"""))
    #tie
    if player1 == 1 and player2 == 1:
        print("its a tie")
    elif player1 == 2 and player2 == 2:
        print("its a tie")
    elif player1 == 3 and player2 == 3:
        print("its a tie")
    #player 1 wins
    elif player1 == 1 and player2 == 3:
        print("player 1 wins")
    elif player1 == 2 and player2 == 1:
        print("player 1 wins")
    elif player1 == 3 and player2 == 2:
        print("player 1 wins")
    #player 2 wins
    elif player1 == 3 and player2 == 1:
        print("player 2 wins")
    elif player1 == 1 and player2 == 2:
        print("player 2 wins")
    elif player1 == 1 and player2 == 3:
        print("player 2 wins")
    else:
        print("error incorect input")
    