# ============================================================================
# DICTIONARIES & SETS in Python
# ============================================================================

# ==========================
# DICTIONARIES- a collection of data in key-value pairs.
# Dictionaries are used to store data values in key:value pairs.
# ==========================

# Creating dictionaries
empty_dict = {}

# eg.-2 
marks={
    "Harry":100,
    "krishna":200,
    "Rohan":99
}
#print(marks,type(marks))
#print(marks["Harry"])

#updating
marks.update({"Harry":400,"Renuka":500})
print(marks)

#Getting Values:
print(marks.get("shivika")) #None
print(marks.get("Harry")) #400


#methods
#print(marks.keys())
#print(marks.values())
#print(marks.items())
#popitems()
#pop()

#-----------------------------------------------more------------------------------------------

#eg.-2
dict_with_values = {
    "name": "John", 
    "age": 30,
    "city": "New York"}

dict_from_dict = dict(name="Alice", age=25)

# Accessing values
print(dict_with_values["name"])  # John
print(dict_with_values.get("age"))  # 30
print(dict_with_values.get("country", "Not found"))  # Not found

# Adding/Updating items
dict_with_values["country"] = "USA"
dict_with_values.update({"age": 31, "job": "Engineer"})

# Removing items
del dict_with_values["city"]  # Using del
dict_with_values.pop("job")  # Using pop
dict_with_values.popitem()  # Removes last item

# Iterating through dictionaries
for key in dict_with_values:
    print(f"{key}: {dict_with_values[key]}")

for key, value in dict_with_values.items():
    print(f"{key}: {value}")

for key in dict_with_values.keys():
    print(key)

for value in dict_with_values.values():
    print(value)


# Properties of python Dictionaires
#1.it is onordered.
#1.it is mutable.
#1.it is indexed.
#1.it is cannot contain duplicate keys.



# Dictionary methods
print(dict_with_values.keys())  # dict_keys(['name', 'age', 'country'])
print(dict_with_values.values())  # dict_values(['John', 31, 'USA'])
print(dict_with_values.items())  # dict_items([('name', 'John'), ('age', 31), ('country', 'USA')])
print(len(dict_with_values))  # 3
print("name" in dict_with_values)  # True

# Copy dictionary
dict_copy = dict_with_values.copy()
dict_deep = dict(dict_with_values)

# =======================================================Sets==========================================
# why do we need set?- no element can repeat in set.-in sitution where no element should return-remove duplicates.
#e.g. 
s={3,1,4,5,5,7,9}
print(s) # prints {3,1,4,5,7,9} # also doesnot maintain order.

#priorities of sets
#1. sets are onordered= Element's order doesnot matter.
#2. sets are unindexed= cannot access elements by index
#there is no way to chanege items in sets.
#sets cannot contain duplicate value.




# Creating sets----{}
empty_set = set()  # Note: {} creates an empty dict, not set.

set_with_values = {1, 2, 3, 4, 5}

set_from_list = set([1, 2, 2, 3, 3, 4])  # {1, 2, 3, 4} - removes duplicates
set_from_string = set("hello")  # {'h', 'e', 'l', 'o'}

# Adding/Removing items
set_with_values.add(6)
set_with_values.update([7, 8, 9])  # Add multiple items
set_with_values.remove(6)  # Raises error if not found
set_with_values.discard(8)  # No error if not found
set_with_values.pop()  # Remove arbitrary item

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union=take all value from both set but no repetition.
union = set_a | set_b  # {1, 2, 3, 4, 5, 6}
union = set_a.union(set_b)

# Intersection= common between two sets
intersection = set_a & set_b  # {3, 4}
intersection = set_a.intersection(set_b)

# Difference=
difference = set_a - set_b  # {1, 2}
difference = set_a.difference(set_b)

# Symmetric difference
sym_diff = set_a ^ set_b  # {1, 2, 5, 6}
sym_diff = set_a.symmetric_difference(set_b)

# Subset/Superset
print(set_a.issubset(set_b))  # False
print(set_a.issuperset(set_b))  # False
print({1, 2}.issubset(set_a))  # True

#-------------------------------------set methods---------------------------------
# len method
print(len(set_with_values))
print(3 in set_with_values)
# copy method
set_copy = set_with_values.copy()
# clear method
set_with_values.clear()  # Empties the set

# ==========================
# PRACTICAL EXAMPLES
# ==========================

# Dictionary example: Student grades
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95
}

# Find students with grade > 80
top_students = {name: grade for name, grade in students.items() if grade > 80}
print(top_students)

# Set example: Remove duplicates from list
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)

# Nested dictionary
company = {
    "employees": {
        "emp1": {"name": "John", "dept": "IT"},
        "emp2": {"name": "Jane", "dept": "HR"}
    },
    "locations": ["NYC", "LA", "Chicago"]
}

print(company["employees"]["emp1"]["name"])  # John

#===============================================Questions=====================================================

#. Write a program to create a dictionary of hindi words with values as their english translation.provide user with an option to look it up.
words={
    "madad":"help",
    "kursi":"chai",
    "billi":"cat"

}
word=input("Enter a word you want meanig of :")
print(words[word])

#.write a program to input eight numbrs from users & display all the unigue numbers (once).
s=()
n=int(input("enter a number:"))
s.add(int(n))
n=int(input("enter a number:"))
s.add(int(n))
n=int(input("enter a number:"))
s.add(int(n))
n=int(input("enter a number:"))
s.add(int(n))
n=int(input("enter a number:"))
s.add(int(n))
n=int(input("enter a number:"))
s.add(int(n))
n=int(input("enter a number:"))
s.add(int(n))
print(s)

# can we have a set with 18(int) & '18' (str) as a value in it?
s=[]
s.add(18)
s.('18')
print(s) # s={'18',18}

#.Find length of the set?
s=set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s)) # answer-2 bcz 1==1.0


#.s={} find type of s.
print(type (s)) # dictionary.


#.



