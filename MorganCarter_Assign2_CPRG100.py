'''
Morgan Carter
January 17, 2024
This python program asks for a user's first name and the temperature in
celsius. It then converts the temperature to Fahrenheit and prints the
value. Once the temperature in F is determined, it returns a print statement
that describes the weather.
'''

fn = input('Enter your full name: ')
celsius = float(input('Enter temperature in celsius: '))
#rounding fahrenheit value as I was getting 69.000000001
print(f'Temp in fahrenheit is ' + f'{round(1.8 * celsius + 32, 1)}')
if celsius > 21:
    print(fn + ', it is warm outside')
elif celsius==21:
    print(fn + ', it is perfect outside')
else:
    print(fn + ', it is cool outside')
