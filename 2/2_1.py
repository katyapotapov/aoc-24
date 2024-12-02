with open("input_full.txt") as f:
    # with open("input.txt") as f:
    ls = f.readlines()

nums = [line.split() for line in ls]

nums_n = []
for line in nums:
    j = []
    for i in line:
        j.append(int(i))
    nums_n.append(j)

print(nums_n)

num_safe = 0
for line in nums_n:
    inc = False
    if line[1] > line[0]:
        inc = True

    safe = True
    for i in range(len(line) - 1):
        if inc and line[i + 1] <= line[i]:
            safe = False
            break
        elif not inc and line[i + 1] >= line[i]:
            safe = False
            break
        diff = abs(line[i + 1] - line[i])
        if diff < 1 or diff > 3:
            safe = False
            break

    if safe:
        num_safe += 1

print(num_safe)
