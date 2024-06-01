'''
CPRG 104
Assignment 3
Morgan Carter
April 7, 2024
'''
from functools import reduce
import re

def int_list_creation(num_values): 
    # Initialize an empty list
    int_list = []

    for i in range(num_values):
        # Get integer input from the user
        value = int(input(f'Please enter the integer value number {i + 1} : '))
        # Append the integer to the list
        int_list.append(value)  
        
    return int_list

#Filter function using lambda
def filter_list(int_values):
    return (filter(lambda x: x % 2 == 0 and x % 3 == 0 and x % 7 == 0, int_values))

#Map function to produce cubes of integer values
def int_cubed(filter_values):
    return map(lambda x: float(x)**3, filter_values)

#List comprehension
def list_comprehension(int_values):
    divisible_cubed = [float(x)**3 for x in int_values if x % 2 == 0 and x % 3 == 0 and x % 7 == 0]
    return divisible_cubed

#sorting the result from list comprehension
def sorting(divisible_cubed):
    sorted_divisible_cubed = sorted(divisible_cubed, reverse=True)
    return sorted_divisible_cubed

#Reduce 
def reduced_list(sorted_divisible_cubed):
    reduce_quotient = reduce(lambda x, y: x * y, sorted_divisible_cubed) / sum(sorted_divisible_cubed)
    return reduce_quotient

#Regular Expressions
def only_alphabets_and_spaces(input_string):
    # Define regex pattern for alphabets and spaces
    pattern = r'^[a-zA-Z\s]*$'
    # Use regex search to check if the input string matches the pattern
    match = re.search(pattern, input_string)
    if match:
        return str(match)  # Return the match object if a match was found
    else:
        return False  # Return False if no match was found 

#test code
print('=====' * 10)
num_values = int(input('Please enter the number of integer values: '))
int_values = int_list_creation(num_values)
print('You entered', int_values)
print('=====' * 10)
print('Using Filter and Map Functions')
filter_values = list(filter_list(int_values))
print('The filtered list is', filter_values)
cube_values = list(int_cubed(filter_values))
print('The cubes list is', cube_values)
print('=====' * 10)
print('Using List Comprehension')
divisible_cubed = list_comprehension(int_values)
print('The cubes list genereated by list comprehension is', divisible_cubed)
sorted_divisible_cubed = sorting(divisible_cubed)
print('The list after sorting is', sorted_divisible_cubed)
print('=====' * 10)
print('Using Reduce')
reduce_quotient = reduced_list(sorted_divisible_cubed)
print(reduce_quotient)
print('=====' * 10)
print('Using Regular Expression')
input_string = input('Please enter a string value: ')
regex_result = only_alphabets_and_spaces(input_string)
if regex_result:
    print(f"'{input_string}' has only alphabets and spaces")
    print(regex_result)  # Print the match object as a string
else:
    print(f"'{input_string}' does not have only alphabets and spaces")

