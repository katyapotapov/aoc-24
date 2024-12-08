with open("/Users/katya/Documents/small-projects/aoc-24/7/input_full.txt") as f:

    ls = f.readlines()
ls = [l.strip() for l in ls]

tru = []
for l in ls:
    sol = int(l[: l.find(":")])
    nums_str = l[l.find(":") + 1 :]
    nums = [int(i) for i in nums_str.split()]
    res_so_far = [nums[0]]
    for i_num in range(1, len(nums)):
        new_res = []
        for res in res_so_far:
            new_res.append(res + nums[i_num])
            new_res.append(res * nums[i_num])
        res_so_far = new_res
    print(f"{sol=}")
    print(res_so_far)

    if sol in res_so_far:
        tru.append(sol)

print(sum(tru))
