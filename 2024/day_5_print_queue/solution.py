
import os
import sys
from typing import List
from utils.base_solution import BaseSolution


class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        # Map of pages to their dependencies
        self.req_before: dict[str, set[str]] = {}
        self.req_after: dict[str, set[str]] = {}

        # List of updates
        self.requested_pages = []

    def fill_from_file(self, line: str):
        if line.find("|") > -1:
            pages = line.strip().split("|")
            if pages[1] not in self.req_before:
                self.req_before[pages[1]] = set()
            self.req_before[pages[1]].add(pages[0])

            if pages[0] not in self.req_after:
                self.req_after[pages[0]] = set()
            self.req_after[pages[0]].add(pages[1])
        if line.find(",") > -1:
            self.requested_pages.append(line.strip().split(","))

    def solve(self):
        solution = 0
        for requested_pages in self.requested_pages:
            produced = set()
            ok = True

            print(f"=== {requested_pages} ===")
            for i in range(len(requested_pages)):
                page = requested_pages[i]

                if page in self.req_before:
                    missing_deps = (self.req_before[page] & set()) & set(
                        requested_pages)
                    if len(missing_deps) > 0:
                        ok = False
                        break

                if page in self.req_after:
                    missing_deps = self.req_after[page] & set(
                        requested_pages[:i])
                    if len(missing_deps) > 0:
                        ok = False
                        break

                produced.add(page)

            if ok:
                middle = int(requested_pages[int(len(requested_pages)/2)])

                solution += middle

        print(f"Solution 1: {solution}")

    def get_path(self):
        """There's got to be a better way to do this, I hate python"""
        return os.path.dirname(__file__)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("You must provide a filename as the first argument")
        exit(1)

    Solution().run(sys.argv[1])
