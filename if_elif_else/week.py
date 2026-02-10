day = input('Enter a day')

# apply the weekday.
if day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday':
    print('Weekday')
elif day == 'saturday' or day == 'sunday':
    print('weekend')
else:
    print('invalid input')