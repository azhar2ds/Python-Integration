def fib():
    a, b = 0, 1
    n = 15
    while(n-2):
        a, b = b, b+a
        print(a, end=' ')
        n -= 1


fib()
