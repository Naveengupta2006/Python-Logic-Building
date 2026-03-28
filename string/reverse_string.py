# 
str1 = input("enter a string: ")

# split manually
words = str1.split()

# reverse manually for using reverse()
reverse_words = []
for c in range(len(words) -1,-1,-1):
    reverse_words.append(words[c])


result = ' '.join(reverse_words)

print('Original string', str1)
print('Result', result)