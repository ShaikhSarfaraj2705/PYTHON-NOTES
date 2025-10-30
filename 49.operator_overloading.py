#OPERATOR OVERLOADING:is a feature in python that allows developers to redefine the 
#behavioral of mathematical and comparison operators for custom data types.this means that 
#you can use the standard mathematical operators(+,-,*/,etc)and comparison operators(>,<,==,etc)
#in ypur own classes,just as you would for built-in data types like int,float,and str.
class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
    def __add__(self,x):
        return vector(self.i+x.i,self.j+x.j,self.k+x.k)
v1=vector(5,7,9)
print(v1)
v2=vector(3,6,1)
print(v2)
print("-----------")
print(v1+v2)