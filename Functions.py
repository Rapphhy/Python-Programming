def family(name):
    print(name+ " Oladapo")
family('Rofiat')
family('lekan')

def name(*kids):
    print("The last child is " + kids[2])
name("bolu", "ayo", "tosin")

def add(a,b):
    c=a+b
    print("Sum of values " + str(c))
add(50,100)

def funct(food):
    for x in food:
        print (x)
fruits = ['apple','mango','orange']
funct(fruits)

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)




ADD MORE LINESADD MORE LINESADD MORE LINESADD MORE LINESADD MORE LINES!ADD MORE LINES!ADD MORE LINES!ADD MORE LINES!ADD MORE LINES!ADD MORE LINES!ADD MORE LINES!ADD MORE LINES!ADD MORE LINES!ADD MORE LINES!ADD MORE LINES!