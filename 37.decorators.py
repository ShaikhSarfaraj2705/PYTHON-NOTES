#DECORATORS:python decorators are a powerful and versatile tool that allow you to modify 
#the behavior of functions and methods.
#A decorators is a function that takes another function as an argument and return a new 
#function that modifies the behavior of the original function
def greet(my_func):
    def new_func():
        print("Good morning")
        my_func()
        print("Thank you")
    return new_func

@greet
def my_func():
    print("hello world")

my_func()
#OR
greet(my_func)()