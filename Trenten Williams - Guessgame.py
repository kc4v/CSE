import random

# Trenten Williams
print("Welcome to the guessing game, you get 5 guesses between numbers 1-50, so use them well")


number = random.randint(1, 20)
# print(number)


guesses = 5
number_chosen = 0
# print(str(number) == number_chosen)

while guesses > 0 and number_chosen != (str(number)):
    number_chosen = input("Guess the number ")

    if number_chosen < (str(number)):
        print("Sorry, but its higher than that")
        guesses -= 1

    elif number_chosen == (str(number)):
        print("You got it, nice job")
        print(number)

    elif number_chosen > (str(number)):
        print("Sorry, but it's lower than that")
        guesses -= 1


if guesses == 0:
    print("You got it, jk you got it wrong, the number was " + str(number))
