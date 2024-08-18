# replit

ctrl+enter = run programme // vs code = ctrl+alt+n
ctrl+shift+k = delete the line
alt+up/down arrow = move the line
alt+shift+up/down arrow = copy the line up down
alt+ctrl+b = right side view

<!--This is python comment-->

_P_~~y~~`tho`**n**

a = input()
b = input()
print(int(a)+int(b))

```py
details = ''' Type
Anythig inside
this any programme print
the same typing like input()
print()
etc'''
```

```py
# loop
paragraph = '''ali banat
Hi, how are you?
he said, 'i am fine' '''
for character in paragraph:
    print(character)
```

### change the value not the main

```py
str1 = "ali Haider!"
print(str1.upper())
print(str1.lower())
print(str1.rstrip(!))
print(str1.isupper())
print(str1.istitle())
print(str1.isalnum())
print(str1.isalpha())
```

### if else

```py
a = int(input("Enter age: "))
print("Age is: ",a)

if(a>18):
    print("You can Drive.")
else:
    print("You can not Drive")
```

### elif

```py
num = int(input("Enter a number : "))
if (num < 0):
  print("Number is negetive")
elif (num > 0):
  if (num <= 10):
    print("Number is 1 - 10")
  elif (num > 10 and num <= 20):
    print("Number is 10 - 20")
  else:
    print("Number is greater than 20")
else:
  print("Number is Zero")
print("I am happy")
```

### Time

```py
import time

myTime = time.strftime('%H:%M:%S')
print(myTime)
myHours = time.strftime('%H')
print(myHours)
myMinutes = time.strftime('%M')
print(myMinutes)
mySeconds = time.strftime('%S')
print(mySeconds)
```

### match case

```py

a = int(input("Enter Number: "))
match a:
  case 0:
    print("It's Zero")
  case 4:
    print("It's Four")
  case _ if a<0:
    print(a ,"is negetive")
  case _ if a!=5:
    print(a ," is more than 5")
  case _:
    print(a ,"is numbers")

```

### for loop

```py
text = "Hamza Ali"
for i = in text:
  print(i)
```

### inside for loop

```py
text = "Hamza Khan"
for i in text:
  if(i==a):
    print("alrounder") # inside if
    print(i) # inside if
  print(i) # outside of if
```

### for loop range

```py
for i in range(5):
  print(i) # it will print 0,1,2,3,4
```

```py
for i in range (1, 10):
  print(i) # it will print 1 to 9
```

```py
for i in range(1, 11, 2):
  print(i) # 1,3,5,7,9
```

### while loop

```py
i = 0
while(i<=5):
  print(i)
  i = i + 1
```

```py
i = 0
while(i<=5):
  i = int(input("Enter number: ")) # if the number is more than 5 programme will end
  print(i)
```

### while loop else

```py
i = 5
while(i>0):
  print(i)
  i = i - 1
else:
  print("You have enterd else")
```

### sum

```py
num1 = 20
num2 = 30
print(f"{num1}+{num2}= {num1+num2}")
# print(num1,"+",num2,"=",num1+num2)
print(type(num1))
```

<!--series-->

```py
n = int(input("Enter the last number: "))
sum = 0
for x in range(0,n+1,4):
    sum = sum + x
    print(f"x= {x} sum={sum}")
```

<!-- square -->

```py
n = int(input("Enter the last number: "))
sum = 0
for x in range(1,n+1,1):
    sum = sum + x * x
    print(f"x= {x} sum={sum}")
```

<!-- devide -->

```py
n = int(input("Enter the last number: "))
result = 0
for x in range(1,n+1,1):
    result = result + 1 / x
    print(f"x= {x} result={result}")
```

<!-- multiply -->

```py
n = int(input("Enter the last number: "))
res = 1
for x in range(1,n+1,1):
    res = res * x
    print(f"x= {x} res={res}")
```

<!-- prime -->

```py
# prime number
n = int(input("Enter end number: "))
for i in range(1,n+1,1):
    count = 0
    for j in range(2,i,1):
        if i % j == 0:
            count = 1
            break
    if count == 0:
        print(i)
```

<!-- factorial -->

```py
n = int(input("Enter a number: "))
factorial = 1
for x in range(1,n+1,1):
    factorial = factorial*x
print(factorial)
```

