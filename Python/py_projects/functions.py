# Functions:

'''
# example1:Simple Greeting Function
def greet(name):
    print(f"Hello {name}")

greet("Krishna")


# example2:Add Two Numbers
def greet(name):
    print(f"Hello {name}")

greet("Krishna")

# example3:Return Value (IMPORTANT)
def multiply(x, y):
    return x * y

result = multiply(4, 5)
print(result)

# example4:Check Even or Odd
def multiply(x, y):
    return x * y

result = multiply(4, 5)
print(result)

# example5:Find Largest of Two Numbers
def largest(a, b):
    if a > b:
        return a
    else:
        return b

print("Largest is:", largest(10, 20))


# Count length of string:
def count_length(text):
    return len(text)

print(count_length("python"))

'''
# Return vs Print Function:
#Return- it returns result,print- it prints result. we can store results in new variable.
'''
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

'''

# The pass Statement in function:The pass statement is often used when developing, allowing you to define the structure first and implement details later.
def my_function():
  pass




#==============================================
# Python *args and **kwargs
#If you do not know how many arguments will be passed into your function, add a * before the parameter name.
# This way, the function will receive a tuple of arguments and can access the items accordingly:
#e.g.
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Accessing individual arguments from *args:
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")



# **kwargs:

# ======================Questions=====================================