import bisect
import random
from typing import List

def partition3(numbers, left_position, right_position):
   x, j, t = numbers[left_position], left_position, right_position
   i = j

   while i <= t :
      if numbers[i] < x:
         numbers[j], numbers[i] = numbers[i], numbers[j]
         j += 1

      elif numbers[i] > x:
         numbers[t], numbers[i] = numbers[i], numbers[t]
         t -= 1
         i -= 1
      i += 1   
   return j, t


def quick_sort(numbers, left_position, right_position):
    if left_position >= right_position:
        return
    k = random.randint(left_position, right_position)
    numbers[left_position], numbers[k] = numbers[k], numbers[left_position]
    m1, m2 = partition3(numbers, left_position, right_position)
    quick_sort(numbers, left_position, m1 - 1)
    quick_sort(numbers, m2 + 1, right_position)
    
    return numbers


def element_in_segmenets(
    segments: List[List[int]],
    coordinates: List[int],
) -> List[int]:
    left_boundaries = [segment[0] for segment in segments]
    right_boundaries = [segment[1] for segment in segments]

    left_boundaries = quick_sort(
        numbers=left_boundaries,
        left_position=0,
        right_position=len(left_boundaries) - 1,
    )
    right_boundaries = quick_sort(
        numbers=right_boundaries,
        left_position=0,
        right_position=len(right_boundaries) - 1
    )

    result = []
    for coordinate in coordinates:
        result.append(
            bisect.bisect_right(left_boundaries, coordinate) -  bisect.bisect_left(right_boundaries, coordinate)
        )

    return result


assert quick_sort(
    numbers=[5, 16, 13, 8, 6, 1, 2],
    left_position=0,
    right_position=6,
) == [1, 2, 5, 6, 8, 13, 16]

assert element_in_segmenets(
    segments=[
        [6, 6],
        [0, 3],
        [1, 3],
        [2, 3],
        [3, 4],
        [3, 5],
        [3, 6],
    ], coordinates=[
        1, 2, 3, 4, 5, 6,
    ],
) == [2, 3, 6, 3, 2, 2]
assert element_in_segmenets(
    segments=[
        [-2, 3],
        [0, 3],
        [-1, 0],
        [-1, 3],
        [0, 1],
        [-2, -1],
        [1, 3],
        [2, 3],
        [1, 2],
        [2, 3],
    ], coordinates=[
        -3, -1, 0, 2, 3,
    ],
) == [0, 4, 5, 7, 6]
assert element_in_segmenets(
    segments=[
        [0, 5],
        [7, 10],
    ], coordinates=[
        1, 6, 11
    ],
) == [1, 0, 0]