### greatest common divisor and least common multiple

```py
# Greatest Common Divisor
n = int(input("Enter first number: "))
g = int(input("Enter second number: "))
if g > n:
    t = g
    g = n
    n = t
    num1 = n
    num2 = g
rem = None
while rem != 0:
    rem = n % g # 24)60(2
    n = g       #    48
    g = rem     #  n 12)24(2
                #       24
                #  g     0
print(f"greatest common divivsor = {n}")
# least common multiple

lcm = num1 * num2 / n
print(f"least common multiple = {int(lcm)}")
```

### pattern

```py
n = int(input("Enter the height: "))

for x in range(1,n+1,2):
    print(x*"*")
```

### same

```py
n = int(input("Enter the height: "))

for x in range(n+1):
    print((2*x-1)*"*")
```

### revarse pyramid

```py
n = int(input("Enter number: "))
for x in range(n+1):
    for y in range(n-x):
        print(" ",end="")
    for z in range(x):
        print("*",end="")
    print()
```

### similar

```py
n = int(input("Enter the height: "))

for x in range(n+1):
    print((n-x)*" ",x*"*")
```

### simple

```py
n = int(input("Enter the number: "))
for x in range(n+1):
    for y in range(x):
        print(y+1,end="")
    print()
```

### pyramid

```py
n = int(input("Enter the number: "))
for x in range(1,n+1,2):
    for z in range(int((n-x)/2)):
        print(" ",end="")
    for y in range(x):
        print(y+1,end="")
    print()n = int(input("Enter the number: "))
for x in range(1,n+1,2):
    for z in range(int((n-x)/2)):
        print(" ",end="")
    for y in range(x):
        print(y+1,end="")
    print()

```

### guessing game

```py
from random import randint
for i in range(5):
    guessNumber = int(input("Enter a number between 1 to 5: "))
    randomNumber = randint(1,5)
    if randomNumber == guessNumber:
        print("You won")
    else:
        print(f"You Lost, random number was {randomNumber}")
```

### string to single number

```py
n = input("Enter numbers: ")
list = n.split()
sum = 0
for i in list:
    sum = sum + int(i)
print(sum)
```

### count letter word and numbers

```py
numbersofWord = 0
numbersofLetter = 0
numbersofNumber = 0

text = input("Enter text here: ")

for x in text:
    x = x.lower()
    if x >='a' and x <='z':
        numbersofLetter = numbersofLetter + 1
    elif x >='1' and x <='9':
        numbersofNumber = numbersofNumber + 1
    elif x == " " or x == "." or x == ",":
        numbersofWord = numbersofWord + 1
print(f"numbers of word =  {numbersofWord}")
print(f"numbers of letter = {numbersofLetter}")
print(f"numbers of number = {numbersofNumber}")
```

### matrix

```py
matrix = [
    [1,2,3],
    [4,5,6]
]
for i in matrix:
    for j in i:
        print(j)
```

### Dictionaries

```py
studentid = {
    "1001": "Ali Banat",
    "1002": "Hamza Khan",
    "1003": "Abu Ubaida",
    1004: "Jafar Iqbal"
}
position = {
    1001.1: "student",
    "1002.2": "teacher",
    "1003.3": "guide"
}
print(studentid["1001"],":",position[1001.1])
print(studentid[1004])
print(studentid.get("1003"),":",position.get("1003.3"))
# print(studentid["1005"])
print(studentid.get("1005"))
print(studentid.get(1005,"not a valid key"))
print(studentid.get("1003","not a valid number"))
```

### tuples

```py
#tuples
students = (
    ("ali banat",37,3.21),
    "hamza khan",
    "abu ubaida"
)
# print(students[0],students[2])
# students[1] = "haniya sheikh" in tuples can't change the value
print(students[0][2])
print(students[1:]) # print 1 to end all
```

### set

```py
num = {1,2,3,4,4}
print(num)
num2 = set([1,2,3,4,4])

print(num2)
num2.add(7)
print(num2)
num2.remove(1)
print(num2)
# nu = [ 1, 2, 3,3]
# print(nu)
print(7 in num2)
print(8 in num)
num.add(9)
print(num)
print(10 not in num2)
print(7 not in num2)
print(num | num2)
print(num & num2)
print(num - num2)
```

### stack (last in first out)

