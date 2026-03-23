# Take user name and print: "Hello <name>, welcome!"
name=input("Please enter your name:")
print(f"Hello {name}, welcome!")

# 2. Take two numbers and print: sum, difference, product and division of those numbers.
 
num1=int(input("please enter first number:"))
num2=int(input("please enter second number:"))
print(f"sum of {num1} and {num2} is: {num1+num2}")
print(f"difference of {num1} and {num2} is: {num1-num2}")
print(f"product of {num1} and {num2} is: {num1*num2}")
print(f"division of {num1} and {num2} is: {num1/num2}")


# 3. Take radius of a circle and print area and circumference of the circle.
radius=float(input("please enter radius of the circle:"))
area=3.14*radius*radius
circumference=2*3.14*radius
print(f"area of the circle with radius {radius} is: {area}") # meaning of f is format, it is used to format the string and insert the value of variable in the string. It is a way to make the string more readable and easier to understand.
print(f"circumference of the circle with radius {radius} is: {circumference}")

# 4. Take temperature in Celsius and print it in Fahrenheit.
celsius=float(input("please enter temperature in Celsius:"))        
fahrenheit=(celsius*9/5)+32
print(f"temperature in Fahrenheit is: {fahrenheit}")

# 5. Take a number and print its square and cube.
number=int(input("please enter a number:"))
square=number*number
cube=number*number*number
print(f"square of {number} is: {square}")
print(f"cube of {number} is: {cube}")   

# 6. Take a string and print its length and the first character.
string=input("please enter a string:")
length=len(string)
first_character=string[0]
print(f"length of the string is: {length}")
print(f"first character of the string is: {first_character}")

# 7. Take a list of numbers and print the sum and average of the numbers.
numbers=input("please enter a list of numbers separated by space:").split() # split() is used to split the string into a list of strings based on the separator, in this case, space. It returns a list of strings.
numbers=[int(num) for num in numbers] # convert the list of strings to list of integers-we use list comprehension to iterate through the list of strings and convert each string to integer using int() function.
sum_of_numbers=sum(numbers)
average_of_numbers=sum_of_numbers/len(numbers)
print(f"sum of the numbers is: {sum_of_numbers}")
print(f"average of the numbers is: {average_of_numbers}")   

# 8. Take a list of strings and print the longest string in the list.
strings=input("please enter a list of strings separated by space:").split()
longest_string=max(strings, key=len) # max() function is used to find the longest string in the list. We use key=len to specify that we want to compare the strings based on their length.
print(f"longest string in the list is: {longest_string}")

# 9. Take a list of numbers and print the largest and smallest number in the list.
numbers=input("please enter a list of numbers separated by space:").split()
numbers=[int(num) for num in numbers]
largest_number=max(numbers)
smallest_number=min(numbers)
print(f"largest number in the list is: {largest_number}")
print(f"smallest number in the list is: {smallest_number}")

# 10. Take a list of strings and print the strings in reverse order.
strings=input("please enter a list of strings separated by space:").split()
reversed_strings=strings[::-1] # we use slicing to reverse the list of strings.
print(f"strings in reverse order are: {reversed_strings}")

# 11. Take a list of numbers and print the numbers in sorted order.
numbers=input("please enter a list of numbers separated by space:").split()
numbers=[int(num) for num in numbers]
sorted_numbers=sorted(numbers) # sorted() function is used to sort the list of numbers in ascending order.
print(f"numbers in sorted order are: {sorted_numbers}") 

# 12. Take a list of strings and print the strings in sorted order.
strings=input("please enter a list of strings separated by space:").split()
sorted_strings=sorted(strings) # sorted() function is used to sort the list of strings in ascending order.
print(f"strings in sorted order are: {sorted_strings}")

# 13. Take a list of numbers and print the even and odd numbers in separate lists.
numbers=input("please enter a list of numbers separated by space:").split()
numbers=[int(num) for num in numbers]
even_numbers=[num for num in numbers if num%2==0] # we use list comprehension to iterate through the list of numbers and check if each number is even or odd using the modulus operator. If the number is even, we add it to the even_numbers list, otherwise, we add it to the odd_numbers list.
odd_numbers=[num for num in numbers if num%2!=0]
print(f"even numbers in the list are: {even_numbers}")
print(f"odd numbers in the list are: {odd_numbers}")

# 14. Take a list of strings and print the strings that start with a specific letter.
strings=input("please enter a list of strings separated by space:").split()
letter=input("please enter a letter:")
strings_starting_with_letter=[string for string in strings if string.startswith(letter)] # we use list comprehension to iterate through the list of strings and check if each string starts with the specified letter using the startswith() method. If the string starts with the letter, we add it to the strings_starting_with_letter list.
print(f"strings that start with {letter} are: {strings_starting_with_letter}")  


