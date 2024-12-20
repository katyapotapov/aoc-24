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

memo = {}
for pos in [s_pos, e_pos]:
    memo[pos] = []
    for i in range(len(ls)):
        cur = []
        for j in range(len(ls[0])):
            cur.append(-1)
        memo[pos].append(cur)

def get_shortest_path(e_pos, frontier):
    path_lens = []
    while len(frontier) != 0:
        next_pos, pth = frontier.pop()
        if ls[next_pos[0]][next_pos[1]] == "#":
            continue
        elif next_pos in pth:
            continue
        elif e_pos in memo:
            memo_end_pos = memo[e_pos]
            if memo_end_pos[next_pos[0]][next_pos[1]] > -1:
                path_lens.append(len(pth) + memo_end_pos[next_pos[0]][next_pos[1]])
        elif next_pos == e_pos:
            path_lens.append(len(pth)+1)
        else:
            adj = get_all_adjacent_dirs(next_pos[0], next_pos[1])
            for a in adj:
                frontier.append((a, pth.copy() + [next_pos]))

    return min(path_lens) if path_lens else 1000000000


def fill_memo(pos):
    seen = []
    frontier = [(pos, 0)]
    cur_memo = memo[pos]
    while len(frontier) > 0:
        cur, d = frontier.pop()
        mem = cur_memo[cur[0]][cur[1]]
        if mem == -1 or mem > d+1:
            cur_memo[cur[0]][cur[1]] = d+1 
        elif mem <= d+1:
            continue

        adj = get_all_adjacent_dirs(cur[0], cur[1])
        for a in adj:
            frontier.append((a, d+1))
        seen.append(cur)

    memo[pos] = cur_memo

fill_memo(s_pos)
fill_memo(e_pos)

fair_len = memo[s_pos][e_pos[0]][e_pos[1]]
print(fair_len)


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


shortest_lens = []
for f, s in one_width_adj:
    f_len = memo[s_pos][f[0]][f[1]]
    s_len = memo[e_pos][s[0]][s[1]]
    shortest_lens.append(f_len + s_len + 1)

    # reverse reverse!
    s_len = memo[s_pos][s[0]][s[1]]
    f_len = memo[e_pos][f[0]][f[1]]
    shortest_lens.append(f_len + s_len + 1)

# 
print(shortest_lens)
print(len([l for l in shortest_lens if fair_len - l >= 100]))
# print(len([l for l in shortest_lens if fair_len - l >= 20]))
