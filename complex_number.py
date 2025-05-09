class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return Complex(new_real, new_imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Example usage
if __name__ == "__main__":
    c1 = Complex(2, 3) # Create a complex number 2 + 3i
    c2 = Complex(4, 5) # Create a complex number 4 + 5i
    result = c1 + c2 
    print("Result of c1 + c2:", result)  # Output: Result of c1 + c2: 6 + 8i