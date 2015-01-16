# The prisoner's dilemma
print("Start.")

choices = ["Keep quiet", "Rat out"]

player_a_choice = int(input("Enter choice for A [0, 1] >"))
player_b_choice = int(input("Enter choice for B [0, 1] >"))

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

print("Done.")