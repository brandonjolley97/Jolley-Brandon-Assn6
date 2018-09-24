import math

# Prompting the user to input nSides and sLength values
print("Welcome to the Polygon Area Calculator!")
nSides = eval(input("Please enter the number of sides your polygon has: "))
sLength = eval(input("Please enter the side length: "))

# Calculating the Area
area = (nSides * (sLength ** 2)) / (4 * math.tan(math.pi / nSides))

# Displaying the Results
print("Your polygon has an area of " + str(area))