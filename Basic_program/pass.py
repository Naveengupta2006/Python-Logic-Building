password = input('Enter a password: ')

lenght = len(password)

if lenght < 6:
    print('weak')
elif lenght <= 10:
    print('medium')
else:
    print('strong')    