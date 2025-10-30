#ENUMERATE FUNCTION:the enumerate function is built-in function in python that allows
#to loop over a sequence(such as list, tuple or string) and get the index and value of 
#each elements in the sequence at the same time.
marks=[76,12,66,74,97,32,1,2]
for index, mark in enumerate(marks):
    print(mark)
    if (index==3):
        break
print("_________________________________________________________________________________")

#by default enumerate function start the index at 0, but you can specify a different
#starting index by passing it as an argument to enumerate function
for index, mark in enumerate(marks,start=1):
    print(mark)
    if (index==3):
        break

