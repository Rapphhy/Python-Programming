#Single condition
data = input('Please enter your Number : -')
data = int(data)

if data % 2 == 0:
    print("This is an even number" + str(data))
else:
    print("This is an odd number")

#Multiple condition
data = input('Please enter your number : -')
data = int(data)

if data < 0:
    print("This is negative")
elif data == 0:
    print("This is zero")
elif data % 2 == 0:
    print("This is even number")
else:
    print("This is odd number")

#Nested condition
data = input("Please enter your number : -")
data = int(data)

if data < 0:
    print("This is negative")
else:
    if data % 2 == 0:
        print("This is even number")
    else:
        print("This is odd number")


data = input("Please enter your number : -")
data = int(data)

if data >= 0:
    if data % 2 == 0:
        print("This is even number")
    else:
        print("This is odd number")
else:
    print("This is negative number")

#Logical OR and AND
marks = input("Please enter a mark")
marks = int(marks)

if marks > 100 or marks < 0:
    print("Invalid mark")
else:
    print("Valid mark")


num = input("Please enter your number : -")
num = int(num)

if ((num >= 0) and (num % 2 == 0)):
    print("This is positive")
elif((num >= 0) and (num % 2 )):
    print("This is negative")


