# case 1 - if the file is not present

# how to write the text file (.txt_file)

f = open('sample.txt','w') # file handler object By using it, you can both read and write.(# it exist on hardrive)
print(f.write('hello world'))
print(f.close)
# since file is closed hence this will not work
f.write('hello')

# write multiline strings
f = open('sample1.txt','w')# it exist on hardrive
f.write('hello world')
f.write('\nhow are you')
f.close()

# case 2 - if the file is already present
f = open('sample.txt','w') # it exist on hardrive
f.write('salman khan')
f.close()


# problem with w mode

# introducting append mode
f = open('sample1.txt','a') # 'a' append mode and 'w - write mode
f.write('\nthis is append  mode')
f.close()

# write lines
l = ['hello\n','hi\n','how are you\n','i am fine\n']
f = open('simple.txt','w')
f.writelines(l)
f.close()


