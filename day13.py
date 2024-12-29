import logging
import re

from ortools.sat.python import cp_model


def to_input(lines):
    re_button = r'Button (\w): X\+(\d+), Y\+(\d+)'
    re_prize = r'Prize: X=(\d+), Y=(\d+)'
    res = []
    ax = ay = bx = by = None
    for line in lines:
        if line.startswith("Button"):
            m = re.match(re_button, line)
            if m[1] == 'A':
                ax, ay = int(m[2]), int(m[3])
            elif m[1] == 'B':
                bx, by = int(m[2]), int(m[3])
        elif line.startswith("Prize"):
            m = re.match(re_prize, line)
            px, py = int(m[1]), int(m[2])
            res.append((ax, ay, bx, by, px, py))
            ax = ay = bx = by = None
    print(res)
    return res


def evaluate_games(inp, part):
    solver = cp_model.CpSolver()
    tokens = 0
    for i, (ax, ay, bx, by, px, py) in enumerate(inp):
        if part == 2:
            px += 10000000000000
            py += 10000000000000
            move_limit = 10000000000000
        else:
            move_limit = 100
        model = cp_model.CpModel()
        a = model.NewIntVar(0, move_limit, 'a')
        b = model.NewIntVar(0, move_limit, 'b')
        model.Add(a * ax + b * bx == px)
        model.Add(a * ay + b * by == py)
        model.Minimize(3 * a + b)
        status = solver.Solve(model)
        status_name = solver.StatusName(status)
        if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
            print(f"Game {i + 1}: {solver.value(a)} {solver.value(b)}")
            tokens += 3 * solver.value(a) + solver.value(b)
        else:
            print(f"Game {i + 1}: No solution, status {status} {status_name}")
    return tokens


def test1():
    lines = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""".split('\n')
    inp = to_input(lines)
    res = evaluate_games(inp, 1)
    print("Test 1", res, res == 480)
    res = evaluate_games(inp, 2)
    print("Test 2", res, res == 0)


def main():
    with open('data/aoc2024_day13.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    inp = to_input(lines)
    res = evaluate_games(inp, 1)
    print("Part 1", res)  # 36758
    res = evaluate_games(inp, 2)
    print("Part 2", res)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    logging.basicConfig(level=logging.INFO)
    main()
