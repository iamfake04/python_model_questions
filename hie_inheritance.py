#Hierarchical Inheritance
class Bird:
    def fly(self):
        return "Flying"

class Sparrow(Bird):
    def chirp(self):
        return "Chirp"

class Eagle(Bird):
    def hunt(self):
        return "Hunting"

# Example usage
sparrow = Sparrow()
eagle = Eagle()
print(sparrow.fly())   # Output: Flying
print(sparrow.chirp()) # Output: Chirp
print(eagle.fly())     # Output: Flying
print(eagle.hunt())    # Output: Hunting