```py
books = []
books.append("Learn C")
books.append("Learn C++")
books.append("Learn Java")
print(books)
books.pop()
print(books)
print("now the top book is : ",books[-1])
books.pop()
print("now the top book is : ",books[-1])
books.pop()
if not books:
    print("No books left")
```

### Queue (first in first out)

```py
from collections import deque
que = deque(["ali banat","ruhit sanet", "abu ubaida"])
print(que)
que.popleft()
print(que)
que.popleft()
print(que)
que.popleft()
print(que)

if not que:
    print("no person left")
```

### function

```py
def add(a, b):
    sum = a + b
    sub = a - b
    print(sum)
    print(sub)

add(2,3)
add(5,6)

def addition(x,y,z):
    sum = x+y+z
    print(sum)

addition(1,2,3)
def message():
    print("this is blank message")

message()
```

### function with return

```py
def add(a, b):
    sum = a+b
    return sum
result = add(10,30)
print("Result = ",result)

def large(a,b):
    if a>b:
        return a
    else:
        return b

# result = large(1,2)
# print(result)
# print(large(10,2))
maximum = large
print(maximum(10,2))
```

### xargs

```py
# xargs
def data(id,name,age):
    print(id,name,age)

data(101,"ali banat",22)
data(102,"karim hossain",25)


def data1(*details):
    print(details[0])

data1(101,"ali banat",22)
data1(102,"karim hossain",25)

def add(*numbers):
    sum = 0
    for x in numbers:
        sum = sum + x

    print(sum)

add(10,20,30,40,80)
```

### xxargs

```py
# xxargs

def student(**details):
    print(details)
    print(details["name"])
    print(details["id"])

student(id=101,name= "ali banat")
student(id=102,name="hazi")
```

### lambda function

```py
# function
def calculate(a, b):
    return a*a + 2*a*b + b*b
print(calculate(5, 3))
# lambda function
print((lambda a,b : a*a + 2*a*b + b*b)(5, 3))

math = (lambda x,y : x + y)(2,3)
print(math)

sub = (lambda i,z : i-z)(3,2)
print(sub)

que = (lambda q : q*q*q)(3)
print(que)
```

### map & filter

```py
# map
def square(x):
    return x*x

num = [1,2,4,5]

result = list(map(square,num))
print(result)

# filter
result = list(filter(lambda x : x%2 ==0, num))
print(result)
```

### comprihensions list

```py
num = [1,2,3,4,5]
result = list(map(lambda x : x*x,num))
print(result)
result = [x*x for x in num]
print(result)

result = list(filter(lambda x : x%2==0,num))
print(result)
# similar

result = [x for x in num if x%2==0]
print(result)
```

### adjust two list in one (zip)

```py
name = ["ali banat","hamza khan","abu ubaida","tashrif hossain","abu kaisar"]
id = [101,102,103,104,105]

print(list(zip(name,id,"ABCDF")))
```

### factorial inside factorial (Recursion)

```py
def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))
```

### file

```py
# with open("file.txt","r") as f:
#     print(f.readable())
# f.close()

# g = open("file.txt","r")
# print(g.readable())
# g.close()
# g = open("file.txt","r+")
# file = g.read()
# print(file)
# size = len(file)
# print(size)
# g.close()
# g = open("file.txt","r+")
# print(g.writable())
# g.close()

files = open("file.txt","r+")
# file = files.readlines()
# file = files.readlines()[0]
# print(file)
for line in files:
    print(line)
files.close()
```

### file write

```py
# w to overrite
# r to read
# a to append
# r+ to read & write
file = open("hello.html","w") # create new file, just new name in files.txt and edit to edited file name
# file.readable()
# file.read()

print(file.write("<h1>Bangladesh</h1>"))
file.close()
```

### exception handling

```py
try:
    list = [10,0,20]
    result = list[0]/list[3]
    print(result)
    print("done")
except ZeroDivisionError:
    print("Dividing by zero is not possible.")
# except IndexError:
#     print("Index Error")
finally:
    print("successful")
```

### similar two in one

```py
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1/num2
    print(result)
except (ZeroDivisionError,ValueError):
    print("you have entered incorrect value.")
finally:
    print("thanks")
```

### exception handling function

