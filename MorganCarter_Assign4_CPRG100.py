'''
CPRG 100 Assignment 4
Morgan Carter
February 7, 2024

This program manipulates data types to create a pizza order.
The program asks users for their name, the variety of
toppings for a pizza and calculates the cost of the pizza.
'''

name = input('Please enter a name: ')
toppings = ['Cheese', 'Mushroom', 'Pineapple', 'Chicken', 'Everything', 'Exit']
#creating a varaible top_choice to hold user's input and enter the while loop
top_choice = 1
#creating an empty list to store user's topping choice inputs that correspond to the top_choice index variable
top_list = []
while top_choice != 0:
    #print out topping options and ask user for their top_choice input
    print('Please select a topping (1-5) and 0 to exit')
    top_num = 1
    for i in toppings:
        if i == toppings[-1]:
            print('0- '+i)
        else:
            print(f'{top_num}'+'- '+ i)
            top_num +=1
    top_choice = int(input())
    #error statement for invalid inputs
    if top_choice < 0 or top_choice > 5:
        print('Invalid input! please try again')
    #correspond top_choice input to toppings list element if input is valid and not zero
    if top_choice > 0 and top_choice < 6:
        top_list.append(toppings[top_choice - 1])
#print output summary statements
print('Customer Name is ' + name)
print('You selected: ' + str(top_list))
#calculate pizza cost total based on number of selected toppings
if len(top_list) == 0:
    print('Your total is $0')
elif len(top_list) == 4 or 'Everything' in top_list:
    print('Yor total is $14')
elif len(top_list) == 3:
    print('Your total is $12')
elif len(top_list) == 2:
    print('Your total is $10')
elif len(top_list) == 1:
    print('Your total is $8')
print('Have a wonderful day')

