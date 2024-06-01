'''
Morgan Carter
January 16, 2024
This python file asks users for their name, current year, and birth year
and provides an output sentence that includes their name and age
'''

#age list with 2 elements
year = [0,0]

#ask user to input name
fn = input('Please enter your full name: ')

#ask user to input current year and store it as the first element in the age list
cy = input('Please enter the current year: ')
cy = int(cy)
year[0]=cy

#ask user to input birth year and store it as the second element in the age list
by = input('Please enter your birth year: ')
by = int(by)
year[1] = by

#calculate age
age = year[0]-year[1]

#print name and age to user
print ('My name is ' + fn +', and I am '+ str(age)+' years old.')

