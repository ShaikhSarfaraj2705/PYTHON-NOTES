#SET:
#Set are unorderd collection of  data items.they are store multiple items in single variale.set items are separated by commas and enclosed within curly brackets{}.
#set are unchangeble, meanning you can not change items of the set once created.set don notcontain dublicate value.
n={67,43,45,66,36,35,14}
print(n) 
demo={"sarfaraj",22,8.8,'m',False}
print(demo)

show=set()  #to declare an empty set , we can not use curly bracket{} it show <class 'dict'>
print(type(show))

for items in demo:  #accessing items using for loop
    print(items)

#SET METHODS:
s1={6,9,2,0,1,5}
s2={3,4,7,7,8,0,6}
print(s1.union(s2)) #union-prints all items present in two sets
#s1.update(s2)
#print(s1)
n.add(75)   #add an element
n.remove(43)    #remove the element
n.pop(0) #removes the random value
print(n)
n.clear() #empties the set

print(s1.intersection(s2)) #intersection-prints only items that are similar to both the sets.