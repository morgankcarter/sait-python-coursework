'''
CPRG 100 Assignment 5
Morgan Carter
February 13, 2024

This program will read the text file 'henryTheSquareEaredCat.txt' and replace
each Square/Squares/square with Pentagon/Pentagons/pentgon.
It will then create a new text file called  'henryThePentagonEaredCat.txt'
and ask the user if they would like to keep or remove the new file.
'''
import os

henry_square = open('henryTheSquareEaredCat.txt', mode = 'r')

#replace pentgon with square
henry_pentagon = []
for line in henry_square:
    if 'Square' in line:
        pentagon_upper = line.replace('Square', 'Pentagon')
        henry_pentagon.append(pentagon_upper)
    elif 'Squares' in line:
        pentagon_plural = line.replace('Squares', 'Pentagons')
        henry_pentagon.append(pentagon_plural)
    elif 'square' in line:
        pentagon_lower = line.replace('square', 'pentagon')
        henry_pentagon.append(pentagon_lower)
    else:
        henry_pentagon.append(line)
henry_square.close()

#write new lines to 'henryThePentagonEaredCat.txt'
with open ('henryThePentagonEaredCat.txt', mode = 'w') as henryThePentagonEaredCat:
    for line in henry_pentagon:
        henryThePentagonEaredCat.write(line)

henryThePentagonEaredCat.close()

#ask user if they would like to keep or remove the new file
print('Do you want to keep the newly generated file "henryThePentagonEaredCat.txt": ')
print('enter y for "yes" and n for "no"')
save_or_delete = input()
if save_or_delete == 'y':
    print('henryThePentagonEaredCat.txt has been saved')
elif save_or_delete == 'n':
    os.remove('henryThePentagonEaredCat.txt')
    print('henryThePentagonEaredCat.txt has been deleted')
