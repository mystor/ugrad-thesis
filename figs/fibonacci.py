# Return the i-th number in the fibonacci sequence
def fib(n : int) -> int:
    if n < 2:
        return 1
    return fib(n-2) + fib(n-1)

print(fib(5))
