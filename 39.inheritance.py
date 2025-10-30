#INHERISTANCE:when a class derives from another class.the child class inherit the all the 
#public and protected properties and methods from the parent class.in addition, it can 
#have its own properties and methods,this is called inheritance.
class employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def showDetails(self):
        print(f"the name of employee:{self.id} is {self.name}")
class programmer(employee):
    def code(self,lang):
        print(f"the programmmer {self.id} is {self.name} coding with {lang}")

e=employee(420,"Aatmaram Bhide")
e.showDetails()

p=programmer(410,"sarfaraj shaikh")
p.showDetails()
p.code("java")
print("_________________________________________________________________________________")

#TYPES OF INHERITANCE:
    #1>single inheritance
    #2>miltiple inheritance
    #3>multilevel inheritance
    #4>hierarchical inheritance
    #5>hybrid inheritance
#1>SINGLE INHERITANCE:is a type of inheritance where a class inherits properties and 
#behaviours from a single parent class.

#2>MULTIPLE INHERITANCE:is a powerful feature in object-oriented programming that allows a 
#class to inherits attributes and methods from multiple parent classes.this can be useful 
#in situations where a class needs to inherits functionality from multiple sources.
class employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"the name of employee is{self.name}")

class dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"the name of employee is{self.dance}")

class DancerEmployee(employee,dancer):
    def __init__(self,name,dance):
        self.name=name
        self.dance=dance  

person=DancerEmployee("harshad","kathak")
print(person.name)
print(person.dance)
person.show()
print("_________________________________________________________________________________")

#3>MULTILEVEL INHERITANCE:is a type of inheritance in object-oriented programming where a 
#derived class inherits from another derived class.this type of inheritance allows you to
# build a hierarchy of classes where one class build upon another,leading to more 
#specialized classes.
class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def show_details(self):
        print(f"name   :{self.name}")
        print(f"species:{self.species}")
class dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self,name,species="Dog")
        self.name=name
        self.breed=breed
    def show_details(self):
        animal.show_details(self)
        print(f"breed  :{self.breed}")
class Goldenretriever(dog):
    def __init__(self, name, color):
        dog.__init__(self,name,breed="Golden Retriever")
        self.color=color
    def show_details(self):
        dog.show_details(self)
        print(f"color  :{self.color}")
o=Goldenretriever("tommy","white")
o.show_details()
print("_________________________________________________________________________________")

#4>HIERARCHICAL INHERITANCE:is a type of inheritance in object-oriented programming where
#multiple subclasses inherits from a single base class.in other words, a single base class 
#acts as a parent class for multiple subclasses.
# Parent class
class Animal:
    def speak(self):
        print("This animal makes a sound")
class Dog(Animal):
    def bark(self):
        print("Dog says: Woof!")
class Cat(Animal):
    def meow(self):
        print("Cat says: Meow!")
d = Dog()
c = Cat()
d.speak()
d.bark()
c.speak()
c.meow()
print("_________________________________________________________________________________")

#5>HYBRID INHERITANCE:is a combination of multiple inheritance and single inheritance in 
#object-oriented programming.hybrid inheritance can be implemented by creating a class 
#hierarchy,in which a base class is inherited by multiple derived classes and one of the 
#derived classes is further inherited by a sub-derived class.

# Base class
class Person:
    def display(self):
        print("I am a person")

# Derived class 1 (inherits from Person)
class Student(Person):
    def study(self):
        print("I am studying")

# Derived class 2 (inherits from Person)
class Teacher(Person):
    def teach(self):
        print("I am teaching")

# Derived class 3 (inherits from Student and Teacher - multiple inheritance)
class TeachingAssistant(Student, Teacher):
    def assist(self):
        print("I assist both teaching and learning")
ta = TeachingAssistant()
ta.display()
ta.study()
ta.teach()
ta.assist()
