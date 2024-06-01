''''
Morgan Carter
Assignment 3
January 25, 2024
This program will print the 99 Bottles of Beer on the Wall
'''
bottles = 100
while bottles > 0:
    if(bottles > 1):
        print(f'{bottles} bottles of beer on the wall,')
        print(f'{bottles} bottles of beer!')
        print('Take one down,')
        print('Pass it around,')
        bottles = bottles - 1
        if bottles == 1:
            print(f'{bottles} bottle of beer on the wall!')
            print()
        else:
            print(f'{bottles} bottles of beer on the wall!')
            print()
    else:
        print(f'{bottles} bottle of beer on the wall,')
        print(f'{bottles} bottle of beer!')
        print('Take one down,')
        print('Pass it around,')
        print('No more bottles of beer on the wall!')
        bottles = bottles - 1
      
