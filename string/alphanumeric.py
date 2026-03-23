char = input('enter a alphanumeric: ')

digits = [int(c) for c in char if c.isdigit()]

# calculate  sum without using sum function.
total = 0
for d in digits:
    total += d

average = total / len(digits) if len(digits) > 0 else 0

print('char',char)
print('digits', digits)
print('total', total)
print('averages', average)