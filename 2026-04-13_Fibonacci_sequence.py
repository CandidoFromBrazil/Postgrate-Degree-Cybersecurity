import itertools

def infinite_fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Get the first 32 Fibonacci numbers that are greater than 0
n_fibs = itertools.islice((x for x in infinite_fib() if x > 0), 32)
print(list(n_fibs))