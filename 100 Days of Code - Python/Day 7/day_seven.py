#Hangman
import random
words = ["strong", "tired", "silly", "whimsical", "aloof"]

guessed_letters = []

word_to_guess = str(words[random.randint(0, len(words)-1)])
number_of_guesses = 6
def print_display(d):
    d = ""
    for i in range(0, len(word_to_guess)):
        if guessed_letters.__contains__(word_to_guess[i]):
            d += word_to_guess[i]
        else:
            d += "_"
    print(d)
    return d



display = ""
print_display(display)


while display != word_to_guess:

    guess = input("Guess a letter: ").lower()
    if not guessed_letters.__contains__(guess):
        guessed_letters.append(guess)
    else:
        print("Already guessed!")
        continue
    if not word_to_guess.__contains__(guess):
        number_of_guesses -= 1
        print(guess + " was not in the word.")
        print(str(number_of_guesses) + "/6 lives left")
    display = print_display(display)

    if number_of_guesses <= 0:
        print("You lose! Word was: " + word_to_guess)
        exit()

print("You win!")