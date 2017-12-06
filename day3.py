import math

def read_input():
    return int(open('day3.input').read().strip())

def solve_part1(num):
    x, y = get_position_of_nth_spiral_element(num)
    return abs(x) + abs(y)

def solve_part2(num):
    grid = Grid()
    grid.write(0, 0, 1)

    n = 2
    while True:
        x, y = get_position_of_nth_spiral_element(n)

        mysum = grid.get_sum_of_adjacent_elements(x, y)
        if mysum > num:
            return mysum

        grid.write(x, y, mysum)

        n = n + 1

class Grid:
    def __init__(self):
        self.storage = {}

    def read(self, x, y):
        return self.storage.setdefault((x,y), 0)

    def write(self, x, y, value):
        self.storage[(x,y)] = value

    def get_sum_of_adjacent_elements(self, x, y):
        result = 0 - self.read(x, y)
        for i in range(-1, 2):
            for j in range(-1, 2):
                result = result + self.read(x+i, y+j)
    
        return result

def get_position_of_nth_spiral_element(num):
    if num == 0: raise Exception('invalid position')
    if num == 1: return 0, 0
    # lower right corner contains square roots of odd number
    lower_right_sqrt = int(math.sqrt(num))
    lower_right_sqrt = lower_right_sqrt - 1 if lower_right_sqrt%2 == 0 else lower_right_sqrt

    prev_corner = lower_right_sqrt ** 2
    next_corner = (lower_right_sqrt + 2) ** 2

    if num == prev_corner:
        x = lower_right_sqrt / 2
        y = -x
    else:
        # next loop starts right of prev_corner (e.g. at value 5, 10, 37, ...)
        segment_length = (next_corner - prev_corner) / 4
        offset = num - prev_corner - 1
        segment = offset / segment_length
        segment_offset = offset - segment * segment_length

        d = lower_right_sqrt / 2 # == x and y value of prev_corner
        if segment == 0:
            x,y = d + 1, segment_offset - d
        elif segment == 1:
            x,y = d - segment_offset, d + 1
        elif segment == 2:
            x,y = -d - 1, d - segment_offset
        elif segment == 3:
            x,y = segment_offset - d, -d - 1
    return x, y

#print solve_part1(read_input())
print solve_part2(read_input())
