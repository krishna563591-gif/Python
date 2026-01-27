# write a python program to add a two numbers.

a=6
b=5
print(a+b)

# write a python program to find remainder when a number is divided by b.
a=35
b=6
print("Remainder when a is divided by b is:", a%b)

# check the type of variable assigned using input() function.
a=input("enter a number:,a")
print(type(a))  

# write a python program to take two numbers as input and print their sum.
a=int(input("Enter a number 1 "))
b=int(input("Enter another number 2 "))
print("Number a is:", a)
print("Number b is:", b)
print("sum is", a+b)

# write a python program to take two numbers as input and print their product.
a=int(input("Enter a number 1 "))
b=int(input("Enter another number 2 "))
print("Number a is:", a)    
print("Number b is:", b)
print("product is", a*b)

# write a python program to take two numbers as input and print their division.
a=int(input("Enter a number 1 "))
b=int(input("Enter another number 2 "))
print("Number a is:", a)
print("Number b is:", b)
print("division is", a/b)

# write a python program to take two numbers as input and print their subtraction.
a=int(input("Enter a number 1 "))
b=int(input("Enter another number 2 "))  
print("Number a is:", a)
print("Number b is:", b)
print("subtraction is", a-b)

# Use a comparison operator to find out whether a given variable is greater than 'b' or not.Take a=34 and b=80.
a=int(input("Enter a number 1:,"))
b=int(input("Enter another number 2:,"))
print("Is a greater than b?:", a>b) 

# Write a program to find a average number entered by the user.
a=int(input("enter a number : "))
b=int(input("enter another number : "))
print("average number is :",(a+b)/2)

# Write a program to calculate the square of a number entered by the user.
a=int(input("enter a number : "))
print("square of the number is :",a*a)  

# Write a program to calculate the cube of a number entered by the user.
a=int(input("enter a number : "))
print("cube of the number is :",a*a*a)  

# Write a program to calculate the area of a rectangle.
length=int(input("enter length of rectangle : "))
breadth=int(input("enter breadth of rectangle : "))
area=length*breadth
print("area of rectangle is :",area)   


# Write a program to calculate the area of a circle.
radius=int(input("enter radius of circle : "))
area=3.14*radius*radius
print("area of circle is :",area)

# Write a program to calculate the perimeter of a rectangle.
length=int(input("enter length of rectangle : "))
breadth=int(input("enter breadth of rectangle : "))
perimeter=2*(length+breadth)
print("perimeter of rectangle is :",perimeter)

# Write a program to calculate the perimeter of a circle.
radius=int(input("enter radius of circle : "))
perimeter=2*3.14*radius
print("perimeter of circle is :",perimeter)

# Write a program to convert temperature from Celsius to Fahrenheit.
celsius=int(input("enter temperature in celsius : "))
fahrenheit=(celsius*9/5)+32
print("temperature in fahrenheit is :",fahrenheit)
# Write a program to convert temperature from Fahrenheit to Celsius.
fahrenheit=int(input("enter temperature in fahrenheit : "))
celsius=(fahrenheit-32)*5/9
print("temperature in celsius is :",celsius)

# Write a program to calculate simple interest.
principal=int(input("enter principal amount : "))
rate=int(input("enter rate of interest : "))
time=int(input("enter time in years : "))
simple_interest=(principal*rate*time)/100
print("simple interest is :",simple_interest)

# Write a program to calculate compound interest.
principal=int(input("enter principal amount : "))
rate=int(input("enter rate of interest : "))
time=int(input("enter time in years : "))
compound_interest=principal*(1+rate/100)**time - principal
print("compound interest is :",compound_interest)


