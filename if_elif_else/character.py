# Check whether input character is uppercase, lowercase, digit, or special character.

ch = int(input('Enter a character: '))

if ch.isupper():
    print('Upper case')
elif ch.islower():
    print('Lower case')
elif ch.isdigit():
    print('Digits Case')
else:
    print('Special character')            