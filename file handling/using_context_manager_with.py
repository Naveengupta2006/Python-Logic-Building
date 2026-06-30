# with 

with open('sample1.txt','w') as f:
    f.write('selon bhai')

# try f.read() now
with open('sample1.txt','r') as f:
    print(f.read())

# moving within a file -> 10 char then 10 char
with open('sample.txt','r') as f:
    print(f.read(10))
    print(f.read(10))