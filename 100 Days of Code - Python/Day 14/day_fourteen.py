import random
from operator import truediv

import art
import game_data
score = 0
game_over = False

print(art.logo)

def play_round(s):
    a = game_data.data[random.randint(0, len(game_data.data) - 1)]
    b = game_data.data[random.randint(0, len(game_data.data) - 1)]
    answer = 'a'
    if a["follower_count"] < b["follower_count"]:
        answer = 'b'

    print(f"Compare A: {a["name"]}, a {a["description"]} from {a["country"]}")
    print(art.vs)
    print(f"Against B: {b["name"]}, a {b["description"]} from {b["country"]}")

    guess = str(input("Who has more followers? Type 'A' or 'B': ")).lower()
    print("\n" * 20)

    if guess == answer:
        print(art.logo)
        s += 1
        print(f"You're right! Current score: {s}")
    else:
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {s}")
        exit()
    return s


while True:
    score = play_round(score)


