#DICTIONARY:
#Dictionary are ordered collection of data items.they store  multiple items in single variable.dictionary items are key-value pair that are separated by
#by commas and enclosed within curly brackets{}.
info={
    "name":"sarfaraj",
    "surname":"shaikh",
    "age":22,
    "cet":74.20,
    11.11:22.22,
}
print(info) #resulting all keys and values
print(info["name"]) #resulting a particular value
info["score"]=92.5  #adding new keys & values
info["gender"]="male"
print(info)
#ex.2:
data={
    "tup":("get","set","go"),
    "list":["wow","hmmm","ohhh"]
}
print(data)

#NEXTED DICTIONARY
stud={
    "name":"sarfaraj shaikh",
    "sub":{
        "maths":99.9,
        "phy":99.8,
        "chem":98.9
    }
}
print(stud)
print(stud["sub"])
print(stud["sub"]["chem"])

#DICTIONARY METHODS:
print(info.keys())  #returns all keys
print(info.values())    #returns all values
print(stud.items()) #returns all (key,val) paird as tuples

print(stud.get("name")) #returns the key acccording to value.
print(stud.get("name2"))    #if any key value does not exist then it will return None.
stud.update({"city":"karad"})   #insert the specified items to the dictionary
print(stud)