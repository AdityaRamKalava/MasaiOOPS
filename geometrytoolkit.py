import math

class ShapeCalculator:
    def area(self, a, b=None):
        if b is None:
            # Only one argument: treat as circle radius
            return math.pi * a * a
        else:
            # Two arguments: treat as rectangle length and width
            return a * b

# Example usage
sc = ShapeCalculator()

circle_area = sc.area(5)         # Circle with radius 5
rectangle_area = sc.area(4, 6)   # Rectangle 4x6

print("Area of Circle:", circle_area)
print("Area of Rectangle:", rectangle_area)