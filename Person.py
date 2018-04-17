class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print("You slept 2 hours.")


class Employee(Person):
    def __init__(self, name, age, job):
        super(Employee, self).__init__(name, age)
        self.job = job

    def work(self):
        print("%s ,%s years old goes to work at the %s." % (self.name, self.age, self.job))


class Programmer(Employee):
    def __init__(self, name, age, job, computer):
        super(Programmer, self).__init__(name, age, job)
        self.computer = computer


alex = Employee("Alex", 23, "Engineering Company")
Employee.work(alex)


devon = Programmer("Devon", 32, "Engineering Company")
Programmer.work(devon)
