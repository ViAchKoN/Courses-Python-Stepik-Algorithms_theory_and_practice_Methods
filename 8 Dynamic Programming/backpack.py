import typing as tp


def fill_backpack(
    total_volume: int,
    items_num: int,
    item_weights: tp.List[int],
):
    grid = []

    for _ in range(items_num + 1):
        grid.append([0] * (total_volume + 1))

    for item_num in range(1, items_num + 1):                # moving vertical
        for curr_volume in range(1, total_volume + 1):      # moving horizontal
            grid[item_num][curr_volume] = grid[item_num - 1][curr_volume]

            item_weight = item_weights[item_num - 1]

            if item_weight <= curr_volume:
                grid[item_num][curr_volume] = max(
                    grid[item_num][curr_volume],
                    grid[item_num - 1][curr_volume - item_weight] + item_weight
                )
    return grid[item_num][curr_volume]


assert fill_backpack(
    total_volume=10,
    items_num=3,
    item_weights=[1, 4, 8],
) == 9
