import logging


def to_input(lines):
    topo_map = {}
    start_locations = []
    end_locations = []
    height = len(lines)
    width = len(lines[0])
    for r in range(height):
        for c in range(width):
            h = int(lines[r][c])
            k = (c, r)

            if h == 0:
                start_locations.append(k)
            elif h == 9:
                end_locations.append(k)

            neighbors = []
            if r > 0 and int(lines[r - 1][c]) - h == 1:
                neighbors.append((c, r - 1))
            if r < height - 1 and int(lines[r + 1][c]) - h == 1:
                neighbors.append((c, r + 1))
            if c > 0 and int(lines[r][c - 1]) - h == 1:
                neighbors.append((c - 1, r))
            if c < width - 1 and int(lines[r][c + 1]) - h == 1:
                neighbors.append((c + 1, r))
            topo_map[k] = (h, neighbors)
            # print(k, h, neighbors)
    #    pprint(topo_map)
    print("Start: ", start_locations)
    print("End: ", end_locations)
    return start_locations, end_locations, topo_map


def solve(start_locations, end_locations, topo_map, mode):
    tot = 0
    for s_location in start_locations:
        cnt = 0
        for e_location in end_locations:
            path = bfs2(s_location, e_location, topo_map, mode)
            cnt += path
            # if path:
            #     print(s_location, e_location, path)
        tot += cnt
    return tot


# modified bfs from the internets - no loops, no history, no memory
def bfs2(start_location, end_location, graph, mode):
    queue = [start_location]
    result_cnt = 0

    while queue:
        location = queue.pop(0)
        if location == end_location:
            if mode == 1:
                return 1  # path was found
            result_cnt += 1
            continue
        for current_neighbour in graph[location][1]:
            queue.append(current_neighbour)
    return result_cnt  # number of found paths


def test1():
    lines = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".split('\n')
    start_locations, end_locations, topo_map = to_input(lines)
    res = solve(start_locations, end_locations, topo_map, 1)
    print("Part 1", res, res == 36)
    res = solve(start_locations, end_locations, topo_map, 2)
    print("Part 2", res, res == 81)


def main():
    with open('data/aoc2024_day10.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    start_locations, end_locations, topo_map = to_input(lines)
    res = solve(start_locations, end_locations, topo_map, 1)
    print("Part 1", res)  # 514
    res = solve(start_locations, end_locations, topo_map, 2)
    print("Part 2", res)  # 1162


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
