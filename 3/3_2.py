import re

with open("input_full.txt") as f:
    ls = f.readlines()

sum = 0

mul = True
for l in ls:
    for m in re.finditer("mul\(([0-9]+)\,([0-9]+)\)|don't\(\)|do\(\)", l):
        if "don't" in m.group(0):
            mul = False
        elif "do" in m.group(0):
            mul = True
        else:
            print(f"{m.group(1)=}")
            print(f"{m.group(2)=}")
            if mul:
                sum += int(m.group(1)) * int(m.group(2))

print(sum)
