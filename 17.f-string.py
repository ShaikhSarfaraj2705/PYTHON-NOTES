#F-STRING FORMATTING
#f-string offers a convenient waty to embed python expression inside string literals for formatting.
demo= "my name is {} and i'm from {}"
name="sarfaraj"
city="karad"
print(demo.format(name,city))   #old string formatting method
print(f"my name is {name} and i'm from {city}") #using f-string 
