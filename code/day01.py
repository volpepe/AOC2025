from collections import defaultdict
import numpy as np

from solution import Solution


class Day1(Solution):
    def __init__(self):
        super().__init__(day=1, year=2025)        

    def parse_input(self):
        # self.inp = [
        #     "L68",
        #     "L30",
        #     "R48",
        #     "L5",
        #     "R60",
        #     "L55",
        #     "L1",
        #     "L99",
        #     "R14",
        #     "L82"
        # ]
        self.inp = [(x[0], int(x[1:])) for x in self.inp]
        
    def rotate(self, pos, dir, val):
        if dir == 'R':
            return (pos + val) % 100
        if dir == 'L':
            return (pos - val) % 100

    def rotate_count_zeros(self, pos, dir, val):
        # that's how the kids do it, but i have no time to think
        count = 0
        if dir == 'R':
            fun = lambda x, y: x + y
        if dir == 'L':
            fun = lambda x, y: x - y
        for _ in range(val):
            pos = fun(pos, 1)
            if pos == -1:
                pos = 99
            if pos == 100:
                pos = 0
            count += (pos == 0)
        return pos, count

    def problem_1(self):
        res = 0
        starting_pos = 50
        for dir, val in self.inp:
            new_pos = self.rotate(starting_pos, dir, val)
            res += (new_pos == 0)
            starting_pos = new_pos
        return res
    
    def problem_2(self):
        res = 0
        starting_pos = 50
        for dir, val in self.inp:
            new_pos, click_zero = self.rotate_count_zeros(starting_pos, dir, val)
            res += click_zero
            starting_pos = new_pos
        return res

if __name__ == '__main__':
    print(Day1())

