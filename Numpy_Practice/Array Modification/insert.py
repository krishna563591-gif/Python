# inserting value in an array.
"""
np.insert(array,index,value,axis=None)
array-original array
index-at which index
value- which value
axis-none
axis-0,row-wise- in 2d
axis-1 column wise- in 3d


"""
# inserting in 1d array:
import numpy as np
arr=np.array([10,20,30,40,50,60])
print(arr) # original array
new_arr=np.insert(arr,2,100) # insert 100 at index of 2.
print(new_arr)


# inserting in 2d array:
import numpy as np
arr_2d=np.array([[1,2],[3,4]]) # [1,2]-0 index, [3,4]-1index
# insert new row at index 1.
new_arr_2d= np.insert(arr_2d,1,[5,6],axis=0)
print(new_arr_2d)
