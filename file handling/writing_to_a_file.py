# case 1 - if the file is not present

# how to write the text file (.txt_file)

f = open('sample.txt','w') # file handler object By using it, you can both read and write.
print(f.write('hello world'))
f.close()