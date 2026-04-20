# How objects access attributes

class person:

    # this is construtor
    def __init__(self, name_input, country_input):
        self.name = name_input  # attributes
        self.country = country_input # attributes

    def greet(self): # greet method inside the class
        if self.country == 'India':
            print('Namste',self.name)
        else:
            print('Hello',self.name)      

# how objects access attributes
p = person('nitish','india')

print(p.country)
print(p.name)

# how to access methods
print(p.greet())

# what if i try to access non-existent attributes
#  print(p.gender)

# Attribute creation from outside of the class
p.gender = 'male'

print(p.gender)