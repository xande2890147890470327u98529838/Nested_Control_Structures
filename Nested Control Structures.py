'''
Programmer:Xander Warner
Date: 10/15/19
Program: Double For Loop

This program will nest a For Loop inside of another
For Loop
'''

for i in range(3):
    print("Outer For Loop: " + str(i))
    for l in range(2):
        print("     Inner For Loop: " + str(l))
        
print("\n_____________________\n")


'''
Programmer: Mr. Lange
Date 10/23/19
Program: Categories

This program will ask users of an interest to them
then ask for two items related to that interest
'''

for i in range(4): 
    print("Outer For Loop: " + str(i)) 
    x = 6
    while x >= 0: 
        print("     While Loop " + str(x))
        x = x - 1
