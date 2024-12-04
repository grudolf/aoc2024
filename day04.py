import logging


def find_match(arr, srch, r, c, dr, dc, res):
    if arr[r][c] == srch[0] and arr[r + dr][c + dc] == srch[1] and arr[r + 2 * dr][c + 2 * dc] == srch[2] and \
            arr[r + 3 * dr][c + 3 * dc] == srch[3]:
        res[r][c] = srch[0]
        res[r + dr][c + dc] = srch[1]
        res[r + 2 * dr][c + 2 * dc] = srch[2]
        res[r + 3 * dr][c + 3 * dc] = srch[3]
        print(r, c)
        return 1
    return 0


def part1(arr):
    srch = ['X', 'M', 'A', 'S']
    l = len(srch)
    h = len(arr)
    w = len(arr[0])

    res = [['.' for i in range(w)] for j in range(h)]
    cnt = 0
    for r in range(0, h):
        logging.debug(arr[r])
        for c in range(0, w):
            # horizontal
            if c <= w - l:
                cnt += find_match(arr, srch, r, c, 0, 1, res)
            if c >= l - 1:
                cnt += find_match(arr, srch, r, c, 0, -1, res)
            # vertical
            if r <= h - l:
                cnt += find_match(arr, srch, r, c, 1, 0, res)
            if r >= l - 1:
                cnt += find_match(arr, srch, r, c, -1, 0, res)
            # diagonal
            if c <= w - l and r <= h - l:
                cnt += find_match(arr, srch, r, c, 1, 1, res)
            if c >= l - 1 and r <= h - l:
                cnt += find_match(arr, srch, r, c, 1, -1, res)
            if c <= w - l and r >= l - 1:
                cnt += find_match(arr, srch, r, c, -1, 1, res)
            if c >= l - 1 and r >= l - 1:
                cnt += find_match(arr, srch, r, c, -1, -1, res)
    print(cnt)
    [print(''.join(r)) for r in res]
    return cnt


def find_x(arr, r, c, res):
    if arr[r][c] == 'A':
        tlbr = arr[r - 1][c - 1] + arr[r + 1][c + 1]
        bltr = arr[r + 1][c - 1] + arr[r - 1][c + 1]
        if (tlbr == 'MS' or tlbr == 'SM') and (bltr == 'MS' or bltr == 'SM'):
            res[r][c] = arr[r][c]
            res[r - 1][c - 1] = arr[r - 1][c - 1]
            res[r + 1][c + 1] = arr[r + 1][c + 1]
            res[r + 1][c - 1] = arr[r + 1][c - 1]
            res[r - 1][c + 1] = arr[r - 1][c + 1]
            # print(r, c)
            return 1
    return 0


def part2(arr):
    h = len(arr)
    w = len(arr[0])

    res = [['.' for i in range(w)] for j in range(h)]
    cnt = 0
    for r in range(1, h - 1):
        for c in range(1, w - 1):
            cnt += find_x(arr, r, c, res)
    print(cnt)
    [print(''.join(r)) for r in res]
    return cnt


def to_array(lines):
    return [list(l) for l in lines]


def test1():
    lines = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split('\n')
    arr = to_array(lines)
    print("Part 1", part1(arr) == 18)
    print("Part 2", part2(arr) == 9)


def main():
    with open('data/aoc2024_day04.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    arr = to_array(lines)
    print("Part 1", part1(arr))
    print("Part 2", part2(arr))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
