def fib(a, b):
    while True:
        yield a
        a, b = b, a+b


for x in fib(0, 1):
    if x > 100:
        break
    print(x, end=' ')
