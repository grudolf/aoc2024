import logging


def part1(lines):
    left, right = [], []
    for l, r in [line.split() for line in lines]:
        left.append(int(l))
        right.append(int(r))
    left.sort()
    right.sort()
    diff = 0
    for l, r in zip(left, right):
        diff += abs(l - r)
    return diff


def part2(lines):
    left, right_count = [], {}
    for l, r in [line.split() for line in lines]:
        left.append(l)
        right_count[r] = right_count.get(r, 0) + 1
    total = 0
    for l in left:
        similarity = int(l) * right_count.get(l, 0)
        total += similarity
    return total


def test1():
    lines = """3   4
4   3
2   5
1   3
3   9
3   3""".split('\n')
    print("Part 1", part1(lines) == 11)
    print("Part 2", part2(lines) == 31)


def main():
    with open('data/aoc2024_day01.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    print("Part 1", part1(lines))
    print("Part 2", part2(lines))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
