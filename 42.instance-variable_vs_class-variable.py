#CLASS VARIABLES:are defined at the class level and are shared amoung all  instance of 
#class. they are defined any outside of method and are usuall used to store information 
#that is common to all instances of the class.

#INSTANCE VARIABLE:are defined at the instance level and are unique to each instance of the 
#class.they are defined inside the init method and are usually used to store information 
#that is specific to each instance of class.
class Employee:
    company_name="Google"   #class variable
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"the employee {self.name} is working in {self.company_name}")
e1=Employee("sumit")        #instance variable
e2=Employee("ajay")         #instance variable
e1.show()
e2.show()
#or
Employee.show(e2)