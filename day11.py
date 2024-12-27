import functools
import logging


def to_stones(s):
    return [x for x in s.split()]


def blink(stones):
    res = []
    for stone in stones:
        res.extend(blink_stone(stone))
    return res


def blink_stone(stone):
    if stone == '0':
        return ['1']
    elif len(stone) % 2 == 0:
        m = len(stone) // 2
        left, right = stone[:m], stone[m:].lstrip('0')
        return [left, right if right != '' else '0']
    else:
        return [str(int(stone) * 2024)]


@functools.lru_cache(maxsize=None)
def count_stones(stone, depth):
    if depth == 0:
        return 1
    else:
        # print(stone, depth)
        if stone == '0':
            return count_stones('1', depth - 1)
        elif len(stone) % 2 == 0:
            m = len(stone) // 2
            left, right = stone[:m], stone[m:].lstrip('0')
            return count_stones(left, depth - 1) + count_stones(right if right != '' else '0', depth - 1)
        else:
            return count_stones(str(int(stone) * 2024), depth - 1)


def test1():
    lines = """125 17""".split('\n')
    stones = to_stones(lines[0])
    stones = blink(stones)
    print(stones, stones == to_stones('253000 1 7'))
    stones = blink(stones)
    print(stones, stones == to_stones('253 0 2024 14168'))
    stones = blink(stones)
    print(stones, stones == to_stones('512072 1 20 24 28676032'))
    stones = blink(stones)
    print(stones, stones == to_stones('512 72 2024 2 0 2 4 2867 6032'))
    stones = blink(stones)
    print(stones, stones == to_stones('1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32'))
    stones = blink(stones)
    print(stones, stones == to_stones('2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2'))
    print(len(stones), len(stones) == 22)


def test2():
    cnt = count_stones('125', 6)
    cnt += count_stones('17', 6)
    print(cnt, cnt == 22)


def main():
    with open('data/aoc2024_day11.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    stones = to_stones(lines[0])
    for i in range(25):
        stones = blink(stones)
        print(i, len(stones))
    print("Part 1", len(stones))  # 239714

    cnt = 0
    stones = to_stones(lines[0])
    for stone in stones:
        cnt += count_stones(stone, 75)
    print("Part 2", cnt)  # 284973560658514
    print(count_stones.cache_info())


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    test2()
    logging.basicConfig(level=logging.INFO)
    main()
