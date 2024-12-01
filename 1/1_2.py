import collections

with open("input_full.txt") as f:
    ls = f.readlines()

nums = [line.split() for line in ls]

left = []
right = []
for pair in nums:
    left.append(int(pair[0]))
    right.append(int(pair[1]))

ctr = collections.Counter(right)

score = 0
for i in left:
    score += i * ctr[i]

print(score)
