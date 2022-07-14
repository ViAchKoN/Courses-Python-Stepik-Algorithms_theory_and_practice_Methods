from typing import List


def counting_sort(nums: List[int]) -> List[int]:
    result = []

    nums_count = [0] * 11

    for num in nums:
        nums_count[num] += 1

    for pos, count in enumerate(nums_count):
        while count != 0:
            result.append(pos)
            count -= 1
    return result


assert counting_sort(
    nums=[2, 3, 9, 2, 9]
) == [2, 2, 3, 9, 9]
