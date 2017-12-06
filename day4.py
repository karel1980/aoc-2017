from collections import Counter

def read_input():
    return [l.strip().split(" ") for l in open('day4.input').readlines()]

def solve_part1(lines):
    result = 0
    for l in lines:
        if is_valid_passphrase(l):
            result += 1
    return result

def solve_part2(lines):
    result = 0
    for l in lines:
        if is_valid_passphrase2(l):
            result += 1
    return result

def is_valid_passphrase(l):
    c = Counter(l)

    return c.most_common(1)[0][1] == 1

def is_valid_passphrase2(l):
    return is_valid_passphrase(l) and no_anagrams_in(l)

def no_anagrams_in(l):
    l = [ "".join(sorted(word)) for word in l ]
    return is_valid_passphrase(l)

#print solve_part1(read_input())
print solve_part2(read_input())
