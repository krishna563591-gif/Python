# Reshaping of array: changing dimmesions of an array without modifying the data:
# from 1d array to 2d or 3d.
# syntax:
'''
arr.reshape( rows,columns) specify new shape
should match the dimensions.
'''
# example: 
import numpy as np
arr= np.array([1,2,3,4,5,6])
reshaped_Arr= arr.reshape(2, 3) #  i need 2 rows 3 columns.
print(reshaped_Arr)

# reshaping does not create any copy but it returns the new view.


