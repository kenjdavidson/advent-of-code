
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
        self.map: List[List[str]] = []
        self.antenna: map[str, List[tuple[int, int]]] = {}

    def fill_from_file(self, line: str):
        locations = line.strip()
        locationList = []
        self.map.append(locationList)

        for idx in range(len(locations)):
            locationList.append(locations[idx])
            if locations[idx] == ".":
                continue

            if locations[idx] not in self.antenna:
                self.antenna[locations[idx]] = []

            self.antenna[locations[idx]].append((len(self.map)-1, idx))

    def calculateAntiAntenna(self, freq: str, locs: List[tuple[int, int]]) -> List[tuple[int, int]]:
        # Lets do this grossly for now
        working = 0
        next = 1
        antiAntenna = set()
        while working < len(locs)-1:
            for next in range(working+1, len(locs)):
                first, second = lin_add_tuple(locs[working], locs[next])
                if is_within_map(self.map, first):
                    antiAntenna.add(first)
                if is_within_map(self.map, second):
                    antiAntenna.add(second)

            working += 1

        return antiAntenna

    def calculateAntiAntenna2(self, freq: str, locs: List[tuple[int, int]]) -> List[tuple[int, int]]:
        # Lets do this grossly for now
        working = 0
        next = 1
        antiAntenna = set()
        while working < len(locs)-1:
            for next in range(working+1, len(locs)):
                first, second = lin_tuple_dirs(locs[working], locs[next])

                test = add_tuple(locs[working], first)
                while is_within_map(self.map, test):
                    antiAntenna.add(test)
                    test = add_tuple(test, first)

                test = add_tuple(locs[next], second)
                while is_within_map(self.map, test):
                    antiAntenna.add(test)
                    test = add_tuple(test, second)

            working += 1

        return antiAntenna

    def solve(self):
        solution = set()
        solution2 = 0

        print_map(self.map)

        for key in self.antenna:
            antiAntenna = self.calculateAntiAntenna(key, self.antenna[key])
            antiAntenna2 = self.calculateAntiAntenna2(key, self.antenna[key])
            solution |= antiAntenna
            solution |= antiAntenna2

            for antenna in antiAntenna2:
                if (self.map[antenna[0]][antenna[1]] == "."):
                    self.map[antenna[0]][antenna[1]] = "#"

        print_map(self.map)

        print(f"Solution 1: {len(solution)}")
        print(f"Solution 2: {solution2}")

    def get_path(self):
        """There's got to be a better way to do this, I hate python"""
        return os.path.dirname(__file__)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("You must provide a filename as the first argument")
        exit(1)

    Solution().run(sys.argv[1])
