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

    if player_a_choice == 0:
        if player_b_choice == 0:
            print("Both players win :)")
        else:
            print("Player B won!")
    else:
        if player_b_choice == 0:
            print("Player A won!")
        else:
            print("Both players lose :(")

start_game(player_a_strategy, player_b_strategy)

print("Done.")
