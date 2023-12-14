with open("input14.txt") as file:
    lines = [line.strip() for line in file.readlines()]

grid = []
for line in lines:
    grid.append([ch for ch in line])

total = 0
for c in range(len(grid[0])):
    weight = len(grid)
    for r in range(len(grid)):
        if grid[r][c] == "#":
            weight = len(grid) - r - 1
        if grid[r][c] == "O":
            total += weight
            weight -= 1

print(total)