
def solve_part1(data):
    shifted = data[-1] + data[0:-1]
    both = zip(data, shifted)

    return sum(map(lambda pair: int(pair[0]) if pair[0] == pair[1] else 0, both))

def solve_part2(data):
    shifted = data[len(data)/2:] + data[:len(data)/2]
    both = zip(data, shifted)

    return sum(map(lambda pair: int(pair[0]) if pair[0] == pair[1] else 0, both))

#print solve_part1('91212129')
#print solve_part1(open('day1.input').read().strip())

#print solve_part2('12131415')
print solve_part2(open('day1.input').read().strip())
