#Modules to retrieve data from another source

import Modules
a = Modules.person1["age"]
print(a)

import Modules
Modules.greeting("Jonathan")

import Modules as mx
a = mx.person1["age"]
print(a)


#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#"x" - Create - Creates the specified file, returns an error if the file exists
#"t" - Text - Default value. Text mode
#"b" - Binary - Binary mode (e.g. images)

#Reading the whole file
f = open("Functions.py","r")
print(f.read())

f = open("Functions.py", "r")
for x in f:
    print(x)

# If the file is located in a different location, we have to specify the file path.
# We use readline to return the first line of the file

f = open("Functions.py", "r")
print(f.readline())
f.close()

## write and read using a or w

f= open("Functions.py", "a")
f.write("ADD MORE LINES!")
f.close()
f= open("Functions.py", "r")
print(f.read())

#Create a file

f= open("file.py", "x")
# f= open("file.py", "w")

#Delete the file we created
import os
os.remove("file.py")

import os
if os.path.exists("file.py"):
    os.remove("file.py")
else:
    print("File does not exist")



