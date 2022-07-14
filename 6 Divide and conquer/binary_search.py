from typing import List


def binary_search(
    numbers: List[int],
    look_up: List[int],
):
    sorted_numbers = sorted(numbers)

    result = []
    for looked_up_number in look_up:
        numbers = sorted_numbers
        
        left_pos = 0
        right_pos = len(numbers) - 1
        middle_pos = (left_pos + right_pos) // 2

        while left_pos < right_pos:
            middle_pos = (left_pos + right_pos) // 2
            middle_number = numbers[middle_pos]
            
            if looked_up_number < middle_number:
                middle_pos -= 1
                right_pos = middle_pos
            elif looked_up_number > middle_number:
                middle_pos += 1
                left_pos = middle_pos
            else:
                break

        if numbers[middle_pos] != looked_up_number:
            result.append(-1)
        else:
            result.append(middle_pos + 1)

    return result


assert binary_search(
    numbers=[1, 5, 8, 12, 13],
    look_up=[13, 15, 13, 1],
) == [5, -1, 5, 1]
assert binary_search(
    numbers=[1, 5, 8, 12, 13],
    look_up=[8, 1, 23, 1, 11],
) == [3, 1, -1, 1, -1]
assert binary_search(
    numbers=[4],
    look_up=[3],
) == [-1]
