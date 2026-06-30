# benefit? -> to load a big file in memrory

big_L = ['hello world' for i in range(1000)]

with open('big.txt','w') as f:
    f.writelines(big_L)

with open('big.txt','r') as f:

    chunk_size = 100

    while len(f.read(chunk_size)) > 0:
        
