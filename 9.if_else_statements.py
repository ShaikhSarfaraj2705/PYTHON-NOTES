age=int(input("enter your age: "))
print("your age is: ",age)

if age>18:
    print("you can vote")
elif age==0 or age<0:
    print(" Invalid age")
else:
    print("you can not vote")
print("voting system!!!")
print("_________________________________________________________________________________")

#ex nested if statements
if age<0:
    print("age is negative")
    print("Invalid age!")
elif age>0:
    if age<=18:
        print("age is between 1-18")
        print(" you can not vote")
    elif age>18 and age<60:
        print("please vote")
    else:
        print(" you are too old")
        print("but you can vote")
else:
    print("your age is 0")
    print("Invalid age!")
print("_________________________________________________________________________________")


#SHORT-HAND IF ELSE:there is also a shorthand syntax for the if-else statement that can
#be used when the condition being tested is simple and the code blocks to be executed are short.
a=56
b=45
print("A is greater") if a>b else print("A is equal to B") if a==b else print("B is greater")
#it is not suitable for more complex situations where you need to execute multiple statements
#or perform more complex logic