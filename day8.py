
class Instruction:
    def __init__(self, reg, op, op_arg, dummy_if, test_reg, test, test_arg):
        self.reg = reg
        self.op = op
        self.op_arg = int(op_arg)
        self.test_reg = test_reg
        self.test = test
        self.test_arg = int(test_arg)

    def execute(self, registers):
        registers.setdefault(self.reg, 0)
        registers.setdefault(self.test_reg, 0)
        if self.eval_test(registers):
            if self.op == 'dec':
                registers[self.reg] -= self.op_arg
            else:
                registers[self.reg] += self.op_arg

    def eval_test(self, registers):
        if self.test == '==':
            return registers[self.test_reg] == self.test_arg
        elif self.test == '<=':
            return registers[self.test_reg] <= self.test_arg
        elif self.test == '<':
            return registers[self.test_reg] < self.test_arg
        elif self.test == '>':
            return registers[self.test_reg] > self.test_arg
        elif self.test == '>=':
            return registers[self.test_reg] >= self.test_arg
        elif self.test == '!=':
            return registers[self.test_reg] != self.test_arg
        else:
            raise Exception('unknown test : %s'%(self.test,))

def read_input():
    return [ parse_line(l.strip()) for l in open('day8.input').readlines() ]

def parse_line(line):
    parts = line.split(" ")
    return Instruction(*parts)

def solve_part1(instructions):
    registers = dict()
    for i in instructions:
        i.execute(registers)

    return max(registers.values())

def solve_part2(instructions):
    max_value = 0
    registers = dict()
    for i in instructions:
        i.execute(registers)
        max_value = max(max_value,max(registers.values()))
    return max_value

print solve_part1(read_input())
print solve_part2(read_input())
