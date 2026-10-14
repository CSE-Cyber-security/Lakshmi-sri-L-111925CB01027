# Fibonacci series for n terms (without loop, using recursion)

def fib(n, a=0, b=1):
    if n == 0:
        return
    print(a, end=" ")
    fib(n - 1, b, a + b)

n = int(input("Enter number of terms: "))

if n <= 0:
    print("Please enter a positive number")
else:
    print("Fibonacci series:")
    fib(n)
    print()
