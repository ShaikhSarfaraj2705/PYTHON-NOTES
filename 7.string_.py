#STRING
#anything that you enclose between single or double quotation marks is considered a string.a string is essentially sequence or array of texual data.
string1="demo of string\n"
string2='using single quote'
print(string1,string2)
print("__________________________________________________________________________")

string3='we print "double quote" in single quote'
print(string3)
print("__________________________________________________________________________")


string4='''demonstrating
multi line 
string demo'''
print(string4)
print("__________________________________________________________________________")

#Accessing character of string
#string is like array of characters,we can access part of string by using its index which starts from 0
print(string1[0])
print(string1[1])
print(string1[2])
print(string1[3])
print(string1[4])
print(string1[5])
print("_________________________________________________________________________________")

#looping through the string
for character in string2:
    print(character)        #print all the characters in the string name one by one