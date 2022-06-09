print('Hello world noch einmal, my age is', 26) 
print("Welcome again")

## Strings

name = "TIM"
age = 18

print(name, "is my name and my age is", age)
print(name + " is my name")

print("Hi. \n How are you", name,"?") #\n to pass space

print("First letter of", name, "is",name[0])

print(name.upper())
print(name.lower())
print(name.isupper())

print(len(name))

print(name.index('I'))
print(name.replace('M','C'))


## Numbers

print(78)
number = 79
print(number)
print(78+22)
print(78+22.934)
print(78-22.934)
print(78/22.934)
print(78*22.934)
print(20%6) ## To get the reminder of a division

number = 55
number2 = str(number)
print(number2)
print("number is "+number2)

print(-5)
print(abs(-5)) ## Absolute value function
print(max(4,2,3)) ## Maximum value
print(min(2,3,5,6))
print(bin(3))
print(bin(334))

from math import *

print(sqrt(100))