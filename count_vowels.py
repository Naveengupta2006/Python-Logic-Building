def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

print(count_vowels('Hello World'))
print(count_vowels('PYTHON'))        