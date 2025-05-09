class Rectangle:
    def __init__(self, height, width, corner_x, corner_y):
        self.height = height
        self.width = width
        self.corner_x = corner_x
        self.corner_y = corner_y

    def center(self):
        center_x = self.corner_x + self.width / 2
        center_y = self.corner_y + self.height / 2
        return (center_x, center_y)

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

# Example usage
def create_rectangle(height, width, corner_x, corner_y):
    return Rectangle(height, width, corner_x, corner_y)

# Instantiate a Rectangle object
rect = create_rectangle(10, 5, 0, 0)

# Get the center, area, and perimeter
center = rect.center()
area = rect.area()
perimeter = rect.perimeter()

print("Center:", center)
print("Area:", area)
print("Perimeter:", perimeter)