#SUPER() KEYWORD:the super() keyword in python is used to refer to the parent class.it is
#specially useful when a class inherits from multiple parent classes and you want to call
#a method from one of the parent classes.

#ex.1:
class parentclass():
    def parentmethod(self):
        print("this is a parent method1")
class childclass(parentclass):
    def parentmethod(self):
        print("this is a parent method2") 
    def childmethod(self):
        print("this is a child method")
        super().parentmethod()
p=parentclass()
p.parentmethod()

c=childclass()
c.childmethod()
c.parentmethod()
print("_________________________________________________________________________________")

#ex.2:
class employee:
    def __init__(self,id, name):
        self.id=id
        self.name=name
class programmer(employee):
    def __init__(self ,id , name,lang):
        super().__init__(id, name)
        self.lang=lang
mandhar=employee(111,"mandhar")
pratik=programmer(123,"pratik","java")
print(mandhar.id,mandhar.name)
print(pratik.id,pratik.name,pratik.lang)
        
        
