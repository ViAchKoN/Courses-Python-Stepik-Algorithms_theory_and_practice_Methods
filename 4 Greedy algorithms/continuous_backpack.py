import typing as tp


def fill_backpack(total_volume: int, items: tp.List[tp.List[int]]):
    total_volume = float(total_volume)

    items = [[item[0], item[1], item[0]/item[1]] for item in items]
    items = sorted(items, key=lambda x: x[2], reverse=True)

    filled_volume = 0
    price = 0

    for item in items:
        volume = filled_volume + item[1]
        if volume <= total_volume:
            filled_volume = volume
            price += item[0]
        else:
            price += ((total_volume - filled_volume) / item[1]) * item[0]
            break

    return round(price, 3)


assert fill_backpack(
    total_volume=50,
    items=[
        [60, 20],
        [100, 50],
        [120, 30],
    ]
) == 180.0
assert fill_backpack(
    total_volume=9022,
    items=[
        [3316, 1601],
        [5375, 8940],
        [2852, 6912],
        [3336, 9926],
        [1717, 8427],
    ]
) == 7777.731
