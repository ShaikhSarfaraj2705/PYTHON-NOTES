#LOOPS
# sometimes programmer wants to execute a group of statements a certian number of times,this can be done using loops.
#based on loops are further classified unto following main two types:(i)for loop (ii)while loop

#for loop- can iterate over a sequence of iterable object
name=input("enter your name: ")
for char in name:
    print(char)
print("__________________________________________________________")

#ex using list
fruits=["mango","apple","banana","grapes"]
for f in fruits:
    print(f)
    for l in f:
        print(l)
print("__________________________________________________________")


#range()-to iterate over a sequence
for num in range(1,11): #to print number from 1-10
     print(num)
print("__________________________________________________________")

for num in range(1,11,2):    #third parameter is used to iterate n number
    print(num)
print("_________________________________________________________________________________")

#while loop
#it execute a statements while condition is true
i=0
while i<11:
    print(i)
    i+=1
print("_________________________________________________________________________________")

i=int(input("enter number: "))
while True:
    if i==1:
        print(1)
        break
    elif i==2:
        print(2)
        break
    elif i==3:
        print(3)
        break
    else:
        print("exit")
        break