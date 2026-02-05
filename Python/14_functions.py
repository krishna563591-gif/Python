a=12
b=45
c=56
average=(a+b+c)/3 # function
print(average)

# functions are reusable block of code to perform a specific task.

# syntax: function call
def avg():
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

goodDay()

# Types of functions:
#1. Built in function-already present in python
#2.Defined by the user-e.g.goodDay()

# Functions with Arguments:
def helloDay(name, ending):
    print(f"Good day {name}, {ending}")

helloDay("krishna", "Thank you") #  Good day krishna, Thank you



# Default Arguments:

def helloWorld(name, ending="Thank you"):
    print(f"Good Day,{name}")
    print(ending)
helloWorld("krishna")#Good Day,krishna Thank you
helloWorld("Rohan","Thanks") #Good Day,Rohan Thanks

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


#6. write a function to write multiply table of given number.

def multiply(n):
    for i in range (1,11):
        print (f"{n}*{i}={n*i}")

multiply(5)

