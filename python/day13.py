with open("test13.txt") as file:
    lines = [line.strip() for line in file.readlines()]

grids = []
cur_grid = []
for line in lines:
    if line == "":
        grids.append(cur_grid.copy())
        cur_grid = []
    else:
        cur_grid.append([ch for ch in line])

if cur_grid != []:
    grids.append(cur_grid)


def is_refl_row(grid, r):
    for i in range(min(r, len(grid) - r)):
        if grid[r - i - 1] != grid[r + i]:
            return False
    return True

def is_refl_col(grid, c):
    for i in range(min(c, len(grid[0]) - c)):
        for j in range(len(grid)):
            if grid[j][c - i - 1] != grid[j][c + i]:
                return False
    return True

def summarize(grid, skip_row=None, skip_col=None):
    for r in range(1, len(grid)):
        if r == skip_row:
            continue
        if is_refl_row(grid, r):
            return r * 100
    for c in range(1, len(grid[0])):
        if c == skip_col:
            continue
        if is_refl_col(grid, c):
            return c
    return -1

def summarize_smudge(grid):
    orig_ans = summarize(grid)
    skip_row = None if orig_ans < 100 else orig_ans // 100
    skip_col = None if orig_ans % 100 == 0 else orig_ans % 100
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            orig = grid[i][j]
            grid[i][j] = '.' if orig == '#' else '#'
            ans = summarize(grid, skip_row, skip_col)
            if ans != -1:
                return ans
            grid[i][j] = orig

    # Debug
    print(orig_ans)
    for row in grid:
        print("".join(row))
    assert False

sum = 0
for grid in grids:
    sum += summarize_smudge(grid)
print(sum)
