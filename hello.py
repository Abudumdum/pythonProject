class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print('Hello my name is ' + self.name)






p1 = Person('john', 36)
p1.age = 57
del p1.age
print(p1.name)
print(p1.age)
p1.myfunc()

