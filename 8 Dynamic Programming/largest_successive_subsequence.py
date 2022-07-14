from typing import List


def get_max_successive_subsequence_size(nums: List[int]) -> int:
    num_size = len(nums)

    sequence_size = [1] * num_size

    for forward_pos in range(num_size):
        for backtrack_pos in range(forward_pos):
            if nums[forward_pos] % nums[backtrack_pos] == 0:
                if sequence_size[backtrack_pos] + 1 > sequence_size[forward_pos]:
                    sequence_size[forward_pos] = sequence_size[backtrack_pos] + 1

    return max(sequence_size)


assert get_max_successive_subsequence_size(
    nums=[3, 6, 7, 12],
) == 3
assert get_max_successive_subsequence_size(
    nums=[3, 6, 12, 7, 9, 24, 18, 3, 9, 24],
) == 5