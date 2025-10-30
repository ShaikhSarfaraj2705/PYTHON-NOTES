#ACCESS SPECIFIERS/MODIFIERS:in python programming are used to limit the access of class 
#variables and methods outside of class while implementing the concepts of inheritance.
#TYPES OF ACCESS SPECIFIERS:
    #a]public access modifiers
    #b]private access modifiers
    #c]protected access modiiers

#a]PUBLIC ACCESS SPECIFIERS:all the variables and methods(member functions) in python are 
#by default public.any instance varable in a class followed by the 'self' keyword ie., 
#self.var_name are public accessed.
class student:
    def __init__(self,name, age):
        self.name=name      #public variable
        self.age=age

a=student("sarfaraj",22)
print(a.name)
print(a.age)
print("_________________________________________________________________________________")

#b]PROTECTED ACCESS SPECIFIERS:the termed 'protected' is used to describe a member function 
#(ie., amethod  orattribute) of a class that is intended to be accessed only by the class
#itself and its subclasses.in python the convention for indicating that a member is 
#protected is to prefix its name with a single underscore(_).
class student:
    def __init__(self,name):
        self._name=name     #protected variable
    def _myfunc(self):      #protected method
        return "shaikh"
class subject(student):     #inherited class
    pass

a=student("sarfaraj")
b=subject("sarfaraj")
print(b._myfunc())
print(b._name)
print(a._name)
print("_________________________________________________________________________________")

#c]PRIVATE ACCESS SPECIFIERS:private members of a class(variables or methods) are those 
#members which are only accessible inside the class.we cannot use private  members outside 
#of class.
#in python,there is no strict concept of 'private' access modifiers like in some other 
#programmng languages.however, a convention has been established to indicate that a variable 
#or method should be considered private by prefixing its name with a double underscore(__).
class Student:
    def __init__(self):
        self.__name="shahid"
a=Student()
#print(a.__name)        #cannot be access directly
print(a._Student__name) #can be accessed indirectly