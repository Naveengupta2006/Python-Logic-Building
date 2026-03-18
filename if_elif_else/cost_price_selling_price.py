'''
Write a program that will take user input of cost price
 and selling price and determines whether its a loss or a profit.
 '''

# take a input
cost_price = float(input('enter a number:'))
selling_price = float(input('enter a number:'))

# check profit and loss

if selling_price > cost_price:
    print('Profit')
elif selling_price < cost_price:
    print('Loss')
else:
    print('No profit and No loss')
    
            
