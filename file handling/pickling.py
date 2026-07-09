class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print('Hi my name is ',self.name,'and i am ',self.age,'years old')

p = Person('naveen',20)

# pickle dump
import pickle

with open('person.pkl','wb') as f:
    pickle.dump(p,f)

import pickle

with open('person.pkl','rb') as f:
    pickle.load(f)


