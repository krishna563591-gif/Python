#Types Of Operators in Python
#1. Arithmetic Operators(+, -, *, /, %, **, //)
a=10
b=3
print("Addition:", a+b)          #13
print("Subtraction:", a-b)       #7
print("Multiplication:", a*b)    #30
print("Division:", a/b)          #3.3333 
print("Modulus:", a%b)           #1
print("Exponentiation:", a**b)   #1000
print("Floor Division:", a//b)   #3  

#Assignment Operators(=, +=, -=, *=, /=, %=, **=, //=)
a=5-2 #Assign 5-2 in a.
b=6
b+=3 #Increment the value of b by 3 then assign it back to b. b=b+3
print("Value of b after +=3:", b) #9
b-=3 #Decrement the value of b by 3 then assign it back to b. b=b-3
print("Value of b after -=3:", b) #6

#Comparison Operators(==, !=, >, <, >=, <=)
x=5>4 #True
y=3<=2 #False
print("Is 5 greater than 4?", x)
print("Is 3 less than or equal to 2?", y)
d=5!=5 #False
e=7==7 #True
print("Is 5 not equal to 5?", d)
print("Is 7 equal to 7?", e)    



#Logical Operators(and, or, not)
#Truth Table of "or" operator
p=True
q=False
print("True or False:", p or q)   #True
print("False or False:", q or q)  #False
print("True or True:", p or p)     #True

#Truth Table of "and" operator
print("True and False:", p and q)  #False
print("True and True:", p and p)    #True
print("False and False:", q and q) #False

#Truth Table of "not" operator
print("Not True:", not p)           #False
print("Not False:", not q)          #True

