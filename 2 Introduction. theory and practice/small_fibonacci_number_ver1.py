def fib(n):
    i = 2
    fib_numbers = [0, 1]
    if n < 2:
        return fib_numbers[n]
      
    while i <= n:
        fib_numbers.append(fib_numbers[i-1] + fib_numbers[i-2])
        i += 1
    
    return fib_numbers[i-1]


assert fib(1) == 1
assert fib(3) == 2
assert fib(10) == 55