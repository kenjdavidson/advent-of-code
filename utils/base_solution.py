from abc import abstractmethod
from utils import file_helper as fh

import os


class BaseSolution:
    @abstractmethod
    def fill_from_file(self, line: str):
        pass

    @abstractmethod
    def solve(self, filename: str):
        pass

    def solve(self, filename: str):
        """
        Read filename and call solve
        """
        self.read_input_file(filename)
        return self.solve()

    def read_input_file(self, filename):
        """
        Read the file calling through fill_from_file to populate the required data structure
        """
        filepath = f"{os.path.dirname(__file__)}/{filename}"
        fh.read_file(filepath, self.fill_from_file)
