import re

text='''Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
        when an unknown printer took a galley of type and scrambled it to make a type
        specimen book. It has survived not only five centuries, but also the leap into 
        electronic typesetting, remaining essentially unchanged. It was popularised in 
        the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
        and more recently with desktop publishing software like Aldus PageMaker including
        versions of Lorem Ipsum'''

# pattern="was"
# match=re.search(pattern,text)
# print(match)

pattern=r"[A-Z]+orem"
matches=re.finditer(pattern,text)
for match in matches:
    print(match)
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])
print("________________________________________")
for match in matches:
    print(text[match.span()[0]:match.span()[1]])


