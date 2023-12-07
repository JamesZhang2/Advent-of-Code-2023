with open("input7.txt") as file:
    lines = [line.strip() for line in file.readlines()]

hands = []
for line in lines:
    hand, bid = line.split()
    hands.append((hand, int(bid)))

def ch_to_num(ch, joker=False):
    if ch.isdigit():
        return int(ch)
    elif ch == "T":
        return 10
    elif ch == "J":
        return 0 if joker else 11
    elif ch == "Q":
        return 12
    elif ch == "K":
        return 13
    elif ch == "A":
        return 14
    assert False

def power(hand, joker=False):
    map = {}
    five = 0
    four = 0
    full = 0
    three = 0
    two_pair = 0
    one_pair = 0
    high = 0

    for ch in hand:
        if ch in map:
            map[ch] += 1
        else:
            map[ch] = 1

    if joker:
        # Joker should always be the one with the highest freq
        if 'J' in map:
            if len(map) == 1:
                # only jokers
                five = 1
            else:
                max_ch, max_freq = -1, -1
                for ch in map:
                    if ch == 'J':
                        continue
                    if map[ch] > max_freq:
                        max_freq = map[ch]
                        max_ch = ch
                map[max_ch] += map["J"]
                del map["J"]

    if len(map) == 1:
        five = 1
    elif len(map) == 2:
        for key in map:
            if map[key] == 1 or map[key] == 4:
                four = 1
                break
            else:
                full = 1
                break
    elif len(map) == 3:
        for key in map:
            if map[key] == 3:
                three = 1
                break
        if three != 1:
            two_pair = 1
    elif len(map) == 4:
        one_pair = 1
    else:
        high = 1
    strength = [five, four, full, three, two_pair, one_pair, high]
    for ch in hand:
        strength.append(ch_to_num(ch, joker))
    return strength

# hands = sorted(hands, key=lambda hand: power(hand[0]))
# print(hands)

hands = sorted(hands, key=lambda hand: power(hand[0], joker=True))
print(hands)

ans = 0

for i in range(len(hands)):
    ans += (i + 1) * hands[i][1]

print(ans)
