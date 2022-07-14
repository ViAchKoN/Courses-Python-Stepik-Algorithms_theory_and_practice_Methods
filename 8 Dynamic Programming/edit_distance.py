

def edit_distance(
    input_str: str,
    output_str: str,
) -> int:
    input_size = len(input_str)     # vertical
    output_size = len(output_str)   # horizontal

    grid = []

    for i in range(input_size + 1):
        grid.append([-1] * (output_size + 1))

    for i in range(output_size + 1):
        grid[0][i] = i
    for i in range(1, input_size + 1):
        grid[i][0] = i

    for i in range(1, input_size + 1):           # moving vertical
        for j in range(1, output_size + 1):      # moving horizontal
            diff = (input_str[i - 1] != output_str[j - 1])

            grid[i][j] = min(
                grid[i][j - 1] + 1,
                grid[i - 1][j] + 1,
                grid[i - 1][j - 1] + diff,
            )

    return grid[i][j]


assert edit_distance(
    input_str='distance',
    output_str='editing',
) == 5
assert edit_distance(
    input_str='short',
    output_str='ports',
) == 3
assert edit_distance(
    input_str='ab',
    output_str='ab',
) == 0
