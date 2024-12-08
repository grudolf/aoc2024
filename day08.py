import logging
from itertools import permutations
from pprint import pprint


def to_input(lines):
    antennas = {}
    r, c = 0, 0
    for r, line in enumerate(lines):
        row = list(line)
        for c, antenna in enumerate(row):
            if antenna != ".":
                if not antenna in antennas:
                    antennas[antenna] = []
                antennas[antenna].append((r, c))
    width = c + 1
    height = r + 1
    pprint(antennas)
    print(f"Height: {height}, width: {width}")
    return antennas, width, height


def solve(antennas, width, height, part):
    antinodes = set()   # unique antinodes locations
    for symbol, locations in antennas.items():
        #print(symbol, list(permutations(locations, 2)))
        if part == 2 and len(locations) > 1:
            antinodes.update(locations)             # part2: "some of the new antinodes will occur at the position of each antenna"?
        for a1, a2 in permutations(locations, 2):
            dr, dc = a2[0] - a1[0], a2[1] - a1[1]   # rows, columns diff between locations
            nr, nc = a2[0] + dr, a2[1] + dc         # place on the other side
            while True:
                if 0 <= nr < height and 0 <= nc < width:    # inside?
                    antinodes.add((nr, nc))
                    if part == 2:                   # continue moving in part2
                        nr += dr
                        nc += dc
                        continue
                break
    tot = len(antinodes)
    return tot


def test1():
    lines = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""".split('\n')
    antennas, width, height = to_input(lines)
    res = solve(antennas, width, height, 1)
    print("Part 1", res, res == 14)
    res = solve(antennas, width, height, 2)
    print("Part 2", res, res == 34)


def main():
    with open('data/aoc2024_day08.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    antennas, width, height = to_input(lines)
    print("Part 1", solve(antennas, width, height, 1))  # 24650 is correct for day07.txt...
    print("Part 2", solve(antennas, width, height, 2))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
