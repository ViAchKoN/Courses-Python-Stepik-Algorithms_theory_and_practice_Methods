from typing import List


def get_index(
    nums: List[int],
    left: int,
    right: int,
    key: int,
):

    while (right - left > 1):
        m = left + (right - left) // 2
        if (nums[m] >= key):
            right = m
        else:
            left = m
    return right


def get_longest_nonincreasing_subsequence(nums: List[int]) -> List[int]:
    sequence_size = len(nums)
    
    if sequence_size == 1:
        return [1]

    sequence_pos = [0 for i in range(sequence_size + 1)]
    size = 0  # always points empty slot

    sequence_pos[0] = nums[0]
    size = 1
    for i in range(1, sequence_size):

        if (nums[i] > sequence_pos[0]):

            # new smallest value
            sequence_pos[0] = nums[i]

        elif (nums[i] < sequence_pos[size - 1]):

            # nums[i] wants to extend
            # largest subsequence
            sequence_pos[size] = nums[i]
            size += 1

        else:
            # nums[i] wants to be current
            # end candidate of an existing
            # subsequence. It will replace
            # cell value in sequence_pos
            sequence_pos[get_index(
                sequence_pos, -1, size - 1, nums[i])] = nums[i]

    result = []
    i = 0
    while i != size + 1:
        pos = sequence_pos[i] + 1
        result.insert(0, pos)
        i += 1

    return result


assert get_longest_nonincreasing_subsequence(
    nums=[5, 3, 4, 4, 2],
) == [1, 3, 4, 5]

