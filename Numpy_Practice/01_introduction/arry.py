# Array- collections of datas: 
# storing data in variables:
mark1=90
mark2=94
mark3=80
mark4=70

# storing data in array
marks=[90,94,80,70]

# Types of array:
#1. 1 Dimensional Array- a simple list of numbers stored in a single row.
import numpy as np
ar_1d=np.array([10,20,30,40])


#2.2D Array: datas are stored in rows & columns.
import numpy as np
arr_2d=np.array([1,2,3],
                [4,5,6],
                [7,8,9])
print(arr_2d)


#3.Multi-Dimensional Array-array with more than 2 dimensions-stack of multiple 2d arrays.
import numpy as np

arr_3d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])

print(arr_3d.shape)
# Output: (2, 2, 3) - 2 layers, 2 rows, 3 columns






#matrix-stac
import numpy as np
matrix=np.array([2,4,6],
                [8,10,12])
