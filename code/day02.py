from collections import defaultdict
import math
from typing import List
import numpy as np

from solution import Solution

EXAMPLE_INPUT = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'


class Day2(Solution):
    def __init__(self):
        super().__init__(day=2, year=2025)

    def parse_input(self):
        # self.inp = EXAMPLE_INPUT.split(',')
        self.inp = self.inp[0].split(',')
        self.inp = [tuple(int(t) for t in x.split('-')) for x in self.inp]
        return super().parse_input()
    
    def check_copied_digits_in_range(self, rng) -> List[int]:
        # can be done with math i guess? but i have no time
        s, e = rng
        ids = []
        for n in range(s, e + 1):
            str_n = str(n)
            l_str_n = len(str_n)
            if l_str_n % 2 == 0:
                # can only be done with numbers with even n of digits
                str_n_hlf_1, str_n_hlf_2 = str_n[:l_str_n//2], str_n[l_str_n//2:]
                if str_n_hlf_1 == str_n_hlf_2:
                    ids.append(n)
        return ids 
    
    def check_further_copied_digits_in_range(self, rng):
        # a bit slow. would it be faster with math-only?
        s, e = rng
        ids = set()
        for n in range(s, e + 1):
            str_n = str(n)
            l_str_n = len(str_n)
            for l_cut in range(1, (l_str_n // 2) + 1):
                # we can skip if not all parts would be the same
                if l_str_n % l_cut == 0:
                    str_n_parts = set([str_n[i:i+l_cut] 
                                       for i in range(0, l_str_n, l_cut)])
                    # skip all ids that are already in the set
                    if len(str_n_parts) == 1 and n not in ids:
                        ids.add(n)
        return ids

    def problem_1(self):
        res = 0
        for rng in self.inp:
            res += sum(self.check_copied_digits_in_range(rng))
        return res
    
    def problem_2(self):
        res = 0
        for rng in self.inp:
            res += sum(self.check_further_copied_digits_in_range(rng))
        return res


if __name__ == '__main__':
    print(Day2())

