#dir():the dir() function returns a list of all the attributes and methods(including 
#dunder methods) available for an object.it is useful for  discovering what you can do 
#with an object.
x=[7,8,9]
print(dir(x))

#__dict__:the __dict__ attribute returns a dictionary representation of an object's 
#attribute.it is a useful tool for introspection.
class person:
    def __init__(self):
        self.name="ajinkya"
        self.age=70
p=person()
print(p.__dict__)

#help():the help() function is used to get help documentation for an object,including a 
#description of its attributes and methods.
print(help(x))
print(help(person))