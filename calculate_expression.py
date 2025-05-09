try:
    n = int(input("Enter a value for n: "))
    result = 2**(2*n) + n + 5
    print("The result of 2^(2n) + n + 5 is:", result)
except ValueError:
    print("Invalid input. Please enter an integer.")
except OverflowError:
    print("The result is too large to handle.")
except Exception as e:
    print("An error occurred:", e)