# abstraction

# abstract class

from abc import ABC,abstractmethod
class bankapp(ABC):

    def database(self):
        print('connected to database')

    @abstractmethod
    def security(self):
        pass

class mobileapp(bankapp):

    def financial_security(self):
        print('login into mobile')

    def security(self):
        print('mobile security')

mob = mobileapp()

print(mob.security())