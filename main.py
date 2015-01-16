# The prisoner's dilemma
print("Start.")


# CR: Lack of documentation.
class Player:
    # CR: Lack of documentation.
    # CR: strategy should be a function argument, so it can be complex.
    # CR: Code design - Player should have access to some class/interface which give data about the other player's
    #                   decisions and the results so far, so it can use them in his strategy.
    def __init__(self, strat):
        self.years = 0
        self.strategy = strat

P1 = Player(1)
P2 = Player(0)
# CR: Unused.
choices = ["Keep quiet", "Rat out"]


# CR: Commented-out code.
# def player_a_strategy():
#     return 1
#
#
# def player_b_strategy():
#     global first_turn
#     if player_a_strategy() == 1:
#         if first_turn:
#             return 0
#         else:
#             return 1
#     if player_b_strategy() == 0 and first_turn:
#         if first_turn:
#             return 0
#         else:
#             return 1


# CR: Bad design... This function call shouldn't assume the name of the player classes, it needs an arranged interface
#     to get to the players.
def result(res):
    if res == "A":
        print("Player A won!")
        P2.years += 3
        # CR: Commented-out code.
        # P2.strategy = 1
    if res == "B":
        print("Player B won!")
        P1.years += 3
        # CR: Commented-out code.
        # P1.strategy = 1
    if res == "AB":
        print("Both players win :)")
        P1.years += 1
        P2.years += 1
    if res == "0":
        print("Both players lose :(")
        P1.years += 2
        P2.years += 2


def start_game(player_a_strategy, player_b_strategy):
    for x in range(1, 1001):
        player_a_choice = player_a_strategy
        player_b_choice = player_b_strategy
        if player_a_choice == 0:
            if player_b_choice == 0:
                result("AB")
            else:
                result("B")
                player_a_strategy = 1
        else:
            if player_b_choice == 0:
                result("A")
                player_b_strategy = 1
            else:
                result("0")
        x += 1


start_game(P1.strategy, P2.strategy)
print("Number of years in prison for prisoner A: " + str(P1.years))
print("Number of years in prison for prisoner B: " + str(P2.years))

print("Done.")