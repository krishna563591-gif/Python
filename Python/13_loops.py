# Loops- to do repetative task easily.

#Types of loops.
#1.while loop
i=1
while(i<6):
    print(i)
    i+=1
# output=1 2 3 4 5-runs utill the condition is false.
#Tasks
l=[1,"harry","Rohan",3,"Krishna"]
i=0
while(i<len(l)+1):
    print(l(i))
print(len(l))
i+=1



#2.For Loop-
for i in range(4):
    print(i)




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


# 3. LOOP CONTROL STATEMENTS
print("\n--- LOOP CONTROL STATEMENTS ---")

# break - Exit loop immediately
print("Using break:")
for i in range(10):
    if i == 3:
        break
    print(i)  # Output: 0, 1, 2

# continue - Skip current iteration
print("Using continue:")
for i in range(5):
    if i == 2:
        continue
    print(i)  # Output: 0, 1, 3, 4

# else with loop - Runs if loop completes normally (without break)
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
