N = int(input("Enter the number of terms for Fibonacci series: "))
a, b = 0, 1
print("Fibonacci series:")
for i in range(N):
    print(a, end=' ')
    a, b = b, a + b
print()