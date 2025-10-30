#USER INPUT
#we can take user input directly by using input() function
#this input function gives a return value as string/character hence we have to pass that into a variable. ex variable=input()

name=input("enter name: ")
print("name is: ",name)

#but input function return value as string.hence we have to typecast them whenever required to another datatype. ex variable=int(input())

first=int(input("enter the first num: "))
second=int(input("enter the second num: "))

print("adddtion of two num is ",first+second)