class person:           #create a class using class keyword
    name="sarfaraj"     #attributes or properties
    age=23
    city="karad"
    def info(self):         #methods
        print(f"{self.name} is {self.age} old and he is from {self.city}")
#SELF KEYWORD/PARAMETER:the self parameter is referance to the current instance of a 
#class, and is used to access variables that belongs to the class.
    
a=person()              #creating object of class
a.name="shubham"
a.age=50                #assigning new value to vairables using object
a.city="kasegaon"

b=person()              #creating new object of class
b.name="sahil"
b.age=25
b.city="pune"

a.info()
b.info()                #calling methods using objects


