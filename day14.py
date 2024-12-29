import logging
import re
from dataclasses import dataclass


@dataclass
class Robot:
    start_x: int
    start_y: int
    v_x: int
    v_y: int

    def __repr__(self):
        return f"Robot(({self.start_x},{self.start_y}),({self.v_x},{self.v_y}))"


def to_input(lines):
    rpv = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'
    robots = []
    for line in lines:
        m = re.match(rpv, line)
        if m:
            robots.append(Robot(int(m[1]), int(m[2]), int(m[3]), int(m[4])))
    return robots


def animate_robots(robots, seconds, width, height):
    res = []
    for robot in robots:
        n = Robot((robot.start_x + seconds * robot.v_x) % width,
                  (robot.start_y + seconds * robot.v_y) % height,
                  robot.v_x, robot.v_y)
        res.append(n)
    return res


def calculate(robots, w, h, display=False):
    m = [[0 for _ in range(w)] for _ in range(h)]
    q = [0, 0, 0, 0]
    sum_x, sum_y = 0, 0
    for robot in robots:
        m[robot.start_y][robot.start_x] += 1
        if robot.start_x < (w - 1) / 2:
            if robot.start_y < (h - 1) / 2:
                q[0] += 1
            elif robot.start_y > (h - 1) / 2:
                q[1] += 1
        elif robot.start_x > (w - 1) / 2:
            if robot.start_y < (h - 1) / 2:
                q[2] += 1
            elif robot.start_y > (h - 1) / 2:
                q[3] += 1
        sum_x += robot.start_x
        sum_y += robot.start_y

    safety_factor = q[0] * q[1] * q[2] * q[3]

    avg_x, avg_y = sum_x / len(robots), sum_y / len(robots)
    var_x = sum((robot.start_x - avg_x) ** 2 for robot in robots) / len(robots)
    var_y = sum((robot.start_y - avg_y) ** 2 for robot in robots) / len(robots)

    if display:
        for r in m:
            print(''.join(str(x) if x > 0 else '.' for x in r))
        print(q)

        print(f"Safety factor: {safety_factor}")

        print(f"Variance: {var_x}, {var_y}")
    return safety_factor, var_x, var_y


def test1():
    lines = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3""".split('\n')
    w, h = 11, 7
    inp = to_input(lines)
    calculate(inp, w, h, display=True)
    # print(inp)
    robots = animate_robots(inp, 100, w, h)
    calculate(robots, w, h, display=True)


def main():
    with open('data/aoc2024_day14.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    w, h = 101, 103
    inp = to_input(lines)
    calculate(inp, w, h)
    # print(inp)
    robots = animate_robots(inp, 100, w, h)
    safety_factor, var_x, var_y = calculate(robots, w, h)
    print("Part 1, safety factor at 100 seconds = ", safety_factor)

    min_var_x, min_var_y = 100000, 100000
    egg = 0
    for i in range(9000):
        robots = animate_robots(inp, i, w, h)
        safety_factor, var_x, var_y = calculate(robots, w, h, display=False)
        if var_x <= min_var_x and var_y <= min_var_y:
            min_var_x, min_var_y = var_x, var_y
            egg = i
            # calculate(robots, w, h, display=True)
            print(f"Part 2, possible egg at {i} seconds, variance = {var_x}, {var_y}")

    if egg > 0:
        robots = animate_robots(inp, egg, w, h)
        calculate(robots, w, h, display=True)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    logging.basicConfig(level=logging.INFO)
    main()
