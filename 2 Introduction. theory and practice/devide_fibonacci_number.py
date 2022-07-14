def fib_mod(n, m):
    prev_mod = 0
    curr_mod = 1
    pizano_period = [prev_mod, curr_mod]
    for i in range (1, n):
        prev_mod, curr_mod = curr_mod, (prev_mod + curr_mod) % m
        if prev_mod == 0 and curr_mod == 1:
            pizano_period.pop()
            break
        pizano_period.append(curr_mod)
            
    pos = n % (i - 1)  #pizzano period is length of it or i - 1
    return pizano_period[pos]

assert fib_mod(10, 2) == 1
assert fib_mod(10, 4) == 3
assert fib_mod(10, 3) == 1
assert fib_mod(9, 2) == 0
assert fib_mod(1025, 55) == 5
assert fib_mod(12589, 369) == 89
assert fib_mod(1598753, 25897) == 20305