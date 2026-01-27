#Type or Typecasting in Python
a=31
t=type(a)
print("The type of a is:", t)  #<class 'int'> 

b=5.9
t2=type(b)
print("The type of b is:", t2)  #<class 'float'>
c="Hello, World!"
t3=type(c)
print("The type of c is:", t3)  #<class 'str'>  
d=True
t4=type(d)
print("The type of d is:", t4)  #<class 'bool'>


#Typecasting-changing data type of a variable
#1. int to float        
x=10      #int
y=float(x) #typecasting int to float
print("Value of y:", y)          #10.0
print("Type of y:", type(y))     #<class 'float'>

#2. float to int
a=5.9     #float
b=int(a)  #typecasting float to int
print("Value of b:", b)          #5
print("Type of b:", type(b))     #<class 'int'>

#3. int to str
m=25      #int
n=str(m)  #typecasting int to str
print("Value of n:", n)          #25
print("Type of n:", type(n))     #<class 'str'>

#4. str to int
s="100"    #string
i=int(s)   #typecasting str to int
print("Value of i:", i)          #100
print("Type of i:", type(i))     #<class 'int'>



#5. str to float
str_num="45.67"  #string
float_num=float(str_num) #typecasting str to float
print("Value of float_num:", float_num)        #45.67
print("Type of float_num:", type(float_num))   #<class 'float'> 
#6. float to str
f=9.81          #float
str_f=str(f)   #typecasting float to str
print("Value of str_f:", str_f)          #9.81
print("Type of str_f:", type(str_f))     #<class 'str'>


#7. int to complex
int_num=7          #int
complex_num=complex(int_num) #typecasting int to complex

print("Value of complex_num:", complex_num)        #(7+0j)
print("Type of complex_num:", type(complex_num))   #<class 'complex'>

#8. float to complex
float_number=3.14          #float
complex_number=complex(float_number) #typecasting float to complex
print("Value of complex_number:", complex_number)        #(3.14+0j)
print("Type of complex_number:", type(complex_number))   #<class 'complex'>

#9. complex to str
complex_val=2+3j
str_complex=str(complex_val)
print("Value of str_complex:", str_complex)          #(2+3j)
print("Type of str_complex:", type(str_complex))     #<class 'str'>    

#10. bool to int
bool_val=True
int_from_bool=int(bool_val)
print("Value of int_from_bool:", int_from_bool)          #1
print("Type of int_from_bool:", type(int_from_bool))     #<class 'int'>     

#11. bool to float
bool_value=False
float_from_bool=float(bool_value) 
print("Value of float_from_bool:", float_from_bool)          #0.0
print("Type of float_from_bool:", type(float_from_bool))     #<class 'float
