# creating arrays from python lists.
#syntax:
'''
np.array([ele1,ele2,ele3])

'''
import numpy as np
arr=np.array([1,2,3,4])
print(arr)

# # creating arrays with default values:
# syntax: np.zeros(shape) (3)-for 1d, (3,3) for 2d
import numpy as np
zeroes_array=np.zeros(3)
print(zeroes_array)

#  creating arrays with ones:
import numpy as np
ones_array=np.ones((2,3)) # inside tuples- 2 rows 3 columns.
print(ones_array)

# creating arrays with full(shape,value):
import numpy as np
filled_array=np.full((2,2),7)