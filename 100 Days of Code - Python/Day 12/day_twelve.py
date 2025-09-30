#Number guessing game
import random
print("Welcome to the number guessing game! \nI'm thinking of a number between 1 and 100.")
difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': "))

numberOfGuesses = 0
if difficulty == "hard":
    numberOfGuesses = 5
else:
    numberOfGuesses = 10

randomNumber = random.randint(1,100)
gameOver = False
while numberOfGuesses > 0:
    print(f"You have {numberOfGuesses} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess < randomNumber:
        print("Too low.")
        numberOfGuesses -= 1
    elif guess > randomNumber:
        print("Too high.")
        numberOfGuesses -= 1
    else:
        print(f"You got it! The number was {randomNumber}")
        exit()
    if numberOfGuesses > 0:
        print("Guess again.")
print(f"You lose! The number was: {randomNumber}")
