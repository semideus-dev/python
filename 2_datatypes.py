'''
This file covers the code for the second unit. Concepts covered are:
    - Variables
    - Comments
    - Datatypes
'''

'''
Variables (used to store data)
'''

name = "Semideus"
print(name) # Output -> Semideus

# Redeclaring
name = "Semideus.dev"
print(name) # OUTPUT -> Semideus.dev

# Snake case
is_human = True

# Camel case
isHuman = True

'''
Comments (code is not executed by the intepreter)
'''

# Single line comment
#print("hello world!")

# Multiline comment
"""
a = 10
print("hello world!")
"""


'''
Datatypes
'''

# str
ame = "Semideus"
full_name = 'Semideus.dev'
another_name = str("Demigod")

print(type(name)) # Output -> str

# int
age = 10
num = int("10")

print(type(age)) # Output -> int
print(type(num)) # Output -> int

# float
height = 175.3
weight = float(63.5)

print(type(height)) # Output -> float
print(type(weight)) # Output -> float

# complex
comp = 8 + 4j
another_comp = complex(43 + 11j)

print(type(comp)) # Output -> complex
print(type(another_comp)) # Output -> complex

#  bool
likes_cricket = True

print(type(likes_cricket)) # Output -> True

# list
sports = ["F1", "Cricket", "Football"]

print(sports)
print(type(sports)) # Output -> list

# tuple
fruits = ("apple", "banana", "mango")

print(fruits)
print(type(fruits)) # Output -> tuple

# dict
person = {
	"name": "Semideus.dev",
	"age": 18,
}

print(person)
print(type(person)) # Output -> dict

# set
names = {"Semideus", "Odin", "Loki"}

print(names)
print(type(names)) # Output -> set