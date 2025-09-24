import random

print("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
player_choice = int(input())
computer_choice = random.randint(0,2)

if player_choice == 0:#rock

    match computer_choice:
        case 0:#rock
            print("You both chose rock. You tie.")
        case 1:#paper
            print("You chose rock. The computer chose paper. The computer wins.")
        case 2:#scissors
            print("You chose rock. The computer chose scissors. You win.")
        case _:#any other input
            print("Invalid input.")
elif player_choice == 1:#paper
    match computer_choice:
        case 0:  # rock
            print("You chose paper. The computer rock. You win.")
        case 1:  # paper
            print("You both chose paper. You tie.")
        case 2:  # scissors
            print("You chose paper. The computer chose scissors. The computer wins.")
        case _:  # any other input
            print("Invalid input.")
else:
    match computer_choice:
        case 0:  # rock
            print("You chose scissors. The computer chose rock. The computer wins.")
        case 1:  # paper
            print("You chose scissors. The computer chose paper. You win.")
        case 2:  # scissors
            print("You both chose scissors. You tie.")
        case _:  # any other input
            print("Invalid input.")



