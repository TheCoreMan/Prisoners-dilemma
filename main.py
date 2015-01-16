# The prisoner's dilemma
print("Start.")

choices = ["Keep quiet", "Rat out"]
countA = 0
countB = 0

def player_a_strategy():
    return 1


def player_b_strategy():
    return 0

def result(res):
    global countA
    global countB
    if res == "A":
        print("Player A won!")
        countB += 3
    if res == "B":
        print("Player B won!")
        countA += 3
    if res == "AB":
        print("Both players win :)")
        countA += 1
        countB += 1
    if res == "0":
        print("Both players lose :(")
        countA += 2
        countB += 2

def start_game(player_a_strategy_arg, player_b_strategy_arg):
    player_a_choice = player_a_strategy_arg()
    player_b_choice = player_b_strategy_arg()

    if player_a_choice == 0:
        if player_b_choice == 0:
            result("AB")
        else:
            result("B")
    else:
        if player_b_choice == 0:
            result("A")
        else:
            result("0")
    print("Number of years in prison for prisoner A: " + str(countA))
    print("Number of years in prison for prisoner B: " + str(countB))

start_game(player_a_strategy, player_b_strategy)
print("Done.")
