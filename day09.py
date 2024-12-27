import logging


def to_disk(diskmap):
    if len(diskmap) % 2 != 0:
        diskmap += '0'
    disk_disp = ''
    disk = []
    for i, (fi, sp) in enumerate(zip(*[iter(diskmap)] * 2)):
        print(i, fi, sp)
        disk_disp += chr(48 + i % 10) * int(fi) + '.' * int(sp)
        disk.append((i, int(fi), int(sp)))
        # print(disk)
    print(f"Disk map: {len(disk)}, occupied: {len(disk_disp)}")
    print(disk_disp)
    return disk


def disp_disk(disk):
    disk_disp = ''
    for i, (ind, len, avail) in enumerate(disk):
        disk_disp += chr(48 + i % 10) * len + '.' * avail
    print(disk_disp)


def optimize_1(disk):
    new_disk = []
    l, r = 0, len(disk) - 1
    while l < r + 1:
        left = disk[l]
        ind_l, len_l, avail_l = left
        if len_l > 0:
            new_disk.extend([ind_l] * len_l)
            disk[l] = (ind_l, 0, avail_l)
            continue

        if avail_l == 0:
            l += 1
            continue

        right = disk[r]
        ind_r, len_r, avail_r = right
        if len_r > 0:
            c = min(avail_l, len_r)
            new_disk.extend([ind_r] * c)
            disk[l] = (ind_l, len_l, avail_l - c)
            disk[r] = (ind_r, len_r - c, avail_r)
        else:
            r -= 1
    print(l, r, ''.join(chr(48 + e % 10) for e in new_disk))

    tot = 0
    for i, c in enumerate(new_disk):
        tot += i * c
    return tot


def optimize_2(disk):
    print(disk)
    #disp_disk(disk)
    r = len(disk) - 1
    processed_files = set()
    while r > 0:
        ind_r, len_r, avail_r = disk[r]
        if ind_r in processed_files:
            r -= 1
            continue
        processed_files.add(ind_r)
        moved = False
        for i in range(r):
            ind_l, len_l, avail_l = disk[i]
            if 0 < len_r <= avail_l:
                disk[i] = (ind_l, len_l, 0)  # decrease avail free space on left from avail_l to 0
                disk.insert(i + 1, (ind_r, len_r, avail_l - len_r))  # insert new file on left after existing, calculate new avail free space
                ind_p, len_p, avail_p = disk[r]
                disk[r] = (ind_p, len_p, avail_p + len_r + avail_r)  # increase free space of previous node on the right
                disk.pop(r + 1)
                # print(disk)
                moved = True
                break
        # r -= 1
        if not moved:
            r -= 1

    print(disk)
    #disp_disk(disk)

    block_offset = 0
    checksum = 0
    for (ind_r, len_r, avail_r) in disk:
        for i in range(len_r):
            checksum += ind_r * block_offset
            block_offset += 1
        block_offset += avail_r
    print(block_offset, checksum)
    return checksum


def test1():
    lines = """2333133121414131402""".split('\n')
    diskmap = lines[0]
    disk = to_disk(diskmap)
    res = optimize_1(disk)
    print("Part 1", res, res == 1928)

    disk = to_disk(diskmap)
    res = optimize_2(disk)
    print("Part 2", res, res == 2858)


def main():
    with open('data/aoc2024_day09.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    diskmap = lines[0]
    disk = to_disk(diskmap)
    res = optimize_1(disk)
    print("Part 1", res)  # 6332189866718

    disk = to_disk(diskmap)
    res = optimize_2(disk)  # 50004, 45361
    print("Part 2", res)  # 6353648390778


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
