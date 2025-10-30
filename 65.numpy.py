#1Addition of Arrays:Addition is an arithmetic operation where the corresponding elements of two arrays are added
#together.In NumPy the addition of two arrays is done using the np.add() function.
import numpy as np
a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])
add_ans = np.add(a, b)
print(add_ans)

#2.Subtraction of Arrays:We can subtract two arrays element-wise using the np.subtract() function.This function
#subtracts each element of the second array from the corresponding element in the first array.
sub_ans = np.subtract(a, b)
print(sub_ans)

#3.Multiplication of Arrays:Multiplication in NumPy can be done element-wise using the np.multiply() function.This 
#multiplies corresponding elements of two arrays.
mul_ans = np.multiply(a, b)
print(mul_ans)

#4.Division of Arrays:Division is another important operation that is performed element-wise using the np.divide()
#function. This divides each element of the first array by the corresponding element in the second array
div_ans = np.divide(a, b)
print(div_ans)

#5.Exponentiation (Power):It allows us to raise each element in an array to a specified power. In NumPy, this can 
#be done using the np.power() function.
pow_ans = np.power(a, b)
print(pow_ans)

#6.Modulus Operation:It finds the remainder when one number is divided by another.In NumPy,you can use the np.mod() 
#function to calculate the modulus element-wise between two arrays.
mod_ans = np.mod(a, b)
print(mod_ans)

#7.Broadcasting:
a1= np.array([1, 2, 3])
res = a1 + 1  
print(res) 
#or
a2 = np.array([[1, 3, 5], [7, 9, 11]])
res = a1 + a2
print(res)

#8.Broadcasting in Conditional Operations:We may need to apply a condition to an entire array or a subset of it. 
#Broadcasting can help to perform these operations efficiently without needing loops.
ages = np.array([12, 24, 35, 45, 60, 72])
age_group = np.array(["Adult", "Minor"])
result = np.where(ages > 18, age_group[0], age_group[1])
print(result)

#9.Broadcasting for Matrix Multiplication:In this example, each element of a 2D matrix is multiplied by the 
#corresponding element in a broadcasted vector.
matrix = np.array([[1, 2], [3, 4]])
vector = np.array([10, 20])
result = matrix * vector
print(result)

result=matrix*vector[:, np.newaxis]
print(result)