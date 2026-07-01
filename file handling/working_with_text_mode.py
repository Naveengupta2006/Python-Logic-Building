'''# working with binary files
with open('image.png','r') as f:
    f.read()
'''

'''# working with binary file
with open('file handling/image.png','rb') as f: # rb -> read binary 
    with open('image_copy.png','wb') as wf: # wb -> write binary
        wf.write(f.read())'''

# working with a big binary file
# working with other data type
with open('sample.txt','w') as f:
    f.write('5') # not 5