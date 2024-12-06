import os
import re
import sys
from types import NoneType
from typing import List
import utils.file_helper as fh


def _calculate_result(content: str):
    matches = re.findall("mul\((\d{1,3}),(\d{1,3})\)", content)
    result = 0
    for match in matches:
        x, y = match
        result += int(x) * int(y)

    return result


def _calculate_checked_result(content: str):
    matches = re.findall(
        "(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))", content)

    do_mul = True
    result = 0
    for match in matches:
        cmd, x, y = match

        if cmd == "do()":
            do_mul = True
        elif cmd == "don't()":
            do_mul = False
        elif do_mul:
            result += int(x) * int(y)

    return result


class Solution:
    def fill_from_file(self, line: str):
        """
        Fills the appropriate lists with input file content
        """
        self.content += line.strip()

    def run(self, filename: str):
        self.content = ""

        filepath = f"{os.path.dirname(__file__)}/{filename}"
        fh.read_file(filepath, self.fill_from_file)

        solution = _calculate_result(self.content)
        solution2 = _calculate_checked_result(self.content)

        print(f"Solution 1: {solution}")
        print(f"Solution 2: {solution2}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("You must provide a filename as the first argument")
        exit(1)

    Solution().run(sys.argv[1])
