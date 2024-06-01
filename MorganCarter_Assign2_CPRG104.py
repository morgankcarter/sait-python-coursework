'''
CPRG 104
Assignment 2
Morgan Carter
March 27, 2024
'''

class Number:
    #constructor
    def __init__ (self, name, num):
        self.__name = name
        #asserts to ensure number is an integer, positive, and less than 32,000
        assert isinstance(num, int), 'Invalid Number'
        assert num >= 0, 'Invalid Number'
        assert num < 32000, 'Invalid Number'
        #is number meets conditions, assign to num property
        self.__num = num

    #getter method
    def get_num (self):
        return self.__num
    
    #setter method 
    def set_num (self, new_num):
        self.__num = new_num
    
    #add method
    def add (self, to_add):
        result = self.get_num() + to_add.get_num()
        return Number('Sum', result)
    
    #subtract method
    def subtract (self, to_subtract): 
        result = self.get_num() - to_subtract.get_num()
        return Number('Difference', result)
    
    #multiply method
    def multiply (self, multiplier): 
        result = self.get_num() * multiplier.get_num()
        return Number('Product', result)
    
    #divide method with exception handling for denominator = zero
    def divide (self, divisor):
        try:
            result = self.get_num() / divisor.get_num()
            result = int(result)
            return Number('Quotient', result)
        except ZeroDivisionError: 
            print('You cannot divide by zero')
            return Number('Division_Error', 0)
    
    #to_string method:
    def to_string(self):
        return f'{self.__name} has a value of {self.get_num()}'
    
#test code: Scenario 1

num1 = Number('Number 1', 320)
print(num1.to_string())

num2 = Number('Number 2', 2)
print(num2.to_string())

print('Addition = ',num1.add(num2).get_num())
print('Subtraction =',num1.subtract(num2).get_num())
print('Multiplication =',num1.multiply(num2).get_num())
print('Division = ',num1.divide(num2).get_num())

#test code: Scenario 2
num1 = Number('Number 1', 320)
print(num1.to_string())

num2 = Number('Number 2', 0)
print(num2.to_string())

print('Addition = ',num1.add(num2).get_num())
print('Subtraction =',num1.subtract(num2).get_num())
print('Multiplication =',num1.multiply(num2).get_num())
print('Division = ',num1.divide(num2).get_num())

#test code: Scenario 3
num1 = Number('Number 1', -1)
print(num1.to_string())
    


    
    

    






    