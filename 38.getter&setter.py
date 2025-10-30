class myclass:
    def __init__(self,value):
        self._value=value

#GETTERS:getters in python are methods that are used to access the values of an objects 
#properties.they are used to return the value of specific property and are typically 
#definged using the @property decorator.
    @property       #getter
    def val(self):        
        return  self._value
    
#SETTERS:it is important to note that the getters do not take any parameters and we cannot 
#set the value through the getter method.for that we need sttter method which can be added 
#by decorating method with @property_name.setter
    @val.setter   #setter
    def val(self,new_val):
        self._value=new_val

obj=myclass(10)     #accessing the getter
print(obj.val)

obj.value=50        #accessing the setter
print(obj.val)