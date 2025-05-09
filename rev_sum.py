num = int(input("Enter a number: "))
reversed_num = 0
sum_of_digits = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    sum_of_digits += digit
    num //= 10

print("Reversed Number:", reversed_num)
print("Sum of Digits:", sum_of_digits)