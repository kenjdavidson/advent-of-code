
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
        self.equations: map[str, List[int]] = {}

    def fill_from_file(self, line: str):
        equation = line.strip().split(":")
        self.equations[int(equation[0].strip())] = [int(num)
                                                    for num in equation[1].strip().split(" ")]

    def solve_equation(self, answer: int, values: List[int]) -> int:
        solutions = set()
        solutions.add(values[0])
        for i in range(1, len(values)):
            new_solutions = set()
            for solution in solutions:
                new_solutions.add(solution + values[i])
                new_solutions.add(solution * values[i])

            solutions = new_solutions

        return answer if answer in solutions else 0

    def solve_equation2(self, answer: int, values: List[int]) -> int:
        solutions = set()
        solutions.add(values[0])
        for i in range(1, len(values)):
            new_solutions = set()
            for solution in solutions:
                new_solutions.add(int(str(solution) + str(values[i])))
                new_solutions.add(solution + values[i])
                new_solutions.add(solution * values[i])

            solutions = new_solutions

        return answer if answer in solutions else 0

    def solve(self):
        solution = 0
        solution2 = 0

        print(f"{self.equations}")
        for answer in self.equations:
            solution += self.solve_equation(answer, self.equations[answer])
            solution2 += self.solve_equation2(answer, self.equations[answer])

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
