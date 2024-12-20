from time import sleep


# with open("input_full.txt") as f:
with open("input.txt") as f:
    ls = f.readlines()

ls = [list(l.strip()) for l in ls]

s_pos = None
e_pos = None
for i in ls:
    for j in i:
        if j == "S":
            s_pos = (ls.index(i), i.index(j))
        if j == "E":
            e_pos = (ls.index(i), i.index(j))


def get_all_adjacent_dirs(i, j, vecs=None, not_vecs=None):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    if vecs:
        dirs = vecs
    if not_vecs:
        dirs = [d for d in dirs if d not in not_vecs]
    adj = []
    for d in dirs:
        if (
            i + d[0] < len(ls)
            and i + d[0] >= 0
            and j + d[1] < len(ls[0])
            and j + d[1] >= 0
        ):
            if ls[i + d[0]][j + d[1]] == "#":
                continue
            adj.append((i + d[0], j + d[1]))
    return adj

def get_shortest_path(e_pos, frontier, cutoff = None):
    all_paths = []
    while len(frontier) != 0:
        next_pos, pth = frontier.pop()
        if ls[next_pos[0]][next_pos[1]] == "#":
            continue
        elif next_pos in pth:
            continue
        elif cutoff is not None and len(pth) > cutoff:
            continue
        elif next_pos == e_pos:
            all_paths.append((pth + [next_pos]))
        else:
            adj = get_all_adjacent_dirs(next_pos[0], next_pos[1])
            for a in adj:
                frontier.append((a, pth.copy() + [next_pos]))

    path_lens = [len(s) for s in all_paths]
    return min(path_lens) if path_lens else 1000000000


fair_len = get_shortest_path(e_pos, [(s_pos, [])])
print(fair_len)

memo_end_pos = []
for i in range(1, len(ls)-1):
    cur = []
    for j in range(1, len(ls[0])-1):
        if ls[i][j] == "#":
            cur.append(-1)
        else:
            cur.append(get_shortest_path(e_pos, [((i, j), [])]))
    memo_end_pos.append(cur)

memo_start_pos = []
for i in range(1, len(ls)-1):
    cur = []
    for j in range(1, len(ls[0])-1):
        if ls[i][j] == "#":
            cur.append(-1)
        else:
            cur.append(get_shortest_path(s_pos, [((i, j), [])]))
    memo_start_pos.append(cur)

# get all the blocks adjacent to 1-width blocks
one_width_adj = []
for i in range(1, len(ls)-1):
    for j in range(1, len(ls[0])-1):
        if ls[i][j] == "#":
            ns = get_all_adjacent_dirs(i, j, vecs=[(1, 0), (-1, 0)])
            ew = get_all_adjacent_dirs(i, j, vecs=[(0, 1), (0, -1)])
            if len(ns) == 2:
                one_width_adj.append(ns)
            if len(ew) == 2:
                one_width_adj.append(ew)

print(one_width_adj)

shortest_lens = []
for f, s in one_width_adj:
    f_len = get_shortest_path(f, [(s_pos, [])])
    s_len = get_shortest_path(e_pos, [(s, [])])
    shortest_lens.append(f_len + s_len + 1)

    # reverse reverse!
    s_len = get_shortest_path(s, [(s_pos, [])])
    f_len = get_shortest_path(e_pos, [(f, [])])
    shortest_lens.append(f_len + s_len + 1)

# 
# print(len([l for l in shortest_lens if fair_len - l >= 100]))
print(len([l for l in shortest_lens if fair_len - l >= 20]))