# 15. Take a list of numbers and print the numbers that are greater than a specific number.
numbers=input("please enter a list of numbers separated by space:").split()
numbers=[int(num) for num in numbers]
specific_number=int(input("please enter a specific number:"))
numbers_greater_than_specific_number=[num for num in numbers if num>specific_number] # we use list comprehension to iterate through the list of numbers and check if each number is greater than the specified number. If the number is greater than the specific number, we add it to the numbers_greater_than_specific_number list.
print(f"numbers that are greater than {specific_number} are: {numbers_greater_than_specific_number}")   


# 16. Take a list of strings and print the strings that contain a specific substring.
strings=input("please enter a list of strings separated by space:").split()
substring=input("please enter a specific substring:")
strings_containing_substring=[string for string in strings if substring in string] # we use list comprehension to iterate through the list of strings and check if each string contains the specified substring using the in operator. If the string contains the substring, we add it to the strings_containing_substring list.
print(f"strings that contain {substring} are: {strings_containing_substring}")  

# 17. Take a list of numbers and print the numbers that are divisible by a specific number.
numbers=input("please enter a list of numbers separated by space:").split()
numbers=[int(num) for num in numbers]
specific_number=int(input("please enter a specific number:"))
numbers_divisible_by_specific_number=[num for num in numbers if num%specific_number==0] # we use list comprehension to iterate through the list of numbers and check if each number is divisible by the specified number using the modulus operator. If the number is divisible by the specific number, we add it to the numbers_divisible_by_specific_number list.
print(f"numbers that are divisible by {specific_number} are: {numbers_divisible_by_specific_number}")   


# 18. Take a list of strings and print the strings that are palindromes.
strings=input("please enter a list of strings separated by space:").split()
palindrome_strings=[string for string in strings if string==string[::-1]] # we use list comprehension to iterate through the list of strings and check if each string is a palindrome by comparing the string with its reverse using slicing. If the string is a palindrome, we add it to the palindrome_strings list.
print(f"palindrome strings in the list are: {palindrome_strings}")      

