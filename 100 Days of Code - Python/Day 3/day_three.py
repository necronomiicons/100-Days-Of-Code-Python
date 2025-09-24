print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."   . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
''')
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
print("Your at a cross road. Where do you want to go?")
choice = input("Type \"left\" or \"right\" \n")

if choice == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice = input("Type \"swim\" to swim across the lake or \"wait\" to wait for a boat.\n")
    if choice == "wait":
        print("When you arrive at the island, you find three doors.")
        choice = input("Which door will you choose? \"red\", \"yellow\", \"blue\" \n")
        if choice == "red":
            print("You enter a room engulfed in flames. You are burned alive. Game over.")
        elif choice == "blue":
            print("You enter a room full of beasts. You are devoured. Game over.")
        elif choice == "yellow":
            print("You win!")
        else:
            print("Game over.")
    else:
        print("You are attacked by a trout. Game over.")
else:
    print("You fall into a hole. Game over.")
