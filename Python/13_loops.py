# Loops-loops help to do repetative task very easily.

# range() function: it is used to generate a sequence of numbers. It takes three parameters: start, stop, and step. The start parameter is the number from which the sequence will begin, the stop parameter is the number at which the sequence will end (exclusive), and the step parameter is the increment between each number in the sequence. If the start parameter is not provided, it defaults to 0. If the step parameter is not provided, it defaults to 1.
#e.g. range(5) will generate a sequence of numbers from 0 to 4 (0, 1, 2, 3, 4). range(1, 5) will generate a sequence of numbers from 1 to 4 (1, 2, 3, 4). range(0, 10, 2) will generate a sequence of even numbers from 0 to 8 (0, 2, 4, 6, 8).





#Types of loops.
#===================================================
#1.while loop: runs utill the condition is true. we have to make the condition false at somepoint otherwise its gonna be infinite.

i=1
while(i<6):
    print(i)
    i+=1
# output=1 2 3 4 5-runs utill the condition is false- we have to make the condition false at somepoint otherwise its gonna be infinite.
# we need to either increment or decrement the value of i to make the condition false at some point otherwise it will be infinite loop.
#Tasks
list=[1,"harry","Rohan",3,"Krishna"] # will run untill the condition is true.
i=0
while(i<len(list)): # explained- we are checking the condition that i is less than the length of the list. if it is true then we will print the value at index i and then increment i by 1. this will continue until i is equal to the length of the list, at which point the condition will be false and the loop will stop.
    print(list[i])
    i+=1    
# result: 1 harry Rohan 3 Krishna- we have to make the condition false at somepoint otherwise its gonna be infinite.


#======================================================

#2.For Loop:
# for loop will  take 1 by 1 value of something.

for i in range(1,6,1):  # range(start, stop, step)-important   
    print(i) # result: 1,2,3,4,5
# Before writing for loop ask these questions:
#what should i repeat? how many times should i repeat? what should i do in each repetition like numbers or strings values.

# Beginner mistakes:
# forgeting intendation & colons(:) & using wrong range parameters.




# range function

for i in range(0,4):
    print(i)
   # result: 0,1,2,3- range is exclusive of stop value.

'''
# For loop Iterate-list
l=[1,4,6,234,6,764]
for i l:
    print(i) # result: 1 4 6 234 6 764

# For loop Iterate-tuples
t=(6,231,75,122)
for i t:
    print(i) # result: 6 231 75 122


# For loop Iterate-string example
s= "Harry"
for i s:
    print(s) # result= H a r r y

    '''
# For loop with else
k=[1,7,8]
for item in k:
    print(item)

else:
    print("done")# this is printed when loop the exhaust or end.




# COMPREHENSIVE LOOPS GUIDE WITH EXAMPLES
# ==========================================================================================================

# 1. WHILE LOOP - Repeats while condition is True
# Syntax: while (condition):
#            code block

print("--- WHILE LOOP EXAMPLES ---")

# Example 1: Simple counter
count = 1
while count <= 3:
    print(f"Count: {count}")
    count += 1
# Output: Count: 1, Count: 2, Count: 3

# Example 2: Loop through list
fruits = ["apple", "banana", "orange"]
index = 0
while index < len(fruits):
    print(f"Fruit: {fruits[index]}")
    index += 1

# Example 3: Loop until condition changes
user_input = ""
attempts = 0
while attempts < 3:
    print(f"Attempt {attempts + 1}")
    attempts += 1


# 2. FOR LOOP - Iterates over sequences (list, string, range)
# Syntax: for variable in sequence:
#            code block

print("\n--- FOR LOOP EXAMPLES ---")

# Example 1: Loop through range
print("Numbers 0 to 4:")
for num in range(5):
    print(num)

# Example 2: Loop through list
colors = ["red", "green", "blue"]
for color in colors:
    print(f"Color: {color}")

# Example 3: Loop through string
for letter in "Python":
    print(letter)

# Example 4: Range with start, stop, step
print("Even numbers 0 to 8:")
for num in range(0, 10, 2):
    print(num)

# Example 5: Using enumerate to get index and value
students = ["Alice", "Bob", "Charlie"]
for index, student in enumerate(students):
    print(f"Index {index}: {student}")


#===============================================Break & Continue Statement
# 3. LOOP CONTROL STATEMENTS
print("\n--- LOOP CONTROL STATEMENTS ---")

#1. break - Exit loop immediately
print("Using break:")


for i in range(10):
    if (i == 3):# exit the loop rightnow.
        break
    print(i)  # Output: 0, 1, 2



#2. continue - Skip current iteration
print("Using continue:")


for i in range(5):
    if (i == 2):
        continue  # skip this iteration- skip this particular iteration- iteration means each number for e.g.100. iterations are 0-99 . 
    print(i)  # Output: 0, 1, 3, 4


# pass- when we want skip the loop now & will work later on.
#example:
for i in range(5):
    if (i == 2):
        pass  # do nothing for now, will implement later
    print(i)  # Output: 0, 1, 2, 3, 4   

    




# 3. else with loop - Runs if loop completes normally (without break)
print("Using else with for:")
for i in range(3):
    print(i)
else:
    print("Loop completed!")


# 4. NESTED LOOPS - Loop within a loop
print("\n--- NESTED LOOPS ---")

for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()  # New line after inner loop


# 5. WHEN TO USE WHICH LOOP
print("\n--- WHEN TO USE WHICH LOOP ---")
# Use FOR when: You know exact number of iterations, iterating over sequence
# Use WHILE when: You don't know iteration count, depends on condition

# FOR LOOP example
print("FOR: Iteration count known")
for i in range(3):
    print(f"Iteration {i + 1}")

# WHILE LOOP example
print("WHILE: Until condition met")
password = ""
while password != "secret":
    password = "secret"  # In real code, use input()
    print("Password correct!")

'''
#==================================Questions=================================================================
#1. write a program to print multiplication table of a given number using loop.
n= int(input("Enter a number:"))
for i  range (1,11):
    print(f"{n}*{i}={n*i}") # result: tables of 7-input was 7
    


# 2.write a program to greet all the person names stored in a list 'l'and which starts with s.
l= ["harry","soham", "Sachin","Rahul"]

for name in l:
if (name.startswith("S")):
print(f"hello")


# 3. do question 1 with while loop.


n= int(input("Enter a number:"))
i= 1

while (1<11):
    print(f"{n}*{i}={n*i}") 
    i+=1  # result: tables of 7-input was 7


 #4.  write a program to find wether a given number by user is prime or not? 

n= int(input("Enter a number:"))
for i in range (2,n)
if (n%i)==0:
print("Number is not prime")
break
else:
print("Number is prime)


#5.write a programm to sum of first n natural numbers using while loop.

n= int(input("Enter a number:"))
i=1
while(i<=n):
sum+=i
i+=
print(sum)

#6. write a program to calculate the factoeial of a given number using for loop.
 #5!=1*2*3*4*5

 n= int(input("Enter a number:"))
  product=1
 for i in range(1,n+1):
product=product*1
print (f"the factorial of {n} is {product}")



reamainig other task
 





    '''