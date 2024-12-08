import os
import re
import sys
from types import NoneType
from typing import List
import utils.file_helper as fh

directions = [
    [(0, -1), (0, -2), (0, -3)],
    [(-1, -1), (-2, -2), (-3, -3)],
    [(-1, 0), (-2, 0), (-3, 0)],
    [(-1, 1), (-2, 2), (-3, 3)],
    [(0, 1), (0, 2), (0, 3)],
    [(1, 1), (2, 2), (3, 3)],
    [(1, 0), (2, 0), (3, 0)],
    [(1, -1), (2, -2), (3, -3)]
]


def _check_xmas(puzzle: List[List[str]], start: tuple[int, int], direction: List[tuple[int, int]]):
    chars = ""

    for location in direction:
        x, y = location[0] + start[0], location[1] + start[1]
        if x < 0 or x >= len(puzzle) or y < 0 or y >= len(puzzle[0]):
            return False
        else:
            chars += puzzle[x][y]

    return chars == "MAS"


def _count_xmas(puzzle):
    """
    Start at 0,0 looking for an X, when an X is found, look in each direction and count all the XMAS.
    """
    count = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == "X":
                for direction in directions:
                    if _check_xmas(puzzle, (i, j), direction):
                        count += 1

    return count


x_directions = [
    [(-1, -1), (1, 1)],
    [(1, -1), (-1, 1)]
]


def _check_x_dir(puzzle: List[List[str]],  start: tuple[int, int], direction: List[tuple[int, int]]) -> str:
    chars = ""

    for location in direction:
        x, y = location[0] + start[0], location[1] + start[1]
        if x < 0 or x >= len(puzzle) or y < 0 or y >= len(puzzle[0]):
            chars += ""
        else:
            chars += puzzle[x][y]

    return chars


def _count_x_mas(puzzle):
    """
    Start at 1,1 and go to length-1,length-1 and we want to look for an A.  When we find an A, we can look at
    -1,-1, -1, 1, 1, -1, 1, 1
    """
    count = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == "A":
                x_dir_1 = _check_x_dir(puzzle, (i, j), x_directions[0])
                x_dir_2 = _check_x_dir(puzzle, (i, j), x_directions[1])
                if (x_dir_1 == "MS" or x_dir_1 == "SM") and (x_dir_2 == "MS" or x_dir_2 == "SM"):
                    count += 1

    return count


class Solution:
    def fill_from_file(self, line: str):
        """
        Fills the appropriate lists with input file content
        """
        self.puzzle.append([char for char in line.strip()])

    def run(self, filename: str):
        self.puzzle = []

        filepath = f"{os.path.dirname(__file__)}/{filename}"
        fh.read_file(filepath, self.fill_from_file)

        solution = _count_xmas(self.puzzle)
        solution2 = _count_x_mas(self.puzzle)

        print(f"Solution 1: {solution}")
        print(f"Solution 2: {solution2}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("You must provide a filename as the first argument")
        exit(1)

    Solution().run(sys.argv[1])
