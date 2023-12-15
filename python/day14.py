with open("input14.txt") as file:
    lines = [line.strip() for line in file.readlines()]

grid = []
for line in lines:
    grid.append([ch for ch in line])


def get_load(grid):
    total = 0
    for c in range(len(grid[0])):
        for r in range(len(grid)):
            if grid[r][c] == 'O':
                total += len(grid) - r
    return total

def get_deep_copy(grid):
    grid_copy = []
    for row in grid:
        row_copy = []
        for cell in row:
            row_copy.append(cell)
        grid_copy.append(row_copy)
    return grid_copy

def push(grid, dir):
    grid_copy = get_deep_copy(grid)
    if dir == 'N':
        for c in range(len(grid[0])):
            next_circ = 0
            for r in range(len(grid)):
                if grid[r][c] == 'O':
                    grid_copy[r][c] = '.'
                    grid_copy[next_circ][c] = 'O'
                    next_circ += 1
                elif grid[r][c] == '#':
                    next_circ = r + 1
    elif dir == 'S':
        for c in range(len(grid[0])):
            next_circ = len(grid) - 1
            for r in range(len(grid) - 1, -1, -1):
                if grid[r][c] == 'O':
                    grid_copy[r][c] = '.'
                    grid_copy[next_circ][c] = 'O'
                    next_circ -= 1
                elif grid[r][c] == '#':
                    next_circ = r - 1
    elif dir == 'W':
        for r in range(len(grid)):
            next_circ = 0
            for c in range(len(grid[0])):
                if grid[r][c] == 'O':
                    grid_copy[r][c] = '.'
                    grid_copy[r][next_circ] = 'O'
                    next_circ += 1
                elif grid[r][c] == '#':
                    next_circ = c + 1
    elif dir == 'E':
        for r in range(len(grid)):
            next_circ = len(grid[0]) - 1
            for c in range(len(grid[0]) - 1, -1, -1):
                if grid[r][c] == 'O':
                    grid_copy[r][c] = '.'
                    grid_copy[r][next_circ] = 'O'
                    next_circ -= 1
                elif grid[r][c] == '#':
                    next_circ = c - 1
    return grid_copy

def grid_to_string(grid):
    s = ""
    for row in grid:
        s += "".join(row) + "\n"
    return s

# Part 1

pushed_north = push(grid, 'N')
print(f"Part 1 answer: {get_load(pushed_north)}")

# Part 2

grids = {}
grids[grid_to_string(grid)] = 0
cycles = 0
period = -1
start = -1
while True:
    # We hope it will eventually get into a cycle
    grid = push(grid, 'N')
    grid = push(grid, 'W')
    grid = push(grid, 'S')
    grid = push(grid, 'E')
    cycles += 1
    cur_key = grid_to_string(grid)
    if cur_key in grids:
        print(f"Grid after {cycles} cycles is the same as grid after {grids[cur_key]} cycles")
        period = cycles - grids[cur_key]
        print(f"Period = {period}")
        break
    else:
        grids[grid_to_string(grid)] = cycles

remaining = (1000000000 - cycles) % period
print(f"Remaining: {remaining}")

for i in range(remaining):
    grid = push(grid, 'N')
    grid = push(grid, 'W')
    grid = push(grid, 'S')
    grid = push(grid, 'E')
print(f"Part 2 answer: {get_load(grid)}")