print("Hello, World!")

#Basic Fibonacci sequence loop
print("\nFibonacci Sequence:")
n = 10  # Number of terms to generate
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b