"""
This is your Tic Tac Toe Game
"""
import random
import math
from display import Board
from itertools import cycle

game_logic = Board()
players = cycle(['other', 'computer'])
current_player = next(players)
print(current_player)

print(f"{game_logic.board}\n!!!Welcome to our amazing Tic Tac Toe Game!!!")

player_pos = None
available_space = [1, 2, 3, 4, 5, 6, 7, 8, 9]
already_occupied = []
game_on = True
next_player = False

while game_on and len(available_space) != 0:
    if current_player == 'other':
        print(f"\n Choose your game position as seen in the bracket.\n"
              f"(this corresponds to your position on the Tic Tac Board)\n"
              f"{game_logic.hint_board}")

        while not next_player:
            # keep asking till the current player select a valid option
            try:
                player_pos = int(input("Which one do you choose?\t"))
            except (ValueError, TypeError):
                print("Only integers are allowed")
                next_player = False
            else:
                if player_pos in already_occupied:
                    print("Position already occupied!")
                    next_player = False
                elif player_pos in available_space:
                    print("do sth")  # attach a sticker at that position
                    already_occupied.append(player_pos)
                    available_space.remove(player_pos)

                    next_player = True
                    # game_on = False
                    current_player = next(players)
                    print(f"the next player will be {current_player}")
                    break
                else:
                    print("not a valid position!")
                    next_player = False
    else:
        print("Computer in play mood")
        current_player = next(players)
        print(f"the next player will be {current_player}")


