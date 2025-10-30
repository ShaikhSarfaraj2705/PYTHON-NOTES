# Array Indexing and Slicing
#We can access individual elements in an array using square brackets just like Python lists. The indexing starts at 0.
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[2])
print(arr_2d[1, 2])  

#It allows us to extract sub-arrays using a range of indices. The syntax is [start:stop] where start is inclusive 
#and stop is exclusive.
print(arr[1:4])
print(arr_2d[0:2, 1:3])