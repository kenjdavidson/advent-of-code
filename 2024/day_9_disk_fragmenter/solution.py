
import os
import sys
from typing import List
from utils.base_solution import BaseSolution
from utils.map_utils import is_within_map, lin_add_tuple, lin_tuple_dirs, print_map
from utils.tuple_utils import add_tuple, sub_tuple

guard_directions = ["^", ">", "v", "<"]
guard_movements = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.id = 0
        self.disk: List[str] = []
        self.disk2: List[str] = []

    def fill_from_file(self, line: str):
        stripped = line.strip()
        print(f"len = {len(stripped)}")
        id = 0
        idx = 0
        for char in stripped:
            entry = str(id) if idx % 2 == 0 else "."
            for i in range(int(char)):
                self.disk.append(entry)
                self.disk2.append(entry)

            idx += 1
            id += 1 if idx % 2 == 1 else 0

    def solution(self):
        i, j = 0, len(self.disk)-1

        while True:
            while self.disk[i] != ".":
                i += 1
            while self.disk[j] == ".":
                j -= 1

            if i > j:
                break

            temp = self.disk[i]
            self.disk[i] = self.disk[j]
            self.disk[j] = temp

        i = 0
        solution = 0
        while self.disk[i] != ".":
            solution += int(self.disk[i]) * i
            i += 1

        return solution

    def solution2(self):
        # 1. From the end get the size of data then look for the matching free space and move, repeat.
        #    Pretty slow based on starting from the start each time.
        # 2. Split into an array of chars, start at the end get size, start at the front and look for size
        #    move data and split space array if room remaining, still linear but less.

        return 0

    def solve(self):
        solution = 0
        solution2 = 0

        solution = self.solution()
        solution2 = self.solution2()

        print(f"Solution 1: {solution}")
        print(f"Solution 2: {solution2}")

    def get_path(self):
        """There's got to be a better way to do this, I hate python"""
        return os.path.dirname(__file__)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("You must provide a filename as the first argument")
        exit(1)

    Solution().run(sys.argv[1])
