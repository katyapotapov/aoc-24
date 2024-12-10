from time import sleep
with open("input_full.txt") as f:

    ls = f.readlines()
ls = [l.strip() for l in ls]

heads = []
for i in range(len(ls)):
    for j in range(len(ls[0])):
        if ls[i][j] == "0":
            heads.append((i, j))

def get_valid_adjacent(i, j):
    valid = []
    vecs = [(0,1), (0,-1),(-1,0),(1,0)]
    for vec in vecs:
        new_i = i + vec[0]
        new_j = j + vec[1]
        if new_i >= 0 and new_j >= 0 and new_i < len(ls) and new_j < len(ls[0]):
            valid.append((new_i, new_j))
    return valid

scores = []
for head in heads:
    cur_step = "0"
    cur_heads = [head]
    while cur_step != "9" and len(cur_heads) > 0:
        next_step = str(int(cur_step) + 1)
        possible_paths = []
        for cur_head in cur_heads:
            valid_next = get_valid_adjacent(cur_head[0], cur_head[1])
            for maybe_next in valid_next:
                if ls[maybe_next[0]][maybe_next[1]] == next_step:
                    possible_paths.append(maybe_next)
        cur_heads = possible_paths
        cur_step = next_step
    if cur_step == "9":
        scores.append(len(set(cur_heads)))

print(scores)
print(sum(scores))
