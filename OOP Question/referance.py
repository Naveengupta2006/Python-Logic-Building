'''
1. referance variables hold the object
2. we can create object without referance variable as well
3. An object can have multiple referance variable
4. Assigning a new referance variable to an exiting object does not create a new object.

'''

# object without a referance

class person:

    def __init__(self):
        self.name = 'naveen'
        self.gender = 'male'

p = person()
q = p # same memory address  


# multiple ref
print(p)
print(q)

# change attribute value with the help of 2nd object
print(p.name)
print(q.name)
q.name = 'ankit'
print(q.name)
print(p.name)