with open("test15.txt") as file:
    lines = [line.strip() for line in file.readlines()]

def get_hash(s):
    cur = 0
    for ch in s:
        cur += ord(ch)
        cur *= 17
        cur %= 256
    return cur

words = lines[0].split(",")

ans = 0
for word in words:
    ans += get_hash(word)
print(ans)