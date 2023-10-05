

while True:
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
            play_again = input("do you want to play again y/n:>")
            if play_again != "y":
                print("thanks for playing")
                break     