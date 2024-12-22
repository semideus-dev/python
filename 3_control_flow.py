'''
This file contains the code for the third unit. Concepts covered are:
    - Conditional statements
    - Operators
'''

'''
Conditional statements (choice for the control flow based on a condition)
'''

# If statement
age = 14
if age < 18:
	print("You cannot own a driving license")
	
# Else statement
if age < 18:
	print("You cannot own a driving license")
else:
	print("You can own a driving license")

# Elif statement
marks = 85

if marks >= 90:
    print("A+")
elif marks >= 75:
    print("A")
elif marks >= 50:
	print("B")
else:
	print("F")

# Nested if-else statement
marks = 85

if marks >= 50:  
    if marks >= 90: 
        print("A+")
    elif marks >= 75:  
        print("A")
    else:  
        print("B")
else:
    print("F")

'''
Operators (perform operations on values)
'''

# Arithmetic operators
a = 22
b = 12

print(a+b)  # Addition
print(a-b)  # Subtraction
print(a*b)  # Multiplication
print(a/b)  # Division (float)
print(a//b) # Division (floor)
print(a%b)  # Modulus
print(a**b) # Power


# Comparison operators

print(a>b)  # Greater than
print(a<b)  # Less than
print(a==b) # Equal to
print(a!=b) # Not equal to
print(a>=b) # Greater than or equal to
print(a<=b) # Less than or equal to


# Logical operators
has_id = True

# AND: Both conditions must be True
if age >= 21 and has_id:
    print("Eligible to enter the club.")

# OR: At least one condition must be True
if age < 18 or age > 60:
    print("Eligible for a discount.")

# NOT: Reverses the condition
if not has_id:
    print("ID is required.")
    
    
# Assignment operators
a += b
print(a) # Output -> 22 + 12 = 34


# Identity operators
c = 22
d = a

print(a is not b) # True
print(a is c)     # True
print(a is d)     # True


# Membership operators
nums = [10, 12, 14, 16, 18]

print(a not in nums) # True
print(b in nums)     # True