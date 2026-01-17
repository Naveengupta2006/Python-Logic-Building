# Count the frequency of each word in a sentence.

sentence = 'data science is fun and data science is powerful'

words = sentence.lower().split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)    