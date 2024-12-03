import re

with open("input_full.txt") as f:
    ls = f.readlines()

sum = 0
for l in ls:
    for m in re.finditer("mul\(([0-9]+)\,([0-9]+)\)", l):
        print(f"{m.group(1)=}")
        print(f"{m.group(2)=}")
        sum += int(m.group(1)) * int(m.group(2))

print(sum)
