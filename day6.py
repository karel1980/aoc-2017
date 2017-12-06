
def read_input():
    return [ int(part) for part in open('day6.input').read().strip().split('\t') ]

def solve_part1(banks):
    seen = set()

    while tuple(banks) not in seen:
        seen.add(tuple(banks))
        redistribute(banks)

    return len(seen)

def solve_part2(banks):
    seen_first = dict()

    n = 1
    while tuple(banks) not in seen_first:
        seen_first[tuple(banks)] = n
        redistribute(banks)
        n += 1

    return n - seen_first[tuple(banks)]

def redistribute(banks):
    largest_idx = banks.index(max(banks))
    value = banks[largest_idx]

    banks[largest_idx] = 0

    q = value / len(banks)
    r = value - q * len(banks)

    for i in range(len(banks)):
        banks[(largest_idx + 1 + i) % len(banks)] += q+1 if i < r else q

#print solve_part1(read_input())
print solve_part2(read_input())
