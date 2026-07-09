'''Q-2: Read through a text file, line by line. Use a dict to keep track of 
how many times each vowel (a, e, i, o, and u) appears in the file. Print the 
resulting tabulation -- dictionary.
'''


# Create a sample text file to read from
with open('demo.txt', 'w') as f:
    f.write("Hello World!\nThis is a demo text file for vowel counting.\n")

# create dictionary
vowels = {
    'a':0,
    'e':0,
    'i':0,
    'o':0,
    'u':0
} 

# Read through the file line by line
with open('demo.txt','r') as f:
    for line in f:
        for ch in line.lower():
            if ch in vowels:
                vowels[ch] += 1

print("Vowel counts:", vowels)
