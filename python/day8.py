with open("input8.txt") as file:
    lines = [line.strip() for line in file.readlines()]

dirs = lines[0]
map = {}

for i in range(2, len(lines)):
    line = lines[i]
    key = line[0:3]
    lparen_idx = line.index("(")
    left = line[(lparen_idx + 1):(lparen_idx + 4)]
    comma_idx = line.index(",")
    right = line[(comma_idx + 2):(comma_idx + 5)]
    map[key] = (left, right)

print(map)

# Part 1
key = "AAA"
i = 0
while True:
    key = map[key][0] if dirs[i % len(dirs)] == 'L' else map[key][1]
    if key == "ZZZ":
        print(i + 1)
        break
    i += 1

# Part 2
keys = []
for key in map:
    if key[2] == 'A':
        keys.append(key)
print(keys)

# Too slow!
# i = 0
# while True:
#     new_keys = []
#     for key in keys:
#         new_keys.append(map[key][0] if dirs[i % len(dirs)] == 'L' else map[key][1])
#     end_z = [k for k in new_keys if k[2] == 'Z']
#     if len(end_z) == len(new_keys):
#         print(i + 1)
#         break
#     keys = new_keys
#     i += 1

# Turns out lcm works
# Normally, we would need Chinese Remainder Theorem
# But the input is designed so that the period is the first time we see a word ending with 'Z'
periods = []
for key in keys:
    i = 0
    while True:
        key = map[key][0] if dirs[i % len(dirs)] == 'L' else map[key][1]
        if key[2] == 'Z':
            periods.append(i + 1)
            break
        i += 1

print(periods)


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a - a // b * b)


def lcm(a, b):
    return a * b // gcd(a, b)


ans = 1
for period in periods:
    ans = lcm(ans, period)
print(ans)
