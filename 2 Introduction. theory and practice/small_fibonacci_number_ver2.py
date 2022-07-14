def fib(n):
    prev, curr = 0, 1
    for i in range (1, n):
        prev, curr = curr, prev + curr
        
    return curr


assert fib(1) == 1
assert fib(3) == 2
assert fib(10) == 55