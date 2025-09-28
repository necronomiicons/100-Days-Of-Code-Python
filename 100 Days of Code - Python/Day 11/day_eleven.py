#Blackjack
import random

deck = [1, 2,3,4,5,6,7,8,9,"Joker", "Queen", "King", "Ace"]

def get_card_total(a):
    total = 0
    add_ace = False
    for i in range(0, len(a)):
        if str(a[i]).isalpha():
            if a[i] == "Ace":
                add_ace = True
            else:
                total += 10
        else:
            total += int(a[i])

    if add_ace:
        total = total + 1 if total > 11 else total + 10
    return total

def display_cards(a, b):
    print(f"Your cards: {a}, current total: {get_card_total(a)}")
    print(f"Computer's first card: {b[0]}")

def display_final_cards(a,b):
    print(f"Your cards: {a}, final total: {get_card_total(a)}")
    print(f"Computer's cards: {b}, final total: {get_card_total(b)}")

new_game = 'y'
while new_game == 'y':
    game_over = "False"
    player_cards = []
    computer_cards = []

    for i in range(2):
        player_cards.append(deck[random.randint(0, len(deck)-1)])
        computer_cards.append(deck[random.randint(0, len(deck)-1)])

    choice = 'y'
    while choice == 'y':
        display_cards(player_cards, computer_cards)
        choice = input("Type 'y' to draw another card. Type 'n' to pass.")
        if choice == 'y':
            player_cards.append(deck[random.randint(0, len(deck) - 1)])
            if get_card_total(player_cards) > 21:
                display_cards(player_cards, computer_cards)
                display_final_cards(player_cards, computer_cards)
                print(f"You went over! You lose!")
                game_over = True

    if game_over == "False":

        while get_card_total(computer_cards) < 16:
            computer_cards.append(deck[random.randint(0, len(deck) - 1)])

        display_final_cards(player_cards, computer_cards)

        if get_card_total(computer_cards) == 21:
            print(f"Computer got blackjack. You lose!")
        elif get_card_total(player_cards) == 21:
            print(f"You got blackjack. You win!")
        elif get_card_total(computer_cards) > 21:
            print(f"Computer went over! You win!")
        elif get_card_total(player_cards) > get_card_total(computer_cards):
            print(f"Your score was higher! You win!")
        elif get_card_total(player_cards) < get_card_total(computer_cards):
            print(f"Computer score was higher! You lose!")
        else:
            print("Tie!")
    new_game = input("Play again? Type 'y' or 'n' :")




