import random

player_one_blackjack = "False"

new_card = random.randint(1, 10)

dealer_blackjack = "False"

print("Welcome to a game called Blackjack")

while player_one_blackjack != "True" or dealer_blackjack != "True":

    dealers_card1 = random.randint(2, 12)

    dealers_card2 = random.randint(2, 12)

    player_one_card1 = random.randint(2, 12)

    player_one_card2 = random.randint(2, 12)

    if dealers_card1 == 12:
        dealers_card1 = "A"

        if dealers_card2 == 12:
            dealers_card2 = "A"

            if player_one_card1 == 12:
                dealers_card1 = "A"

                if player_one_card2 == 12:
                    dealers_card2 = "A"

    print("Your first card is %s" % player_one_card1)

    print("Your second card %s" % player_one_card2)

    Total = player_one_card1 + player_one_card2

    print("Your card total is %s" % Total)

    print("Want a new card? Yes or No?")

    if input("") == "yes":

            print(player_one_card1)
            print(player_one_card2)
            print("Your cards total is %s." % Total)

    if input("") == "no":
        print("Your staying with %s" % Total)