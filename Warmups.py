

def reverse_order(first_name, last_name):
    print(last_name + " " + first_name)

def reverse_order(hi):
    first_name = input("First name")
    last_name = input("Last name")
    print("%s, %s" % (last_name, first_name))
    print(reverse_order(hi))

def add_py(number1, number2, number3):
    print(number1 + number2 + number3)


def repeat(string):
    print(string)
    print(string)
    print(string)

    for x in range(3):
        print(string)

def date(month, day, year):
    print(month + "/" + day + "/" + year)

date("12", "8", "17")
