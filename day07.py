import logging
from itertools import product


def to_input(lines):
    inp = []
    for line in lines:
        l, r = line.split(':')
        inp.append((int(l), [int(i) for i in r.split()]))
    return inp


def calculate(expected, vals, comb):
    res = vals[0]
    for val, op in zip(vals[1:], comb):
        if op == '*':
            res = res * val
        elif op == '+':
            res = res + val
        elif op == '|':
            res = int(str(res) + str(val))
        if res > expected:
            return 0
    return res


def solve(inp, part):
    operands = ['+', '*', '|'] if part == 2 else ['+', '*']
    tot = 0
    cnt = 0
    lines = len(inp)
    for expected, vals in inp:
        cnt += 1
        print(f"{cnt}/{lines}: {expected}: {vals}")
        combs = product(operands, repeat=len(vals) - 1)
        for comb in combs:
            res = calculate(expected, vals, comb)
            # print(expected, vals, comb, res, res == expected)
            if expected == res:
                tot += expected
                break
    return tot


def test1():
    lines = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".split('\n')
    inp = to_input(lines)
    print(inp)
    print("Part 1", solve(inp, 1) == 3749)
    print("Part 2", solve(inp, 2) == 11387)


def main():
    with open('data/aoc2024_day07.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    inp = to_input(lines)
    print("Part 1", solve(inp, 1))
    print("Part 2", solve(inp, 2))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
