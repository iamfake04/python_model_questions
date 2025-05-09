import math

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def sin_approx(x_deg, n_terms):
    x_rad = math.radians(x_deg)  # Convert degrees to radians
    result = 0
    sign = 1
    
    for i in range(n_terms):
        term = (x_rad ** (2 * i + 1)) / factorial(2 * i + 1)
        result += sign * term
        sign *= -1  # Alternate the sign
        
    return result

# Input from user
x_deg = float(input("Enter the value of x (in degrees): "))
n_terms = int(input("Enter the number of terms: "))

# Calculate and display the result
approx_sin = sin_approx(x_deg, n_terms)
print(f"Approximation of sin({x_deg}) using {n_terms} terms: {approx_sin}")