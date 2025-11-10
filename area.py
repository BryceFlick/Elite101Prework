import math

shape = input("I can calculate the area of a shape for you. Which shape do you want me to calculate the area of? ")

def getCircleArea():
    radius = float(input("What is the radius of the circle? "))
    return math.pi * math.pow(radius, 2)

def getRectangleArea():
    width = float(input("What is the width of the rectangle? "))
    length = float(input("What is the length of the rectangle? "))
    return width * length

def getSquareArea():
    side = float(input("What is the side length of the square? "))
    return side * side

def getTriangleArea():
    width = float(input("What is the width (base) of the triangle? "))
    height = float(input("What is the height of the triangle? "))
    return 0.5 * width * height

shape = shape.lower()

if shape == "circle":
    print(f"The area of the circle is {getCircleArea()}")

elif shape == "rectangle":
    print(f"The area of the rectangle is {getRectangleArea()}")

elif shape == "square":
    print(f"The area of the square is {getSquareArea()}")

elif shape == "triangle":
    print(f"The area of the triangle is {getTriangleArea()}")

else:
    print("I can only compute a circle, rectangle, square, or triangle.")
