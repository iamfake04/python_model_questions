# Single Inheritance 
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

# Example usage
dog = Dog()
print(dog.speak())  # Output: Bark