```py
def voter(age):
    if age < 18:
        raise ValueError("Invalid Voter")
    return "You are allowd to vote"
try:
    print(voter(19))
    print(voter(18))
    print(voter(17))
except ValueError as a:
    print(a)
```

### class and object

```py
class student:
    roll = ""
    gpa = ""

rahim = student()
print(isinstance(rahim,student))

rahim.roll = 101
rahim.gpa = 3.21
print(f"Rahim,Roll : {rahim.roll},GPA : {rahim.gpa}")

karim = student()
karim.roll = 102
karim.gpa = 2.72
print(f"Karim,Roll : {karim.roll}, GPA : {karim.gpa}")
```

### class and object with methods function

```py
class student:
    roll = ""
    gpa = ""

    def self_value(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"roll = {self.roll}, gpa = {self.gpa}")

karim = student()
karim.self_value(1,3.21)
karim.display()

rahim = student()
rahim.self_value(2,2.72)
rahim.display()
```

### constructor

```py
class Student:
    name = ""
    roll = ""
    gpa = ""

    def __init__(self,name,roll,gpa):
        self.name = name
        self.roll = roll
        self.gpa = gpa

    def Display(self):
        print(f"name = {self.name},roll = {self.roll},gpa = {self.gpa}")

alibanat = Student("ali banat",1,2.67)
alibanat.Display()

hamzakhan = Student("hamza khan",2,3.21)
hamzakhan.Display()
```

### triangle

```py
class Triangle:
    base = ""
    height = ""

    def __init__(self,base,height):
        self.base = base
        self.height = height

    def Calculate(self):
        print(f"Triangle = {0.5*self.base*self.height}")

t1 = Triangle(10,20)
t1.Calculate()

t2 = Triangle(20,30)
t2.Calculate()
```

### inheritance

```py
class phone:
    def call(s):
        print("You can call")
    def message(s):
        print("You can message")

class samsung(phone):
    # def call(self):
    #     print("You can call")
    # def message(self):
    #     print("You can message")
    def photo(s):
        print("You can take a photo")
# p = phone()
# p.call()
# p.message()
# *****
# s = samsung()
# s.call()
# s.message()
# s.photo()
# *****
s = samsung()
s.call()
s.message()
s.photo()
print(issubclass(samsung,phone))
class phone:
    def call(s):
        print("You can call")
    def message(s):
        print("You can message")

class samsung(phone):
    # def call(self):
    #     print("You can call")
    # def message(self):
    #     print("You can message")
    def photo(s):
        print("You can take a photo")
# p = phone()
# p.call()
# p.message()
# *****
# s = samsung()
# s.call()
# s.message()
# s.photo()
# *****
s = samsung()
s.call()
s.message()
s.photo()
print(issubclass(samsung,phone))
```

### method overriding

```py
# class phone:
#     def __init__(self):
#         print("i am in phone class")

# class samsung(phone):
#     pass

# s = samsung()
# ************************
# class phone:
#     def __init__(self):
#         print("i am in phone class")

# class samsung(phone):
#     # init overrite
#     def __init__(self):
#         print("i am inside samsung")

# s = samsung()
#***************************************
class phone:
    def __init__(self):
        print("i am in phone class")

class samsung(phone):
    # init overrite
    def __init__(self):
        super().__init__() # if i want phone class msg too
        print("i am inside samsung")

s = samsung()
```

### Types of inheritance

```py
class shape:
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("I am area method of shape class")
class triangle(shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of triangle = ",area)
class rectangle(shape):
    def area(self):
        area = self.dim1 * self.dim2

        print("Area of rectangle: ",area)

t = triangle(20,30)
t.area()
r = rectangle(20,30)
r.area()
```

###

```py
# class A:
#     def display1(self):
#         print("I am inside A class")

# class B(A):
#     def display2(self):
#         print("I am inside B class")

# class C(B):
#     def display3(self):
#         print("I am inside C class")

# result = C()
# result.display1()
# result.display2()
# result.display3()
# ***********************************************************
# class A:
#     def display1(self):
#         print("I am inside A class")

# class B(A):
#     def display2(self):
#         print("I am inside B class")

# class C(B):
#     def display3(self):
#         super().display1()
#         super().display2()
#         print("I am inside C class")

# result = C()
# # result.display1()
# # result.display2()
# result.display3()

# ********************************************
class A:
    def display(s):
        print("I am inside A class")

class B:
    def display(s):
        print("I am inside B class")

class C(B,A):
        pass

result = C()
result.display()
```

