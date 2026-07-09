import json

class Person:

    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

person = Person('naveen','gupta',20,'male')

# as a string

def show_object(person):
    if isinstance(person,Person):
        return "{} {} age -> {} gender -> {}".format(person.fname, person.lname, person.age, person.gender)
with open('demo.json','w') as f:
    json.dump(person,f, default=show_object)


# as a dict 
def show_object(person):
    if isinstance(person,Person):
        return {'name':person.fname + ' ' + person.lname, 'age':person.age,'gender':person.gender}
with open('demo.json','w') as f:
    json.dump(person,f, default=show_object)