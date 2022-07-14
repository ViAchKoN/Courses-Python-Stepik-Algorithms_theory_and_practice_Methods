def fib_digit(n):
    prev_last_number, curr_last_number = 0, 1
    for i in range (1, n):
        prev_last_number, curr_last_number = curr_last_number, (prev_last_number + curr_last_number) % 10
        
    return curr_last_number


assert fib_digit(18) == 4   # 2584
assert fib_digit(24) == 8   # 46368
assert fib_digit(36) == 2   # 14930352