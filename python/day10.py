with open("test10a.txt") as file:
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

def try_loop(grid, start_r, start_c, dir_in):
    # dir facing out
    dir_map = {'|': [(1, 0), (-1, 0)],
               '-': [(0, -1), (0, 1)],
               '7': [(1, 0), (0, -1)],
               'F': [(1, 0), (0, 1)],
               'L': [(-1, 0), (0, 1)],
               'J': [(-1, 0), (0, -1)],
               '.': []}
    loop = []
    while True:
        loop.append((start_r, start_c))
        if start_r < 0 or start_r >= len(grid) or start_c < 0 or start_c >= len(grid[0]):
            return []
        if grid[start_r][start_c] == 'S':
            return loop
        dir_in_neg = (-dir_in[0], -dir_in[1])
        cur_ch = grid[start_r][start_c]
        if dir_in_neg not in dir_map[cur_ch]:
            return []
        choices = dir_map[cur_ch]
        if dir_in_neg == choices[0]:
            dir_in = choices[1]
        else:
            dir_in = choices[0]
        start_r = start_r + dir_in[0]
        start_c = start_c + dir_in[1]


def find_loop(grid, animal):
    animal_r, animal_c = animal
    if animal_r > 0:
        # ch = grid[animal_r - 1][animal_c]
        loop = try_loop(grid, start_r=animal_r - 1, start_c=animal_c, dir_in=(-1, 0))
        if loop != []:
            return loop
    if animal_r < len(grid) - 1:
        # ch = grid[animal_r + 1][animal_c]
        loop = try_loop(grid, start_r=animal_r + 1, start_c=animal_c, dir_in=(1, 0))
        if loop != []:
            return loop
    if animal_c > 0:
        # ch = grid[animal_r][animal_c - 1]
        loop = try_loop(grid, start_r=animal_r, start_c=animal_c - 1, dir_in=(0, -1))
        if loop != []:
            return loop
    if animal_c < len(grid[0]) - 1:
        # ch = grid[animal_r][animal_c + 1]
        loop = try_loop(grid, start_r=animal_r, start_c=animal_c + 1, dir_in=(0, 1))
        if loop != []:
            return loop


loop = find_loop(grid, animal)

# print(loop)
print(len(loop) / 2)

# Part 2: BFS/DFS from the boundary
frontier = []
for r in range(len(grid)):
    frontier.append((r, 0))
    frontier.append((r, len(grid[0]) - 1))
for c in range(1, len(grid[0]) - 1):
    frontier.append((0, c))
    frontier.append((len(grid) - 1, c))

o_count = 0
while len(frontier) != 0:
    cell = frontier[len(frontier) - 1]
    cell_r = cell[0]
    cell_c = cell[1]
    frontier.pop()
    if (cell_r, cell_c) in loop or grid[cell_r][cell_c] == 'O':
        continue
    grid[cell_r][cell_c] = 'O'
    o_count += 1
    if cell_r > 0:
        frontier.append((cell_r - 1, cell_c))
    if cell_r < len(grid) - 1:
        frontier.append((cell_r + 1, cell_c))
    if cell_c > 0:
        frontier.append((cell_r, cell_c - 1))
    if cell_c < len(grid[0]) - 1:
        frontier.append((cell_r, cell_c + 1))

print(len(grid) * len(grid[0]) - o_count - len(loop))

# for line in grid:
#     print("".join(line))
