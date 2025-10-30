#LIST_METHODS
#lists
list=[1,2,4,7,0,7,3,2,54,2]
print(list)         #display a result
print("_________________________________________________")       

            #LIST SLICING
print(list[3])      #display a  particular value
#list slicing:
print(list[1:3])    #to print range values
print(list[:3])     #it start from beginnig value and end with specified idx range
print(list[2:])     #it start  from  specified idx and show all remainnig  value
print(list[-3:-1])  #it  start from  end and show a range value from ending
print("_________________________________________________")    
#list methods does not support to print statement when we write list methods inside the  print function it 
#shows none value *ex.print(list.append(22))   *output:none

list.append(9)      #add element at end of the  list
list.sort()         #sort list in ascending order
list.sort(reverse=True)#sort index in descending order
list.reverse()      #it reverse the list
list.insert(2,11)   #to add  elment in paricular idx number
list.remove(7)      #removes the first occurance of value
list.pop(4)         #use to remove element by intering  idx number

print(list)
print("_________________________________________________")       
a=list.index(3)
b=list.count(7)
print(a)
print(b)