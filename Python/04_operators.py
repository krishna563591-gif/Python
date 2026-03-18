#Types Of Operators in Python

#=======================================================
#1. Arithmetic Operators(+, -, *, /, %, **, //)
a=10
b=3
print("Addition:", a+b)          #13
print("Subtraction:", a-b)       #7
print("Multiplication:", a*b)    #30
print("Division:", a/b)          #3.3333 
print("Modulus:", a%b)           #1
print("Exponentiation:", a**b)   #1000
print("Floor Division:", a//b)   #3   # if its float it will round down to the nearest whole number. For example, 10.0//3 will give 3.0, while 10//3 will give 3.

#======================================================
#2. Assignment Operators(=, +=, -=, *=, /=, %=, **=, //=)
a=5-2 #Assign 5-2 in a.
b=6
b+=3 #Increment the value of b by 3 then assign it back to b. b=b+3
print("Value of b after +=3:", b) #9
b-=3 #Decrement the value of b by 3 then assign it back to b. b=b-3
print("Value of b after -=3:", b) #6




#==============================================

#3. Comparison Operators(==-equal, !=-not equal, >-greater than, <-less than, >=-greater than or equal to, <=-less than or equal to )
x=5>4 #True 
y=3<=2 #False
print("Is 5 greater than 4?", x)
print("Is 3 less than or equal to 2?", y)
d=5!=5 #False
e=7==7 #True
print("Is 5 not equal to 5?", d)
print("Is 7 equal to 7?", e)    
# comparison operators helps to compare two values and return a boolean result (True or False). 


#======================================================

#4. Logical Operators(and, or, not) = used to combine conditional statements.

#Truth Table of "or" operator: at least one condition must be true for the result to be true.
# cond1=True cond2=True # result: True
# cond1=True cond2=False # result: True 
# cond1=False cond2=True # result: True
# cond1=False cond2=False # result: False   


#Truth Table of "and" operator:  all conditions must be true for the result to be true. 
# cond1=True cond2=True # result: True
# cond1=True cond2=False # result: False
# cond1=False cond2=True # result: False
# cond1=False cond2=False # result: False



#Truth Table of "not" operator: it negates the value of the condition. If the condition is true, it returns false, and if the condition is false, it returns true.
# cond1=True # result: False
# cond1=False # result: True

#======================================================================

# Identity Operators(is, is not) = used to compare the memory location of two objects.
# commonly used to check if two variables point to the same object in memory.
a=[1, 2, 3]
b=a # b is assigned the same list as a, so they point to the same memory location.
c=[1, 2, 3] # c is a new list with the same content as a, but it is a different object in memory.
print("a is b:", a is b) #True
print("a is c:", a is c) #False
print("a is not c:", a is not c) #True



#===================================================================================
# Membership Operators(in, not in) = used to test if a sequence contains a certain value.
my_list=[1, 2, 3, 4, 5]
print("Is 3 in my_list?", 3 in my_list) #True
print("Is 6 in my_list?", 6 in my_list) #False
print("Is 6 not in my_list?", 6 not in my_list) #True   

# we can also use membership operators with strings to check if a substring is present in a string.
my_string="Hello, World!"
print("Is 'Hello' in my_string?", 'Hello' in my_string) #True
print("Is 'Python' in my_string?", 'Python' in my_string) #False    
