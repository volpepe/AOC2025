from collections import defaultdict
import numpy as np

from solution import Solution

EXAMPLE_INPUT='''987654321111111
811111111111119
234234234234278
818181911112111'''

class Day3(Solution):
    def __init__(self):
        super().__init__(day=3, year=2025)

    def parse_input(self):
        # self.inp = EXAMPLE_INPUT.split('\n')
        self.inp = [
            [int(x) for x in line]
            for line in self.inp
        ]
        return super().parse_input() 
    
    def find_largest_val(self, line, st_idx = 0, end_idx = 1):
        mx = 0; argmx = 0
        for i in range(st_idx, len(line) - end_idx):
            if line[i] > mx:
                argmx = i
                mx = line[i]
        return mx, argmx

    def find_line_count_with_joltage_size(self, joltage_size, line):
        line_counter = 0
        last_found_digit_idx = -1
        for idx in range(joltage_size):
            mx, argmx = self.find_largest_val(
                line, st_idx=last_found_digit_idx + 1, 
                end_idx=joltage_size-1-idx)
            last_found_digit_idx = argmx
            line_counter += (mx * 10 ** (joltage_size - 1 - idx))
        return line_counter

    def problem_1(self):
        res = 0
        for line in self.inp:
            res += self.find_line_count_with_joltage_size(
                joltage_size=2,
                line=line
            )
        return res
    
    def problem_2(self):
        res = 0
        for line in self.inp:
            res += self.find_line_count_with_joltage_size(
                joltage_size=12,
                line=line
            )
        return res

    
if __name__ == '__main__':
    print(Day3())

