'''
# # Trenten Williams
# # (This is python 2.7)
#
# print(3 + 5)
# print(3 - 5)
# print(3 * 5)
# print(6 / 2)
# print(3 ** 5)
#
#
# print("See if you can figure this out")
# print(5 % 3)
#
#
# car_name: 'Shadow Car'
# car_type: 'Lamborghini Sesto Elemento'
# car_cylinders: 8
# car_mpg: 9000.1
#
# # Inline printing
# print("I have a car called the %s. It's a %s." % car_name, car_type)
#
#
# name = input("What is your name? ")
# print("Hello %s." % name)
#
# age = input("How old are you? ")
# print("Wow %s, That's pretty old." % age)

"""
# Functions


def print_hw():
    print("Hello World")


print_hw()
print_hw()
print_hw()


def say_hi(name):  # name is a parameter
    print("Hello %s." % name)
    print("Enjoy your day.")


say_hi("Trent")


def print_age(name, age):
    print("%s is %d years old" % (name, age))
    age += 1  # age = age + 1
    print("Next year, he will be %d" % age)


print_age("Trent", 14)


def f(x):
    return x ** 3 + 4 * x ** 2 + 7 * x - 4


print(f(3))
print(f(4))
print(f(5))


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"


print(grade_calc(90))
print(grade_calc(80))
print(grade_calc(70))
print(grade_calc(60))


def happy_bday(name):
    print("Happy birthday to you" + ",")
    print("Happy birthday to you" + ",")
    print("Happy birthday to " + name + ",")
    print("Happy birthday to you" + ".")


happy_bday("Trent")

# Loops

for num in range(1000000):
    print(num + 100000000000000000000000000000000000000000000000000000001)

a = 1
while True:
    print(a)

import random

number = random.randint(1, 2)
print(number)
# Trenten Williams
print("Welcome to the guessing game, you get 5 guesses, so use them well")

number_chosen = input("Guess the number ")

guesses = 5

print(str(number) == number_chosen)

if number_chosen <= number:

# Trenten Williams
print("Welcome to the guessing game, you get 5 guesses between numbers 1-50, so use them well")

import random

number = random.randint(1, 19)
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
        guesses -= 1
        print(number)


    elif number_chosen > (str(number)):
        print("Sorry, but it's lower than that")
        guesses -= 1

import random

rounds = 0

money = 15

while money > 0:
    print("Type yes to continue or type no to stop")
    bet = input("Bet $1 to get even more money")

    if bet == "yes":
        t = random.randint(1, 6)

        t2 = random.randint(1, 6)

        print("You ")
# The input command ALWAYS gives a string
"""
# Lists

the_count = [1, 2, 3, 4, 5]
shopping_list = ["Noodles", "Eggrolls", "Milk", "Rice", "Soda", "Chips"]

print(shopping_list[2])

print(len(shopping_list))

# Going through a list
for item in shopping_list:
    print(the_count)

for num in the_count:
    print(num * 2)

len(shopping_list)    # Gives me the length of the list
range(3)     # Gives a list of the numbers 0 through 2
range(len(shopping_list))   # A list of EVERY index in a list

for num in range(len(shopping_list)):
    item = shopping_list[num]
    print("The item at index %d is %s" % (num + 1, item))

# Turn things into a list
str1 = "Hello class!"
listOne = list(str1)
print(listOne)
listOne[11] = '.'
print(listOne)
print("".join(listOne))

# Add things to list
shopping_list.append("Coka cola")
print(shopping_list)

# Removing things from a list
shopping_list.remove("Chips")
print(shopping_list)
shopping_list.pop(0)
print(shopping_list)

# the string class
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.punctuation)
print(string.digits)

# Dealing with strings
strTwo = "ThIS Is A vEry OlD SenTanCe"
lowercase = strTwo.lower()
print(lowercase)
'''
# Dictionaries - Made up of Key: Value pairs
dictionary = {'name': 'Lance', 'age': 23, 'height': 5 * 12 + 7}

# Accessing dictionaries
print(dictionary['name'])
print(dictionary['age'])
print(dictionary['height'])

# Adding to a dictionary
dictionary['weight'] = 280
print(dictionary)

large_dictionary = {
    'CA': 'California',
    'FL': 'Florida',
    'OH': 'Ohio'
}
print(large_dictionary['CA'])

larger_dictionary = {
    'CA': [
        'Fresno',
        'Sacramento',
        'Los Angele'
    ],
    'FL': [
        'Tampa',
        'Orlando',
        'Miami'
    ],
    'OH': [
        'Cleavland',
        'Cincinnati',
    ]
}
print(larger_dictionary['FL'])
print(larger_dictionary['OH'][1])

largest_dictionary = {
    'CA': {
        'NAME': 'California',
        'POPULATION': 39250000,
        'BORDER ST': [
            'Oregon',
            'Nevada',
            'Arizona'
        ]
    },
    'AZ': {
        'NAME': 'Arizona',
        'POPULATION': 6931000,
        'BORDER ST': [
            'California',
            'Utah',
            'Nevada',
            'New Mexico'
        ]
    },
    'NY': {
        'NAME': "New York",
        'POPULATION': 19750000,
        'BORDER ST': [
            'Vermont',
            'Massachusetts',
            'Connecticut',
            'Pennsylvania',
            'New Jersey'
        ]
    }
}

current_node = largest_dictionary['CA']
print(current_node)
print(current_node['NAME'])
print(current_node['POPULATION'])

world_map = ()


# Defining functions
def hello_world():
    print("Hello World!")
hello_world()


def square_it(number):
    return number ** 2


square_it(3)
print(square_it(3))


def tip_calc(subtotal):
    tax_amt = subtotal * 0.18
    return tax_amt


0.18 # tax_amt CANNOT be used outside of the def!


def total_bill(bill_amt):
    total = bill_amt + tip_calc(bill_amt)
    print("Your total bill is %d" % total)


total_bill(100)


def distance(x1, y1, x2, y2):
    inside = (x2 - x1) ** 2 + (y2 - y1) ** 2
    answer = inside ** 0.5  # This is a square root
    return answer


print(distance(0, 0, 3, 4))


