# with open("input6.txt") as file:
#     lines = [line.strip() for line in file.readlines()]
def num_ways(time, dist):
    count = 0
    for i in range(time):
        if i * (time - i) > dist:
            count += 1
    return count

def num_ways_fast(time, dist):
    min_t = -1
    max_t = -1
    for i in range(time):
        if i * (time - i) > dist:
            min_t = i
            break
    for i in range(time, 0, -1):
        if i * (time - i) > dist:
            max_t = i
            break
    return max_t - min_t + 1

print(num_ways(30, 200))
print(num_ways(58, 434) * num_ways(81, 1041) * num_ways(96, 2219) * num_ways(76, 1218))

print(num_ways_fast(71530, 940200))
print(num_ways_fast(58819676, 434104122191218))