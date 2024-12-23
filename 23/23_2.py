with open("input_full.txt") as f:
# with open("input.txt") as f:
    ls = f.readlines()

ls = [l.strip() for l in ls]


from collections import defaultdict

nodes = defaultdict(list)

for c1, c2 in [l.split("-") for l in ls]:
    nodes[c1].append(c2)
    nodes[c2].append(c1)

def is_all_connected(n, l):
    for i in l:
        if n not in nodes[i]:
            return False
    return True

def check_cycles(n, nodes, longest_cycle):
    cur_longest_cycle = longest_cycle.copy()
    upper = len(nodes)
    # cur node, cycle so far
    front = [(node, [n]) for node in nodes[n]]
    next_front = []
    for i in range(len(nodes)):
        while len(front) > 0:
            nxt, path = front.pop()
            pth = path.copy()
            # print(front)
            # print(nxt)
            # print(pth)
            # print()
            all_other_paths = []
            for _, p in front:
                all_other_paths += p
            if nxt in all_other_paths:
                continue
            if nxt in cur_longest_cycle:
                continue
            if not is_all_connected(nxt, pth):
                if len(cur_longest_cycle) < len(pth):
                    cur_longest_cycle = pth.copy()
                continue
            
            if nxt in pth:
                pth = pth[path.index(nxt):]
                if len(cur_longest_cycle) < len(pth):
                    cur_longest_cycle = pth.copy()
                continue
            pth.append(nxt)
            next_front += [(node, pth) for node in nodes[nxt]]
        front = next_front.copy()
        next_front = []
        
    return cur_longest_cycle

conn = []
longest_cycle = []
for n in nodes:
    print(f"node {n}")
    print(f'longest cycle {",".join(sorted(longest_cycle))}')
    if n in longest_cycle:
        continue
    maybe_cycle = check_cycles(n, nodes.copy(), longest_cycle)
    # print(f"{maybe_cycle=}")
    # print(f"{n[0]=}")
    if len(longest_cycle) < len(maybe_cycle):
        longest_cycle = maybe_cycle.copy()

print(longest_cycle)
print(len(longest_cycle))
print(",".join(sorted(longest_cycle)))
