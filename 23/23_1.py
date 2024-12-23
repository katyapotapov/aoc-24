from time import sleep


with open("input_full.txt") as f:
    # with open("input.txt") as f:
    ls = f.readlines()

ls = [l.strip() for l in ls]


from collections import defaultdict

nodes = defaultdict(list)

for c1, c2 in [l.split("-") for l in ls]:
    nodes[c1].append(c2)
    nodes[c2].append(c1)

def check_cycles(n, nodes):
    upper = len(nodes)
    all_cycles = [] 
    # cur node, cycle so far
    front = [(node, [n]) for node in nodes[n]]
    next_front = []
    for i in range(3):
        while len(front) > 0:
            nxt, path = front.pop()
            pth = path.copy()
            # print(front)
            # print(nxt)
            # print(pth)
            # print()
            if nxt in pth:
                pth = pth[path.index(nxt):]
                all_cycles.append(pth)
                continue
            pth.append(nxt)
            next_front += [(node, pth) for node in nodes[nxt]]
        front = next_front.copy()
        next_front = []
        
    return all_cycles

conn = []
for n in nodes:
    if n[0] != "t":
        continue
    maybe_cycle = check_cycles(n, nodes.copy())
    # print(f"{maybe_cycle=}")
    # print(f"{n[0]=}")
    s_cycles = [c for c in maybe_cycle if len(c) == 3]
    t_cycles = [i for i in s_cycles if n in i]
    if t_cycles:
        conn += t_cycles

def dedup_list(l):
    uniq = []
    for i in l:
        not_uniq = False
        for u in uniq:
            if set(i) == set(u):
                not_uniq = True 
                break
        if not_uniq:
            continue
        uniq.append(i)
    return uniq

uniq = dedup_list(conn)
print(uniq)
print(len(uniq))
