#MAGIC/DUNDER METHODS:these are a special methods that you can define  in your classes, 
#and when invoked,they give a powerful  way to manipulate  objects and there behavior.
#magic methods also known as 'dunders' from the double underscores surrounding there names,
#are powerful tools  that allow you to costomize behavior of your classes.

#__len__ method:the len method is used to get the length of an object.this is useful when
#you want to be able to find the size of datastructiure,such as  a list or dictionary.
class employee():
    name="arjit"
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    def __str__(self):
        return f"Employee is:{self.name}"
    def __repr__(self):
        return f"Employee is:{self.name}"
    def __call__(self):
        print("__call__ method is called")
e=employee()
print(len(e))

#__str__ and __repr__ method:the str and repr methods are both used to convert an object 
#to a string representation.the str method is used when you want to print out an object,
#while the repr method is used  when you want to get a string representation  of an object 
#that can be used to recreate the object.
print(str(e))
print(repr(e))

#__call__ method:the call method is used to make an  object callable,meaning that you can 
#pass it as a parameter to a  function and it will  be executed  when the function is called.
print(e())