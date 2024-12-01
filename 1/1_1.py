with open("input.txt") as f:
    ls = f.readlines()

nums = [line.split() for line in ls]


list1 = []
list2 = []

for i in nums:
    list1.append(int(i[0]))
    list2.append(int(i[1]))

list1 = sorted(list1)
list2 = sorted(list2)

print(f"{sum([abs(i - j) for i, j in zip(list1, list2)])}")
