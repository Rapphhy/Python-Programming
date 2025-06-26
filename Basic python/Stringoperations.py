data = "A big boy"
print(data[3])
print(data[2:5])
print(data[2:])
print(data[:5])
print(data[8])

#Upper and lower case
data = "This is learning"
print(len(data))
print(data.upper())
print(data.lower())
print(data.capitalize())

#replace data
data = " This is testing world "
print(data.replace("world", "python"))
print(data.replace("This","That").replace("world","life"))
print(len(data.replace(" ","")))
print(len(data))

#Finding string
print(data.find("testing"))
print(data.find("python"))

#Split data
result = data.split(" ")
print(len(result))
for data in result:
    print(data)

#Remove space from left,right and both sides
data = " This is testing world "
print(len(data.rstrip()))
print(len(data.lstrip()))
print(len(data.strip()))

#Case sensitive comparison
a= "Hello"
b= "hello"
if (a.lower() == b.lower()):
    print("This is case sensitive")
else:
    print("This is not sensitive")
