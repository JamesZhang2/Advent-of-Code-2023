with open("input5.txt") as file:
    lines = [line.strip() for line in file.readlines()]
lines[0] = lines[0][(lines[0].find(":") + 2):]
seeds = [int(num) for num in lines[0].split(" ")]

maps = []
cur_map = []
for l in range(2, len(lines)):
    if lines[l] == "":
        maps.append(cur_map.copy())
        cur_map = []
        continue
    if lines[l][0].isdigit():
        nums = [int(num) for num in lines[l].split()]
        cur_map.append((nums[0], nums[1], nums[2]))
maps.append(cur_map)


def get_loc(maps, seed):
    key = seed
    for map in maps:
        for (dest, src, rng) in map:
            if 0 <= key - src < rng:
                key = dest + (key - src)
                break
    return key


min_loc = 1e20
for seed in seeds:
    loc = get_loc(maps, seed)
    min_loc = min(min_loc, loc)
print(min_loc)


# Too slow!
# min_loc_2 = 1e20
# for i in range(0, len(seeds), 2):
#     start = seeds[i]
#     for j in range(start, start + seeds[i + 1]):
#         loc = get_loc(maps, j)
#         min_loc = min(min_loc, loc)
# print(min_loc_2)

def get_min_loc_range(maps, seed_start, seed_end):  # inclusive
    # print(len(maps), seed_start, seed_end)
    assert seed_start <= seed_end
    if len(maps) == 0:
        return seed_start
    cur = seed_start
    min_loc = 1e20
    while cur <= seed_end:
        # print(f"cur: {cur}, seed_end: {seed_end}, elts left: {seed_end - cur + 1}, len(maps): {len(maps)}")
        found = False
        for (dest, src, rng) in maps[0]:
            if 0 <= cur - src < rng:
                shift = dest - src
                min_loc = min(min_loc,
                              get_min_loc_range(maps[1:], cur + shift, min(seed_end + shift, src + rng - 1 + shift)))
                cur = min(src + rng, seed_end + 1)
                found = True
                break
        # Key not found
        if not found:
            min_src = 1e21  # smallest src bigger than key
            for (dest, src, rng) in maps[0]:
                if src > cur:
                    min_src = min(min_src, src)
            if min_src == 1e21:
                # every src is smaller than cur
                min_loc = min(min_loc, get_min_loc_range(maps[1:], cur, seed_end))
                cur = seed_end + 1
            else:
                min_loc = min(min_loc, get_min_loc_range(maps[1:], cur, min(seed_end, min_src - 1)))
                cur = min_src
    return min_loc


min_loc_2 = 1e20
for i in range(0, len(seeds), 2):
    min_loc_2 = min(min_loc_2, get_min_loc_range(maps, seeds[i], seeds[i] + seeds[i + 1] - 1))
print(min_loc_2)
