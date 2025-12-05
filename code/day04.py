from collections import defaultdict
import numpy as np

from solution import Solution

EXAMPLE_INPUT = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''


class Day4(Solution):
    def __init__(self):
        super().__init__(day=4, year=2025)

    def parse_input(self):
        # self.inp = EXAMPLE_INPUT.split('\n')
        return super().parse_input(type='str_map') 
    
    def get_surroundings(self, y, x):
        surrounding_pos = set()
        x_minus_1 = max(0,x-1)
        x_plus_1 = min(x+1, self.map.shape[1]-1)
        y_minus_1 = max(0,y-1)
        y_plus_1 = min(y+1, self.map.shape[0]-1)
        surrounding_pos.add((y_minus_1, x_minus_1))
        surrounding_pos.add((y_minus_1, x))
        surrounding_pos.add((y_minus_1, x_plus_1))
        surrounding_pos.add((y, x_minus_1))
        surrounding_pos.add((y, x))
        surrounding_pos.add((y, x_plus_1))
        surrounding_pos.add((y_plus_1, x_minus_1))
        surrounding_pos.add((y_plus_1, x))
        surrounding_pos.add((y_plus_1, x_plus_1))
        surrounding_pos.remove((y, x))
        return surrounding_pos
    
    def find_forkliftable_rolls(self, map):
        counter = 0
        forkliftable_pos = set()
        for y in range(map.shape[0]):
            for x in range(map.shape[1]):
                if map[y, x] == '@':
                    surr_pos = self.get_surroundings(y, x)
                    count_rolls = 0
                    for (sy, sx) in surr_pos:
                        if map[sy, sx] == '@':
                            count_rolls += 1
                    if count_rolls < 4:
                        counter += 1
                        forkliftable_pos.add((y, x))
        return counter, forkliftable_pos
    
    def update_map(self, map, forkliftable_pos):
        map = map.copy()
        for (y, x) in forkliftable_pos:
            map[y, x] = '.'
        return map

    def problem_1(self):
        res = 0
        res, _ = self.find_forkliftable_rolls(self.map)
        return res
    
    def problem_2(self):
        res = 0
        fun_2_map = self.map.copy()
        while True:
            # slow but it's fine... guess what? i dont have time
            n_forkliftable, forkliftable_pos = self.find_forkliftable_rolls(
                fun_2_map
            )
            if n_forkliftable > 0:
                res += n_forkliftable
                fun_2_map = self.update_map(fun_2_map, forkliftable_pos)
            else:
                break
        return res

    
if __name__ == '__main__':
    print(Day4())