# 19. Take a list of numbers and print the numbers that are prime.
numbers=input("please enter a list of numbers separated by space:").split()
numbers=[int(num) for num in numbers]
def is_prime(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True
prime_numbers=[num for num in numbers if is_prime(num)] # we use list comprehension to iterate through the list of numbers and check if each number is prime using the is_prime() function. If the number is prime, we add it to the prime_numbers list.
print(f"prime numbers in the list are: {prime_numbers}")    

# 20. Take a list of strings and print the strings that are anagrams of a specific string.
strings=input("please enter a list of strings separated by space:").split()
specific_string=input("please enter a specific string:")
anagram_strings=[string for string in strings if sorted(string)==sorted(specific_string)] # we use list comprehension to iterate through the list of strings and check if each string is an anagram of the specified string by comparing the sorted characters of both strings. If the sorted characters are the same   we add the string to the anagram_strings list.
print(f"strings that are anagrams of {specific_string} are: {anagram_strings}")


# 21. Take a list of numbers and print the numbers that are perfect squares.
numbers=input("please enter a list of numbers separated by space:").split()
numbers=[int(num) for num in numbers]
perfect_square_numbers=[num for num in numbers if int(num**0.5)**2==num] # we use list comprehension to iterate through the list of numbers and check if each number is a perfect square by comparing the integer value of the square root of the number squared with the original number. If they are equal, we add the number to the perfect_square_numbers list.
print(f"perfect square numbers in the list are: {perfect_square_numbers}")



# 22. Take a list of strings and print the strings that are in uppercase.
strings=input("please enter a list of strings separated by space:").split()
uppercase_strings=[string for string in strings if string.isupper()] # we use list comprehension to iterate through the list of strings and check if each string is in uppercase using the isupper() method. If the string is in uppercase, we add it to the uppercase_strings list.
print(f"strings that are in uppercase are: {uppercase_strings}")    

# 23. Take a list of numbers and print the numbers that are in descending order.
numbers=input("please enter a list of numbers separated by space:").split()
numbers=[int(num) for num in numbers]
descending_order_numbers=sorted(numbers, reverse=True) # sorted() function is used to sort the list of numbers in descending order by setting the reverse parameter to True.
print(f"numbers in descending order are: {descending_order_numbers}")   

# 24. Take a list of strings and print the strings that are in lowercase.
strings=input("please enter a list of strings separated by space:").split()
lowercase_strings=[string for string in strings if string.islower()] # we use list comprehension to iterate through the list of strings and check if each string is in lowercase using the islower() method. If the string is in lowercase, we add it to the lowercase_strings list.
print(f"strings that are in lowercase are: {lowercase_strings}")    

# 25. Take a list of numbers and print the numbers that are in ascending order.
numbers=input("please enter a list of numbers separated by space:").split()
numbers=[int(num) for num in numbers]
ascending_order_numbers=sorted(numbers) # sorted() function is used to sort the list of numbers in ascending order.
print(f"numbers in ascending order are: {ascending_order_numbers}") 

# 26. Take a list of strings and print the strings that are in title case.
strings=input("please enter a list of strings separated by space:").split()
title_case_strings=[string for string in strings if string.istitle()] # we use list comprehension to iterate through the list of strings and check if each string is in title case using the istitle() method. If the string is in title case, we add it to the title_case_strings
list.print(f"strings that are in title case are: {title_case_strings}")

# 27. Take a list of numbers and print the numbers that are in even order.
numbers=input("please enter a list of numbers separated by space:").split()
numbers=[int(num) for num in numbers]
even_order_numbers=[num for num in numbers if num%2==0] # we use list comprehension to iterate through the list of numbers and check if each number is in even order by checking if the number is even using the modulus operator. If the number is even, we add it to the even_order_numbers list.
print(f"numbers in even order are: {even_order_numbers}")   


# 28. Take a list of strings and print the strings that are in title case.
strings=input("please enter a list of strings separated by space:").split()
title_case_strings=[string for string in strings if string.istitle()] # we use list comprehension to iterate through the list of strings and check if each string is in title case using the istitle() method. If the string is in title case, we add it to the title_case_strings list.
print(f"strings that are in title case are: {title_case_strings}")  


# 29. Take a list of numbers and print the numbers that are in odd order.
numbers=input("please enter a list of numbers separated by space:").split()
numbers=[int(num) for num in numbers]
odd_order_numbers=[num for num in numbers if num%2!=0] # we use list comprehension to iterate through the list of numbers and check if each number is in odd order by checking if the number is odd using the modulus operator. If the number is odd, we add it to the odd_order_numbers list.
print(f"numbers in odd order are: {odd_order_numbers}")

# 30. Take a list of strings and print the strings that are in uppercase.
strings=input("please enter a list of strings separated by space:").split()
uppercase_strings=[string for string in strings if string.isupper()] # we use list comprehension to iterate through the list of strings and check if each string is in uppercase using the isupper() method. If the string is in uppercase, we add it to the uppercase_strings list.
print(f"strings that are in uppercase are: {uppercase_strings}")    


# 31. Take a list of numbers and print the numbers that are in prime order.
numbers=input("please enter a list of numbers separated by space:").split()
numbers=[int(num) for num in numbers]
def is_prime(num):  
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True 

prime_order_numbers=[num for num in numbers if is_prime(num)] # we use list comprehension to iterate through the list of numbers and check if each number is in prime order using the is_prime() function. If the number is prime, we add it to the prime_order_numbers list.
print(f"numbers in prime order are: {prime_order_numbers}")



# 32. Take a list of strings and print the strings that are in lowercase.
strings=input("please enter a list of strings separated by space:").split()
lowercase_strings=[string for string in strings if string.islower()] # we use list comprehension to iterate through the list of strings and check if each string is in lowercase using the islower() method. If the string is in lowercase, we add it to the lowercase_strings list.
print(f"strings that are in lowercase are: {lowercase_strings}")        


# 33. Take a list of numbers and print the numbers that are in perfect square order.
numbers=input("please enter a list of numbers separated by space:").split()
numbers=[int(num) for num in numbers]
perfect_square_order_numbers=[num for num in numbers if int(num**0.5)**2==num] # we use list comprehension to iterate through the list of numbers and check if each number is in perfect square order by comparing the integer value of the square root of the number squared with the original number. If they are equal, we add the number to the perfect_square_order_numbers list.  
print(f"numbers in perfect square order are: {perfect_square_order_numbers}")


# 34. Take a list of strings and print the strings that are in title case.
strings=input("please enter a list of strings separated by space:").split()
title_case_strings=[string for string in strings if string.istitle()] # we use list comprehension to iterate through the list of strings and check if each string is in title case using the istitle() method. If the string is in title case, we add it to the title_case_strings list.
print(f"strings that are in title case are: {title_case_strings}")  

# 35. Take a list of numbers and print the numbers that are in even order.
numbers=input("please enter a list of numbers separated by space:").split()
numbers=[int(num) for num in numbers]
even_order_numbers=[num for num in numbers if num%2==0] # we use list comprehension to iterate through the list of numbers and check if each number is in even order by checking if the number is even using the modulus operator. If the number is even, we add it to the even_order_numbers list.
print(f"numbers in even order are: {even_order_numbers}")       

# 36. Take a list of strings and print the strings that are in title case.
strings=input("please enter a list of strings separated by space:").split()
title_case_strings=[string for string in strings if string.istitle()] # we use list comprehension to iterate through the list of strings and check if each string is in title case using the istitle() method. If the string is in title case, we add it to the title_case_strings list.
print(f"strings that are in title case are: {title_case_strings}")  
