#Loops:
# A loop means:
# Repeat something again and again.
'''
print(1)
print(2)
print(3)
print(4)
print(5)
'''
# Same thing using loop
'''
for i in range(1, 6): # 6 is exclusive-last one .
    print(i)

 for loop is Used when you know how many times to run   

 range()-gives range of numbers-range(start, end,step)-step-difference.
'''


'''
# Example for loop:
for i in range(6):
    if i == 3:
        continue   # skip 3
    elif i == 5:
        break      # stop at 5
    else:
        pass       # do nothing
    print(i)

'''

# While Loop:Used when you don’t know how many times-runs until condition becomes falls.
'''
i = 1
while i <= 5: # run the loop until 1 is less & equal to 5.
    print(i) 
    i += 1

'''
# questions:

#For Loop:

'''
# Given an integer N, print numbers from 1 to N using a for loop.
N = int(input("Enter a number: "))

for i in range(1, N + 1):
    print(i)
'''

# While Loop: runs until conditon becomes false:
# examples:

'''
n = int(input("Enter number: "))
while n >= 1: # This becomes an infinite loop (runs forever)
    print(n)
    n -= 1
'''

#example2:
num = 1
total = 0

while num <= 5:
    total += num
    num += 1

print("Sum =", total)

