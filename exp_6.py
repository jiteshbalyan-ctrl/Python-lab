# create a program that defines a function to calculate the area of a circle based on the radius entered by the user
# using math library for pi constant
import math
def calculate_area(radius):
    area = math.pi * radius ** 2
    return area

radius = float(input("Enter the radius of the circle: "))
print("The area of the circle is:", calculate_area(radius))