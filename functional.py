import unittest
def calculate_rectangle_area(length, width):
    area = length * width
    return area

# Input from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate and display the area
area = calculate_rectangle_area(length, width)
print(f"The area of the rectangle is: {area}")