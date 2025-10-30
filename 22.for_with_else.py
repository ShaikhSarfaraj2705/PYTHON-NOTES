#FOR LOOP WITH ELSE STATEMENT
#python allows the else keyword to be used with the for and while loop too.
#the else block apppear after the body of the loop
#the statement in else block will be executed after all the iterations are completed.
for i in range(10):
    print(i)
else:
    print("executed after for loop")

for el in range(10):
    print(el)
    if el==5:
        
        break
else:
    print("executed after for loop")
