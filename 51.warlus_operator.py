#WARLUS OPERATOR:the warlus operator is a new addition to python 3.8 and  allow you to 
#assign a value to a variable within an expression.this can be useful when you need to use 
#a value multiple times in a loop,but don't want to repeat the calculation.the warlus 
#operator is represented by the := syntax and can be used in vaiety of contexts including 
#while loops and if statements.

#ex.1:
a=False
print(a)
print(a:=True)
print("_________________________________________________________________________________")

#ex.2:
numbers=[1,2,3,4,5]
while(n:=len(numbers))>0:
    print(numbers.pop())
print("_________________________________________________________________________________")

#ex.3
# foods=list()
# while True:
#     food=input("what food do you like?: ")
#     if food=="quit":
#         break
#     foods.append(food)

foods=list()
while(food:=input("what food do you like?: "))!="quit":
    foods.append(food)