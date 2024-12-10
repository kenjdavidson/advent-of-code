
from typing import Any, List


def is_within_map(map: List[List[Any]], location: tuple[int, int]) -> bool:
    return location[0] >= 0 and location[0] < len(map) and location[1] >= 0 and location[1] < len(map[0])


def print_map(map: List[List[Any]]):
    print(f"Map: {len(map)} x {len(map[0])}")
    for row in map:
        print("".join([str(col) for col in row]))


def lin_add_tuple(first: tuple[int, int], second: tuple[int, int]) -> List[tuple[int, int]]:
    """
    Returns a list containing the possible linear additions for each pair of tuples.  Probably a better name
    for it, but a linear addition provides the extrapolation at the both end of a line created by the two
    tuples.
    There's got to be a smarter way to do this!!
    """
    points = []
    if (first[0] >= second[0] and first[1] >= second[1]):
        points.append((first[0] + abs(first[0]-second[0]),
                      first[1] + abs(first[1]-second[1])))
        points.append((second[0] - abs(first[0]-second[0]),
                       second[1] - abs(first[1]-second[1])))
    elif (first[0] >= second[0] and first[1] <= second[1]):
        points.append((first[0] + abs(first[0]-second[0]),
                      first[1] - abs(first[1]-second[1])))
        points.append((second[0] - abs(first[0]-second[0]),
                       second[1] + abs(first[1]-second[1])))
    elif (first[0] <= second[0] and first[1] >= second[1]):
        points.append((second[0] + abs(first[0]-second[0]),
                      second[1] - abs(first[1]-second[1])))
        points.append((first[0] - abs(first[0]-second[0]),
                       first[1] + abs(first[1]-second[1])))
    elif (first[0] <= second[0] and first[1] <= second[1]):
        points.append((second[0] + abs(first[0]-second[0]),
                      second[1] + abs(first[1]-second[1])))
        points.append((first[0] - abs(first[0]-second[0]),
                       first[1] - abs(first[1]-second[1])))

    return points


def lin_tuple_dirs(first: tuple[int, int], second: tuple[int, int]) -> List[tuple[int, int]]:
    """
    Return a list containing two directions tuples that can be followed to eternity (or they are
    of the map).
    """
    points = []
    if (first[0] >= second[0] and first[1] >= second[1]):
        points.append((abs(first[0]-second[0]), abs(first[1]-second[1])))
        points.append((-abs(first[0]-second[0]), -abs(first[1]-second[1])))
    elif (first[0] >= second[0] and first[1] <= second[1]):
        points.append((abs(first[0]-second[0]), -abs(first[1]-second[1])))
        points.append((-abs(first[0]-second[0]), abs(first[1]-second[1])))
    elif (first[0] <= second[0] and first[1] >= second[1]):
        points.append((abs(first[0]-second[0]), -abs(first[1]-second[1])))
        points.append((-abs(first[0]-second[0]), abs(first[1]-second[1])))
    elif (first[0] <= second[0] and first[1] <= second[1]):
        points.append((abs(first[0]-second[0]), abs(first[1]-second[1])))
        points.append((-abs(first[0]-second[0]), -abs(first[1]-second[1])))

    return points
