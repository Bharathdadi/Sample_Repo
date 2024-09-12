def fibonacci(n):
    """Generate a Fibonacci series up to the nth term."""
    fib_series = []
    a, b = 0, 1
    while len(fib_series) < n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Input: number of terms
try:
    num_terms = int(input("Enter the number of terms you want in the Fibonacci series: "))
    if num_terms <= 0:
        raise ValueError("The number of terms must be a positive integer.")
    print(fibonacci(num_terms))
except ValueError as ve:
    print(f"Invalid input: {ve}")
