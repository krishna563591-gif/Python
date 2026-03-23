
#   Arithmetic Operators: +, -, *, /, //, %, **
'''
#1.Take two integer inputs from users and perform all arithmetic operations on them and show the results.
num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
print(f"Addition: {num1} + {num2} = {num1+num2}")
print(f"Subtraction: {num1} - {num2} = {num1-num2}")
print(f"Multiplication: {num1} * {num2} = {num1*num2}")
print(f"Division: {num1} / {num2} = {num1/num2}")
print(f"Floor Division: {num1} // {num2} = {num1//num2}")
print(f"Modulus: {num1} % {num2} = {num1%num2}")
print(f"Exponentiation: {num1} ** {num2} = {num1**num2}")   

#2.Take two float inputs from users and print their squire,cube and average.
num1=float(input("enter the first number: "))
num2=float(input("enter the second number: "))
print(f"Square of {num1} is: {num1**2}")
print(f"Square of {num2} is: {num2**2}")
print(f"Cube of {num1} is: {num1**3}")
print(f"Cube of {num2} is: {num2**3}")
average=(num1+num2)/2
print(f"The average of {num1} and {num2} is: {average}")


# 3.Take length and width from user and calculate area.
length=float(input("Enter the length: "))
width=float(input("Enter the width: "))
area=length*width
print(f"The area of the rectangle is: {area}")

#4.Take radius and calculate area of circle (3.14 * r * r).
radius=float(input("Enter the radius: "))
area=3.14*radius*radius
print(f"The area of the circle is: {area:.2f}")

# 5.Take total numbers of 5 sujects and their percentage.
subject1=float(input("Enter marks for subject 1: "))
subject2=float(input("Enter marks for subject 2: "))
subject3=float(input("Enter marks for subject 3: "))
subject4=float(input("Enter marks for subject 4: "))
subject5=float(input("Enter marks for subject 5: "))
total_marks=subject1+subject2+subject3+subject4+subject5
percentage=(total_marks/500)*100
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%") #.2f is used to format the percentage to 2 decimal places.

# Take salary and increase by 10% and print the new salary.
salry=int(input("enter the salry amount:"))
new_salary=salry+(salry*0.10)
print(f"The new salary after 10% increase is: {new_salary}")

# Take a number and divide it by 2 using /= operator.
num=float(input("Enter a number: "))
num/=2 # This is equivalent to num = num / 2
print(f"The number after dividing by 2 is: {num}")

# Take a number and multiply it by 5 using *= operator.
num=float(input("Enter a number: "))
num*=5 # This is equivalent to num = num * 5
print(f"The number after multiplying by 5 is: {num}")   

# Take two numbers and swap them using arithmetic operators. swap meaning num1 will be assigned to num2 and num2 will be assigned to num1.
num1=float(input("Enter the first number: ")) 
num2=float(input("Enter the second number: "))
print(f"Before swapping: num1 = {num1}, num2 = {num2}")
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(f"After swapping: num1 = {num1}, num2 = {num2}") 

# Take a number and check if it is even using %.
num=int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

# Take a number and check if it is odd using %.
num=int(input("Enter a number: "))
if num % 2 != 0:
    print(f"{num} is an odd number.")
else:
    print(f"{num} is an even number.")  

# Take total seconds and convert into minutes (use // and %).
total_seconds=int(input("Enter total seconds: "))
minutes=total_seconds//60
seconds=total_seconds%60
print(f"{total_seconds} seconds is equal to {minutes} minutes and {seconds} seconds.")

# Take two numbers and print their power result.
base=float(input("Enter the base number: "))
exponent=float(input("Enter the exponent: "))
result=base**exponent
print(f"{base} raised to the power of {exponent} is: {result}") 

# Take price and Discount percentage and calculate final price and discount amount.
price=float(input("Enter the price: "))
discount_percentage=float(input("Enter the discount percentage: "))
discount_amount=price*(discount_percentage/100)
final_price=price-discount_amount
print(f"Discount Amount: {discount_amount}")
print(f"Final Price: {final_price}")

# Take two numbers and print remainder without using % (use formula).
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
remainder=num1-(num2*(num1//num2))


# Take a number and print half of it.
full_number = int(input("enter a number : "))
half_number = full_number / 2
print(f"half number is {half_number}")


# Take base and height and calculate area of triangle.

base_of_triangle=float(input("enter the base:"))
height_of_triangle=float(input("enter the base:"))
area_of_triangle=1/2*base_of_triangle*height_of_triangle
print("area of triangle is:{area_of_triangle}")

# Take a number and print its square root using ** 0.5.
number = float(input("Enter a number: "))
square_root = number ** 0.5
print(f"Square root is {square_root}")

# Take monthly salary and calculate yearly salary.
monthly_salary=int(input("enter mothly salary:"))
yearly_salary=monthly_salary*12
print(f"yearly is salary:{yearly_salary}")


# Take total bill and number of people, calculate per person share.
total_bill=int(input("enter the total bill:"))
total_peoples=int(input("enter the total peoples:"))
per_person_share=total_bill/total_peoples
print(f"per person share is :{per_person_share}")

'''
#============================================================
# 2.COMPARISON OPERATORS ( == != > < >= <= )
'''
# Take two integers and check if they are equal.
int1=int(input("enter the first number:"))
int2=int(input("enter the second number:"))
if int1==int2:
    print("both numbers are equal")
else:
    print("they are not equal")
'''

