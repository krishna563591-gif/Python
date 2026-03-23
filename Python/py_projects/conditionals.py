# Conditionals Questions:
''''
#Take a number and check if it is positive, negative, or zero.
num=int(input('enter a number:'))
if num>0:
    print("number is positive")
elif num==0:
    print('num is zero')
else:
    print('num is negative')

'''


'''
# 3. Take age and print: "Child" if age < 13, "Teen" if age 13–19,"Adult" otherwise.
age=int(input('enter your age:'))
if age<13:
    print('child')
elif age>=13 and<=19:
    print('Teen')
else:
    print('Adult')

'''

'''

# 4.Take marks and print: "Fail" if < 35, "Pass" if 35–59",First Class" if 60–79,"Distinction" if 80+.

marks = int(input('Enter marks: '))

if marks < 35:
    print('Fail')
elif 35 <= marks <= 59:
    print('Pass')
elif 60 <= marks <= 79:
    print('First Class')
else:
    print('Distinction')
'''





'''

# Take a number and check if it is divisible by 3, 5, or both.
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
elif num % 3 == 0:
    print("Divisible by 3")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 3 or 5")

'''

#11. Take a number and check if it is 1-digit, 2-digit, or 3-digit.
digit = int(input('Enter a number: '))

if -9 <= digit <= 9:
    print('Single digit')
elif -99 <= digit <= 99:
    print('2 digits')
elif -999 <= digit <= 999:
    print('3 digits')
else:
    print('More than 3 digits')


#13. Take a number and check if it lies between 10 and 50.
num = int(input("Enter a number: "))

if 10 <= num <= 50:
    print("Number is between 10 and 50")
else:
    print("Number is not between 10 and 50")

#14. Take username and check: "admin" → ,Admin Access "guest" → Guest Access, otherwise → Invalid User

username = input("Enter username: ")

if username == "admin":
    print("Admin Access")
elif username == "guest":
    print("Guest Access")
else:
    print("Invalid User")


#15. Take password and check if it matches "python123".
password = input("Enter password: ")

if password == "python123":
    print("Access Granted")
else:
    print("Wrong Password")


#1. Take three numbers and print the largest.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest is:", a)
elif b >= a and b >= c:
    print("Largest is:", b)
else:
    print("Largest is:", c)


#2. Take three numbers and print the smallest.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    print("Smallest is:", a)
elif b <= a and b <= c:
    print("Smallest is:", b)
else:
    print("Smallest is:", c)


#3. Take a number and check if it is divisible by 2 and 3.
num = int(input("Enter a number: "))

if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both 2 and 3")
else:
    print("Not divisible by both")




#2. Take age and gender and check special ticket discount eligibility.
#3. Take salary and experience and classify promotion eligibility.
#4. Take two numbers and check if both are positive, both negative, or mixed.

#5. Take number and check if it lies in:0–50,51–100, 101–200,above 200.

# 6. Take character input and check:uppercase,lowercase, digit,special character.

#8. Take a number and check Armstrong number (3-digit).
#9. Take balance and withdrawal amount. Check if transaction is allowed.
#10. Take score and print performance message.
#11. Take age and check insurance premium category.
#12. Take two numbers and check if they are both even, both odd, or mixed.