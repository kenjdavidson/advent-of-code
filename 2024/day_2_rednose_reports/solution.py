import os
import sys
import re
from types import NoneType
from typing import List
import utils.file_helper as fh


def _is_valid_difference(value: int) -> bool:
    """
    Check that the absolute value is between 1 and 3
    """
    return abs(value) > 0 and abs(value) < 4


def _is_valid_sequence(previous_value: int, value: int) -> bool:
    """
    Check that the previous_value is not None and is the same value 
    """
    return (type(previous_value) is NoneType) or (previous_value < 0 and value < 0) or (previous_value > 0 and value > 0)


def _check_data(first: int, second: int, previous_diff: int) -> int:
    """
    Compares values in relation to the previous check
    """
    diff = second - first
    if _is_valid_difference(diff) and _is_valid_sequence(previous_diff, diff):
        return diff
    else:
        raise ValueError("Inavlid difference or sequence")


def _check_report(report: List[int]):
    """
    Check a single report by moving through each pair of numbers checking the requirements.
    """
    try:
        diff = _check_data(report[0], report[1], None)

        for i in range(1, len(report)-1):
            diff = _check_data(report[i], report[i+1], diff)

        return 1
    except ValueError:
        return 0


def _check_report_dual(report: List[int]):
    """
    Traverse the report (working) performing the same test using two pointers.  If we come 
    across an invalid value, remove it and continue parsing.  If we come across a second invalid
    value, then fail.

    After some playing this doesn't work; it's failing on the first value being the failing value.
    Will come back to this a little later.
    """
    working_report = [v for v in report]
    i, j = 0, 1
    bad_report = False
    diff = None

    while j < len(working_report):
        try:
            diff = _check_data(working_report[i], working_report[j], diff)
            i, j = i+1, j+1
        except ValueError:
            if bad_report:
                print(f"{report} = 0")
                return 0

            working_report.remove(working_report[j])
            bad_report = True

    return 1


def _check_report_iter(report: List[int]):
    """
    Since I'm not smart enough to think of something elegant, let's brute force attempt
    by retrying every combindation of the List.  This hurts me inside, but it should
    work and then we can compare.
    """
    valid = _check_report(report)

    remove = 0
    while valid is 0 and remove < len(report):
        working_report = report[:remove] + report[remove+1:]
        valid = _check_report(working_report)
        remove += 1

    return valid


class Solution:
    def fill_from_file(self, line: str):
        """
        Fills the appropriate lists with input file content
        """
        report = line.strip().split(" ")
        self.reports.append([int(r) for r in report])

    def run(self, filename: str):
        self.reports = []

        filepath = f"{os.path.dirname(__file__)}/{filename}"
        fh.read_file(filepath, self.fill_from_file)

        safety = 0
        tolerate = 0
        for report in self.reports:
            safety += _check_report(report)
            tolerate += _check_report_iter(report)

        print(f"Solution 1: {safety}")
        print(f"Solution 2: {tolerate}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("You must provide a filename as the first argument")
        exit(1)

    Solution().run(sys.argv[1])
