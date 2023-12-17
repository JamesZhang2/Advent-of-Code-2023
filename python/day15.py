with open("input15.txt") as file:
    lines = [line.strip() for line in file.readlines()]

def get_hash(s):
    cur = 0
    for ch in s:
        cur += ord(ch)
        cur *= 17
        cur %= 256
    return cur

words = lines[0].split(",")

# Part 1

ans = 0
for word in words:
    ans += get_hash(word)
print(ans)

# Part 2

boxes = []
for i in range(256):
    boxes.append([])  # list of [label, focal length] pairs
    # Not using tuples since python tuples are immutable

for word in words:
    if '-' in word:
        label = word[:-1]
        key = get_hash(label)
        for pair in boxes[key]:
            if pair[0] == label:
                boxes[key].remove(pair)
                break
    else:
        assert '=' in word
        label = word[:-2]
        focal_len = int(word[-1])
        key = get_hash(label)

        found = False
        for pair in boxes[key]:
            if pair[0] == label:
                pair[1] = focal_len
                found = True
                break
        if not found:
            boxes[key].append([label, focal_len])

# print(boxes)

power = 0
for i in range(256):
    for j in range(len(boxes[i])):
        power += (i + 1) * (j + 1) * boxes[i][j][1]

print(power)

