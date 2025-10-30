#STRING SLICING
str=" to show slicing in string"
print(str[0:7]) #it print character from index 0 to index 7-1(6)
print("_________________________________________________________________________________")

print(len(str)) # to show length of an string we use length function- len()
print("_________________________________________________________________________________")

print(str[3:8]) #print chatacter from index 3 to index 8-1(7)
print(str[:16]) # start print from starting (0th index) to index 16-1(15)
print(str[:-14])# print letter from start & end with removing last 14 letter
print(str[:len(str)-14])# as like upper case
print(str[-10:-1]) #start printing from  index-10 to -1
print("_________________________________________________________________________________")
#STRING METHODS
str1="Sa R fA rA j ^^^^^^^"
print(len(str1))    #to check the length of string
print(str1.upper()) #to print string in upper case letter
print(str1.lower()) #to print string in lower case letter
print(str1.rstrip("^")) #remove characters from right
print(str1.replace("Sa R fA rA j","ShA hI d"))  #to replace string with another string
print(str1.split(" "))  # it print character in array form
print("_________________________________________________________________________________")

str2="string METHODS are very simple"
print(str2.capitalize())    # capitalize first letter of string and rest of letter are convert into small letter
print(str2.count("e"))      #total occurence of letter in string
print(str2.endswith("e"))   #print boolean value true or false. true if specified character is end in string otherwise false
print(str2.find("are"))     #it find the first occurence of letter print the index of it
print(str2.index("are"))    #as like upper case

print(str2.islower())       #print true if all characters in string are in lower case otherwise false
print(str2.isupper())       #print true if all characters in string are in upper case otherwise false
