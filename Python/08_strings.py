# We can write strings in 3 ways:

#1.Using single quotes
str1='Hello, World!'
print("String using single quotes:", str1)

#2.Using double quotes
str2="Hello, Python!"
print("String using double quotes:", str2)

#3.Using triple quotes
str3="""Hello,
This is a multi-line string."""
print("String using triple quotes:", str3)
print("Type of str3:", type(str3))  #<class 'str'>

#String Slicing
name="krishna"
print("length of the string 'krishna':", len(name))  #8
print("Original String:", name) #krishna
print("First character:", name[0])  #k
print("Last character:", name[-1])  #a

# Indexing and slicing of string: we can extract a part of the string using slicing.

#Indexing of the string: 
text='Python'
print(text[0])  #P
print(text[1])  #y
print(text[2])  #t
print(text[3])  #h
print(text[4])  #o
print(text[5])  #n

#Negative indexing of the string:
print(text[-1])  #n
print(text[-2])  #o
print(text[-3])  #h
print(text[-4])  #t
print(text[-5])  #y
print(text[-6])  #P 

# Slicing of the string:

name_slice1=name[0:4]  #slicing from index 0 to 3-excluding index 4.
print("Sliced String (0-4):", name_slice1)  #kris
name_slice2=name[2:6]  #slicing from index 2 to 5-excluding index 6
print("Sliced String (2-6):", name_slice2)  #ishn
name_slice3=name[:5]   #slicing from start to index 4-excluding index 5
print("Sliced String (:5):", name_slice3)   #krish
name_slice4=name[3:]   #slicing from index 3 to end of the string
print("Sliced String (3:):", name_slice4)   #shna




#Skip characters while slicing: [START:STOP:STEP] STEP-SKIPING CHARACTERS
a="abcdefghijklmnopqrstuvwxyz"
print(a[1:9:4]) #answer-beh
#frist lets print[1:9]-'bcdefghi' start from 1 & skip 9th index.
#now [1:9:4]-'beh' start from index 1 & skip 4 characters.

#====================================
#Reversing a string using slicing
word='krishna'
print(word[:7])  #krishna - means [0:7]
print(word[0:])  #krishna - means [0:7]


# String Methods:
#1. len(): Returns the length of the string.
word="Hello, World!"
print("Length of word:", len(word))  #13

#2. upper(): Converts all characters in the string to uppercase.
print("Uppercase:", word.upper())  #HELLO, WORLD!

#3. lower(): Converts all characters in the string to lowercase.
print("Lowercase:", word.lower())  #hello, world!

#4. strip(): Removes any leading and trailing whitespace from the string.
word_with_spaces="   Hello, World!   "
print("Stripped String:", word_with_spaces.strip())  #Hello, World!

#5. replace(): Replaces a specified phrase with another specified phrase.
print("Replaced String:", word.replace("World", "Python"))  #Hello, Python

#6. split(): Splits the string into a list where each word is a list item.
print("Split String:", word.split(","))  #['Hello', ' World!']

#7. find(): Searches the string for a specified value and returns the position of where it was found.
print("Position of 'World':", word.find("World"))  #7
#8. count(): Returns the number of times a specified value occurs in a string.
print("Count of 'l':", word.count("l"))  #3

#9. isalpha(): Returns True if all characters in the string are alphabetic.
print("Is alphabetic:", word.isalpha())  #False (because of comma and space

#10. isdigit(): Returns True if all characters in the string are digits.
num_str="12345"
print("Is digit:", num_str.isdigit())  #True



#imporant string functions
#11. startswith(): Returns True if the string starts with the specified value.
print("Starts with 'Hello':", word.startswith("Hello"))  #True

#12. endswith(): Returns True if the string ends with the specified value.
print("Ends with 'World!':", word.endswith("World!"))  #True


#13. capitalize(): Converts the first character to upper case.
print("Capitalized String:", word.capitalize())  #Hello, world!

#14. title(): Converts the first character of each word to upper case.
print("Title String:", word.title())  #Hello, World!
#15. center(): Returns a centered string.
print("Centered String:", word.center(20, '-'))  #---Hello, World!

#16. join(): Joins the elements of an iterable to the end of the string.
words_list=["Hello", "World", "from", "Python"]
print("Joined String:", " ".join(words_list))  #Hello World from Python

#17. format(): Formats specified values in a string.
name="Alice"
age=30
print("Formatted String:", "My name is {} and I am {} years old.".format(name, age))
#My name is Alice and I am 30 years old.   

#18. ord(): Returns the Unicode code of a character.
char='A'    
print("Unicode of 'A':", ord(char))  #65

#19. chr(): Returns the character that represents the specified Unicode code.
code=65
print("Character of Unicode 65:", chr(code))  #A
#20. zfill(): Fills the string with zeros until it reaches the specified length.
num_str="42"
print("Zero filled String:", num_str.zfill(5))  #00042


#String Concatenation
word1="Hello"
word2="World"
concatenated=word1 + ", " + word2 + "!"
print("Concatenated String:", concatenated)  #Hello, World!

#String Repetition
repeat_word="Ha"
repeated=repeat_word * 3
print("Repeated String:", repeated)  #HaHaHa

#String Membership
sentence="The quick brown fox"
print("Is 'quick' in sentence?", "quick" in sentence)  #True
print("Is 'slow' not in sentence?", "slow" not in sentence)  #True
#Escape Characters
print("He said, \"Hello!\"")  #He said, "Hello!"
print('It\'s a beautiful day!')  #It's a beautiful day!
print("First Line\nSecond Line")
#First Line
#Second Line
print("Column1\tColumn2\tColumn3")  #Column1	Column2
#String Formatting using f-strings (Python 3.6+)
name="Bob"
age=25
formatted_string=f"My name is {name} and I am {age} years old."
print("Formatted String using f-strings:", formatted_string)

#Raw Strings
raw_string=r"C:\Users\Name\Documents"
print("Raw String:", raw_string)  #C:\Users\Name\Documents
#Multiline Strings
multiline_string="""This is a string
that spans multiple
lines."""
print("Multiline String:", multiline_string)
#This is a string
#that spans multiple
#lines.     
#String Methods for Checking Content
alphanumeric="abc123"
print("Is Alphanumeric:", alphanumeric.isalnum())  #True
whitespace="   \t\n"
print("Is Whitespace:", whitespace.isspace())  #True
alphabetic="Hello"
print("Is Alphabetic:", alphabetic.isalpha())  #True
digit_string="4567"
print("Is Digit:", digit_string.isdigit())  #True   


#Escape Sequences in Strings-there are more escape sequences.
a="krishna is a good boy\n but not \"bad\" one"
print(a)  




