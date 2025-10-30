import numpy as np

#One Dimensional Array:A one-dimensional array is a type of linear array.
list_1 = [1, 2, 3, 4]
sample_array = np.array(list_1)
print("List in python : ", list_1)
print("Numpy Array in python :",sample_array)

print(type(list_1))
print(type(sample_array))
print("_________________________________________________________________________________")

#Multi-Dimensional Array:A Multi-Dimensional Array is an array that can store data in more than one dimension such 
#as rows and columns. In simple terms it is a array of arrays.
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = [9, 10, 11, 12]

sample_array = np.array([list_1, list_2,list_3])
print("Numpy multi dimensional array in python\n",sample_array)
print("_________________________________________________________________________________")

#1.Axis: Axis of an array describes the order of the indexing into the array.
#Axis 0 = one dimensional
#Axis 1 = Two dimensional
#Axis 2 = Three dimensional

#2.Shape: Number of elements along with each axis and is returned as a tuple.
print("shape of the array :",sample_array.shape)
print("_________________________________________________________________________________")

#3.Rank: Rank of an array is simply the number of axes or dimensions it has.
#One-dimensional array has rank 1
#Two-dimensional array has rank 2

#4.Data type objects (dtype): Data type objects (dtype) is an example of numpy.dtype class. It describes how the 
#bytes in the fixed-size block of memory corresponding to an array item should be interpreted.
sample_array_1 = np.array([[0, 4, 2]])
sample_array_2 = np.array([0.2, 0.4, 2.4])
print("Data type of the array 1 :",sample_array_1.dtype)
print("Data type of array 2 :",sample_array_2.dtype)
print("_________________________________________________________________________________")

#5.numpy.fromiter(): The fromiter() function create a new one-dimensional array from an iterable object.
var = "Geekforgeeks"
arr = np.fromiter(var, dtype = 'U2')
print("fromiter() array :",arr)
print("_________________________________________________________________________________")

#6.numpy.arange(): This is an inbuilt NumPy function that returns evenly spaced values within a given interval.
print(np.arange(1, 20 , 2, dtype = np.float32))
print("_________________________________________________________________________________")

#7.numpy.linspace(): This function returns evenly spaced numbers over a specified between two limits. 
print(np.linspace(3.5, 15, 5, dtype = np.int32))
print("_________________________________________________________________________________")

#8.numpy.empty(): This function create a new array of given shape and type without initializing value.
print(np.empty([4, 3],dtype = np.int32,order = 'f'))
print("_________________________________________________________________________________")

#9.numpy.ones(): This function is used to get a new array of given shape and type filled with ones (1).
print(np.ones([4, 3],dtype = np.int32,order = 'f'))
print("_________________________________________________________________________________")

#10.numpy.zeros(): This function is used to get a new array of given shape and type filled with zeros (0). 
print(np.zeros([4, 3],dtype = np.int32,order = 'f'))
print("_________________________________________________________________________________")

#11.ndarray.ndim: Returns the number of dimensions (axes) of the array.
print("Dimensions:", sample_array.ndim) 
print("_________________________________________________________________________________")

#12.ndarray.size: Returns the total number of elements in the array. 
print("Size:", sample_array.size) 
print("_________________________________________________________________________________")

#13.ndarray.dtype: Provides the data type of the array elements. 
print("Data type:", sample_array.dtype)  
print("_________________________________________________________________________________")

#14.ndarray.itemsize: Returns the size in bytes of each element
print("Item size:", sample_array.itemsize)
print("_________________________________________________________________________________")