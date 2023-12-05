with open("input1.txt") as file:
    lines = [line.strip() for line in file.readlines()]
sum = 0
for line in lines:
    first = -1
    last = -1
    for char in line:
        if char.isdigit():
            if first == -1:
                first = int(char)
            last = int(char)
    sum += first * 10 + last
print(sum)

sum2 = 0
words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
for line in lines:
    firstIdx = 1e6
    lastIdx = -1
    firstVal = -1
    lastVal = -1
    for word in words:
        if word in line:
            if line.find(word) < firstIdx:
                firstIdx = line.find(word)
                firstVal = words[word]
            if line.rfind(word) > lastIdx:
                lastIdx = line.rfind(word)
                lastVal = words[word]
    for i in range(len(line)):
        if line[i].isdigit():
            if i < firstIdx:
                firstVal = int(line[i])
                break
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            if i > lastIdx:
                lastVal = int(line[i])
                break
    sum2 += firstVal * 10 + lastVal
print(sum2)