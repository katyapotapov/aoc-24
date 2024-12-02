with open("input_full.txt") as f:
    # with open("input.txt") as f:
    ls = f.readlines()

nums = [line.split() for line in ls]

nums_n = []
for i, line in enumerate(nums):
    j = []
    for num in line:
        j.append(int(num))
    nums_n.append((i, j))

print(nums_n)


def check_safe(line):
    safe = True
    inc = False
    if line[1] > line[0]:
        inc = True

    for i in range(len(line) - 1):
        if inc and line[i + 1] <= line[i]:
            safe = False
        elif not inc and line[i + 1] >= line[i]:
            safe = False
        diff = abs(line[i + 1] - line[i])
        if diff < 1 or diff > 3:
            safe = False

    return safe


safe_ids = []
more_to_check = []
for line_id, line in nums_n:
    safe = check_safe(line)
    if not safe:
        for j in range(len(line)):
            dup_line = line.copy()
            del dup_line[j]
            more_to_check.append((line_id, dup_line))

    if safe:
        print(f"SAFE {line=}")
        safe_ids.append(line_id)

for line_id, line in more_to_check:
    safe = check_safe(line)
    if safe:
        safe_ids.append(line_id)

print(len(set(safe_ids)))
