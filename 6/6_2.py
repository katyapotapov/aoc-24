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


def check_loops(room):
    total_iters = 0
    cur_pos = guard_pos
    cur_dir = (-1, 0)
    # uhh there's a weird bug so i just added 1 to this
    all_pos = set()
    while total_iters < 16900:
        maybe_new_pos = (cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1])
        if (
            maybe_new_pos[0] < 0
            or maybe_new_pos[0] >= len(room)
            or maybe_new_pos[1] < 0
            or maybe_new_pos[1] >= len(room[0])
        ):
            break
        if room[maybe_new_pos[0]][maybe_new_pos[1]] == "#":
            cur_dir = get_next_dir(cur_dir)
            continue
        cur_pos = maybe_new_pos
        all_pos.add(cur_pos)
        total_iters += 1

    # print(total_iters)
    if total_iters >= 16900:
        return True


total_loop_configs = 0
for i in range(len(ls)):
    for j in range(len(ls[0])):
        if ls[i][j] != ".":
            continue
        new_room = ls.copy()
        old_str = new_room[i]
        new_str = old_str[:j] + "#" + old_str[j + 1 :]
        new_room[i] = new_str
        if check_loops(new_room):
            total_loop_configs += 1

print(total_loop_configs)
