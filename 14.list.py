#LIST
#ordered collection of data items. they store multiple items in single variable.list items are separated by commas and enclosed within square brackets.
#list are changeble meaning we can alter them after creation.
#index-[0] [1] [2] [3]  [4] [5]
marks=[ 6  ,9  ,6  ,7  ,10  ,3]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])
print(marks[-3])    #negative index
print(marks[len(marks)-3])
print(marks[6-3])
print(marks[3])
#to check element present in list
if 7 in marks:
    print("present")
else:
    print("not present")
#printing range values:
print(marks[1:])
print(marks[2:-2])
print(marks[3:4])
print(marks[::2])   #jump index

#LIST COMPREHENSION:
#is used to creating new list from other iterable like list,tuple,dictionary,sets and even array and string
list=[i*i for i in range(11)]
print(list)
# we can also add condition in list:
lst=[i*i for i in range(11) if i%2==0]
print(lst)