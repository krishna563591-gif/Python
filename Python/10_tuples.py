"""
TUPLES IN PYTHON
================
A tuple is an immutable (unchangeable) collection of items.
Tuples are ordered and allow duplicate values.
"""
# The Diffrence between list & tuple is you cannot be change the items.

# 1. Creating Tuples
a= (1,45,342,345,False,"Rohan","Shivam")
print(a)

# Empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")

# Single element tuple (note the comma)
single_tuple = (1,)
print(f"Single element tuple: {single_tuple}")

# Multiple elements
my_tuple = (1, 2, 3, 4, 5)
print(f"Integer tuple: {my_tuple}")

# Mixed data types
mixed_tuple = (1, "hello", 3.14, True)
print(f"Mixed tuple: {mixed_tuple}")

# Without parentheses (still a tuple)
tuple_no_parens = 1, 2, 3
print(f"Tuple without parentheses: {tuple_no_parens}")

# From a list
list_to_tuple = tuple([1, 2, 3])
print(f"Tuple from list: {list_to_tuple}")


#.Tuple Methods:
# 1.my_tuple = (1, 2, 2, 3, 2, 4)
count = my_tuple.count(2)
# Resulting count: 3

# index tuple
my_tuple = (10, 20, 45, 10, 30, 10, 55)
index_of_10 = my_tuple.index(10)
# Resulting index: 0 (the first occurrence is at index 0-ignore later on value)


#len(tuple): Returns the total number of elements in the tuple.
#max(tuple): Returns the largest item in the tuple.
#min(tuple): Returns the smallest item in the tuple.
#sum(tuple): Returns the sum of all numeric items in the tuple.
#sorted(tuple): Returns a new sorted list of the elements in the tuple (does not modify the original tuple).
#tuple(iterable): Converts other iterables (like lists, strings, or sets) into a tuple. 



#------------------------------------Practice----------------------------------------------
# write a program to store seven fruits in a list entered by the user.

fruits=[]
f1=("enter name of fruit:,")
fruits.append(f1)
f2=("enter name of fruit:,")
fruits.append(f2)
f3=("enter name of fruit:,")
fruits.append(f3)
f4=("enter name of fruit:,")
fruits.append(f4)
f5=("enter name of fruit:,")
fruits.append(f5)
f6=("enter name of fruit:,")
fruits.append(f6)
f7=("enter name of fruit:,")
fruits.append(f7)
print(fruits)

# write a program to accept marks of 6 students & display them in a sorted manner.

marks=[]
f1=int(input("enter marks:,"))
marks.append(f1)
f2=int(input("enter marks:,"))
marks.append(f2)
f3=int(input("enter marks:,"))
marks.append(f3)
f4=int(input("enter marks:,"))
marks.append(f4)
f5=int(input("enter marks:,"))
marks.append(f5)
f6=int(input("enter marks:,"))
marks.append(f6)
f7=int(input("enter marks:,"))
marks.append(f7)
marks.sort()
print(marks)


# Write a program to sum a list of 4 numbers.
l=[22,33,55,66]
total=sum(l)
print(total)