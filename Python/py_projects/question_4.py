# Swap two numbers (with & without third variable): meaning, how to swap the values of two variables in Python, both with and without using a third variable.
# With third variable:
a = 5
b = 10
c = a # Store the value of a in a temporary variable c
a = b # Assign the value of b to a
b = c   # Assign the value of c (original value of a) to b  
print("After swapping with third variable:")
print("a =", a)
print("b =", b) 

# Without third variable:
x = 15
y = 20
x = x + y  # Step 1: Add x and y, and store the result in x
y = x - y  # Step 2: Subtract the new value of y from x, and store the result in y (which is the original value of x)   
x = x - y  # Step 3: Subtract the new value of y from x, and store the result in x (which is the original value of y)
print("After swapping without third variable:")
print("x =", x)
print("y =", y)

# Convert Kilometers → Miles:
kilometers=int(input("Enter distance in kilometers:"))
miles=kilometers*0.621371
print(f"{kilometers} kilometers is equal to {miles} miles.")


# Convert Celsius → Fahrenheit:
celsius=int(input("Enter temperature in Celsius:"))
fahrenheit=(celsius * 9/5) + 32
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

# Convert Fahrenheit → Celsius:
fahrenheit=int(input("Enter temperature in Fahrenheit:"))
celsius=(fahrenheit - 32) * 5/9
print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")    

# Convert Kilograms → Pounds:
kilograms=int(input("Enter weight in kilograms:"))
pounds=kilograms*2.20462
print(f"{kilograms} kilograms is equal to {pounds} pounds.")

# Convert Pounds → Kilograms:
pounds=int(input("Enter weight in pounds:"))
kilograms=pounds/2.20462
print(f"{pounds} pounds is equal to {kilograms} kilograms.")

# Convert Meters → Feet:
meters=int(input("Enter length in meters:"))
feet=meters*3.28084
print(f"{meters} meters is equal to {feet} feet.")

# Convert Feet → Meters:
feet=int(input("Enter length in feet:"))    
meters=feet/3.28084
print(f"{feet} feet is equal to {meters} meters.")

#Convert total seconds → hours, minutes, seconds:
total_seconds=int(input("Enter total seconds:"))
hours=total_seconds//3600
remaining_seconds=total_seconds%3600
minutes=remaining_seconds//60
seconds=remaining_seconds%60
print(f"{total_seconds} seconds is equal to {hours} hours, {minutes} minutes, and {seconds} seconds.")

# Convert hours, minutes, seconds → total seconds:
hours=int(input("Enter hours:"))
minutes=int(input("Enter minutes:"))
seconds=int(input("Enter seconds:"))
total_seconds=(hours*3600)+(minutes*60)+seconds
print(f"{hours} hours, {minutes} minutes, and {seconds} seconds is equal to {total_seconds} seconds.")

# Convert total days → years, months, days:
total_days=int(input("Enter total days:"))
years=total_days//365
remaining_days=total_days%365
months=remaining_days//30
days=remaining_days%30
print(f"{total_days} days is equal to {years} years, {months} months, and {days} days.")

# Convert years, months, days → total days:
years=int(input("Enter years:"))
months=int(input("Enter months:"))
days=int(input("Enter days:"))
total_days=(years*365)+(months*30)+days
print(f"{years} years, {months} months, and {days} days is equal to {total_days} days.")        


# Convert total seconds → days, hours, minutes, seconds:
total_seconds=int(input("Enter total seconds:"))
days=total_seconds//86400
remaining_seconds=total_seconds%86400
hours=remaining_seconds//3600
remaining_seconds=remaining_seconds%3600
minutes=remaining_seconds//60
seconds=remaining_seconds%60
print(f"{total_seconds} seconds is equal to {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.") 


# Take principal, rate, time → calculate compound interest:
principal=float(input("Enter the principal amount:"))
rate=float(input("Enter the annual interest rate (in %):"))
time=float(input("Enter the time in years:"))
compound_interest=principal*(1+(rate/100))**time - principal
print(f"The compound interest is: {compound_interest:.2f}")

# Take principal, rate, time → calculate simple interest:
principal=float(input("Enter the principal amount:"))
rate=float(input("Enter the annual interest rate (in %):"))
time=float(input("Enter the time in years:"))
simple_interest=(principal*rate*time)/100
print(f"The simple interest is: {simple_interest:.2f}") 

# Take base, height → calculate area of triangle:
base=float(input("Enter the base of the triangle:"))
height=float(input("Enter the height of the triangle:"))
area=(base*height)/2
print(f"The area of the triangle is: {area:.2f}")

# Take radius → calculate area of circle:
import math 
radius=float(input("Enter the radius of the circle:"))
area=math.pi*radius**2
print(f"The area of the circle is: {area:.2f}")

# Take length, width → calculate area of rectangle:
length=float(input("Enter the length of the rectangle:"))
width=float(input("Enter the width of the rectangle:"))
area=length*width
print(f"The area of the rectangle is: {area:.2f}")

# Take side → calculate area of square:
side=float(input("Enter the side length of the square:"))
area=side**2
print(f"The area of the square is: {area:.2f}")

# Take base1, base2, height → calculate area of trapezium:
base1=float(input("Enter the length of the first base of the trapezium:"))
base2=float(input("Enter the length of the second base of the trapezium:"))
height=float(input("Enter the height of the trapezium:"))
area=((base1+base2)*height)/2
print(f"The area of the trapezium is: {area:.2f}")

# Take radius → calculate volume of sphere:
import math 
radius=float(input("Enter the radius of the sphere:"))
volume=(4/3)*math.pi*radius**3
print(f"The volume of the sphere is: {volume:.2f}") 



# Without using built-in functions: Convert decimal → binary:
decimal=int(input("Enter a decimal number:"))
binary=""
while decimal > 0:
    remainder=decimal%2
    binary=str(remainder)+binary
    decimal=decimal//2
print(f"The binary representation is: {binary}")    

#Take a number → check if it is Armstrong number
number=int(input("Enter a number:"))
order=len(str(number))
sum=0
temp=number
while temp > 0:
    digit=temp%10
    sum+=digit**order
    temp//=10
if number == sum:
    print(f"{number} is an Armstrong number.")
else:    print(f"{number} is not an Armstrong number.") 

# Take salary → calculate tax based on slabs:
salary=float(input("Enter your salary:"))
if salary <= 250000:
    tax=0
elif salary <= 500000:
    tax=(salary-250000)*0.05
elif salary <= 1000000:
    tax=(salary-500000)*0.2 + 12500
else:  
    tax=(salary-1000000)*0.3 + 112500
print(f"The tax on a salary of {salary} is: {tax:.2f}")




 