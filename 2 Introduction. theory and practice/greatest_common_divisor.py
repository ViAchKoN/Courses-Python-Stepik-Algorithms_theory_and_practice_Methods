def gcd(a, b):
    while True:
        if a == 0:
            return b
        if b == 0:
            return a
        if b >= a:
            a, b = b, a
        a, b = b, a % b
    
    
    
assert gcd(18, 35) == 1
assert gcd(14159572, 63967072) == 4