user1Input = raw_input("Player 1 - Type R for Rock, SP for Spock, L for Lizard, P for Paper or S for Scissors to make your choice ").lower()
user2Input = raw_input("Player 2 - Type R for Rock, SP for Spock, L for Lizard, P for Paper or S for Scissors to make your choice ").lower()


def checkWinner():
    if(user1Input == user2Input):
        print("Draw")

    if(user1Input == "r" and user2Input == "p"):
        print("Paper covers Rock, Player 2 Wins")
    elif(user1Input == "r" and user2Input == "sp"):
        print("Spock vaporizes Rock, Player 2 Wins")

    elif(user1Input == "p" and user2Input == "s"):
        print("Paper gets cut by Scissors, Player 2 Wins")
    elif(user1Input == "p" and user2Input == "l"):
        print("Paper gets eaten by Lizard. Player2 Wins")

    elif(user1Input == "s" and user2Input == "r"):
        print("Scissors gets crushed by Rock, Player 2 Wins")
    elif(user1Input == "s" and user2Input == "sp"):
        print("Scissors get smashed by Spock")

    elif(user1Input == "p" and user2Input == "r"):
        print("Paper covers Rock, Player 1 Wins")
    elif(user1Input == "sp" and user2Input == "r"):
        print("Spock vaporizes Rock, Player 1 Wins")

    elif(user1Input == "s" and user2Input == "p"):
        print("Paper gets cut by Scissors, Player 1 Wins")
    elif(user1Input == "l" and user2Input == "p"):
        print("Paper gets eaten by Lizard. Player 1 Wins")

    elif(user1Input == "r" and user2Input == "s"):
        print("Scissors gets crushed by Rock, Player 1 Wins")
    elif(user1Input == "sp" and user2Input == "s"):
        print("Scissors get smashed by Spock, Player 1 Wins")
checkWinner()