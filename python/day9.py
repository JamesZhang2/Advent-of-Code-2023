with open("input9.txt") as file:
    lines = [line.strip() for line in file.readlines()]

lsts = []
for line in lines:
    lsts.append([int(num) for num in line.split()])

# print(lsts)

def sum_extrap(lst, rev=False):
    if rev:
        lst.reverse()
    lasts = []
    lasts.append(lst[-1])
    all_zero = False
    while not all_zero:
        new_lst = []
        for i in range(len(lst) - 1):
            new_lst.append(lst[i + 1] - lst[i])
        lst = new_lst
        lasts.append(lst[len(lst) - 1])

        all_zero = True
        for num in lst:
            if num != 0:
                all_zero = False

    new_lasts = [0]
    for i in range(len(lasts)):
        new_lasts.append(new_lasts[i] + lasts[len(lasts) - i - 1])
    return new_lasts[-1]

sum = 0
for lst in lsts:
    sum += sum_extrap(lst)

print(sum)

sum2 = 0
for lst in lsts:
    sum2 += sum_extrap(lst, rev=True)

print(sum2)