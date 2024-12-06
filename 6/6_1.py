with open("input_full.txt") as f:
    ls = f.readlines()

ls = [l.strip() for l in ls]

guard_pos = (-1, -1)
for i in range(len(ls)):
    j = ls[i].find("^")
    if j >= 0:
        guard_pos = (i, j)
        break


def get_next_dir(dir):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_ind = dirs.index(dir)
    ret = dirs[(dir_ind + 1) % 4]
    return ret


cur_pos = guard_pos
cur_dir = (-1, 0)
# uhh there's a weird bug so i just added 1 to this
# After solving: the "weird bug" was that putting a tuple in the set() constructor unwraps the tuple so its elements
# are unpacked - so the set looks like {4, 5, (4, 6), (4, 7), ...} instead of {(4, 5), (4, 6), ...}
all_pos = set()
print(all_pos)
while True:
    maybe_new_pos = (cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1])
    if (
        maybe_new_pos[0] < 0
        or maybe_new_pos[0] >= len(ls)
        or maybe_new_pos[1] < 0
        or maybe_new_pos[1] >= len(ls[0])
    ):
        break
    if ls[maybe_new_pos[0]][maybe_new_pos[1]] == "#":
        cur_dir = get_next_dir(cur_dir)
        continue
    cur_pos = maybe_new_pos
    all_pos.add(cur_pos)

print(len(all_pos))
