with open("input12.txt") as file:
    lines = [line.strip() for line in file.readlines()]

def arrangements(record: str, groups):
    exp_total = sum(groups)  # expected
    act_total = record.count("#")  # actual
    q_marks = record.count("?")
    if act_total > exp_total or q_marks + act_total < exp_total:
        return 0
    if q_marks == 0:
        act_groups = [len(s) for s in record.split(".")]
        act_groups = [num for num in act_groups if num != 0]
        return 1 if act_groups == groups else 0
    return arrangements(record.replace('?', '.', 1), groups) + arrangements(record.replace('?', '#', 1), groups)


ans = 0
for line in lines:
    pair = line.split(" ")
    record = pair[0]
    groups = [int(num) for num in pair[1].split(",")]
    # print(arrangements(record, groups))
    ans += arrangements(record, groups)
print(ans)