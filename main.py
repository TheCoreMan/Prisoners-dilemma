# The prisoner's dilemma
print("Start.")


# CR: Lack of documentation.
class Player:
    # CLASS
    # This class represents the players in the game.
    # The __init__ of the class has a strategy argument.
    # It sets a years attribute to 0 and a strategy attribute to start.
    # Over the course of the game, the years attribute increases.
    # CR: strategy should be a function argument, so it can be complex.
    # CR: Code design - Player should have access to some class/interface which give data about the other player's
    # decisions and the results so far, so it can use them in his strategy.

    def __init__(self, strat):
        self.years = 0
        self.strategy = strat
        self.choices = []

    def stratlist(self, strat):
        self.choices.append(strat)


def player_1_strategy():
    return 1


def player_2_strategy():
    return 0


P1 = Player(player_1_strategy)
P2 = Player(player_2_strategy)


# CR: Bad design... This function call shouldn't assume the name of the player classes,
#     it needs an arranged interface to get to the players.


def result(res):
    if res == "A":
        print("Player A won!")
        P2.years += 3
    if res == "B":
        print("Player B won!")
        P1.years += 3
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
                P1.stratlist(str(player_a_choice))
                P2.stratlist(str(player_b_choice))
            else:
                result("B")
                P1.stratlist(str(player_a_choice))
                P2.stratlist(str(player_b_choice))
                player_a_strategy = 1
        else:
            if player_b_choice == 0:
                result("A")
                P1.stratlist(str(player_a_choice))
                P2.stratlist(str(player_b_choice))
                player_b_strategy = 1
            else:
                result("0")
                P1.stratlist(str(player_a_choice))
                P2.stratlist(str(player_b_choice))
        x += 1


start_game(P1.strategy, P2.strategy)
print("Number of years in prison for prisoner A: " + str(P1.years))
print("Number of years in prison for prisoner B: " + str(P2.years))
print(P1.choices)
print(P2.choices)

print("Done.")