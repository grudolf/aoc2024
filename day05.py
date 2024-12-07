import logging
from itertools import pairwise


def to_input(lines):
    rules, updates = set(), []
    for line in lines:
        if '|' in line:
            rules.add(line)
        elif ',' in line:
            updates.append([int(p) for p in line.split(',')])
    return rules, updates


def solve(rules, updates):
    tot, tot_fixed = 0, 0
    bad_pages = []
    for page_list in updates:
        ok = True
        for l, r in pairwise(page_list):
            if f"{r}|{l}" in rules:
                bad_pages.append(page_list)
                ok = False
                break
        if ok:
            tot += page_list[len(page_list) // 2]

    tot_fixed = 0
    for page_list in bad_pages:
        done = False
        while not done:
            done = True
            for i, (l, r) in enumerate(pairwise(page_list)):
                if f"{r}|{l}" in rules:
                    done = False
                    page_list[i], page_list[i + 1] = r, l
                    break
        tot_fixed += page_list[len(page_list) // 2]

    return tot, tot_fixed


def test1():
    lines = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".split('\n')
    rules, updates = to_input(lines)
    res1, res2 = solve(rules, updates)
    print("Part 1", res1 == 143)
    print("Part 2", res2 == 123)


def main():
    with open('data/aoc2024_day05.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    rules, updates = to_input(lines)
    res1, res2 = solve(rules, updates)
    print("Part 1", res1)
    print("Part 2", res2)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
