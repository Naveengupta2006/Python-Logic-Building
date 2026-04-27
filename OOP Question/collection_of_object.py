# list of object

class Person:

    def __init__(self, name,gender):
        self.name = name
        self.gender = gender

p1 = Person('nitish','male')
p2 = Person('ankit','male')
p3 = Person('ankita','female')

l = [p1, p2, p3]

print(l)

for i in l:
    print(i.name, i.gender)