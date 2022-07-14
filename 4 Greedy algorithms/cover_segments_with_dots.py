import typing as tp


def cover_segments(
    segments: tp.List[tp.List[int]],
):
    segments = sorted(segments, key=lambda x: x[1])
    
    result = [segments[0][1]]
    
    for segment in segments[1:]:
        left, right = segment
        if left > result[-1]:
            result.append(right)  
    return result    


assert cover_segments(
    segments=[
        [1, 3], 
        [2, 5], 
        [3, 6],
    ]
) == [3]
assert cover_segments(
    segments=[
        [4, 7],
        [1, 3],
        [2, 5],
        [5, 6],
    ]
) == [3, 6]
assert cover_segments(
    segments=[
        [4, 7],
        [1, 3],
        [2, 5],
        [5, 6],
        [6, 8],
    ]
) == [3, 6]
