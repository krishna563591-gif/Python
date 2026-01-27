# Python Conditionals Examples
"""
PYTHON CONDITIONALS - THEORY

Conditionals allow programs to make decisions based on conditions.
They control the flow of execution by running different code blocks
depending on whether conditions are True or False.

Key Concepts:
- if: Executes code if condition is True
- else: Executes code if condition is False
- elif: Else-if, checks another condition if previous was False
- Logical operators: and, or, not - combine multiple conditions
- Comparison operators: ==, !=, <, >, <=, >= - evaluate conditions
- Ternary operator: Quick inline conditional (value_if_true if condition else value_if_false)

Truthiness:
- True values: Non-zero numbers, non-empty strings, non-empty collections
- False values: 0, None, False, empty strings, empty collections
"""
#practice
a=int(input("enter your age:"))
if(a>=18):
    print("you are above the age of consent.")
    print("Good For You")
else:
    print("your are above the age of consent")




# 1. If Statement
age = 18
if age >= 18:
    print("You are an adult")

# 2. If-Else Statement
score = 45
if score >= 50:
    print("You passed")
else:
    print("You failed")

# 3. If-Elif-Else Statement----important.
temp = 25
if temp < 0:
    print("It's freezing")
elif temp < 15:
    print("It's cold")
elif temp < 25:
    print("It's cool")
else:
    print("It's warm")

# 4. Nested If---------important
num = 10
if num > 0:
    if num > 5:
        print("Positive and greater than 5")
    else:
        print("Positive but less than or equal to 5")
else:
    print("Not positive")

# Relational Operators=comparision operators

# 5. Using Logical Operators
# and= true if both operands are true else false.
# or=tru if at least one oprands are true else false.
#not= inverts true to false & false to true.
name = "Ali"
has_ticket = True
if name and has_ticket:
    print("You can enter")

# 6. Using 'not' operator
is_raining = False
if not is_raining:
    print("No rain, go outside")

# 7. Ternary Conditional (One-liner)
height = 180
status = "Tall" if height > 170 else "Not tall"
print(status)

#=============================Questions==================================================
#.Write a python program to find the greatest of four numbers entered by users.
n1=int(input("enter 4 digits number:"))
n2=int(input("enter 4 digits number:"))
n3=int(input("enter 4 digits number:"))
n4=int(input("enter 4 digits number:"))
if(n1>n2 and n1>n3 and n1>n4):
    print("Greatest Number is n1:",n1)
elif(n2>n1 and n2>n3 and n2>n4):
    print("Greatest Number is n2:",n2)

elif(n3>n1 and n3>n2 and n3>n4):
    print("Greatest Number is n3:",n3)
elif(n4>n1 and n4>n2 and n4>n3):
    print("Greatest Number is n4:",n4)


# write a program to find out weather a student has passes or failed if it requires of 40% & at least 33% in each subject to pass.assume 3 subjects & take marks as input from users.
mark1=int(input("enter marks 1:"))
mark2=int(input("enter marks 2:"))
mark3=int(input("enter marks 3:"))

#check for total percentage.
total_percentage=(100*(mark1+mark2+mark3)/300)
if(total_percentage>=40 and mark1>=33 and mark2>=33 and mark3>=33):
    print("you are passed:",total_percentage)
else:
    print("you are failed ,try again:",total_percentage)

#. write a program to filter out comment as spam. when someone enter following inputs.
p1="buy online"
p2="click this"
p3="free money"
message=input("Enter a comment:")
if((p1 in message) or (p2 in message) or (p3 in message)):
    print("This comment is spam")
else:
    print("This is not a spam")


# write a program to find whether a given username contains less than 10 characters or not.
username=input("enter your username:")
if(len(username)<10):
    print("yes this user name has less than 10 characters:",username)
else:
    print("No this username has more than 10 characters:",username)


# write a program which finds out whether a given name is present in a list or not.
l=["harry","krishna","subham","sita"]
name=input("enter a name:")
if(name in l):
   print("Your name is in list")
else:
   print ("your name is not in the list")
