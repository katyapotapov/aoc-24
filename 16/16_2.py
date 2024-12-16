from time import sleep


with open("input_full.txt") as f:
# with open("input.txt") as f:
    ls = f.readlines()

ls = [l.strip() for l in ls]

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
            adj.append((d[0], d[1]))
    return adj


memo = []
import math

for i in range(len(ls)):
    hi = []
    for j in range(len(ls[0])):
        hi.append(math.inf)
    memo.append(hi)


def get_shortest_path(e_pos, frontier):
    path_scores = []

    # cur pos, score, dir, path so far
    while len(frontier) > 0:
        cur_f, cur_score, cur_dir, path = frontier.pop()
        if memo[cur_f[0]][cur_f[1]] < cur_score - 1001:
            # another path has a better way
            continue
        elif memo[cur_f[0]][cur_f[1]] > cur_score:
            memo[cur_f[0]][cur_f[1]] = cur_score
        # next_to_explore_dirs = get_all_adjacent_dirs(cur_f[0], cur_f[1], not_vecs=(-cur_dir[0], -cur_dir[1]))
        next_to_explore_dirs = get_all_adjacent_dirs(cur_f[0], cur_f[1])
        for n in next_to_explore_dirs:
            new_f = (cur_f[0] + n[0], cur_f[1] + n[1])

            if len(path) > len(ls) * len(ls[0]):
                raise Exception("You fked up")

            # we have a cycle, drop this one
            if new_f in path:
                continue
            new_path = path.copy()
            new_path.append(new_f)

            if cur_dir == n:
                new_score = cur_score + 1
            else:
                if (cur_dir[0] != 0 and cur_dir[0] == -n[0]) or (
                    cur_dir[1] != 0 and cur_dir[1] == -n[1]
                ):
                    new_score = cur_score + 2001
                else:
                    new_score = cur_score + 1001
            if new_f == e_pos:
                path_scores.append((new_f, new_score, n, new_path))
            else:
                frontier.append((new_f, new_score, n, new_path))

    frontier_to_return = []
    if len(path_scores) == 0:
        return frontier_to_return
    min_score = min([s for (_, s, _, _) in path_scores])
    print(f"{min_score=}")
    for d, score, p, path in path_scores:
        if score == min_score:
            frontier_to_return.append((score, d, p, path))
    return frontier_to_return
    # print([pos for pos, sc, _, _ in frontier])
    # print(frontier)
    # print(len(frontier))
    # print(len(path_scores))


# outside_frontier = [(s_pos, 0, (0, 1))]

# cur pos, score, dir, path so far
frontier = [(s_pos, 0, (0, 1), [])]
f = get_shortest_path(e_pos, frontier)
# print(f)
# print(len(f))
all_spots = []
for hey in f:
    print(hey)
    print(len(hey))
    _, _, _, i = hey
    all_spots += i

# + 1 because start_pos
print(len(set(all_spots)) + 1)

# viz
for i in range(len(ls)):
    out = ""
    for j in range(len(ls[0])):
        if (i, j) in all_spots:
            out += "O"
        elif ls[i][j] == "#":
            out += "#"
        else:
            out += "."
    # print(out)


# already_seen = []
# # pos, score, dir
# while len(outside_frontier) > 0:
#     # print(outside_frontier)
#     next_pos, next_score, next_dir = outside_frontier.pop()
#     already_seen.append(next_pos)
#     if next_pos == e_pos:
#         print(next_score)
#
#     adj_dirs = get_all_adjacent_dirs(next_pos[0], next_pos[1])
#     inside_frontier = [(next_pos, next_score, next_dir, already_seen)]
#     maybe_next = []
#     for d in adj_dirs:
#         next_e_pos = (next_pos[0] + d[0], next_pos[1] + d[1])
#         # print(next_e_pos)
#         if next_e_pos in already_seen:
#             continue
#         outside_frontier += get_shortest_path(next_e_pos, inside_frontier.copy())
