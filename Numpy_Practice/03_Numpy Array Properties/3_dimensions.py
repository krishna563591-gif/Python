# To know the numbers of Dimensions of array:
import numpy as np

arr_1d = np.array([1, 2, 3]) # sigle row list-1d array.



arr_2d = np.array([[1, 2, 3], [4, 5, 6]]) #  list withrow & columns-2d array.


arr_3d = np.array([                      # stack of mutltiple 2d arrays-3d array.
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print(arr_1d.ndim)  # 1
print(arr_2d.ndim)  # 2
print(arr_3d.ndim)  # 3

#ndim= number of dimentiosns.