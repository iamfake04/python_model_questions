#Multiple Inheritance
class Flyable:
    def fly(self):
        return "Flying"

class Swimmable:
    def swim(self):
        return "Swimming"

class Duck(Flyable, Swimmable):
    def quack(self):
        return "Quack"

# Example usage
duck = Duck()
print(duck.fly())   # Output: Flying
print(duck.swim())  # Output: Swimming
print(duck.quack()) # Output: Quack