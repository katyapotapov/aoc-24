from time import sleep


with open("input_full.txt") as f:
# with open("input.txt") as f:
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


def get_shortest_path(e_pos, frontier):
    all_paths = []
    while len(frontier) != 0:
        next_pos, pth = frontier.pop()
        if ls[next_pos[0]][next_pos[1]] == "#":
            continue
        elif next_pos in pth:
            continue
        elif next_pos == e_pos:
            all_paths.append((pth + [next_pos]))
        else:
            adj = get_all_adjacent_dirs(next_pos[0], next_pos[1])
            for a in adj:
                frontier.append((a, pth.copy() + [next_pos]))

    path_lens = [len(s) for s in all_paths]
    return min(path_lens)


fair_len = get_shortest_path(e_pos, [(s_pos, [])])
print(fair_len)

shortest_lens = []
for i in range(len(ls)):
    for j in range(len(ls[0])):
        if ls[i][j] == "#":
            ls[i][j] = "."
            shortest_lens.append(get_shortest_path(e_pos, [(s_pos, [])]))
            ls[i][j] = "#"

print(len([l for l in shortest_lens if fair_len - l >= 100]))
