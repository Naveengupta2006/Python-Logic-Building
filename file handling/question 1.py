'''Q-1: Write a function get_final_line(filename), which takes filename as input and return final line of the file.
Note: You can choose any file of your choice.'''

def get_final_line(filename):
    with open(filename, 'r') as f:
        return f.readlines()[-1]

# Create the file with some content
with open('filename.txt', 'w') as f:
    f.write("data science\n")
    f.write('python\n')
    f.write('deep learning\n')
    f.write('java\n')

# Call the function and print the returned final line
file = get_final_line('filename.txt')
print(file)


