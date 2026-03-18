print("krishna Thapa")
print("this is a python program")
print("this is a second prgram")
print("this is krishna re-learning python")

#Why python is popular?
#1. Easy to learn and use
#2. Large community and support
#3. Versatile and powerful libraries
#4. Cross-platform compatibility
#5. Used in various fields like web development, data science, machine learning, etc.   

# What is programming?
# Programming is the process of creating instructions that a computer can understand and execute. It involves writing code in a programming language to solve problems, automate tasks, or create applications. Programming allows us to communicate with computers and make them perform specific tasks based on our instructions. It is a fundamental skill in the field of computer science and is used in various industries to develop software, websites, games, and more.    

#How code Runs?
#1. Writing Code: The programmer writes code in a programming language using a text editor or an integrated development environment (IDE).
#2. Compilation/Interpretation: The code is either compiled or interpreted. In compiled languages, the code is translated into machine code before execution. In interpreted languages like Python, the code is executed line by line without the need for compilation.
#3. Execution: The computer executes the instructions in the code, performing the specified tasks.
#4. Output: The results of the code execution are displayed as output, which can be in the form of text, images, or other data depending on the program's functionality.

#Python use-interpreter-which means code is executed one by one. where as in compiler all code is converted into machine code at once and then executed. This allows for faster execution in compiled languages, while interpreted languages like Python offer more flexibility and ease of debugging.
# python start from top to bottom and execute line by line. if there is an error in any line, it will stop the execution and display the error message. This is why it is important to write code in a logical and organized manner to avoid errors and ensure smooth execution.


# Variables & Data Types in Python:

# Variables: A variable is a named location in memory that stores a value. It can hold different types of data and can be changed during the program's execution. Variables are used to store and manipulate data in a program. In Python, you can create a variable by simply assigning a value to it using the equals sign (=). 
# memory simply is a label of a box where we can store data. we can give a name to that box and use it to store and retrieve data whenever needed. This is what variables do in programming. They allow us to create a named location in memory where we can store and manipulate data throughout our program.
# variables dont store data directly,they point to a location in memory where the data is stored. When we assign a value to a variable, it creates a reference to that value in memory. This means that if we change the value of the variable, it will point to a new location in memory where the new value is stored, while the old value remains unchanged. This is an important concept to understand when working with variables in programming.

# For example:
x = 10
my_name = "Hello, World!"
print(x)  # Output: 10
print(my_name)  # Output: Hello, World!
print(x, my_name)  # Output: 10 Hello, World!


# Rules for naming variables:
# 1. Variable names must start with a letter (a-z, A-Z) or an underscore (_). eg: my_variable, _myVariable, var123 are valid variable names, while 1variable (starts with a number), my-variable (contains a hyphen), class (reserved keyword), and my variable (contains a space) are invalid variable names.  
# 2. Variable names can contain letters, numbers, and underscores, but cannot start with a number.
# 3. Variable names cannot be the same as reserved keywords in Python (e.g., if, else, while, for, etc.).
# 4. Variable names are case-sensitive, meaning that "myVariable" and "myvariable" are considered different variables.


# Data Types: Python has several built-in data types that allow you to store different kinds of data. Some common data types include:
# 1. int: Used to store whole numbers (e.g., 1, 42, -5).
# 2. float: Used to store decimal numbers (e.g., 3.14, -0.5).
# 3. str: Used to store text (e.g., "Hello, World!").
# 4. bool: Used to store boolean values (True or False).
# 5. list: Used to store an ordered collection of items (e.g., [1, 2, 3], ["apple", "banana", "cherry"]).   
# 6. tuple: Used to store an ordered, immutable collection of items (e.g., (1, 2, 3), ("apple", "banana", "cherry")).
# 7. dict: Used to store key-value pairs (e.g., {"name": "Alice", "age": 30}).
# 8. set: Used to store an unordered collection of unique items (e.g., {1, 2, 3}, {"apple", "banana", "cherry"}).
# 9. NoneType: Used to represent the absence of a value (None).
# You can use the type() function to check the data type of a variable. For example:
x = 10
print(type(x))  # Output: <class 'int'>
my_name = "Hello, World!"
print(type(my_name))  # Output: <class 'str'>
is_valid = True
print(type(is_valid))  # Output: <class 'bool'>
my_list = [1, 2, 3]
print(type(my_list))  # Output: <class 'list'>
my_tuple = (1, 2, 3)
print(type(my_tuple))  # Output: <class 'tuple'>
my_dict = {"name": "Alice", "age": 30}
print(type(my_dict))  # Output: <class 'dict'>
my_set = {1, 2, 3}
print(type(my_set))  # Output: <class 'set'>
my_none = None
print(type(my_none))  # Output: <class 'NoneType'>

# Dynamic Typing: Python is a dynamically typed language, which means that you don't need to declare the data type of a variable when you create it. The data type is determined automatically based on the value assigned to the variable. This allows for more flexibility in programming, as you can change the type of a variable by simply assigning a new value to it. For example:
x = 10  # x is an integer
print(type(x))  # Output: <class 'int'>
x = "Hello, World!"  # x is now a string
print(type(x))  # Output: <class 'str'>


#input() function: The input() function is used to take user input in Python. It allows you to prompt the user for input and returns the input as a string. You can use the input() function to get data from the user and store it in a variable for further processing. For example:
name = input("Enter your name: ")
print("Hello, " + name + "!")  # Output: Hello, [user's name]!
age = input("Enter your age: ")
print("You are " + age + " years old.")  # Output: You are [user's age] years old.  

# input fuction always returns a string, so if you want to get a different data type (e.g., int or float), you need to convert the input using the appropriate type conversion function. For example:
age = int(input("Enter your age: ")) # Convert the input to an integer
print("You are " + str(age) + " years old.")  # Output: You are [user's age] years old.

float_intg= float(input("Enter a decimal:")) # Convert the input to a float
print("You entered: " + str(float_intg))  # Output: You entered: [user's decimal]
