def get_items(num: int):
    result = []
    remainder = num 
    i = 1
    while i < remainder-i:
        remainder -= i
        result.append(i)
        i += 1        
    result.append(remainder)
    
    return result


assert get_items(
    num=2
) == [2]
assert get_items(
    num=4
) == [1, 3]
assert get_items(
    num=6
) == [1, 2, 3]
assert get_items(
    num=16
) == [1, 2, 3, 4, 6]
assert get_items(
    num=15
) == [1, 2, 3, 4, 5]
