
IN_GROUP = 2
IN_GARBAGE = 3
ESCAPED_GARBAGE = 4

def read_input():
    return open('day9.input').read()

def solve_all(stream):
    score = 0
    depth = 0
    garbage_count = 0
    mode = IN_GROUP # IN_GROUP, IN_GARBAGE, ESCAPED_GARBAGE
    for i in range(len(stream)):
        char = stream[i]
        if mode == IN_GROUP:
            if char == "{":
                depth += 1
                score += depth
            elif char == "}":
                depth -= 1
            elif char == "<":
                mode = IN_GARBAGE
        elif mode == IN_GARBAGE:
            if char == ">":
                mode = IN_GROUP
            elif char == "!":
                mode = ESCAPED_GARBAGE
            else:
                garbage_count += 1
        elif mode == ESCAPED_GARBAGE:
            mode = IN_GARBAGE

    print score, garbage_count

solve_all(read_input())
