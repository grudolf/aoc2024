import logging

DIRECTIONS = [
    # 0:symbol, 1:delta, 2:index_on_turn
    ['^', (-1, 0), 1],
    ['>', (0, 1), 2],
    ['V', (1, 0), 3],
    ['<', (0, -1), 0],
]


def move(location, direction):
    delta_row, delta_col = DIRECTIONS[direction][1]
    return location[0] + delta_row, location[1] + delta_col


def is_out_of_bounds(target_location, map_height, map_width):
    if target_location[0] < 0 or target_location[0] >= map_height:
        return True
    if target_location[1] < 0 or target_location[1] >= map_width:
        return True
    return False


def is_occupied(lab_map, location):
    return lab_map[location[0]][location[1]] == '#'


def already_visited(lab_map, location):
    return lab_map[location[0]][location[1]] == 'X'


def mark_location(lab_map, location):
    lab_map[location[0]][location[1]] = 'X'


def add_obstacle(lab_map, location):
    lab_map[location[0]][location[1]] = '#'


def remove_obstacle(lab_map, location):
    lab_map[location[0]][location[1]] = '.'


def draw_map(lab_map, location):
    [print(''.join(r)) for r in lab_map]
    print(location)


def part1(lab_map, location, direction):
    guards_path = []
    map_height, map_width = len(lab_map), len(lab_map[0])
    steps = 1
    mark_location(lab_map, location)
    while True:
        target_location = move(location, direction)
        if is_out_of_bounds(target_location, map_height, map_width):
            break
        if is_occupied(lab_map, target_location):
            direction = DIRECTIONS[direction][2]
        else:
            location = target_location
            if not already_visited(lab_map, location):
                steps += 1
            mark_location(lab_map, location)
            # draw_map(lab_map, location)
            guards_path.append(location)
    return steps, guards_path


def part2(lab_map, start_location, start_direction, guards_path):
    map_height, map_width = len(lab_map), len(lab_map[0])
    cnt = 0
    for obstacle_location in set(guards_path):
        add_obstacle(lab_map, obstacle_location)
        visited_location_direction = set()
        location = start_location
        direction = start_direction
        while True:
            target_location = move(location, direction)
            if is_out_of_bounds(target_location, map_height, map_width):
                break
            if is_occupied(lab_map, target_location):
                direction = DIRECTIONS[direction][2]
            else:
                location = target_location
                key = (location[0], location[1], direction)
                if key in visited_location_direction:
                    cnt += 1
                    print(f"Obstacle {cnt} at {obstacle_location}")
                    break
                visited_location_direction.add(key)
                # draw_map(lab_map, location)
        remove_obstacle(lab_map, obstacle_location)
    return cnt


def to_input(lines):
    directions = [dd[0] for dd in DIRECTIONS]
    lab_map = []
    location, direction = None, None
    for r, line in enumerate(lines):
        row = list(line)
        lab_map.append(row)
        for d in directions:
            if d in row:
                c = row.index(d)
                direction = directions.index(d)
                location = (r, c)
                break
    draw_map(lab_map, location)
    print(location, direction)
    return lab_map, location, direction


def test1():
    lines = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".split('\n')
    lab_map, location, direction = to_input(lines)
    steps, guards_path = part1(lab_map, location, direction)
    print("Part 1", steps, steps == 41)

    lab_map, location, direction = to_input(lines)
    results = part2(lab_map, location, direction, guards_path)
    print("Part 2", results, results == 6)


def main():
    with open('data/aoc2024_day06.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    lab_map, location, direction = to_input(lines)
    steps, guards_path = part1(lab_map, location, direction)
    print("Part 1", steps)

    lab_map, location, direction = to_input(lines)
    results = part2(lab_map, location, direction, guards_path)
    print("Part 2", results)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
