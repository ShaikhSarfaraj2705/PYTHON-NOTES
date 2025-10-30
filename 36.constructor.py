#CONSTRUCTOR:the constructor is a special method in a class used to create and initialize
#an object of a class.a constructor is a unique function that get called automatically 
#when an object is created of a class.

#Types of  constructor:
#i)default constructor
class employee:
    def __init__(self):
        print("employee is working")
a=employee()
print("_________________________________________________________________________________")
#ii)parameterized constructor
class person:
    def __init__(self,n,a,c):
        self.name=n
        self.age=a
        self.city=c
    def info(self):
        print(f"{self.name} is {self.age} old and he is from {self.city}")
    
a=person("sarfaraj",22,"karad")
a.info()