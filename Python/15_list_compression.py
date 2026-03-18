# create a list of integers and print their squares.
list=[1,2,3,4,5]
squares=[i*i for i in list] # explained: for each element i in list, calculate i*i and add it to the new list squares
print(squares) # output: [1, 4, 9, 16, 25]

# create a list and print even numbers.
numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=[i for i in numbers if i%2==0] # explained: for each element i in numbers, check if it is even (i%2==0) and if true, add it to the new list even_numbers
print(even_numbers) # output: [2, 4, 6, 8, 10]

# create a list andprint odd numbers.
odd_numbers=[i for i in numbers if i%2!=0] # explained: for each element i in numbers, check if it is odd (i%2!=0) and if true, add it to the new list odd_numbers
print(odd_numbers) # output: [1, 3, 5, 7, 9]

# create a list of strings and print their lengths.
strings=["hello", "world", "python", "programming"]
lengths=[len(s) for s in strings] # explained: for each element s in strings, calculate its length using len(s) and add it to the new list lengths
print(lengths) # output: [5, 5, 6, 11]

# create a list of integers and print their cubes.
cubes=[i**3 for i in list] # explained: for each element i in list, calculate i**3 (i raised to the power of 3) and add it to the new list cubes
print(cubes) # output: [1, 8, 27, 64, 125]

# create a list of integers and print their squares if they are even.
even_squares=[i*i for i in list if i%2==0] # explained: for each element i in list, check if it is even (i%2==0) and if true, calculate i*i and add it to the new list even_squares
print(even_squares) # output: [4, 16]

