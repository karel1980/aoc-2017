
def read_input():
    return [ int(l.strip()) for l in open('day5.input').readlines() ]

def solve_part1(l):
    pos = 0

    jumps = 0
    while pos >= 0 and pos < len(l):
        pos = increment_and_jump(l, pos)
        jumps += 1

    return jumps

def increment_and_jump(l, pos):
    nextpos = pos + l[pos]
    l[pos] += 1

    return nextpos

def solve_part2(l):
    pos = 0

    jumps = 0
    while pos >= 0 and pos < len(l):
        pos = increment_and_jump2(l, pos)
        jumps += 1

    return jumps

def increment_and_jump2(l, pos):
    offset = l[pos]
    nextpos = pos + offset

    if offset >= 3: l[pos] -= 1
    else: l[pos] += 1

    return nextpos

#print solve_part1(read_input())
print solve_part2(read_input())
