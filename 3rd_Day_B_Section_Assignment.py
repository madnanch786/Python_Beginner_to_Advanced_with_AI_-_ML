# Section A
'''

**1. What are data types in Python? List any 4 with examples.**

Data types classify the type of value a variable can hold. Four common Python data types and examples:

- **int:** Represents integer values, e.g. `x = 5`
- **float:** Represents decimal numbers, e.g. `y = 3.14`
- **str:** Represents sequences of characters, e.g. `name = "Ali"`
- **bool:** Represents True/False values, e.g. `is_valid = True`

***

**2. What is the difference between implicit and explicit type conversion? Give one example of each.**

- **Implicit Type Conversion:**  
  Python automatically converts one data type to another when needed, without user intervention.  
  *Example:*  
  ```python
  x = 5      # int
  y = 2.0    # float
  result = x + y   # Python converts x to float; result is 7.0 (float)
  ```

- **Explicit Type Conversion:**  
  The user manually converts the data type using conversion functions.  
  *Example:*  
  ```python
  a = "10"
  b = int(a)   # Converts string to int, b is now 10 (int)
  ```

***

**3. What are operators in Python? Explain any three types with examples.**

Operators are special symbols or keywords that perform operations on operands (variables and values).

- **Arithmetic Operators:** Perform mathematical calculations.  
  Example: `+`, `-`, `*`, `/`  
  ```python
  sum = 2 + 3   # result is 5
  ```
  
- **Comparison Operators:** Compare values and return a Boolean result.  
  Example: `==`, `!=`, `<`, `>`  
  ```python
  is_equal = (4 == 4)   # result is True
  ```
  
- **Logical Operators:** Combine conditional statements.  
  Example: `and`, `or`, `not`  
  ```python
  result = (True and False)   # result is False
  ```

'''
# Section B
'''
1. Take input in celcius and prints its equilent in Fahrenheit and kelvin ( Use explicit type conversion and arithmetic operators.)
formula:
Fahrenheit= (Cx9/5)+32
Kelvin=C+273.5
'''
celcius=float(input("Enter tempratue in Celcius: "))
fahrenheit=(celcius*9/5)+32
kelvin=celcius+273.5
print("Fahrenheit=",fahrenheit)
print("Kelvin=",fahrenheit)
'''
2. Write a program that take total bill aount and number of freinds as input.
calculate how uch each person will pay
also print he data type of each variable used
'''
totalBill=float(input("Please Enter the Total Bill: "))
totalFriends=int(input("Please Enter the Total No of Friends: "))
perFriendBill=float(round(totalBill/totalFriends,2))
print(f"Total Friends:{totalFriends}\nTotal Bill:{totalBill}\nBill Each will Pay: {perFriendBill} ")
print(f"Type of totalBill Variable:{type(totalBill)}\nType of totalFriend Variable:{type(totalFriends)}\nType of perFriendBill Variable: {type(perFriendBill)} ")

#---------------Section C----------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Section C: Application /Output Based
1. Predict the Output:
x = 5
y = 2.0
print(x // y)
print(x ** y)

Output:

x // y → 2.0
Because 5 // 2.0 performs floor division and returns a float.

x ** y → 25.0
Because 5 ** 2.0 = 25 (returned as float).

Indetify and correct the error:

if = 10
print(if)

Answer:
Error:

if is a reserved keyword in Python, so it cannot be used as a variable name.

Corrected code:
num=10
print(num)
'''