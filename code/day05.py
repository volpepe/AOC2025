from collections import defaultdict
import numpy as np

from solution import Solution

EXAMPLE_INPUT = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''


class Day5(Solution):
    def __init__(self):
        super().__init__(day=5, year=2025)

    def parse_input(self):
        # self.inp = EXAMPLE_INPUT.split('\n')
        self.fresh_ingredients_ranges = set()
        self.ingredient_id = set()
        ing_flag = False
        for l in self.inp:
            if len(l) == 0:
                ing_flag = True
                continue
            if ing_flag:
                self.ingredient_id.add(int(l.rstrip()))
            else:
                self.fresh_ingredients_ranges.add(
                    tuple([int(x.rstrip()) for x in l.split('-')])
                )
        return super().parse_input()
    
    def check_if_fresh(self, ingrd):
        for (lb, ub) in self.fresh_ingredients_ranges:
            if lb <= ingrd <= ub:
                return True
        return False
    
    def remove_intersections(self):
        sorted_ranges = sorted(self.fresh_ingredients_ranges,
                               key = lambda x: x[0])
        for i in range(len(sorted_ranges[:-1])):
            print(f'range {sorted_ranges[i]}')
            j = (i + 1)
            while True:
                # refresh
                si, ei = sorted_ranges[i]
                # don't look over the end of the list
                if j == len(sorted_ranges):
                    break
                sj, ej = sorted_ranges[j]
                # if looking over the end of the range, stop
                if sj > ei:
                    break
                # otherwise, check if next range is entirely contained
                # within current
                if si <= sj <= ei and \
                   si <= ej <= ei:
                    # flatten the j range
                    sorted_ranges[j] = (-1, -1)
                    j += 1
                    continue
                # if not, check for partial overlaps
                if sj <= ei <= ej:
                    if (si != sj):
                        sorted_ranges[i] = (si, sj - 1)
                    else:
                        sorted_ranges[i] = (-1, -1)
                j += 1
        sorted_ranges = set(sorted_ranges)
        if (-1, -1) in sorted_ranges:
            sorted_ranges.remove((-1, -1))
        return sorted_ranges
    
    def count_fresh_ids(self, uniq_ranges):
        count = 0
        for (si, ei) in uniq_ranges:
            count += ((ei - si) + 1)
        return count

    def problem_1(self):
        res = 0
        for ingrd in self.ingredient_id:
            res += self.check_if_fresh(ingrd)
        return res
    
    def problem_2(self):
        res = 0
        uniq_sorted_ranges = self.remove_intersections()
        res = self.count_fresh_ids(uniq_sorted_ranges)
        return res

    
if __name__ == '__main__':
    print(Day5())

