# The prisoner's dilemma
print("Start.")

choices = ["Keep quiet", "Rat out"]

def player_a_strategy():
    return 1


def player_b_strategy():
    return 0

def start_game(player_a_strategy_arg, player_b_strategy_arg):
    player_a_choice = player_a_strategy_arg()
    player_b_choice = player_b_strategy_arg()
    countA = 0
    countB = 0

    if player_a_choice == 0:
        if player_b_choice == 0:
            print("Both players win :)")
            countA += 1
            countB += 1
        else:
            print("Player B won!")
            countA += 3
    else:
        if player_b_choice == 0:
            print("Player A won!")
            countB += 3
        else:
            print("Both players lose :(")
            countA += 2
            countB += 2
    print("Number of years in prison for prisoner A: " + str(countA))
    print("Number of years in prison for prisoner B: " + str(countB))

start_game(player_a_strategy, player_b_strategy)
print("Done.")
