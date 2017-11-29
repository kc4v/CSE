#
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
    return x**3 + 4 * x**2 + 7 * x - 4


print(f(3))
print(f(4))
print(f(5))



def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >=80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
print(grade_calc(90))
print(grade_calc(80))
print(grade_calc(70))
print(grade_calc(60))