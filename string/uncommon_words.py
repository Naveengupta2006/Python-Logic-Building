# Find uncommon words from two Strings.

# take the input
str1 = input('enter a string: ')
str2 = input('enter a string: ')

# manually using the split function
word_a = str1.split()
word_b = str2.split()

uncommon = []

# using the for loop
for word in word_a:
    if word_a.count(word) == 1 and word not in word_b:
        uncommon.append(word)

for word in word_b:
    if word_b.count(word) == 1 and word not in word_a:
        uncommon.append(word)


print('Word A',str1)
print('Word B',str2)
print('Uncommon', uncommon)                