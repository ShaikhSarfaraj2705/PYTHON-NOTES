#CLASS METHOD:a class method is a type of method that is bound to the class and not the 
#instance of class.in other worf=ds,it operates on the  class as a whole rather than on a 
#specific instance of the class.class method are defined using the '@classmethod' 
#decorator,followed by a function defintion.the first argument as the function is always 
#'cls',which represent the class itself.

class Employee:
    ename="rohit"
    company="Google"
    def show(self):
        print(f"employee name is {self.ename} and the company name is {self.company}")

    def change_name(self,new_ename):
        self.ename=new_ename

    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company
e1=Employee()
e1.show()
print("_________________________________________________________________________________")

e1.change_name("prithiraj")
e1.show()
print(Employee.ename)
print("_________________________________________________________________________________")

e1.change_company("tesla")
e1.show()
print(Employee.company)
