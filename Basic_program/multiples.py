number_checks = int(input('Enter a number: '))

if number_checks % 3 == 0 and number_checks % 7 == 0:
    print('Number multiple of both 3 and 7')
elif number_checks % 3 == 0:
    print('Number multiple of 3')
elif number_checks % 7 == 0:
    print('Number multiple of 7')
else:
    print('Number not multiple by both:')                