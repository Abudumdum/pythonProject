class Person:
    def __init__(self, firstname, lastname):
        self.FirstName = firstname
        self.Lastname = lastname

    def printname(self):
        print(self.FirstName, self.Lastname)


# class Student(Person):
#     pass

class Student(Person):
    def __init__(self, firstname, lastname, year):
        Person.__init__(self, firstname, lastname)
        # super().__init__(firstname, lastname)
        self.Gradyear = year
    def Welcome(self):
        print('welcome', self.Lastname, self.FirstName, 'to the class of ', self.Gradyear)


x = Student('Mike', 'Olsen', 2030)
x.printname()
print(x.Gradyear)
x.Welcome()

