# Count how many numbers are divisible by 3 between 1 and 50.
count = 0

for i in range(1,51):
    if i % 3 == 0:
        count += 1
print(count)