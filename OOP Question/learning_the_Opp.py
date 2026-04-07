class Atm:

    # construtor it is a special function -> superpower
    def __init__(self):  # this is the construtor
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        Hi how can i help you ?
        1. Press 1 to create pin
        2. press 2 to change pin
        3. press 3 to check balance
        4. press 4 to withdraw
        5. Anything else to exit
        """)

        if user_input == '1':
            # create pin
            self.create_pin()
            pass
        elif user_input == '2':
            # change pin
            self.change_pin()
            pass
        elif user_input == '3':
            #check balance
            self.check_balance()
            pass
        elif user_input == '4':
            # withdraw
            pass
        else:
            exit()
    def create_pin(self):
        user_pin = input('enter your pin')
        self.pin = user_pin

        user_balance = int(input('enter balance'))
        self.balance = user_balance

        print('pin created successfully')
        self.menu()

    def change_pin(self):
        old_pin = input('enter old pin')

        if old_pin == self.pin:
            # let him change the pin
            new_pin = input('enter new pin')
            self.pin = new_pin
            print('pin successful')
            self.menu()
        else:
            print('no change')    
            self.menu()

    def check_balance(self):
        user_pin = input('enter your pin')
        if user_pin == self.pin:
            print('Your balance is', self.balance)
        else:
            print('get lost')    



obj = Atm() # create the object  
