from typing import Tuple, List

def calculator(
    num: int,
) -> Tuple[int, List[int]]:
    ops = {1: 0}
    prevs = {}
    for i in range(1, num):
        for i_x in [i * 3, i * 2, i + 1]:
            if i_x > num:
                continue
            if ops.get(i_x) is None or ops[i] + 1 < ops[i_x]:
                ops[i_x] = ops[i] + 1
                prevs[i_x] = i
    nums = [num]
    if prevs:
        k = prevs[num]
        while k != 1:
            nums.append(k)
            k = prevs[k]
        nums.append(1)
        nums.reverse()
    return ops[num], nums
        
assert calculator(
    num=1,
) == (
    0,
    [1],
)
assert calculator(
    num=5,
) == (
    3,
    [1, 2, 4, 5],
)
assert calculator(
    num=96234,
) == (
    14,
    [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234],
)
