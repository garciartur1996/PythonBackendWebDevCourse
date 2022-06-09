from audioop import tomono


print('Hello world noch einmal, my age is', 26) 
print("Welcome again")

'''
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

## Getting users input

name_user = input('Input your Name: ')
age_user = int(input('Input your age: '))
print("Your name is:",name_user, "and your age is:",age_user)

## Python exercise for word replacement

sentence_user = input("Enter your sentence: ")
print("Your sentence is:", sentence_user)
word_to_replace = input("Enter the word of the sentence that you want to replace: ")
word_to_replace_with = input("Enter the word to replace it with: ")
print(sentence_user.replace(word_to_replace,word_to_replace_with))
'''

## Lists in python

list_countries = ['UK',2,'Nigeria','Australia','Mexico']
print(list_countries)
#print(list_countries[1])
#print(list_countries[1][0])
print(list_countries[2:])
print(list_countries[1:4])
print(type(list_countries))
print(type(list_countries[1]))
name = 'tom'
print(type(name))
list_countries[0] = True
print(list_countries)
print(list_countries[-1])
print(list_countries[-2])
print(len(list_countries))
#print(len(list_countries[0]))
print(type(list_countries[0]))

countries = list(('UK',2,'Nigeria','Australia','Mexico')) ##List constructor, another way to declare a list using "list(())"
print(countries)
print(type(countries))

