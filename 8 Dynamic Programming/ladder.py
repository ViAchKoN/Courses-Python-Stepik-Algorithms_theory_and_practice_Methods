import typing as tp


def get_max_sum_in_ladder(
    steps: tp.List[int],
):
    prev_sum = None
    curr_sum = None
    for step in steps:
        if prev_sum is None:
            prev_sum = step
        elif curr_sum is None:
            curr_sum = max(step, prev_sum + step)
        else:
            prev_sum, curr_sum = curr_sum, max(prev_sum+step, curr_sum+step)

    return curr_sum or prev_sum


assert get_max_sum_in_ladder(
    steps=[1, 2]
) == 3
assert get_max_sum_in_ladder(
    steps=[2, -1]
) == 1
assert get_max_sum_in_ladder(
    steps=[-1, 2, 1]
) == 3
