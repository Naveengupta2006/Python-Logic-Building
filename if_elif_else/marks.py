s1 = int(input('Enter a marks: '))
s2 = int(input('Enter a marks: '))
s3 = int(input('Enter a marks: '))

if s1 > s2 and s1 > s3:
    print('Student 1 topper:')
elif s2 > s1 and s2 > s3:
    print('Student 2 topper:')
elif s3 > s1 and s3 > s1:
    print('Student 3 topper:')        