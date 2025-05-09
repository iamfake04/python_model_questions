print("Select operation:")

choice = input("Enter choice (+/-/* or /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '+':
    print(f"Result: {num1 + num2}")
elif choice == '-':
    print(f"Result: {num1 - num2}")
elif choice == '*':
    print(f"Result: {num1 * num2}")
elif choice == '/':
        print(f"Result: {num1 / num2}")

