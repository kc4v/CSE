

def say_hi(name):  # name is a parameter
    print("Hello %s." % name)
    print("Enjoy your day.")


say_hi("Trent")


def print_age(name, age):
    print("%s is %d years old" % (name, age))
    age += 1  # age = age + 1
    print("Next year, he will be %d" % age)


print_age("Trent", 14)


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


 def happy_bday(name):
    print("Happy birthday to you" + ",")
    print("Happy birthday to you" + ",")
    print("Happy birthday to " + name + ",")
    print("Happy birthday to you" + ".")

 happy_bday("Trent")

# Loops

for num in range(10):
    print(num + 1)

import random
print(random.randint(0, 10))

# Comparisons
print(1 == 1)  # Is 1 equal to 1?
print(1 != 2)  # Is 1 not equal to 2?
print(10 <= 15)
print(not False)

# Recasting
c = '1'
print(c == 1)  # prints false
print(int(c) == 1)   # Both are ints
print(c == str(1))   # Both are strings

# The input command ALWAYS gives a string
