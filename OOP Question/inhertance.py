
# parent

class user:

    def __init__(self):
        self.name = 'naveen'


    def login(self):
        print('login')



# child class

class student(user):


    def enroll(self):
        print('enroll into the course') 

u = user()
s = student()

print(s.name)
s.login()
s.enroll()