import logging
import re


def part1(line):
    score = 0
    pat = r'mul\((\d+),(\d+)\)'
    results = re.findall(pat, line)
    for (a, b) in results:
        score += int(a) * int(b)
    return score


def part1a(line):
    return sum([(int(a) * int(b)) for (a, b) in re.findall(r'mul\((\d+),(\d+)\)', line)])


def part2(lines):
    # get everything between do() and don't() (or EOL)
    results = ''.join(re.findall(r'do\(\)(.*?)(?=don\'t\(\)|$)', 'do()' + lines))
    return part1(results)


def test1():
    line = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    print("Part 1", part1(line) == 161)
    line = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    print("Part 2", part2(line) == 48)


def main():
    with open('data/aoc2024_day03.txt', 'rt') as f:
        line = ''.join([line.rstrip('\n') for line in f])  # remove CRs and rejoin into a single string
    print("Part 1", part1(line))  # 180233229
    print("Part 2", part2(line))  # 106266128 is too high, but 95411583 is ok -


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
