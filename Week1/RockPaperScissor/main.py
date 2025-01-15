import random

print("Welcome to Rock Paper Scissor Game!")

print("\nPlease make your Selection")
print("For Rock enter 1; for Paper enter 2; for Scissor enter 3")

computer_choice = random.randint(1, 3)
player_choice = None

# check choice:
def check_choice(option: int):
    """This function check entered option and maps it to piece respectively"""
    if option == 1:
        return "Rock (i.e option 1)"
    elif option == 2:
        return  "Paper (i.e option 2)"
    elif option == 3:
        return  "Scissor (i.e option 3)"
    else:
        return "Invalid"

# check winning:
def check_wining():
    """This func. checks winning"""
    if player_choice == 1:
        if computer_choice == 1:
            print("\nIt was a tie. You both picked Rock")
        elif computer_choice == 2:
            print("\nPaper wraps over Rock! The computer wins!")
        elif computer_choice == 3:
            print("\nRock smashes Scissor! You have won!")

    elif player_choice == 2:
        if computer_choice == 1:
            print("\nPaper wraps over Rock! You have won!")
        elif computer_choice == 2:
            print("\nIt was a tie. You both picked Paper!")
        elif computer_choice == 3:
            print("\nScissor cut through Paper! The computer wins!")

    elif player_choice == 3:
        if computer_choice == 1:
            print("\nRock smashes Scissor! The computer wins!")
        elif computer_choice == 2:
            print("\nScissor cut through Paper! You have won!")
        elif computer_choice == 3:
            print("\nIt was a tie. You both picked Scissor!")

game_on = True
while game_on:
    ask_player = True
    while ask_player:
        try:
            player_choice = int(input("\nEnter a valid option\t"))
        except (ValueError, TypeError):
            print("Only integer value are allowed!")
        else:
            if player_choice not in [1, 2, 3]:
                print("Enter a value within 1 to 3 (inclusively)")
            else:
                break

    # check entries for winning:
    print(f"\nThe computer chose {check_choice(option=computer_choice)}")
    check_wining()

    # ask for another trial
    another_chance = input("\nWill you play again? enter 'y' or 'n'\t")

    if another_chance not in ['yes', 'y']:
        print("Thank you for playing")
        game_on = False
