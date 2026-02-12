time = int(input('Enter a time: '))

if 0 <= time < 12:
    print('its AM')
elif 12 <= time < 23:
    print('its PM')
else:
    print('invalid time')        