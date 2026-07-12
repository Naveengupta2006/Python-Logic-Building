# why is it important to handle exceptions
# how to handle exceptions
# -> try except block

# let create a file

with open('sample.txt','w') as f:
    f.write('hello')

# try except demo
try:
    with open('sample2.txt','r') as f:
        print(f.read())
except FileNotFoundError:
    print('File not found')


# catching specific exception
try:
    f = open('sample2.txt','r') 
    print(f.read())
    print(m)
except FileNotFoundError:
    print('some error occured')

