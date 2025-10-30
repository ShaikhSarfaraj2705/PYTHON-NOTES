#CLASS METHOD AS ALTERNATIVE CONSTRUCTORS:
#-when you want to create an object  from data thatbis stored in different format, such as 
#a string or dictionary.
#when you ewant ot  create an object  with a different set of default valuesthan what is 
#provided by default constructor.

#ex.1:
class person:
    def __init__(self,name,age):
        self.name=name 
        self.age=age
    @classmethod
    def from_string(cls,string):
        name, age=string.split("-")
        return cls(name,int(age))
p1=person.from_string("ayush ranvijay kumar-50")
print(p1.name)
print(p1.age)
print("_________________________________________________________________________________")

#ex.2:
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def from_string(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])
e=Employee("akshay",25000)
print(e.name)
print(e.salary)
e1=Employee.from_string("shambhuraj-50000")
print(e1.name)
print(e1.salary)