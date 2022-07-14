from typing import List


def get_longest_nonincreasing_subsequence(nums: List[int]) -> List[int]:
    nums_size = len(nums)

    sequence_size = [0] * nums_size
    sequence_pos = [0] * (nums_size + 1)

    min_value = 0

    nums = nums[:: -1]

    for i in range(nums_size):
        temp_min_value = 1

        temp_max_value = min_value

        while temp_min_value <= temp_max_value:
            mid = (temp_min_value + temp_max_value) // 2

            if nums[sequence_pos[mid]] <= nums[i]:
                temp_min_value = mid + 1

            else:
                temp_max_value = mid - 1

        new_min_value = temp_min_value
        sequence_size[i] = sequence_pos[new_min_value - 1]

        if new_min_value > min_value:
            sequence_pos[new_min_value] = i
            min_value = new_min_value

        elif nums[i] < nums[sequence_pos[new_min_value]]:
            sequence_pos[new_min_value] = i

    result = [0] * min_value
    k = sequence_pos[min_value]
    for i in range(min_value - 1, -1, -1):
        result[i] = nums_size - k
        k = sequence_size[k]
        
    return result[::-1]


assert get_longest_nonincreasing_subsequence(
    nums=[5, 3, 4, 4, 2],
) == [1, 3, 4, 5]
