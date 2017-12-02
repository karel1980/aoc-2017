
def read_input():
    return [ [ int(item) for item in line.strip().split('\t') ] for line in open('day2.input').readlines() ]

def solve_part1(sheet):
    return sum([ max(row) - min(row) for row in sheet ])

def solve_part2(sheet):
    return sum([ find_integer_division(row) for row in sheet ])

def find_integer_division(row):
    for i in range(len(row)):
        for j in range(len(row)):
            if i==j: continue
            if int(row[i] / row[j])*row[j] == row[i]:
                return row[i] / row[j]
    raise Exception('should not happen')

#print solve_part1(read_input())
print solve_part2(read_input())