'''
# Take two numbers and check if first is greater than second.
int1=int(input("enter the first number:"))
int2=int(input("enter the second number:"))
if int1>int2:
    print("first is greater than second")
else:
    print("first is not greater than second")
'''

'''
# Take age and check if age is greater than 18.
age=int(input('enter your age:'))
if age>18:
    print('your age greater than 18')
else:
    print("age is not more than 18")
'''

'''
# Take salary and check if salary is at least 50000.
salary=int(input("enter the salary:"))
least_salary=50000
if salary>=50000:
    print("salary is at least 50000")
else:
    print("salary is less than 50000")
'''

'''
# Take password input and check if it equals "admin".
password=input("enter a password:")
admin_password='admin'
if password==admin_password:
    print("it matched")
else:
    print("did not matched")
'''


'''
# Take a number and check if it is positive.
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive")
else:
    print("The number is not positive")
'''

#==========================
# LOGICAL OPERATORS ( and or not )
'''
# Take age and check if age > 18 and age < 60.
age = int(input("Enter your age: "))

if age > 18 and age < 60:
    print("Age is between 18 and 60")
else:
    print("Age is not in the range")

'''
'''
# Take marks and check if marks >= 35 and marks <= 100.
marks = int(input("Enter your marks: "))

if marks >= 35 and marks <= 100:
    print("Valid marks (Pass range)")
else:
    print("Invalid or Fail")

'''

'''
# Take salary and check if salary > 30000 and experience > 2.
salary = int(input("Enter your salary: "))
experience = int(input("Enter your experience (in years): "))

if salary > 30000 and experience > 2:
    print("Eligible")
else:
    print("Not eligible")
'''



'''
# Take age and check if not (age < 18).

age = int(input("Enter your age: "))

if not (age < 18):
    print("Eligible (18 or above)")
else:
    print("Not eligible")

'''



'''' 
# Take salary and check if salary > 50000 or department == "IT".

salary = int(input("Enter your salary: "))
department = input("Enter your department: ")

if salary > 50000 or department == "IT":
    print("Eligible")
else:
    print("Not eligible")
'''

'''
# Take two strings and check if both are equal and not empty.
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if str1 == str2 and str1 != "" and str2 != "":
    print("Both strings are equal and not empty")
else:
    print("Condition not satisfied")

# Take number and check if it is divisible by 3 and 5
number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("Number is divisible by both 3 and 5")
else:
    print("Number is not divisible by both 3 and 5")

'''



'''

# Take username and check if username == "admin" or username == "root".
username = input("Enter username: ")

if username == "admin" or username == "root":
    print("Access granted")
else:
    print("Access denied")

# Take salary and check if salary > 40000 and not salary > 100000.

salary = int(input("Enter your salary: "))

if salary > 40000 and not salary > 100000:
    print("Salary is in the required range")
else:
    print("Salary is not in the range")
'''

#=====================================================
# ASSIGNMENT OPERATORS( = += -= *= /= //= %= **= )


'''

# Create a variable x = 10 and print it.
x=10
print(x)

# Take a number from user and assign it to variable num. Print num.
num=input("enter a number :")
print(num)

#Create x = 5. Increase x by 3 using +=. Print result.
x=5
x+=3
print(x)

'''
'''
# Create marks = 80. Reduce it by 5 using -=.
marks=80
marks-=5
print(marks)

# Take a number and double it using *=.
number=int(input("enter a number:"))
number*=2
print(f'double is:{number}')
'''


'''

# Take a float number and divide it by 2 using /=.
number = float(input("Enter a number: "))

number /= 2
print(f"Result after dividing by 2: {number}")

# Create x = 15. Apply %= 4 and then += 2
x = 15
x %= 4   # 15 % 4 = 3
x += 2   # 3 + 2 = 5

print(x)  # Output: 5

# Create x = 7. Apply **= 2 and then -= 10
x = 7
x **= 2   # 7^2 = 49
x -= 10   # 49 - 10 = 39

print(x)  # Output: 39

# Take a number and apply a chain of operations using assignment operators.
num = float(input("Enter a number: "))

num += 5
num *= 2
num /= 3
num -= 4

print(f"Final result: {num}")

'''
#======================================
# BOOLEAN QUESTIONS:(True, False, Boolean expressions, and logic):

# 1. What is a Boolean value in Python?-A Boolean value represents truth or falsehood.
# 2. What are the two Boolean constants?-True or False
# 3. What will be the output?   print(10 > 5): True
#4. What will be the output? print(5 == 10) :False  
# 5. What will be the output? print(5 != 5): False



'''
# 27. Take a string input and print True if it equals "admin".
string=input("ENTER A PASSWORD:")
if string=="admin":
    print("True")
else:
    print("false")


#28. Take password input and print True if password is not "1234".
password = input("Enter your password: ")
if password != "1234":
    print(True)
else:
    print(False)

#29. Take a number and print True if it is divisible by 3 and 5.
number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print(True)
else:
    print(False)


#30. Take a number and print True if it is not zero.
number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print(True)
else:
    print(False)

'''

