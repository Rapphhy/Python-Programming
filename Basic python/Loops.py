z = 8
for i in range(1,11,2):
    print(str(z) + " * " + str(i) + " = " + str(z*i) )



list = [12,14,18,20,22]
z = 0
for i in list:
    z= z+i
    print(i)
print("sum is " + str(z))

number = input("Please enter the number : - ")
i = 1
while(i<=10):
    print(int(number)*i)
    i=i+1

number = input("Please enter your number : -")
for i in range(1,11):
    if(int(number)*1 == 60):
        break
    print(int(number)*i)

number = input("Please enter your number : -")
for i in range(1,11):
    if(int(number)*i%10 == 0):
        continue
    print(int(number)*i)