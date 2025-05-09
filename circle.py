import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

# Example usage
if __name__ == "__main__":
    circle = Circle(5)
    print("Area:", circle.area())          # Output: Area: 78.53981633974483
    print("Perimeter:", circle.perimeter()) # Output: Perimeter: 31.41592653589793