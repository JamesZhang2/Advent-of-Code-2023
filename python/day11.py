with open("input11.txt") as file:
    lines = [line.strip() for line in file.readlines()]

grid = []
for line in lines:
    grid.append([ch for ch in line])
    if '#' not in line:
        grid.append([ch for ch in line])

# print(len(grid))

new_grid = []

for r in range(len(grid)):
    new_grid.append([])

for c in range(len(grid[0])):
    found = False
    for r in range(len(grid)):
        if grid[r][c] == '#':
            found = True
            break
    if not found:
        for r in range(len(grid)):
            new_grid[r].append(".")
    for r in range(len(grid)):
        new_grid[r].append(grid[r][c])

pos = []
for r in range(len(new_grid)):
    for c in range(len(new_grid[0])):
        if new_grid[r][c] == '#':
            pos.append((r, c))


def dist(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])


sum = 0
for pt1 in pos:
    for pt2 in pos:
        sum += dist(pt1, pt2)

print(sum / 2)
