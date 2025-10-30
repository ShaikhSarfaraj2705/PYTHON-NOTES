#EXCEPTION HANDLING
#exception handling is the process of responding to unwanted and unexpected events when a computer program runs.
#exception handling deals with these events to avoid the program or system crashing,
#and without this process, exceptions would discrupt the normal operations of the program.
a=input("Enter the number:")
print(f"multiplication of table {a} is ")
try:
    for i in range(1,11):
        print(f"{a} x {i} = {int(a)*i}")
except Exception as e:
    print(e)
print("some line of code")
print("end of the program")
print("_________________________________________________________________________________")

#user defined exception
a=input("Enter the number:")
print(f"multiplication of table {a} is ")
try:
    for i in range(1,11):
        print(f"{a} x {i} = {int(a)*i}")
except:
    print("INVALID INPUT!!!")
print("some line of code")
print("end of the program")
print("_________________________________________________________________________________")

#specific Exception handling
try:
    num=int(input("enter an integer: "))
    a=[6,4]
    print(a[num])
except ValueError:
    print(ValueError)
except IndexError:
    print(IndexError)