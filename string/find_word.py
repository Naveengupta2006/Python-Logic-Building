def find_word(sentence, word):
    words = sentence.split()
    location = 1

    for w in words:
        if w == word:
            return f"location of word is {location}"
        
        location += 1

    return'word not found in sentence.'

sentence = input('enter the sentence: ')
word = input('enter the word to find: ')

result = find_word(sentence, word)
print(result)


