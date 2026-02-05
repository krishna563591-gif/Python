# deleting the element in an array:
# syntax:
'''  
np.delete(array,indexing,axis=None)-flatten array

'''
# examples:
import numpy as np
arr=np.array([10,20,30,40,50,60])
new_arr=np.delete(arr,0)
print(new_arr)

# deleting in 2d array:

arr_2d=np.array([[1,2,3],[4,5,6]])
new_2d_arr= np.delete(arr_2d,0,axis=0) # 0 indexing means- first row.
print(new_2d_arr)
