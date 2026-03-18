
# functions are reusable block of code to perform a specific task.

# syntax: function call
def avg(): # def-define, avg-function name,():parameters
    a=12
    b=45
    c=56
    average=(a+b+c)/3 # function
    print(average)

    avg() # function-call
    avg() # function-call
    avg() # function-call
    avg() # function-call
    avg() # function-call
    avg() # function-call

    # quick quiz: write a program to a user with"good day" using function.

    def goodDay():
       print ("good day")

goodDay() # calling the function


#=================================================================================
# return.
def squire(x):
    return x*x
x=squire(25)
print(x) #625
# reason- when we use return, the function will return the value to the caller and the function will be terminated. so we can store the value in a variable and use it later in the program.


# print & return are not same: print simply display value while return gives the value return.

#=======================================================================================




#======================================================================================
# Types of functions: 

#1. Built in function-already present in python: e.g. print(), input(), len(), type(), int(), str() etc.

#2.Defined by the user-e.g.goodDay()

# 3. Anonymous function- it is a function without a name, it is also called lambda function. e.g. lambda x: x*x

#4. Recursive function- it is a function that calls itself. e.g. factorial(n)= n*factorial(n-1)

#==================================================
# Functions with Arguments:
def helloDay(name, ending):
    print(f"Good day {name}, {ending}")

helloDay("krishna", "Thank you") #  Good day krishna, Thank you

#===========================

# Default Arguments:

def helloWorld(name, ending="Thank you"):
    print(f"Good Day,{name}")
    print(ending)
helloWorld("krishna")#Good Day,krishna Thank you
helloWorld("Rohan","Thanks") #Good Day,Rohan Thanks


#=========================================
#keyword Arguments: 
# when we pass the arguments in the form of key=value, it is called keyword arguments. 
# e.g. helloWorld(name="krishna", ending="Thank you")
#example:
def helloWorld(name, ending="Thank you"):
    print(f"Good Day,{name}")
    print(ending)
helloWorld(name="krishna") #Good Day,krishna Thank you
helloWorld(name="Rohan", ending="Thanks") #Good Day,Rohan Thanks
helloWorld(ending="Thanks", name="Rohan") #Good Day,Rohan Thanks

# Positional Arguments: when we pass the arguments in the form of position, it is called positional arguments.
#  e.g. helloWorld("krishna", "Thank you")

# Variable Length Arguments: when we want to pass a variable number of arguments to a function, we can use variable length arguments.
#  e.g. def helloWorld(*args):   
#example:
def helloWorld(*args):
    for i in args:
        print(f"Good Day,{i}")
helloWorld("krishna", "Rohan", "Sohan") # Good Day,krishna Good Day,Rohan Good Day,Sohan

#=======================================

# **kwargs: when we want to pass a variable number of keyword arguments to a function, we can use **kwargs.
# e.g. def helloWorld(**kwargs):
# example:
def helloWorld(**kwargs):
    for key, value in kwargs.items():
        print(f"Good Day,{key}, {value}")
helloWorld(name="krishna", ending="Thank you") # Good Day,name, krishna Good Day,ending, Thank you
helloWorld(name="Rohan", ending="Thanks") # Good Day,name, Rohan Good Day,ending, Thanks
helloWorld(ending="Thanks", name="Rohan") # Good Day,ending, Thanks Good Day,name, Rohan

#=========================================
#

# Recursion: function that calls itself- it is most direct way to code an alorithm.
'''
factorial(0)=1
factorial(1)=1
factorial(2)=2*1
factorial(3)=3*2*1
factorial(4)=4*3*2*1
factorial(5)=5*4*3*2*1
factorial(n)=n* n-1*3*2*1
factorial(n)= n*factorial(n-1)

'''


def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)



# e.g.
n=int(input("enter a number:"))
print(f"factorial of this number is:{factorial(n) }")

#======================================

# Lambda Function: it is a function without a name, it is also called anonymous function. e.g. lambda x: x*x
# example:
square=lambda x: x*x
print(square(5)) #25


#=======================================Practice-Set==============================================
#1. Write a program to using function to find greatest of three number.
e=1
f=3
g=5
def greatest(e,f,g):
if(a>b and a>c):
    return a
elif(b>a and b>c):
    return b
