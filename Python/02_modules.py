#Modules In Python
#A module is a file containing Python definitions and statements. It can be imported and used in other Python programs. Modules help in organizing code and reusing it across different projects.   

#Creating a module
#To create a module, simply create a Python file with the desired functions, classes, or variables. For example, let's create a module named "math_operations.py" with some basic math functions:   
# math_operations.py
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"  


#Using a module
#To use the functions defined in the module, you can import it in another Python file. For example, let's create a file named "main.py" that imports the "math_operations" module and uses its functions:   
# main.py
import math_operations
result1 = math_operations.add(5, 3)
result2 = math_operations.subtract(5, 3)
result3 = math_operations.multiply(5, 3)
result4 = math_operations.divide(5, 3)
print("Addition:", result1)
print("Subtraction:", result2)
print("Multiplication:", result3)
print("Division:", result4)     

#Output:
#Addition: 8
#Subtraction: 2
#Multiplication: 15
#Division: 1.6666666666666667

  
#Importing specific functions
#Instead of importing the entire module, you can also import specific functions from the module. For example:
# main.py
from math_operations import add, subtract
result1 = add(5, 3)
result2 = subtract(5, 3)
print("Addition:", result1)
print("Subtraction:", result2)
#Output:
#Addition: 8
#Subtraction: 2 

