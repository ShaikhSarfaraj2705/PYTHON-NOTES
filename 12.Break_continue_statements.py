#BREAK AND CONTINUE STATEMENT
#break -it enables a program to skip over a part of the code
for el in range(1,11):
    print("5 X ",el,"=",5*el)
    if el==5:
        print("break")
        break
print("__________________________________________________________")


#continue-it skips the rest of the loop statement and causes the next iteration to occur
for num in range(1,11):
    if num ==5:
        print("continue")
        continue
    print("5 X ",num,"=",5*num)
