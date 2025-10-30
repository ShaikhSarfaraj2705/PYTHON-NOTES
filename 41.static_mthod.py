#STATIC METHOD:static methods in python are methods that belongs to a class rather than an 
#instance of class they are defined using @staticmethod decorator and do not have access 
#to the instance of class(ie.,self).they are called on the class itself, not on an 
#instance of class.
class math:
    @staticmethod
    def add(a,b):
        return a+b
result=math.add(56,32)
print(result)