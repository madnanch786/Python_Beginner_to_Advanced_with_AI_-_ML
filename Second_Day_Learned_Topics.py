'''
Today we learned about:
1. Variables
2. Execution Sequence
3. Variable Types
4. User Input
5. Type Conversions
6. Expressions
7. Statements
8. Round Off
'''

# Variables are used to allocate memory to store values.
# A value may be of type: String, Integer, Float, Boolean, None, or other advanced types.

a = 5
b = 10
sum = a + b
print("Sum:", sum)

# Identify variable types
a = 55
b = 88.6
c = "Usman"
d = True
e = None

print("Variable a type is:", type(a))
print("Variable b type is:", type(b))
print("Variable c type is:", type(c))
print("Variable d type is:", type(d))
print("Variable e type is:", type(e))

# Take input from user and perform type conversion
no1 = input("Enter Number 1: ")
no2 = input("Enter Number 2: ")

# Convert string input to integers
cno1 = int(no1)
cno2 = int(no2)

sum = cno1 + cno2

# Use f-string for better formatting
print(f"The Sum of {cno1} and {cno2} is: {sum}")

# Round off example
value = 3.14159
print("Rounded value (2 decimal places):", round(value, 2))