#\*\*

```py
from abc import ABC,abstractmethod

class shape(ABC):
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area(self):
        pass
        # print("shape has no area")
class triangle(shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print(f"Area of Triangle is : {area}")

class rectangle(shape):
    def area(self):
        area = self.dim1 * self.dim2
        print(f"Area of rectangle is : {area}")

# s1 = shape(20,30)
# s1.area()

result = triangle(10,20)
result.area()

r2 = rectangle(10,20)
r2.area()
```

### polymorphic

```py
# polymorphic
print(len("ali banat"))
print(len([10,20,30]))


def add(x, y, z=0):
    return x+y+z

print(add(4,6))
print(add(4,6,10))
```

### magic mathod

```py
class Bike:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def __eq__(self,other):
        return self.name == other.name and self.color == other.color

    def __str__(self):
        return f"name = {self.name}, color = {self.color}"

    def display(self):
        print(f"name = {self.name}, color = {self.color}")

Bike1 = Bike("Yamaha","Blue")
Bike2 = Bike("Yamaha","Blue")
print(Bike1==Bike2)






# class Bike:
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
#     def __str__(self):
#         return f"name = {self.name}, color = {self.color}"

#     def display(self):
#         print(f"name = {self.name}, color = {self.color}")

# Bike1 = Bike("Yamaha","Blue")
# Bike2 = Bike("Apache","Silver")
# print(str(Bike1))
# print(str(Bike2))




# class Bike:
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color

#     def display(self):
#         print(f"name = {self.name}, color = {self.color}")

# Bike1 = Bike("Yamaha","Blue")
# # Bike1.display()
# print(Bike1)
# Bike2 = Bike("Apache","Silver")
# Bike2.display()
```

### module

```py
# from area import area_rectangle,area_triangle
from area import *
area_rectangle(5,10)
area_triangle(5,10)
# print(pow(2,3))
```

from area file

```py
def area_triangle(b,h):
    print(f"Area of triangle is : {0.5*b*h}")
def area_rectangle(a,b):
    print(f"Area of rectangle is : {a*b}")
```

### Regular Expression

```py

# match -> match if first word match
# search -> match from whole text
import re
pattern = r"olour"
print(re.findall(pattern,"Red is Colour, i love red colour"))
# import re
# pattern = r"Colour"
# if re.search(pattern,"Red is Colour, i love red colour"):
#     print("Match")
# else:
#     print("Not Match")
# import re
# pattern = r"Colour"
# if re.match(pattern,"Colour is Colour, i love red colour"):
#     print("Match")
# else:
#     print("Not Match")
```

### find text number start end span

```py
import re
pattern = r"colour"
text = "black is a colour, i like black colour"
match = re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())

```

### replace (sub)

```py
import re
pattern = r"colour"
text1 = "this is blue colour, i like this colour"
text2 = re.sub(pattern,"color",text1,count=1) # count 1 means replace 1 from starting. 2 replace 2
print(text2)
# import re
# pattern = r"colour"
# text1 = "this is blue colour, i like this colour"
# text2 = re.sub(pattern,"color",text1)
# print(text2)
```

### meta character

```py
import re
# pattern = r"a*" # a* means a can be 0 or more no issue
# pattern = r"a+" # a+ must be a use one or more
# pattern = r"a+b" # must be a after b
# pattern = r"a*c" # a 0 or mor but b is must
# pattern = r"ice(-)?creame" # ? means 0 or one use
pattern = r"a{1,3}$" # 1 to 3 a can be use not more or less
if re.match(pattern,"a"):
    print("match")




# import re
# # pattern = r"colour"
# # pattern = r"col..r" # use . instead one word two . for two words
# pattern = r"^colo.r$" # ^ must start colo and must end $ means(r)
# if re.match(pattern,"colour"):
#     print("match")
```

### character class

```py
import re

# pattern = r"[aeiou]" # any word match will be ok
# pattern = r"[A-Z]" # A to Z any one word found Ok
pattern = r"[A-Z][a-z][0-9]" # serial wise A-> a-> 0 = Aa0 ok
if re.search(pattern,"Al0"):
    print("matched")
```
