with open("input11.txt") as file:
    lines = [line.strip() for line in file.readlines()]

grid = []
empty_rows = set()
empty_cols = set()
expansion = 1000000
for i in range(len(lines)):
    line = lines[i]
    grid.append([ch for ch in line])
    if '#' not in line:
        empty_rows.add(i)

for c in range(len(grid[0])):
    found = False
    for r in range(len(grid)):
        if grid[r][c] == '#':
            found = True
            break
    if not found:
        empty_cols.add(c)

pos = []
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == '#':
            pos.append((r, c))


def dist(pt1, pt2, expansion):
    d = 0
    r_min = min(pt1[0], pt2[0])
    r_max = max(pt1[0], pt2[0])
    for r in range(r_min, r_max):
        if r in empty_rows:
            d += expansion
        else:
            d += 1
    c_min = min(pt1[1], pt2[1])
    c_max = max(pt1[1], pt2[1])
    for c in range(c_min, c_max):
        if c in empty_cols:
            d += expansion
        else:
            d += 1
    return d


sum = 0
for pt1 in pos:
    for pt2 in pos:
        sum += dist(pt1, pt2, expansion=expansion)

print(sum / 2)
