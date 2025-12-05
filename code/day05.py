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
        self.inp = EXAMPLE_INPUT.split('\n')
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
        pass


    def problem_1(self):
        res = 0
        for ingrd in self.ingredient_id:
            res += self.check_if_fresh(ingrd)
        return res
    
    def problem_2(self):
        res = 0
        return res

    
if __name__ == '__main__':
    print(Day5())

