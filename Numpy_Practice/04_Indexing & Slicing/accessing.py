# Accessing elements with indexing in an array:[0,1,23........]
#Syntax:
#array[index] # 1d array
#array[row,column] # 2d array


import numpy as np
arr= np.array([10,20,30,40,50])
print(arr[0]) # first element
print(arr[2]) # 30
print(arr[-1]) # last element.


# slicing an array: extracting subsets of an array:
# syntax: arr[start,stop,step] stop-excluded element.step default value-1
# arr[start:end],strt to end -1
# negative step,-1 reverse.


arr1= np.array([10,20,30,40,50,60])
print(arr[1:5]) # index 1 to 4.
print(arr[:4]) # index 0 to 3.
print(arr[::2]) # it picks every 2nd element.
print(arr[::-1]) # reverse the whole array



# Fancy Indexing: selecting multiple multple elements at once.
arr2=np.array([10,20,30,40,50,60])
print(arr2[[0,2,4]]) # 10 30 50

# 

