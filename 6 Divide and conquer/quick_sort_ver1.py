import random
from typing import List


def quick_sort(
    numbers: List[int],
    left_position: int,
    right_position: int,
):
    if left_position >= right_position:
        return numbers

    new_left_position = left_position
    new_right_posistion = right_position
    
    number_to_compare = numbers[random.randint(left_position, right_position)]

    while new_left_position <= new_right_posistion:
        while numbers[new_left_position] < number_to_compare:
            new_left_position += 1
        while numbers[new_right_posistion] > number_to_compare:
            new_right_posistion -= 1
        if new_left_position <= new_right_posistion:
            numbers[new_left_position], numbers[new_right_posistion] = numbers[new_right_posistion], numbers[new_left_position]
            new_left_position += 1
            new_right_posistion -= 1
    quick_sort(numbers, left_position, new_right_posistion)
    quick_sort(numbers, new_left_position, right_position)
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
        insertions = 0
        for number in left_boundaries:
            if number <= coordinate:
                insertions += 1
        for number in right_boundaries:
            if number < coordinate:
                insertions -= 1

        result.append(insertions if insertions else 0)

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
