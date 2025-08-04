import random

def lottery():
    for i in range(6):
        yield random.randint(1,100)
    yield random.randint(100,200)

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for r in lottery():
    print("Next winner is %d" % r)

x = fibonacci(7)
print("Fib(7) is", x)

