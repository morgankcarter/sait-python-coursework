'''
CPRG 104 
Assignment 1
Morgan Carter
March 20, 2024
'''

class Person:
    #constructor
    def __init__(self, name, age, gender, birth_date):
        self.__name = name
        self.__age = age
        self.__birth_date = birth_date
        self.__gender = gender
    
    #getters methods
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_birth_date(self):
        return self.__birth_date
    
    def get_gender(self):
        return self.__gender

    #setters methods
    def set_name(self, new_name):
        self.__name = new_name
    
    def set_age(self, new_age):
        self.__age = new_age
    
    def set_birth_date(self, new_birth_date):
        self.__birth_date = new_birth_date

    def set_gender(self, new_gender):
        self.__gender = new_gender
    
    #to_string method
    def to_string(self):
        return f"Name : {self.get_name()}\nAge : {self.get_age()}\nGender : {self.get_gender()}"
    

class Employee(Person):

    no_of_employees = 0 # Class variable to keep track of total employees

    def __init__(self, name, age, birth_date, gender, company_name, salary, designation):
        Person.__init__(self, name, age, birth_date, gender) # initialize parent class in the child class constructor
        self.__company_name = company_name
        self.__salary = salary
        self.__designation = designation
        Employee.no_of_employees += 1 #increment to count a new employee upon instantiation of a new employee object

    #getters methods
    def get_company_name(self):
        return self.__company_name
    
    def get_salary(self):
        return self.__salary
    
    def get_designation(self):
        return self.__designation
    
    @staticmethod
    def get_no_of_employees():
        return Employee.no_of_employees

    #setters methods
    def set_company_name(self, new_company_name):
        self.__company_name = new_company_name
    
    def set_salary(self, new_salary):
        self.__salary = new_salary
    
    def set_designation(self, new_designation):
        self.__designation = new_designation

    #to_string method 
    def to_string(self):
        # calls the parent to_string() method to get the name, age, and gender. Then concatenate with the employees salary.
        return f"{super().to_string()}\nSalary : {self.get_salary()}"
    
    #increase_salary method
    def increase_salary(self, percentage):
        self.__salary = self.__salary * (1 + (percentage/100))
    
    # get_name method. Overrides the parent get_name method to ensure employee designation is printed.
    def get_name(self):
        return f'{super().get_name()}\nDesignation : {self.get_designation()}'

        
        
#test code #1
employee1 = Employee("Maria", 25, "Female", "25-Jun-1996", "BMO", 7000, "developer")
print("Number of Employee's objects after creating the first employee = ", Employee.get_no_of_employees())
print("====="*15)
print("Employee 1 information")
print("====="*5)
print(employee1.to_string() + '\n')
print("====="*15)

#test code #2
employee2 = Employee("Hamdy", 35, "Male", "25-June-1987", "BMO", 10000, "designer")
print("Number of Employee's objects after creating the second employee = ", Employee.get_no_of_employees())
print("====="*15)
print("Employee 2 information")
print("====="*5)

percentage = float(input("What is the increase percentage? "))
employee2.increase_salary(percentage)
print(employee2.to_string())