elif(c>a and c>b):
    return c
e=1
f=3
g=5
print (greatest(e,f,g))

#2.write a program using function to convert celsious to fahrenheit.

def f_to_c(f):
    return 5*(f-32)/9
f=int(input("enter tem in f:"))
c= f_to_c(f)
#print(f_to_c)
print(f"{round(c,2)}°C")


#3.How do you prevent a python print() function to print a new line at the end.
print("a")
print("b")
print("c",end "")
print("d" end "")

#4. Write a recursive function to calculate the sum of first n natural numbers.
'''
sum(1)= 1
sum(2)= 1+2
sum(3)= 1+2+3
sum(4)= 1+2+3+4
sum(5)= 1+2+3+4+5
sum(n)= 1+2+3+4....n-1+n
sum(n)=sum(n-1)+n

def sum(n):
    if(n==1):
     return 1

return sum(n-1)+n

#print(sum(4))
'''





#5.write a python function which converts inches to cms.

def inch_to_cm(inch):
    return inch*2.54
n= int(input("enter a value in inch:"))
print(f"the in cm is {inch_to_cm(n)}")


# 6.print even numbers between 1 to 10 using function.
def count_even(n):
    count=0
    for i in range(1,n+1): # range(1,11) will give us numbers from 1 to 10
        if i%2==0:
          print(i)
          count+=1
    return count # return the count of even numbers between 1 to n
result=count_even(10)
print(result) #result:5

#7.write a python function to check if a number is prime or not.
def is_prime(n):
    if n<=1: # prime numbers are greater than 1, so if n is less than or equal to 1, it is not a prime number.
        return False # return false if n is less than or equal to 1, because prime numbers are greater than 1.
    for i in range(2,n): # check if n is divisible by any number from 2 to n-1, if it is divisible, then it is not a prime number.
        if n%i==0:  # if n is divisible by i, then it is not a prime number, so return false.
            return False # if n is not divisible by any number from 2 to n-1, then it is a prime number, so
    return True # if n is not divisible by any number from 2 to n-1, then it is a prime number, so return true.
n=int(input("enter a number:")) # take input from user and store it in variable n, then check if n is prime or not using is_prime function.
if is_prime(n):     # if is_prime(n) returns true, then n is a prime number, so print that n is a prime number.
    print(f"{n} is a prime number") # if is_prime(n) returns false, then n is not a prime number, so print that n is not a prime number.
else:
    print(f"{n} is not a prime number") # if is_prime(n) returns false, then n is not a prime number, so print that n is not a prime number.


# Student pass or fail checker:
def check_result(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"   
marks=int(input("enter your marks:")) # take input from user and store it in variable marks, then check if marks is greater than or equal to 40 using check_result function.
result=check_result(marks)
print(f"You have {result}") 

# Write a python function to find the largest element in a list.
def largest_element(lst):
    largest=lst[0] # assume the first element is the largest
    for i in lst: # iterate through the list
        if i>largest: # if the current element is greater than the largest, then update the largest
            largest=i
    return largest # return the largest element in the list
lst=[1,2,3,4,5] # create a list of numbers
print(f"The largest element in the list is: {largest_element(lst)}") # call the largest_element function and print the result.  


# Write a python function to find the second largest element in a list.
def second_largest(lst):
    largest=lst[0] # assume the first element is the largest
    second_largest=lst[0] # assume the first element is the second largest
    for i in lst: # iterate through the list
        if i>largest: # if the current element is greater than the largest, then update the largest and second largest
            second_largest=largest
            largest=i
        elif i>second_largest and i!=largest: # if the current element is greater than the second largest and not equal to the largest, then update the second largest
            second_largest=i
    return second_largest # return the second largest element in the list
lst=[1,2,3,4,5] # create a list of numbers
print(f"The second largest element in the list is: {second_largest(lst)}") # call the second_largest function and print the result.


# Write a python function to find the sum of all elements in a list.
def sum_of_elements(lst):
    total=0 # initialize total to 0
    for i in lst: # iterate through the list
        total+=i # add the current element to the total
    return total # return the total sum of all elements in the list
lst=[1,2,3,4,5] # create a list of numbers
print(f"The sum of all elements in the list is: {sum_of_elements(lst)}") # call the sum_of_elements function and print the result.

