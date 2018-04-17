import random

"""
A general guide for Hangman
1. Make a word bank - 10 item
2. Pick a random item from the list
3. Add a guess to the list of letters guessed
4.  Reveal letters already guessed
5. Create the win condition


"""

print("Welcome to hangman")
print("Guess the word to win!")

word_bank = ["siege", "semester", "hangman", "computer", "community", "blackjack", "warmups",
             "america", "pycharm", "projects"]

print("You start off with 10 guesses, when you guess wrong wrong then you will lose a guess, the game will end when you \
guess the word or you run out of guesses.")

word = word_bank[random.randint(1, len(word_bank) - 1)]
# print(word)

guesses_left = 10
letters_guessed = []

while word != letters_guessed:

    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print("".join(output))

    if output == list(word):
        exit(0)
    your_guess = input()

    letters_guessed.append(your_guess)
    print(letters_guessed)

    if your_guess in word:
        print("Nice, you got %s" % your_guess)
    else:
        guesses_left -= 1
        print("You guessed %s." % your_guess)
        print("You have %s guesses left" % guesses_left)

    if guesses_left == 0:
        print("Sorry but you have ran out of guesses, the word was (%s)." % word)
        exit(0)
