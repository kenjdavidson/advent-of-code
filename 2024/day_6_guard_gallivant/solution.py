
import os
import sys
from typing import List
from utils.base_solution import BaseSolution

guard_directions = ["^", ">", "v", "<"]
guard_movements = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def add_tuples(tuple1: tuple[int, int], tuple2: tuple[int, int]):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])


class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.map = []
        self.guard_found = False
        self.guard_location = (0, 0)
        self.guard_direction = guard_directions[0]

    def fill_from_file(self, line: str):
        floor = line.strip()
        self.map.append([f for f in floor])

        for i in range(len(floor)):
            if floor[i] in guard_directions:
                print(f"Found guard {floor[i]}")
                self.guard_found = True
                self.guard_location = (self.guard_location[0], i)
                self.guard_direction = guard_directions.index(floor[i])

        if not self.guard_found:
            self.guard_location = (
                self.guard_location[0]+1, self.guard_location[1])

    def guard_in_map(self, location: tuple[int, int]) -> bool:
        return location[0] >= 0 and location[1] >= 0 and location[0] < len(self.map) and location[1] < len(self.map[0])

    def solve(self):
        # Walk the solution adding all tuples to a set, then count the tuples.
        solution = set()
        solution2 = 0
        turns = {}

        print(f"{self.map}")
        print(f"start {self.guard_location} {self.guard_direction}")

        while self.guard_in_map(self.guard_location):
            solution.add(self.guard_location)
            move_to = (self.guard_location[0] + guard_movements[self.guard_direction]
                       [0], self.guard_location[1] + guard_movements[self.guard_direction][1])

            if self.guard_in_map(move_to) and self.map[move_to[0]][move_to[1]] == "#":
                # If the guard runs into a turn, store it with the direction he was walking, so we can
                # check if we've turned on this path previously
                turns[self.guard_location] = self.guard_direction
                self.guard_direction = (self.guard_direction+1) % 4
                continue

            self.guard_location = (self.guard_location[0]+guard_movements[self.guard_direction]
                                   [0], self.guard_location[1]+guard_movements[self.guard_direction][1])

            # After we get to the new spot, we need to simulate a right turn and look in that direction to
            # see if we forced a turn here whether it would run into a previous turn.  This isn't super
            # optimal, but should work.
            check_direction = (self.guard_direction+1) % 4
            check_position = add_tuples(
                self.guard_location, guard_movements[check_direction])
            while self.guard_in_map(check_position) and self.map[check_position[0]][check_position[1]] != "#":
                if check_position in turns and turns[check_position] == check_direction:
                    solution2 += 1
                    break

                check_position = add_tuples(
                    check_position, guard_movements[check_direction])

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
