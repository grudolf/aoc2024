import logging
from itertools import pairwise


def safe(nums):
    direction = 1 if nums[1] > nums[0] else -1
    for c, n in pairwise(nums):
        if direction == 1:
            if n - c < 1 or n - c > 3:
                return False
        else:
            if c - n < 1 or c - n > 3:
                return False
    return True


def part1(lines):
    cnt = 0
    for line in lines:
        nums = [int(i) for i in line.split()]
        if safe(nums):
            cnt += 1
    return cnt


def part2(lines):
    cnt = 0
    for line in lines:
        nums = [int(i) for i in line.split()]
        if safe(nums):
            cnt += 1
        else:
            for i in range(len(nums)):
                dampened = nums.copy()
                del dampened[i]
                if safe(dampened):
                    cnt += 1
                    break
    return cnt


def test1():
    lines = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".split('\n')
    print("Part 1", part1(lines) == 2)
    print("Part 2", part2(lines) == 4)


def main():
    with open('data/aoc2024_day02.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    print("Part 1", part1(lines))
    print("Part 2", part2(lines))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
