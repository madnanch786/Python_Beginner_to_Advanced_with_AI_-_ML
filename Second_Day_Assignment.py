# Take input from the user for the diameter of a circle and calculate its area

import math

# Input diameter from user
d = float(input("Enter diameter of the circle: "))

# Calculate radius
r = d / 2

# Get value of pi from math module
pi = math.pi

# Calculate area of circle
area = pi * (r ** 2)

# Display result rounded to 2 decimal places
print("Area of Circle:", round(area, 2))
