from typing import List


def get_longest_nonincreasing_subsequence(nums: List[int]) -> List[int]:
    nums_size = len(nums)

    sequence_size = [1] * nums_size
    sequence_pos = [-1] * nums_size

    for forward_pos in range(nums_size):
        for backtrack_pos in range(forward_pos):
            if nums[forward_pos] <= nums[backtrack_pos]:
                if sequence_size[backtrack_pos] + 1 > sequence_size[forward_pos]:
                    sequence_size[forward_pos] = sequence_size[backtrack_pos] + 1
                    sequence_pos[forward_pos] = backtrack_pos

    max_subsequence_size = max(sequence_size)

    pos = sequence_size.index(max_subsequence_size)

    result = []
    while True:
        result.insert(0, pos + 1)
        pos = sequence_pos[pos]

        if pos == -1:
            break

    return result


assert get_longest_nonincreasing_subsequence(
    nums=[5, 3, 4, 4, 2],
) == [1, 3, 4, 5]

