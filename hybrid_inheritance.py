#Hybrid Inheritance
class Animal:
    def eat(self):
        return "Eating"

class Mammal(Animal):
    def breathe(self):
        return "Breathing"

class WingedAnimal(Animal):
    def fly(self):
        return "Flying"

class Bat(Mammal, WingedAnimal):
    def echolocation(self):
        return "Using echolocation"

# Example usage
bat = Bat()
print(bat.eat())         # Output: Eating
print(bat.breathe())     # Output: Breathing
print(bat.fly())         # Output: Flying
print(bat.echolocation())# Output: Using echolocation