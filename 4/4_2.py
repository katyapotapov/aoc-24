with open("input_full.txt") as f:
    ls = f.readlines()


# diagonal
def check_adjacent_tiles(i, j, a, b, c):
    new_i = i + a
    new_j = j + b
    if new_i < 0 or new_i >= len(ls):
        return
    if new_j < 0 or new_j >= len(ls[i]):
        return
    if ls[new_i][new_j] == c:
        # Annoying hack
        if a > 0:
            a = 1
        else:
            a = -1
        if b > 0:
            b = 1
        else:
            b = -1
        return (a, b)


total_words = 0
for i in range(len(ls)):
    for j in range(len(ls[i])):
        if ls[i][j] == "A":
            vs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            m_s = []
            for x, y in vs:
                m = check_adjacent_tiles(i, j, x, y, "M")
                if m is not None:
                    m_s.append(m)
            if len(m_s) != 2:
                continue
            s_s = []
            for x, y in m_s:
                s = check_adjacent_tiles(i, j, x * -1, y * -1, "S")
                if s is not None:
                    s_s.append(s)
            if len(s_s) == 2:
                total_words += 1

print(total_words)
