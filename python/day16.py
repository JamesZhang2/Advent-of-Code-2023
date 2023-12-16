with open("input16.txt") as file:
    lines = [line.strip() for line in file.readlines()]

grid = []
for line in lines:
    grid.append([ch for ch in line])


def count_energized(start):
    history = set()
    beams = [start]  # (r, c, delta_r, delta_c)
    while len(beams) > 0:
        beam = beams.pop()
        if beam in history:
            continue
        r = beam[0]
        c = beam[1]
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            continue
        history.add(beam)
        delta_r = beam[2]
        delta_c = beam[3]
        assert delta_r * delta_c == 0
        if grid[r][c] == '.':
            beams.append((r + delta_r, c + delta_c, delta_r, delta_c))
        elif grid[r][c] == '/':
            if delta_c != 0:
                beams.append((r - delta_c, c, -delta_c, 0))
            elif delta_r != 0:
                beams.append((r, c - delta_r, 0, -delta_r))
        elif grid[r][c] == '\\':
            if delta_c != 0:
                beams.append((r + delta_c, c, delta_c, 0))
            elif delta_r != 0:
                beams.append((r, c + delta_r, 0, delta_r))
        elif grid[r][c] == '-':
            if delta_c != 0:
                # pass through
                beams.append((r, c + delta_c, delta_r, delta_c))
            elif delta_r != 0:
                # split
                beams.append((r, c - 1, 0, -1))
                beams.append((r, c + 1, 0, 1))
        elif grid[r][c] == '|':
            if delta_r != 0:
                # pass through
                beams.append((r + delta_r, c, delta_r, delta_c))
            elif delta_c != 0:
                # split
                beams.append((r - 1, c, -1, 0))
                beams.append((r + 1, c, 1, 0))

    energized = set()
    for beam in history:
        energized.add((beam[0], beam[1]))
    return len(energized)


# Part 1
print(count_energized(start=(0, 0, 0, 1)))

# Part 2
max_energized = -1
for r in range(len(grid)):
    max_energized = max(max_energized, count_energized(start=(r, 0, 0, 1)))
    max_energized = max(max_energized, count_energized(start=(r, len(grid[0]) - 1, 0, -1)))
for c in range(len(grid[0])):
    max_energized = max(max_energized, count_energized(start=(0, c, 1, 0)))
    max_energized = max(max_energized, count_energized(start=(len(grid) - 1, c, -1, 0)))
print(max_energized)