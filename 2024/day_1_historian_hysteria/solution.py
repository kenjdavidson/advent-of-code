import os
import sys
import re
import utils.file_helper as fh


class Solution:
    def fill_from_file(self, line: str):
        """
        Fills the appropriate lists with input file content
        """
        match = re.search("^(\\d+)\\s+(\\d+)$", line)
        self.left.append(int(match.group(1)))
        self.right.append(int(match.group(2)))

    def run(self, filename: str):
        self.left, self.right = [], []

        filepath = f"{os.path.dirname(__file__)}/{filename}"
        fh.read_file(filepath, self.fill_from_file)

        self.left.sort()
        self.right.sort()

        count = 0
        similarity = 0
        for first, second in zip(self.left, self.right):
            # Count the difference between left and right
            count += abs(first - second)

            # Apply the similarity function of left * count(left)
            similarity += first * self.right.count(first)

        print(f"Solution 1: {count}")
        print(f"Solution 2: {similarity}")


if __name__ == "__main__":
    Solution().run(sys.argv[1])
