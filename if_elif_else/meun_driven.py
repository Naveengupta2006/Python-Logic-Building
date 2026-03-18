'''
Write a menu-driven program -
cm to ft
km to miles
USD to INR
exit
'''

def cm_to_ft():
    cm = float(input('enter a cm'))
    ft = cm * 0.0328
    print("Cm to fit", round(ft, 2))

def km_to_miles():
    km = float(input('enter a km'))
    miles = km * 0.621
    print('km to miles', round(miles, 2)) 

def usd_to_inr():
    usd = float(input('enter usd'))
    inr = usd * 83
    print('usd to inr', round(inr, 2))


while True:
    print('---Menu---')
    print('1. cm-to_ft')
    print('2. km_to_miles')
    print('3. usd_to_inr')
    print('exit')


    choice = int(input('enter a number:'))

    if choice == 1:
        cm_to_ft()
    elif choice == 2:
        km_to_miles()
    elif choice == 3:
        usd_to_inr()
    else:
        print('exit')
        
                    
