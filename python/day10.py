with open("input10.txt") as file:
    lines = [line.strip() for line in file.readlines()]

grid = []
for line in lines:
    grid.append([ch for ch in line])

animal = (-1, -1)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            animal = (i, j)
            break

print(grid, animal)

# loop = []

def try_loop(grid, start_r, start_c, dir_in) -> int:
    # dir facing out
    dir_map = {'|': [(1, 0), (-1, 0)],
               '-': [(0, -1), (0, 1)],
               '7': [(1, 0), (0, -1)],
               'F': [(1, 0), (0, 1)],
               'L': [(-1, 0), (0, 1)],
               'J': [(-1, 0), (0, -1)],
               '.': []}
    count = 0
    while True:
        count += 1
        if start_r < 0 or start_r >= len(grid) or start_c < 0 or start_c >= len(grid):
            return -1
        if grid[start_r][start_c] == 'S':
            return count
        dir_in_neg = (-dir_in[0], -dir_in[1])
        cur_ch = grid[start_r][start_c]
        if dir_in_neg not in dir_map[cur_ch]:
            return -1
        choices = dir_map[cur_ch]
        if dir_in_neg == choices[0]:
            dir_in = choices[1]
        else:
            dir_in = choices[0]
        start_r = start_r + dir_in[0]
        start_c = start_c + dir_in[1]

def try_loop_rec(grid, start_r, start_c, dir_in, count) -> int:
    if start_r < 0 or start_r >= len(grid) or start_c < 0 or start_c >= len(grid):
        return -1
    if grid[start_r][start_c] == 'S':
        return count
    # dir facing out
    dir_map = {'|': [(1, 0), (-1, 0)],
               '-': [(0, -1), (0, 1)],
               '7': [(1, 0), (0, -1)],
               'F': [(1, 0), (0, 1)],
               'L': [(-1, 0), (0, 1)],
               'J': [(-1, 0), (0, -1)],
               '.': []}
    dir_in_neg = (-dir_in[0], -dir_in[1])
    cur_ch = grid[start_r][start_c]
    if dir_in_neg not in dir_map[cur_ch]:
        return -1
    choices = dir_map[cur_ch]
    if dir_in_neg == choices[0]:
        new_dir_in = choices[1]
    else:
        new_dir_in = choices[0]

    return try_loop(grid, start_r=start_r + new_dir_in[0], start_c=start_c + new_dir_in[1], dir_in=new_dir_in, count=count + 1)

def find_loop(grid, animal):
    animal_r, animal_c = animal
    if animal_r > 0:
        # ch = grid[animal_r - 1][animal_c]
        loop_len = try_loop(grid, start_r=animal_r - 1, start_c=animal_c, dir_in=(-1, 0))
        if loop_len != -1:
            return loop_len / 2
    if animal_r < len(grid) - 1:
        # ch = grid[animal_r + 1][animal_c]
        loop_len = try_loop(grid, start_r=animal_r + 1, start_c=animal_c, dir_in=(1, 0))
        if loop_len != -1:
            return loop_len / 2
    if animal_c > 0:
        # ch = grid[animal_r][animal_c - 1]
        loop_len = try_loop(grid, start_r=animal_r, start_c=animal_c - 1, dir_in=(0, -1))
        if loop_len != -1:
            return loop_len / 2
    if animal_c < len(grid[0]) - 1:
        # ch = grid[animal_r][animal_c + 1]
        loop_len = try_loop(grid, start_r=animal_r, start_c=animal_c + 1, dir_in=(0, 1))
        if loop_len != -1:
            return loop_len / 2


print(find_loop(grid, animal))