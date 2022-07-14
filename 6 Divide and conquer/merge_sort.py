from typing import List, Tuple


def merge_sort(
    numbers: List[int],
) -> Tuple[List[int], int]:
    size = len(numbers)
    inversions = 0

    if size == 1:
        return numbers, inversions
    else:
        middle = size // 2
        left_part = numbers[:middle]
        right_part = numbers[middle:]
    
        left_sorted, left_inversion = merge_sort(left_part)
        right_sorted, right_inversion = merge_sort(right_part)

        inversions += left_inversion + right_inversion

        whole_sorted = []

        while left_sorted and right_sorted:
            if left_sorted[0] <= right_sorted[0]:
                whole_sorted.append(left_sorted.pop(0))
            else:
                whole_sorted.append(right_sorted.pop(0))
                inversions += len(left_sorted)

        whole_sorted.extend(left_sorted or right_sorted)

        return whole_sorted, inversions


assert merge_sort(
    numbers=[1, 3, 4, 7, 2, 5, 6, 8],
) == ([1, 2, 3, 4, 5, 6, 7, 8], 5)
assert merge_sort(
    numbers=[2, 3, 9, 2, 9],
) == ([2, 2, 3, 9, 9], 2)
assert merge_sort(
    numbers=[9, 2],
) == ([2, 9], 1)