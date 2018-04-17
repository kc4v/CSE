import random

rounds = 0

money = 15

most_money = 15.00

highest_round = 0

while money > 0:

    t = random.randint(1, 6)

    t2 = random.randint(1, 6)

    print("You made a bet of one dollar")

    if (t + t2) == 7:
        money += 4
        print("You won your bet.")
        print("You got your dollar back plus a 4 dollar bonus.")
        print("$%s.00 left." % money)

    if (t + t2) != 7:
        money -= 1
        print("You have lost your bet")
        print("$%s.00 dollars left." % money)
        rounds += 1

    if money >= most_money:
        left_over_money = (money - most_money)
        most_money = left_over_money + most_money
        highest_round = rounds
print("GAAAAAAAMMMMEEEEE OOOOOVVVVVEEEEERRRR. You lose.")
print("You did %s rounds but you should of stopped when you had $%s0 dollars on round %s." % (rounds, most_money,
                                                                                              highest_round))
